import uvicorn
from fastapi import FastAPI
from routes.course import course

app = FastAPI()


app.include_router(course)

def start_server():
    # print('Starting Server...')       

    uvicorn.run(
        "app",
        host="0.0.0.0",
        port=8020,
        log_level="debug",
        reload=True,
    )
    # webbrowser.open("http://127.0.0.1:8020")

if __name__ == "__main__":
    start_server()