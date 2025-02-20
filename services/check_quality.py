import subprocess

def check_quality(path):
    """Check the quality of the code"""
    result = subprocess.run(["pylint", path], capture_output=True, text=True)
    return result.returncode

