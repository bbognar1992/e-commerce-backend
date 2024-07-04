from config.settings import settings
from config.setup import create_application
from routers.api import router

app = create_application(router, settings)
