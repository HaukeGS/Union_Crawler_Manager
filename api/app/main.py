import uvicorn
from fastapi import FastAPI, Request
from typing import List, Optional

app = FastAPI()


@app.get("/hello")
def read_root():
    return {"Hello": "World"}


@app.get("/get/{levels:path}")
async def read_item(levels: str, q: Optional[str] = None):
    # Split the levels by "/" to get a list of them
    level_list = levels.split("/")
    # Combine all levels into a single string
    item_id = " ".join(level_list)

    if q:
        return {"item": item_id, "q": q}
    return {"item": item_id}

@app.post("/set/{levels:path}")
async def read_item(request: Request, levels: str, q: Optional[str] = None):
    test = await request.json
    # Split the levels by "/" to get a list of them
    level_list = levels.split("/")
    # Combine all levels into a single string
    item_id = " ".join(level_list)
    item_id += str(test)
    if q:
        return {"item": item_id, "q": q}
    return {"item": item_id}
@app.get("/get/Crawler/lance")
def getCrawlerInfo():
    return "Tat"

@app.get("/get/Crawler/")
def getCrawlerInfo():
    return "Tat"
@app.post("/set/Crawler")
def setCrawlerStats():
    return "Tat"




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
