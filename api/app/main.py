import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def read_root():
    return {"Hello": "World"}


@app.get("/tut")
def read_item():
    return "Tat"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
