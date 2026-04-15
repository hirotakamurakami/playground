from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Hello World</h1>
    <p>Current time: {now}</p>
    """
