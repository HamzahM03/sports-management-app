from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.organization_schema import OrganizationCreate, OrganizationResponse, OrganizationUpdate
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

@router.patch(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def update_organization(
    organization_id: int,
    organization_data: OrganizationUpdate,
    db: Annotated[Session, Depends(get_db)],
):
    return OrganizationService.update_organization(
        db=db,
        organization_id=organization_id,
        organization_data=organization_data,
    )

@router.delete(
    "/{organization_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_organization(
    organization_id: int,
    db: Annotated[Session, Depends(get_db)],
) -> None:
    OrganizationService.delete_organization(
        db=db,
        organization_id=organization_id,
    )