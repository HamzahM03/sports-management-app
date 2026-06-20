from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Waiver(Base):
    __tablename__ = "waivers"

    waiver_id: Mapped[int] = mapped_column(primary_key=True, index=True)

    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.organization_id"),
        nullable=False,
        index=True,
    )

    waiver_name: Mapped[str] = mapped_column(String(150), nullable=False)
    s3_key: Mapped[str | None] = mapped_column(String(500), nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    organization = relationship("Organization")
    signed_waivers = relationship("SignedWaiver", back_populates="waiver")