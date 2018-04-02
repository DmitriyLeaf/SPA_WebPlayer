# -*- coding: utf-8 -*-
"""Song model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary
from sqlalchemy.orm import relationship, backref

from webplayer.model import DeclarativeBase, metadata, DBSession


class Song(DeclarativeBase):
    __tablename__ = 'songs'

    song_id = Column(Integer, primary_key=True)
    data = Column(Unicode(255), nullable=False)


    user_id = Column(Integer, ForeignKey('tg_user.user_id'), index=True)
    user = relationship('User', uselist=False,
                        backref=backref('songs',
                                        cascade='all, delete-orphan'))

    def __repr__(self):
    	return '<Song: name=%s, data=%s>' % (
    		repr(self.song_id),
    		repr(self.data))

    @classmethod
    def get(cls, song_id):
    	return DBSession.query(cls).filter_by(song_id=song_id).first()

__all__ = ['Song']
