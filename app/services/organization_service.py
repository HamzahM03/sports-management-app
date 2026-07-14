from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.exceptions import OrganizationNotFoundError
from app.models.organization import Organization
from app.repositories.organization_repository import OrganizationRepository
from app.schemas.organization_schema import OrganizationCreate, OrganizationUpdate


class OrganizationService:

    @staticmethod
    def create_organization(
        db: Session,
        organization_data: OrganizationCreate,
    ) -> Organization:

        return OrganizationRepository.create(
            db=db,
            name=organization_data.name,
        )

    @staticmethod
    def get_organization(
        db: Session,
        organization_id: int,
    ) -> Organization:
        
        organization = OrganizationRepository.get_by_id(db=db, organization_id=organization_id)

        if organization is None:
            raise OrganizationNotFoundError(
                f"Organization {organization_id} was not found"
            )

        return organization

    @staticmethod
    def list_organizations(
        db: Session,
    ) -> list[Organization]:

        return OrganizationRepository.get_all(db=db)
    
    @staticmethod
    def update_organization(
        db: Session,
        organization_id: int,
        organization_data: OrganizationUpdate,
    ) -> Organization:

        organization = OrganizationService.get_organization(
            db=db,
            organization_id=organization_id,
        )

        return OrganizationRepository.update(
            db=db,
            organization=organization,
            organization_data=organization_data,
        )
    
    
    @staticmethod
    def delete_organization(
        db: Session,
        organization_id: int,
    ) -> None:

        organization = OrganizationService.get_organization(
            db=db,
            organization_id=organization_id,
        )

        OrganizationRepository.delete(
            db=db,
            organization=organization,
        )