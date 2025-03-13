from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .. import models, schemas, security
from ..database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from datetime import datetime
from typing import Optional

router = APIRouter(prefix="/shanyraks")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/users/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
        user = db.query(models.User).filter(models.User.username == username).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found", headers={"WWW-Authenticate": "Bearer"})
        return user
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

@router.post("/", response_model=schemas.Shanyrak)
def create_shanyrak(shanyrak: schemas.ShanyrakCreate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_shanyrak = models.Shanyrak(**shanyrak.dict(), owner_id=current_user.id)
    db.add(db_shanyrak)
    db.commit()
    db.refresh(db_shanyrak)
    return db_shanyrak

@router.get("/{shanyrak_id}", response_model=schemas.Shanyrak)
def read_shanyrak(shanyrak_id: int, db: Session = Depends(get_db)):
    db_shanyrak = db.query(models.Shanyrak).filter(models.Shanyrak.id == shanyrak_id).first()
    if db_shanyrak is None:
        raise HTTPException(status_code=404, detail="Shanyrak not found")
    total_comments = len(db_shanyrak.comments)
    return schemas.Shanyrak(id=db_shanyrak.id, type=db_shanyrak.type, price=db_shanyrak.price, address=db_shanyrak.address, area=db_shanyrak.area, rooms_count=db_shanyrak.rooms_count, description=db_shanyrak.description, owner_id=db_shanyrak.owner_id, total_comments=total_comments)

@router.patch("/{shanyrak_id}", response_model=schemas.Shanyrak)
def update_shanyrak(shanyrak_id: int, shanyrak: schemas.ShanyrakCreate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_shanyrak = db.query(models.Shanyrak).filter(models.Shanyrak.id == shanyrak_id).first()
    if db_shanyrak is None:
        raise HTTPException(status_code=404, detail="Shanyrak not found")
    if db_shanyrak.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    for field, value in shanyrak.dict().items():
        setattr(db_shanyrak, field, value)
    db.commit()
    db.refresh(db_shanyrak)
    return db_shanyrak

@router.delete("/{shanyrak_id}", response_model=schemas.Shanyrak)
def delete_shanyrak(shanyrak_id: int, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_shanyrak = db.query(models.Shanyrak).filter(models.Shanyrak.id == shanyrak_id).first()
    if db_shanyrak is None:
        raise HTTPException(status_code=404, detail="Shanyrak not found")
    if db_shanyrak.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    db.delete(db_shanyrak)
    db.commit()
    return db_shanyrak

@router.post("/{shanyrak_id}/comments", response_model=schemas.Comment)
def create_comment(shanyrak_id: int, comment: schemas.CommentCreate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_comment = models.Comment(
        **comment.dict(),
        author_id=current_user.id,
        shanyrak_id=shanyrak_id,
        created_at=datetime.now(),
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

@router.get("/{shanyrak_id}/comments", response_model=schemas.CommentList)
def read_comments(shanyrak_id: int, db: Session = Depends(get_db)):
    db_comments = db.query(models.Comment).filter(models.Comment.shanyrak_id == shanyrak_id).all()
    if not db_comments:
        return schemas.CommentList(comments=[])
    schema_comments = [schemas.Comment.model_validate(db_comment) for db_comment in db_comments]
    return schemas.CommentList(comments=schema_comments)

@router.patch("/{shanyrak_id}/comments/{comment_id}", response_model=schemas.Comment)
def update_comment(shanyrak_id: int, comment_id: int, comment: schemas.CommentCreate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id, models.Comment.shanyrak_id == shanyrak_id).first()
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    if db_comment.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    for field, value in comment.dict().items():
        setattr(db_comment, field, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment

@router.delete("/{shanyrak_id}/comments/{comment_id}", response_model=schemas.Comment)
def delete_comment(shanyrak_id: int, comment_id: int, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id, models.Comment.shanyrak_id == shanyrak_id).first()
    db_shanyrak = db.query(models.Shanyrak).filter(models.Shanyrak.id == shanyrak_id).first()
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    if db_comment.author_id != current_user.id and db_shanyrak.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    db.delete(db_comment)
    db.commit()
    return db_comment

@router.get("/", response_model=schemas.ShanyrakSearchResultList)
def search_shanyraks(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    type: Optional[str] = Query(None),
    rooms_count: Optional[int] = Query(None),
    price_from: Optional[int] = Query(None),
    price_until: Optional[int] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(models.Shanyrak)

    if type:
        query = query.filter(models.Shanyrak.type == type)
    if rooms_count:
        query = query.filter(models.Shanyrak.rooms_count == rooms_count)
    if price_from:
        query = query.filter(models.Shanyrak.price >= price_from)
    if price_until:
        query = query.filter(models.Shanyrak.price <= price_until)

    total = query.count()
    shanyraks = query.offset(offset).limit(limit).all()
    return schemas.ShanyrakSearchResultList(
        total=total,
        objects=[schemas.ShanyrakSearchResult.model_validate(shanyrak) for shanyrak in shanyraks],
    )