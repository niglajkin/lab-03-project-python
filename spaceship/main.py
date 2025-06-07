from spaceship.app import make_app
from spaceship.config import Settings
from spaceship.routers.api import router as api_router

app = make_app(Settings())
app.include_router(api_router, prefix="/api")