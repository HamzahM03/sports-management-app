from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Session(Base):
    __tablename__ = "sessions"

    session_id: Mapped[int] = mapped_column(primary_key=True, index=True)

    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.organization_id"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(150), nullable=False)
    starts_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    ends_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    organization = relationship("Organization")
    check_ins = relationship("CheckIn", back_populates="session")