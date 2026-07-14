from fastapi import FastAPI

from app.routers.organization_routes import router as organization_router
from app.exception_handlers import organization_not_found_handler
from app.exceptions import OrganizationNotFoundError


app = FastAPI(
    title="Sports Management Platform",
)

app.add_exception_handler(
    OrganizationNotFoundError,
    organization_not_found_handler,
)

app.include_router(organization_router)


@app.get("/")
def health_check():
    return {"status": "ok"}