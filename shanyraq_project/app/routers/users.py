from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, security
from ..database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

router = APIRouter(prefix="/auth/users")

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

@router.patch("/me", response_model=schemas.User)
def update_user(user: schemas.UserUpdate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    if user.password:
        hashed_password = security.get_password_hash(user.password)
        user.password = hashed_password
    else:
        user.password = current_user.hashed_password
    for field, value in user.dict(exclude_unset=True).items():
        setattr(current_user, field, value)
    db.commit()
    db.refresh(current_user)
    return current_user

@router.get("/me", response_model=schemas.User)
def read_user(current_user: models.User = Depends(get_current_user)):
    return current_user

@router.post("/favorites/shanyraks/{shanyrak_id}")
def add_to_favorites(shanyrak_id: int, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_shanyrak = db.query(models.Shanyrak).filter(models.Shanyrak.id == shanyrak_id).first()
    if db_shanyrak is None:
        raise HTTPException(status_code=404, detail="Shanyrak not found")
    current_user.favorite_shanyraks.append(db_shanyrak)
    db.commit()
    return {"message": "Added to favorites"}

@router.get("/favorites/shanyraks", response_model=schemas.FavoriteShanyrakList)
def read_favorites(current_user: models.User = Depends(get_current_user)):
    return schemas.FavoriteShanyrakList(shanyraks=[schemas.FavoriteShanyrak.model_validate(shanyrak) for shanyrak in current_user.favorite_shanyraks])

@router.delete("/favorites/shanyraks/{shanyrak_id}")
def remove_from_favorites(shanyrak_id: int, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_shanyrak = db.query(models.Shanyrak).filter(models.Shanyrak.id == shanyrak_id).first()
    if db_shanyrak is None:
        raise HTTPException(status_code=404, detail="Shanyrak not found")
    current_user.favorite_shanyraks.remove(db_shanyrak)
    db.commit()
    return {"message": "Removed from favorites"}