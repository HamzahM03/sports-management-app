from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship as orm_relationship

from app.models.base import Base


class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"

    emergency_contact_id: Mapped[int] = mapped_column(primary_key=True, index=True)

    participant_id: Mapped[int] = mapped_column(
        ForeignKey("participants.participant_id"),
        nullable=False,
        index=True,
    )

    contact_name: Mapped[str] = mapped_column(String(150), nullable=False)
    relationship: Mapped[str | None] = mapped_column(String(50), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)

    participant = orm_relationship("Participant", back_populates="emergency_contacts")