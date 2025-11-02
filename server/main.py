# vasu - server
# author - nlkguy
# /server/main.py



from fastapi import FastAPI
from fastapi import Request
import random

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

@app.get("/")
def root():
    return {
        "status" : "Vasu Running",
        "docs"  : "docs",
        "ingest" : "ingest",
        "docs"  : "https://github.com/nlkguy/vasu-siem-xdr",
        "author" : "https://github.com/nlkguy"
    }

@app.get("/recent")
def recent():
    recents = {}
    for i in range(20):
        recents[i] = random.random()
    return recents





# ---------------- ingest -----------------------

@app.post("/ingest")
async def ingest(request: Request):
    data = await request.json()
    print(data)
    return {"status": "OKAY!"}

