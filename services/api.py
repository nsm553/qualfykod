import os
import uvicorn
from fastapi import FastAPI, HTTPException
from detect_bugs import check_syntax
from check_code import find_bugs
from check_quality import check_quality
from check_performance import check_performance


app = FastAPI()

SRC_DIR = "data"

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/analyze/code")
async def analyze_code():
    """ 
    detect bugs 
    check quality
    check performance
    """
    results = find_bugs()

    if not results:
        raise HTTPException(status_code=400, detail="No files are found")

    quality = check_quality(results)

    if not quality:
        raise HTTPException(status_code=400, detail="No quality is found")

    performance = check_performance(results)

    if not performance:
        raise HTTPException(status_code=400, detail="No performance is found")
    
    return {

        "results": results,
        "quality": quality,
        "performance": performance
    }.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)