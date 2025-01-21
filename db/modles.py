from db import Base
from db.utils import CreatedModel

from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, Mapped
from sqlalchemy import String, Integer, ForeignKey, BigInteger




class User(CreatedModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    phone_number: Mapped[str] = mapped_column(String(255))

    customers: Mapped["Customer"] = relationship(back_populates="user", cascade="all, delete-orphan")
    employees: Mapped["Employee"] = relationship(back_populates="user", cascade="all, delete-orphan")



class Customer(CreatedModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship(back_populates="customers")
    posts: Mapped["Post"] = relationship(back_populates="customer", cascade="all, delete-orphan")


class Post(CreatedModel):

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    file: Mapped[str] = mapped_column(String(255))
    deadline: Mapped[str] = mapped_column(String(255))
    status: Mapped[int] = mapped_column(Integer)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id", ondelete="CASCADE"))

    customer: Mapped["Customer"] = relationship(back_populates="posts")
    post_subjobs: Mapped["PostSubjob"] = relationship(back_populates="post", cascade="all, delete-orphan")



class Job(CreatedModel):

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))

    subjobs: Mapped["Subjob"] = relationship(back_populates="job", cascade="all, delete-orphan")


class Subjob(CreatedModel):

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id", ondelete="CASCADE"))

    job: Mapped["Job"] = relationship(back_populates="subjobs")
    subjob_employees: Mapped["SubjobEmployee"] = relationship(back_populates="subjob", cascade="all, delete-orphan")


class Employee(CreatedModel):

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    expirance: Mapped[str] = mapped_column(String(255))
    linkedin: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    rating: Mapped[int] = mapped_column(Integer)
    cv: Mapped[str] = mapped_column(String(255))

    user: Mapped["User"] = relationship(back_populates="employees")
    subjob_employees: Mapped["SubjobEmployee"] = relationship(back_populates="employee", cascade="all, delete-orphan")


class PostSubjob(CreatedModel):
    __tablename__ = "post_subjob"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id", ondelete="CASCADE"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"))

    post: Mapped["Post"] = relationship(back_populates="post_subjobs")


class SubjobEmployee(CreatedModel):

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id", ondelete="CASCADE"))
    subjob_id: Mapped[int] = mapped_column(ForeignKey("subjobs.id", ondelete="CASCADE"))

    employee: Mapped["Employee"] = relationship(back_populates="subjob_employees")
    subjob: Mapped["Subjob"] = relationship(back_populates="subjob_employees")


metadata = Base.metadata
