from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn
app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def hello_world():
    return "FastAPI Hello world! Version 1"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)