from enum import Enum as EnumType
from sqlalchemy import Column, DateTime, func, JSON, Integer, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(EnumType):
    PROCESSING = "processing"
    DONE = "done"
    FAILED = "failed"


class Inbox(Base):
    __tablename__ = 'inbox'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    payload = Column(JSON, nullable=False)
    state = Column(Enum(State), nullable=False, default=State.PROCESSING)

    outbox = relationship("Outbox", back_populates="inbox", uselist=False)


class Outbox(Base):
    __tablename__ = 'outbox'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    payload = Column(JSON, nullable=False)
    state = Column(Enum(State), nullable=False, default=State.PROCESSING)

    inbox_id = Column(Integer, ForeignKey('inbox.id'), nullable=False)
    inbox = relationship("Inbox", back_populates="outbox")
