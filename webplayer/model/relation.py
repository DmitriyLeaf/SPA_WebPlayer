# -*- coding: utf-8 -*-
"""Relation model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary
from sqlalchemy.orm import relationship, backref

from webplayer.model import DeclarativeBase, metadata, DBSession

import random, math

class Relation(DeclarativeBase):
    __tablename__ = 'relations'

    left_sound_id = Column(Integer, primary_key=True)
    weight = Column(Integer, nullable=False)
    right_sound_id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('tg_user.user_id'), index=True)
    user = relationship('User', uselist=False,
                        backref=backref('relations',
                                        cascade='all, delete-orphan'))

    def __repr__(self):
        return'<Relation: left=%s, weight=%s, right=%s>' % (
            repr(self.left_sound_id),
            repr(self.weight),
            repr(self.right_sound_id))

    @classmethod
    def get_by_left(cls, id):
        return DBSession.query(cls).filter_by(left_sound_id=id).first()

    @classmethod
    def get_by_right(cls, id):
        return DBSession.query(cls).filter_by(right_sound_id=id).first()

    @classmethod
    def generation_new_relation(cls, sound_quantity):
        DBSession.query(cls).delete()
        
        for i in xrange(1, sound_quantity+1):
            for j in xrange(1, sound_quantity+1):
                DBSession.add(Relation(left_sound_id=i, weight=random.randint(0, 100), right_sound_id=j))

    @classmethod
    def generation_null_relation(cls, sound_quantity):
        DBSession.query(cls).delete()
        
        for i in xrange(1, sound_quantity+1):
            for j in xrange(1, sound_quantity+1):
                DBSession.add(Relation(left_sound_id=i, weight=int(100-100/1.618), right_sound_id=j))

    @classmethod
    def increase_own_value(cls, sound_id):
        current = DBSession.query(cls).filter_by(left_sound_id=sound_id, right_sound_id=sound_id).first()
        rate = int((100 - current.weight) - (100 - current.weight) / 1.618)
        DBSession.query(cls).\
            filter_by(left_sound_id=sound_id, right_sound_id=sound_id).\
            update({"weight": cls.weight + rate}, synchronize_session='fetch')

__all__ = ['Relation']
