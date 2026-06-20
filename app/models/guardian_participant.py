from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship as orm_relationship

from app.models.base import Base


class GuardianParticipant(Base):
    __tablename__ = "guardian_participants"

    guardian_participant_id: Mapped[int] = mapped_column(primary_key=True, index=True)

    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.organization_id"),
        nullable=False,
        index=True,
    )

    guardian_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id"),
        nullable=False,
        index=True,
    )

    participant_id: Mapped[int] = mapped_column(
        ForeignKey("participants.participant_id"),
        nullable=False,
        index=True,
    )

    relationship: Mapped[str | None] = mapped_column(String(50), nullable=True)

    participant = orm_relationship("Participant", back_populates="guardians")
    guardian = orm_relationship("User")

    __table_args__ = (
        UniqueConstraint(
            "organization_id",
            "guardian_user_id",
            "participant_id",
            name="uq_guardian_participant",
        ),
    )