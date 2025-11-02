# vasu - server
# author - nlkguy
# /server/main.py

# temp stirage in json file
# redo in sqlite local db
# todo - postgreql

from datetime import datetime


from fastapi import FastAPI
from fastapi import Request
from typing import Any, Dict

import random, os, json
# ✅ ⚠️ ❌ 
app = FastAPI(
    title="Vasu Server"
)

# allow cors - for agent and dashboard
# re-do later <--------
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

LOG_DATA_FILE = "data/logs.json"
os.makedirs("data", exist_ok=True)



# ---- funcs -------


# save log to file
def save_log(payload: Dict[str, Any]) -> None:
    try:
        with open(LOG_DATA_FILE, "a") as f:
            json.dump(payload, f)
            f.write("\n")
    except Exception as e:
        print(f"Error writing log: {e}")

# load logs from file
def load_logs(limit: int = 20):
    if not os.path.exists(LOG_DATA_FILE):
        return []
    try:
        with open(LOG_DATA_FILE, "r") as f:
            lines = f.readlines()
        return [json.loads(line) for line in lines[-limit:]]
    except Exception as e:
        print(f" Error reading logs: {e}")
        return []

# ---- routes -------

@app.get("/")
def root():
    return {
        "status" : "Vasu Running",
        "docs"  : "docs",
        "ingest" : "ingest",
        "repo"  : "https://github.com/nlkguy/vasu-siem-xdr",
        "author" : "https://github.com/nlkguy"
    }



@app.get("/status")
def status():
    log_count = 0
    if os.path.exists(LOG_DATA_FILE):
        log_count = sum(1 for _ in open(LOG_DATA_FILE))
    return {
        "server_time": datetime.now().isoformat(),
        "log_count": log_count,
        "random_seed": random.randint(1000, 9999),
        "status": "active"
    } 


# ---------------- ingest -----------------------

@app.post("/ingest")
async def ingest(request: Request):
    data = await request.json()
    print(data)
    return {"status": "OKAY!"}

