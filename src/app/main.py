from .config.settings import settings
from .config.setup import create_application
from .routers import router

app = create_application(router, settings)
