import uvicorn
from fastapi import FastAPI

from backend.utils.config import settings
from backend.src.api.v1  import router as v1_router

app = FastAPI(title='Japanese Learning Service')

app.include_router(v1_router)


if __name__ == "__main__":
    uvicorn.run('main:app', host=settings.run.host, port=settings.run.port, reload=settings.run.reload)

# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
