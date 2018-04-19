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

    @classmethod
    def generation_test_data(cls, quantity):
        try:
            last_sound = DBSession.query(cls).order_by(cls.sound_id.desc()).first()
            last = last_sound.sound_id + 1
        except:
            last = 1

        for i in xrange(last, last+quantity):
            DBSession.add(Sound(sound_name='Test Song #%s' % i, data='Test Data #%s' % i, user_id=1))

    @classmethod
    def clear_data(cls):
        DBSession.query(cls).delete()

__all__ = ['Sound']
