from fastapi import FastAPI

app = FastAPI()


@app.get("/") # This is the route 127.0.0.1:8000/
async def home():
    return {"message": "Hello World Dikshika"}