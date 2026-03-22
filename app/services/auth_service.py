from sqlmodel import Session, select
from app.models.user import User
from app.core.security import hash_password

from app.core.security import verify_password
from app.core.jwt import create_access_token


def create_user(session: Session, user_data: dict):

    # check if user already exists
    existing_user = session.exec(
        select(User).where(User.email == user_data["email"])
    ).first()

    if existing_user:
        return None

    hashed_password = hash_password(user_data["password"])

    db_user = User(
        email=user_data["email"],
        hashed_password=hashed_password
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


def authenticate_user(session: Session, email: str, password: str):

    user = session.exec(
        select(User).where(User.email == email)
    ).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    token = create_access_token({"sub": user.email})

    return token