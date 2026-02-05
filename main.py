from fastapi import FastAPI
from database import BaseClass, engine
from routes import router

BaseClass.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
async def home():
    return {"status":"working fine"}