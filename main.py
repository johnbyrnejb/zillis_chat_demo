import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def chatbot_response(user_message):
    return f"Chatbot says: You said '{user_message}'"


@app.get("/", response_class=HTMLResponse)
async def chatbot_page(request: Request):
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
