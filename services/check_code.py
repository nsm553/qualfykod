import os

from detect_bugs import check_syntax
from fastapi import HTTPException

SRC_DIR = "data"


async def root():
    return {"message": "Hello"}


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

        results.append({
            "file": file,
            "bugs": result
        })
    return results

def scan_directory(directory):
    """Recursively scan directory and check for bugs in Python files"""
    all_results = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                try:
                    result = check_syntax(path)
                    all_results.append({
                        "file": os.path.relpath(path, directory),
                        "bugs": result
                    })
                except Exception as e:
                    all_results.append({
                        "file": os.path.relpath(path, directory),
                        "error": str(e)
                    })
    
    return all_results

async def find_bugs_recursive():
    """Detect bugs in all Python files recursively"""
    if not os.path.exists(SRC_DIR):
        raise HTTPException(status_code=400, detail="Source directory not found")
        
    results = scan_directory(SRC_DIR)
    if not results:
        raise HTTPException(status_code=400, detail="No Python files found")
        
    return results
