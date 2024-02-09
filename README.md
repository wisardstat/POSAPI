# fastapi-tutorial-mssql
The FastAPI SQL database tutorial modified to use `mssql+pyodbc`.

Proof-of-concept that using FastAPI with mssql does *not* require
aioodbc and `async def` for path operation functions.

# How to run:

## create virtual environment

```
python -m venv venv
```

```
# for linux
source .venv/myproject/bin/activate

or
# for windows
venv\Scripts\activate.bat

venv\Scripts\deactivate.bat
```

## Creare Project by poentry
ติดตั้ง poentry สำหรับกำหนดรายละเอียดของ Project
```
pip install poetry
```

Start poentry เพื่อใส่รายละเอียด
```
poetry init
```

เพิ่ม Library และ package
```
poetry add fastapi "uvicorn[standard]" pydantic email-validator
```

## Run Fast-API
To launch uvicorn:
```
uvicorn sql_app.main:app --reload

uvicorn inventory_app.main:app --reload
```

## Link เข้าเว็บ
```
http://127.0.0.1:8000/docs
```

```
python -m pip freeze > requirements.txt
```

## Refrence
Then load the fancy interactive docs page at

http://localhost:8000/docs

Details at

https://fastapi.tiangolo.com/tutorial/

and

https://fastapi.tiangolo.com/tutorial/sql-databases/

GitHub discussion:

https://github.com/sqlalchemy/sqlalchemy/issues/6521

Notes:

- You may need to tweak `SQLALCHEMY_DATABASE_URL` in database.py to connect
to your SQL Server instance.