from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware

from .settings import Settings
from ..utils.init_db import create_tables


def create_application(
        router: APIRouter,
        settings: Settings,
        create_tables_on_start: bool = True,
) -> FastAPI:
    app = FastAPI(
        debug=bool(settings.DEBUG),
        title=settings.TITLE,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)

    @app.on_event("startup")
    def on_startup() -> None:
        """
        Initializes the database tables when the application starts up.
        """
        create_tables()

    return app
