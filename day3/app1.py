from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run("app1:app", reload=True)
