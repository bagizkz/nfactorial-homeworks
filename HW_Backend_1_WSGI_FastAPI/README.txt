# Backend Homework: WSGI & FastAPI

## Задания:

### 1. `server-ping-pong` (WSGI)
       ```bash
       gunicorn server_ping_pong:application
       ```

       - `http://127.0.0.1:8000/ping` — ответ `pong` || `Not Found`.

### 2. `server-request-info` (WSGI)
       ```bash
       gunicorn server_request_info:application
       ```

       - `http://127.0.0.1:8000/info` — инфо о запросе.

### 3, 4, 5 `fastapi-hello` `fastapi-meaning-life` `fastapi-nfactorial` (FastAPI)

       ```bash
       uvicorn fastapi_app:app --reload
       ```
    - 3. `http://127.0.0.1:8000/` — ответ:
         ```
           "message": "Hello, nfactorial!"
         ```

    2. POST-запрос `http://127.0.0.1:8000/meaning-of-life` — ответ:
         ```
           "meaning": "42"
         ```

    3. Перейдите по адресу: `http://127.0.0.1:8000/5` — ответ:
         ```
           "nfactorial": 120
         ```