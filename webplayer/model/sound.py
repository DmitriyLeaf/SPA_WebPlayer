# -*- coding: utf-8 -*-
"""Sound model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary
from sqlalchemy.orm import relationship, backref

from webplayer.model import DeclarativeBase, metadata, DBSession

from os import listdir
import mutagen
import tg

class Sound(DeclarativeBase):
    __tablename__ = 'sounds'

    sound_id = Column(Integer, primary_key=True)
    sound_name = Column(String(32), nullable=True) #TIT1-3(2)
    date = Column(String(32), nullable=True) #TDRC
    album = Column(String(32), nullable=True) #TALB
    genre = Column(String(32), nullable=True) #TCON
    artist = Column(String(32), nullable=True) #TPE1
    data = Column(String(32), nullable=True)

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

    #@classmethod
    #def get_url(cls, id):
        #return 'music/' + DBSession.query(cls).filter_by(sound_id=id).first() + '.mp3'

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

    @classmethod
    def upload_files(cls, directory):
        directory = 'C:\\Users\\Leafmen\\Desktop\\python\\diploma\\webplayer\\webplayer\\public\\music'
        files = listdir(directory)

        for file in files:
            sound = {}
            meta = mutagen.File(directory + '/' + file)

            try:
                sound['name'] = str(meta['TIT2']).encode('utf8')
            except:
                sound['name'] = 'Null'
            
            try:
                sound['date'] = str(meta['TDRC']).encode('utf8')
            except:
                sound['date'] = 'Null'

            try:
                sound['album'] = str(meta['TALB']).encode('utf8')
            except:
                sound['album'] = 'Null'

            try:
                sound['genre'] = str(meta['TCON']).encode('utf8')
            except:
                sound['genre'] = 'Null'

            try:
                sound['artist'] = str(meta['TPE1']).encode('utf8')
            except:
                sound['artist'] = 'Null'
            
            sound['data'] = file

            DBSession.add(Sound(
                sound_name=sound['name'],
                date = sound['date'],
                album = sound['album'],
                genre = sound['genre'],
                artist = sound['artist'],
                data = sound['data'], 
                user_id=1))



__all__ = ['Sound']
