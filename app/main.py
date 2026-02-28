from fastapi import FastAPI
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        docs_url="/docs" if settings.DEBUG else None,  # hide docs in production
        redoc_url="/redoc" if settings.DEBUG else None,  # hide redoc in production
    )

    register_routes(app)

    return app


def register_routes(app: FastAPI):
    from app.api.v1.routes import health

    app.include_router(health.router, prefix="/api/v1", tags=["Health"])


app = create_app()
