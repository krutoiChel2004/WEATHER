import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base

from routers.router_data import router as router_data

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)

app.include_router(router_data)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
