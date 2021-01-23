from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from khairo.settings import DEBUG

template = Jinja2Templates(directory="./khairo/templates")

app = FastAPI(debug=DEBUG)
app.mount("/static", StaticFiles(directory="./khairo/static"), name="static")
