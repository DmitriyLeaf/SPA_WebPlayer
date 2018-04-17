# -*- coding: utf-8 -*-
"""Sound model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary
from sqlalchemy.orm import relationship, backref

from webplayer.model import DeclarativeBase, metadata, DBSession


class Sound(DeclarativeBase):
    __tablename__ = 'sounds'

    sound_id = Column(Integer, primary_key=True)
    sound_name = Column(Unicode(64), nullable=False)
    data = Column(Unicode(255), nullable=False)

    user_id = Column(Integer, ForeignKey('tg_user.user_id'), index=True)
    user = relationship('User', uselist=False,
                        backref=backref('songs',
                                        cascade='all, delete-orphan'))

    def __repr__(self):
    	return '<Sound: name=%s, data=%s>' % (
    		repr(self.sound_id),
    		repr(self.data))

    @classmethod
    def get(cls, id):
    	return DBSession.query(cls).filter_by(sound_id=id).first()

__all__ = ['Sound']
