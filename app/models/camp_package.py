from datetime import datetime
from decimal import Decimal

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class CampPackage(Base):
    __tablename__ = "camp_packages"

    camp_package_id: Mapped[int] = mapped_column(primary_key=True, index=True)

    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.organization_id"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    session_count: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    organization = relationship("Organization")
    participant_packages = relationship("ParticipantPackage", back_populates="camp_package")