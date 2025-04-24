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

    def __repr__(self):
        return f"<User {self.username}"
