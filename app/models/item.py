# from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.database import Base

# from sqlalchemy.orm import relationship


# if TYPE_CHECKING:
#     from .user import User  # noqa: F401


class Item(Base):  # noqa: WPS110
    """Item class."""

    __tablename__ = "item"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    # owner = relationship("User", back_populates="items")
