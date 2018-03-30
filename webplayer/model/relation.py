# -*- coding: utf-8 -*-
"""Relation model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary
from sqlalchemy.orm import relationship, backref

from webplayer.model import DeclarativeBase, metadata, DBSession


class Relation(DeclarativeBase):
    __tablename__ = 'relations'

    left_uid = Column(Integer, primary_key=True)
    right_uid = Column(Integer, primary_key=True)
    weight = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey('tg_user.user_id'), index=True)
    user = relationship('User', uselist=False,
                        backref=backref('relations',
                                        cascade='all, delete-orphan'))


__all__ = ['Relation']
