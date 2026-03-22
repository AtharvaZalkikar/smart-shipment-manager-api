from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class User(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)

    email: str = Field(index=True, unique=True)         # unique users & it is "Indexed" for faster lookup during logins

    hashed_password: str                                # stores encrypted password (never plain text)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )