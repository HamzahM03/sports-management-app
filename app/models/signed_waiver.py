from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class SignedWaiver(Base):
    __tablename__ = "signed_waivers"

    signed_waiver_id: Mapped[int] = mapped_column(primary_key=True, index=True)

    participant_id: Mapped[int] = mapped_column(
        ForeignKey("participants.participant_id"),
        nullable=False,
        index=True,
    )

    waiver_id: Mapped[int] = mapped_column(
        ForeignKey("waivers.waiver_id"),
        nullable=False,
        index=True,
    )

    signed_file_s3_key: Mapped[str | None] = mapped_column(String(500), nullable=True)

    signed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    status: Mapped[str] = mapped_column(String(50), nullable=False, default="signed")

    participant = relationship("Participant")
    waiver = relationship("Waiver", back_populates="signed_waivers")

    __table_args__ = (
        UniqueConstraint("participant_id", "waiver_id", name="uq_participant_waiver"),
    )