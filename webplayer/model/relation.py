# -*- coding: utf-8 -*-
"""Relation model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary
from sqlalchemy.orm import relationship, backref

from webplayer.model import DeclarativeBase, metadata, DBSession


class Relation(DeclarativeBase):
    __tablename__ = 'relations'

    left_song_id = Column(Integer, primary_key=True)
    weight = Column(Integer, nullable=False)
    right_song_id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('tg_user.user_id'), index=True)
    user = relationship('User', uselist=False,
                        backref=backref('relations',
                                        cascade='all, delete-orphan'))

    def __repr__(self):
        return'<Relation: left=%s, weight=%s, right=%s>' % (
            repr(self.left_song_id),
            repr(self.weight),
            repr(self.right_song_id))

    @classmethod
    def get_by_left(cls, id):
        return DBSession.query(cls).filter_by(left_song_id=id).first()

    @classmethod
    def get_by_right(cls, id):
        return DBSession.query(cls).filter_by(right_song_id=id).first()

__all__ = ['Relation']