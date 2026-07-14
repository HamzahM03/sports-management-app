#This file is used simply to talk to database. 
from sqlalchemy.orm import Session

from app.models.organization import Organization

from app.schemas.organization_schema import OrganizationCreate

class OrganizationRepository:

    @staticmethod
    def create(
        db: Session,
        organization_data: OrganizationCreate,
    ) -> Organization:

        organization = Organization(
            **organization_data.model_dump()
        )

        db.add(organization)
        db.commit()
        db.refresh(organization)

        return organization

    @staticmethod
    def get_by_id(
        db: Session,
        organization_id: int,
    ) -> Organization | None:

        return (
            db.query(Organization)
            .filter(
                Organization.organization_id == organization_id
            )
            .first()
        )

    @staticmethod
    def get_all(
        db: Session,
    ) -> list[Organization]:

        return db.query(Organization).all()