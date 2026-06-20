from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class ParticipantPackage(Base):
    __tablename__ = "participant_packages"

    participant_package_id: Mapped[int] = mapped_column(primary_key=True, index=True)

    participant_id: Mapped[int] = mapped_column(
        ForeignKey("participants.participant_id"),
        nullable=False,
        index=True,
    )

    camp_package_id: Mapped[int] = mapped_column(
        ForeignKey("camp_packages.camp_package_id"),
        nullable=False,
        index=True,
    )

    package_name_at_purchase: Mapped[str] = mapped_column(String(100), nullable=False)
    price_paid: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    total_sessions: Mapped[int] = mapped_column(Integer, nullable=False)
    remaining_sessions: Mapped[int] = mapped_column(Integer, nullable=False)

    purchased_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    participant = relationship("Participant")
    camp_package = relationship("CampPackage", back_populates="participant_packages")
    check_ins = relationship("CheckIn", back_populates="participant_package")