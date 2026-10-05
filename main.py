from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import ai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-customer-support01.netlify.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai.router, prefix="/api/ai")


@app.get("/")
def root():
    return {"message": "AI Customer Support API is running"}