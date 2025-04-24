from __future__ import annotations  # For forward references in type hints
from datetime import datetime
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so  # orm stands for Object Relational Mapping. SO stands for SQLAlchemy ORM
from app import db


class User(db.Model):
    # These are not instance variables, but class variables with type annotations
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))
    # Personal information
    first_name: so.Mapped[str] = so.mapped_column(sa.String(64))
    last_name: so.Mapped[str] = so.mapped_column(sa.String(64))
    phone_number: so.Mapped[Optional[str]] = so.mapped_column(sa.String(20), nullable=True)

    # Address information
    address_line1: so.Mapped[Optional[str]] = so.mapped_column(sa.String(128), nullable=True)
    address_line2: so.Mapped[Optional[str]] = so.mapped_column(sa.String(128), nullable=True)
    city: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64), nullable=True)
    state: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64), nullable=True)
    postal_code: so.Mapped[Optional[str]] = so.mapped_column(sa.String(20), nullable=True)
    country: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64), nullable=True)

    # Account information
    created_at: so.Mapped[datetime] = so.mapped_column(sa.DateTime, default=sa.func.now())
    last_login: so.Mapped[Optional[datetime]] = so.mapped_column(sa.DateTime, nullable=True)
    is_active: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=True)

    # Relationships
    orders: so.Mapped[list["Order"]] = so.relationship(back_populates="user")
    payment_methods: so.Mapped[list["PaymentMethod"]] = so.relationship(back_populates="user")

    def __repr__(self):
        return f"<User {self.username}"
