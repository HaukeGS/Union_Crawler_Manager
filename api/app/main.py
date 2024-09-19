import uvicorn
from fastapi import FastAPI, Request
from typing import List, Optional
import sqlite3
con = sqlite3.connect("Session.db")
cur = con.cursor()

app = FastAPI()


def initDatabase():
    pass

@app.get("/init")
def read_root():
    cur.execute("CREATE TABLE Crawler(type, tech_level, upkeep, remaining_upgrade_cost, structure_points, lance_id, bay_id, storage_id, armoury_id)")
    cur.execute("CREATE TABLE Lance(lance_id, mach_id)")
    cur.execute("CREATE TABLE Mech(mach_id, structure_points, energy_points, heat_capacity, salvage_vaue_sum, chassis_id, system_id, module_id)")
    cur.execute("CREATE TABLE Storage(storage_id, scrap_id, mech_parts_id)")
    cur.execute("CREATE TABLE Scrap(scrap_id, tech_level)")
    cur.execute("CREATE TABLE (type, tech_level, upkeep, remaining_upgrade_cost, structure_points, lance_id, bay_id, storage_id, armoury_id)")

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
