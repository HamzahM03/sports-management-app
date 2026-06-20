from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class CheckIn(Base):
    __tablename__ = "check_ins"

    check_in_id: Mapped[int] = mapped_column(primary_key=True, index=True)

    participant_id: Mapped[int] = mapped_column(
        ForeignKey("participants.participant_id"),
        nullable=False,
        index=True,
    )

    session_id: Mapped[int] = mapped_column(
        ForeignKey("sessions.session_id"),
        nullable=False,
        index=True,
    )

    participant_package_id: Mapped[int] = mapped_column(
        ForeignKey("participant_packages.participant_package_id"),
        nullable=False,
        index=True,
    )

    checked_in_by_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id"),
        nullable=False,
        index=True,
    )

    checked_in_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    status: Mapped[str] = mapped_column(String(50), nullable=False, default="present")

    participant = relationship("Participant")
    session = relationship("Session", back_populates="check_ins")
    participant_package = relationship("ParticipantPackage", back_populates="check_ins")
    checked_in_by = relationship("User")

    __table_args__ = (
        UniqueConstraint("participant_id", "session_id", name="uq_participant_session_check_in"),
    )