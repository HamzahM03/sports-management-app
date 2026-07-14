from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class ParticipantCreate(BaseModel):
    organization_id: int
    first_name: str
    last_name: str
    date_of_birth: date | None = None
    notes: str | None = None


class ParticipantUpdate(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date | None = None
    notes: str | None = None
    status: str


class ParticipantResponse(BaseModel):
    participant_id: int
    organization_id: int
    first_name: str
    last_name: str
    date_of_birth: date | None
    notes: str | None
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)