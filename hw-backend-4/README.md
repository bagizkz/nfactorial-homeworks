# hw-backend-4
[Скриншот test_task1.py](./test_task1.py)

## Сделано:
- GET /books: список книг. Страница = 10 книг. По дефолту отображается первая страница, кнопки "вперед" и "назад". Если страница первая, не показывается "назад".
- GET /books/{id}: Страница о книге. Если не найдена - “Not Found”
- GET /books/new: форма добавления книг. Принимает параметры: title, author, year, total_pages, genre

## Стек:
- **FastAPI**
- **Uvicorn** 
- **Jinja2Templates** 
- **Pydantic** 
- **HTML**