from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.api.exeption_handlers import request_validation_exception_handler
from app.api.routers.links import router as links_router
from app.api.routers.notes import router as notes_router
from app.core.config import get_settings
from app.api.routers.pages import router as router_page

from fastapi.staticfiles import StaticFiles

settings = get_settings()
app = FastAPI(title=settings.app_name, version="0.1.0")
app.mount('/static', StaticFiles(directory="static"), name="static")

app.add_exception_handler(RequestValidationError,request_validation_exception_handler)

app.include_router(links_router)
app.include_router(router_page)
app.include_router(notes_router)

@app.get('/health', tags=['service'])
def health_check()-> dict[str,str]:
  return {"status": "ok"}



