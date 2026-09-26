from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import get_settings

settings = get_settings()

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False} if settings.database_url.startswith("sqlite") else {},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_db_and_tables():
    from app import models  # noqa: F401

    Base.metadata.create_all(bind=engine)


def ensure_default_admin():
    from sqlalchemy import select

    from app.core.security import hash_password
    from app.models import User

    db = SessionLocal()
    try:
        admin = db.execute(select(User).where(User.username == "admin")).scalar_one_or_none()
        if admin is None:
            db.add(
                User(
                    username="admin",
                    email="admin@ai-soc.local",
                    password_hash=hash_password("StrongPass123!"),
                    role="ADMIN",
                    is_active=True,
                )
            )
            db.commit()
    finally:
        db.close()
