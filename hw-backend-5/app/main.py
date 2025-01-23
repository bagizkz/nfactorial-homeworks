from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .repository import BooksRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")
repository = BooksRepository()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# @app.get("/books")
# def get_books(request: Request):
#     books = repository.get_all()
#     return templates.TemplateResponse(
#         "books/index.html",
#         {"request": request, "books": books},
#     )


# (сюда писать решение)



@app.get("/books")
def get_books(request: Request, page: int = 1):
    books_per_page = 10 
    start = (page - 1) * books_per_page
    end = start + books_per_page

    books = repository.get_all()[start:end]

    has_next = len(repository.get_all()) > end

    return templates.TemplateResponse(
        "books/index.html", 
        {"request": request, "books": books, "page": page, "has_next": has_next}
    )


@app.get("/books/new")
def new_book(request: Request):
    return templates.TemplateResponse("books/new.html", {"request": request})


@app.post("/books")
def create_book(request: Request, title: str = Form(...), author: str = Form(...), 
                year: int = Form(...), total_pages: int = Form(...), genre: str = Form(...)):
    new_book = {
        "id": len(repository.get_all()) + 1, 
        "title": title,
        "author": author,
        "year": year,
        "total_pages": total_pages,
        "genre": genre
    }

    repository.save(new_book)  

    return RedirectResponse(url="/books", status_code=303)


@app.get("/books/{id}")
def get_book(request: Request, id: int):
    book = repository.get_one(id)
    if book is None:
        return "Not Found", 404
    
    return templates.TemplateResponse("books/detail.html", {"request": request, "book": book})



# HW5 - редактирование

@app.get("/books/{id}/edit")
def edit_book(request: Request, id: int):
    book = repository.get_one(id)
    if book is None:
        return "Not Found", 404

    return templates.TemplateResponse("books/edit.html", {"request": request, "book": book})

@app.post("/books/{id}/edit")
def update_book(request: Request, id: int, title: str = Form(...), author: str = Form(...),
                year: int = Form(...), total_pages: int = Form(...), genre: str = Form(...)):
    book = repository.get_one(id)
    if book is None:
        return "Not Found", 404

    book["title"] = title
    book["author"] = author
    book["year"] = year
    book["total_pages"] = total_pages
    book["genre"] = genre

    return RedirectResponse(url=f"/books/{id}", status_code=303)


# HW5 - удаление

@app.post("/books/{id}/delete")
def delete_book(id: int):
    book = repository.get_one(id)
    if book is None:
        return "Not Found", 404

    repository.books = [b for b in repository.books if b["id"] != id]  # Удаляем книгу
    return RedirectResponse(url="/books", status_code=303)

# (конец решения)
