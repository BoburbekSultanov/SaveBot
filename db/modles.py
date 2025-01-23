import enum

from aiogram.utils.markdown import text

from db import Base
from db.utils import CreatedModel

from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, Mapped
from sqlalchemy import String, Integer, ForeignKey, BigInteger, Enum, DateTime, Column, func


class MyEnum(enum.Enum):
    image = "image"
    video = "video"
    documents = "document"
    others = "others"


tz = "TIMEZONE('Asia/Tashkent', NOW())"




class Category(CreatedModel):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_type: Mapped[str] = mapped_column(Enum(MyEnum))

    images: Mapped["Image"] = relationship(back_populates="user", cascade="all, delete-orphan")
    videos: Mapped["Video"] = relationship(back_populates="user", cascade="all, delete-orphan")
    documents: Mapped["Document"] = relationship(back_populates="user", cascade="all, delete-orphan")
    others: Mapped["Other"] = relationship(back_populates="user", cascade="all, delete-orphan")


class Image(CreatedModel):  # noqa
    file_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"))

    categories: Mapped["Category"] = relationship(back_populates="customer", cascade="all, delete-orphan")


class Video(CreatedModel):
    file_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"))

    categories: Mapped["Category"] = relationship(back_populates="customer", cascade="all, delete-orphan")


class Document(CreatedModel): # noqa
    file_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"))

    categories: Mapped["Category"] = relationship(back_populates="customer", cascade="all, delete-orphan")


class Other(CreatedModel):
    file_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"))

    categories: Mapped["Category"] = relationship(back_populates="customer", cascade="all, delete-orphan")


metadata = Base.metadata
