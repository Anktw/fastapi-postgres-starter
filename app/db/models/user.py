from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=True, default=None)
    last_name = Column(String, nullable=True, default=None)

    @validates('email')
    def lowercase_email(self, key, email):
        return email.lower()