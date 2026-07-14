from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.organization_schema import OrganizationCreate, OrganizationResponse
from app.services.organization_service import OrganizationService


router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)


@router.post(
    "/",
    response_model=OrganizationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_organization(
    organization_data: OrganizationCreate,
    db: Annotated[Session, Depends(get_db)],
):
    return OrganizationService.create_organization(
        db=db,
        organization_data=organization_data,
    )


@router.get(
    "/",
    response_model=list[OrganizationResponse],
)
def list_organizations(
    db: Annotated[Session, Depends(get_db)],
):
    return OrganizationService.list_organizations(db=db)


@router.get(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def get_organization(
    organization_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    
    return OrganizationService.get_organization(
        db=db,
        organization_id=organization_id,
    )