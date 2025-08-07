import uvicorn
from fastapi import FastAPI

from utils.config import settings

app = FastAPI(title='Japanese Learning Service')


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run('main:app', host=settings.run.host, port=settings.run.port, reload=settings.run.reload)

# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
