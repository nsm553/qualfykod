import os
import uvicorn
from fastapi import FastAPI, HTTPException
from detect_bugs import check_syntax

app = FastAPI()

SRC_DIR = "data"

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/analyze/bugs")
async def find_bugs():
    """ detect bugs """
    files = os.listdir(SRC_DIR)
    if not files:
        raise HTTPException(status_code=400, detail="No files are found")
    
    results = []
    for file in files:
        path = os.path.join(SRC_DIR, file)
        result = check_syntax(path)
        print ("result: " + result)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)