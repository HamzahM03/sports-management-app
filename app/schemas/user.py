from datetime import datetime

from pydantic import BaseModel, ConfigDict


class OrganizationCreate(BaseModel):
    name: str


class OrganizationUpdate(BaseModel):
    name: str


class OrganizationResponse(BaseModel):
    organization_id: int
    name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)