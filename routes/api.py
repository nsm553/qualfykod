import os
from fastapi import FastAPI, HTTPException
from services import detect_bugs

app = FastAPI()

SRC_DIR = "src_dir"

@app.get("/analyze/bugs")
def find_bugs():
    """ detect bugs """
    files = os.listdir(SRC_DIR)
    if not files:
        raise HTTPException(status_code=400, detail="No files are found")
    
    results = []
    for file in files:
        path = os.path.join(SRC_DIR, file)
        result = detect_bugs.check_syntax(path)

