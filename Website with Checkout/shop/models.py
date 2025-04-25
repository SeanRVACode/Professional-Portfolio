from __future__ import annotations  # For forward references in type hints
from datetime import datetime
from typing import TYPE_CHECKING, Optional
import sqlalchemy as sa
import sqlalchemy.orm as so  # orm stands for Object Relational Mapping. SO stands for SQLAlchemy ORM
from shop import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from shop import login


@login.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


if TYPE_CHECKING:
    from .payment_method import PaymentMethod  # type: ignore
    from .order import Order  # type: ignore


class User(UserMixin, db.Model):
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
    payment_methods: so.Mapped[list["StoredPaymentMethod"]] = so.relationship(back_populates="user")

    def __repr__(self):
        return f"<User {self.username}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class StoredPaymentMethod(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("user.id"))
    stripe_payment_method_id: so.Mapped[str] = so.mapped_column(sa.String(255), unique=True)
    last4: so.Mapped[str] = so.mapped_column(sa.String(4))  # Last 4 digits of card for display
    card_type: so.Mapped[str] = so.mapped_column(sa.String(32))  # visa, mastercard, etc.
    expiry_month: so.Mapped[int] = so.mapped_column(sa.Integer)
    expiry_year: so.Mapped[int] = so.mapped_column(sa.Integer)
    is_default: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=False)
    created_at: so.Mapped[datetime] = so.mapped_column(sa.DateTime, default=sa.func.now())

    # Relationship
    user: so.Mapped["User"] = so.relationship(back_populates="payment_methods")

    def __repr__(self):
        return f"<StoredPaymentMethod {self.id} - {self.card_type} *{self.last4}>"


class Order(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("user.id"))
    stripe_payment_intent_id: so.Mapped[str] = so.mapped_column(sa.String(255), unique=True)
    stripe_session_id: so.Mapped[str] = so.mapped_column(sa.String(255), unique=True)
    amount: so.Mapped[float] = so.mapped_column(sa.Float)
    status: so.Mapped[str] = so.mapped_column(sa.String(64))  # pending, completed, failed, etc.
    created_at: so.Mapped[datetime] = so.mapped_column(sa.DateTime, default=sa.func.now())

    # Relationship
    user: so.Mapped["User"] = so.relationship(back_populates="orders")

    def __repr__(self):
        return f"<Order {self.id} - {self.status}>"
