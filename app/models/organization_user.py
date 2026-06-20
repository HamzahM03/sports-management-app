from sqlalchemy import ForeignKey, String, DateTime, func, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


#Purpose: What role does a user have in an organization?
class OrganizationUser(Base):
    __tablename__ = "organization_users"

    organization_user_id: Mapped[int] = mapped_column(primary_key=True, index=True)

    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.organization_id"),
        nullable=False,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id"),
        nullable=False,
    )

    role: Mapped[str] = mapped_column(String(50), nullable=False)
    joined_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    organization = relationship("Organization", back_populates="users")
    user = relationship("User", back_populates="organizations")

    __table_args__ = (
        UniqueConstraint("organization_id", "user_id", name="uq_organization_user"),
    )