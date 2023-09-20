from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
import uvicorn
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# Simple chatbot response function (replace with your chatbot logic)
def chatbot_response(user_message):
    return f"Chatbot says: You said '{user_message}'"


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/chatbot")
async def chatbot(message: str):
    response = chatbot_response(message)
    return {"response": response}


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8000
    reload = True

    uvicorn.run("main:app", host=host, port=port, reload=reload)
