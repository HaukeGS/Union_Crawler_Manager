from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"Hello": "World"}


@app.get("/tut")
def read_item():
    return "Tat"
