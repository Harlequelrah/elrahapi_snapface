from fastapi import FastAPI
from .settings.database import engine, authentication
from .settings.models_metadata import target_metadata
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from .snapface.router import app_snapface
from .settings.logger.router import app_logger
from .settings.logger.model import Logger
app = FastAPI()

target_metadata.create_all(bind=engine)

@app.get("/")
async def hello():
    return {"message":"hello"}
app.include_router(app_snapface)
app.include_router(app_logger)

app.add_middleware(
    ErrorHandlingMiddleware,
    LoggerMiddlewareModel=Logger,
    session_factory=authentication.session_factory,
)

