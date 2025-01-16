from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

comments = []

class Comment(BaseModel):
    text: str
    category: str



# Параметры пагинации
COMMENTS_PER_PAGE = 5


# Главная страница
@app.get("/", response_class=HTMLResponse)
async def read_root(page: int = 1):
    # индекс начала и конца пагинации
    start = (page - 1) * COMMENTS_PER_PAGE
    end = start + COMMENTS_PER_PAGE

    comments_page = comments[start:end]




    # HTML
    comments_html = "".join(
        f"<p>{comment.text} ({comment.category})</p>" for comment in comments_page
    )

    html_content = f"""
    <html>
        <head>
            <title>VoxPop</title>
            <style>
                body {{ font-family: Arial, sans-serif; }}
                .comment-form {{ margin-bottom: 20px; }}
            </style>
        </head>
        <body>
            <br><h1>Salem, VoxPop</h1><br>
            <div class="comment-form">
                <h3>Добавить комментарии:</h3>
                <form action="/comments/" method="post">
                    <label for="text">Текст комментария:</label><br>
                    <input type="text" id="text" name="text" required><br><br>
                    <label for="category">Категория:</label><br>
                    <select id="category" name="category" required>
                        <option value="positive">Позитивный</option>
                        <option value="negative">Негативный</option>
                    </select><br><br>
                    <input type="submit" value="Отправить">
                </form>
            </div>
            <div class="comments">
                <h3>Все комментарии:</h3>
                {comments_html}
            </div>
            <div class="pagination">
                {'<a href="/?page=' + str(page - 1) + '">Пред</a> ' if page > 1 else ''}
                {'<a href="/?page=' + str(page + 1) + '">След</a>' if len(comments) > page * COMMENTS_PER_PAGE else ''}
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Добавление коммент
@app.post("/comments/")
async def add_comment(text: str = Form(...), category: str = Form(...)):
    new_comment = Comment(text=text, category=category)
    comments.insert(0, new_comment)  # в начало
    return HTMLResponse(content="<html><body><h2>Комментарий добавлен!</h2><a href='/'>Назад</a></body></html>")