from ..config.database import Base, engine
from ..models.user import User


def create_tables():
    """
    Creates all database tables defined in the application.
    """
    Base.metadata.create_all(bind=engine)
    User.metadata.create_all(bind=engine)
