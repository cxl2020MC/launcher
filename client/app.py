from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/webui", StaticFiles(directory="./static"), name="static")

@app.get("/")
def read_root():
    return {"ok": True, "msg": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)