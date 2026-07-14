from datetime import datetime

from pydantic import BaseModel, ConfigDict


class OrganizationBase(BaseModel):
    name: str
    email: str | None = None
    phone: str | None = None
    address: str | None = None

class OrganizationCreate(BaseModel):
    pass


class OrganizationUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    address: str | None = None

class OrganizationRead(BaseModel):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class OrganizationResponse(BaseModel):
    organization_id: int
    name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)