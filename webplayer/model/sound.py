# -*- coding: utf-8 -*-
"""Sound model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary
from sqlalchemy.orm import relationship, backref

from webplayer.model import DeclarativeBase, metadata, DBSession

from os import listdir
import mutagen
from mutagen import File
import tg, shutil, os

class Sound(DeclarativeBase):
    __tablename__ = 'sounds'

    sound_id = Column(Integer, primary_key=True)
    sound_name = Column(String(32), nullable=True) #TIT2 (1-3)
    date = Column(String(32), nullable=True) #TDRC
    album = Column(String(32), nullable=True) #TALB
    genre = Column(String(32), nullable=True) #TCON
    artist = Column(String(32), nullable=True) #TPE1
    picture = Column(String(32), nullable=True) #APIC:
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
        tree = 'C:\\Users\\Leafmen\\Desktop\\python\\diploma\\webplayer\\webplayer\\public'
        directory = tree + '\\music' + directory
        #files = listdir(tg.url('/music' + directory))
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

            sound['data'] = str(file).encode('utf8')

            try:
                pic = meta.tags.getall("APIC")[0].data
                with open(tree + '\\img\\%s.jpg' % sound['data'], 'wb') as img:
                    img.write(pic)
                sound['picture'] = '%s.jpg' % sound['data']
            except:
                sound['picture'] = 'Null'

            DBSession.add(Sound(
                sound_name=sound['name'],
                date = sound['date'],
                album = sound['album'],
                genre = sound['genre'],
                artist = sound['artist'],
                data = sound['data'],
                picture = sound['picture'],
                user_id=1))

    @classmethod
    def sort_by_date(cls):
        sounds = DBSession.query(Sound).all()
        sorted_dict = {}
        
        for sound in sounds:
            try:
                sorted_dict[sound.date].append([sound.sound_name, sound.data])
            except:
                sorted_dict[sound.date] = [[sound.sound_name, sound.data]]

        return sorted_dict

    @classmethod
    def sort_by_artist(cls):
        sounds = DBSession.query(Sound).all()
        sorted_dict = {}
        
        for sound in sounds:
            try:
                sorted_dict[sound.artist].append([sound.sound_name, sound.data])
            except:
                sorted_dict[sound.artist] = [[sound.sound_name, sound.data]]

        return sorted_dict

    @classmethod
    def sort_by_genre(cls):
        sounds = DBSession.query(Sound).all()
        sorted_dict = {}
        
        for sound in sounds:
            try:
                sorted_dict[sound.genre].append([sound.sound_name, sound.data])
            except:
                sorted_dict[sound.genre] = [[sound.sound_name, sound.data]]

        return sorted_dict

    @classmethod
    def sort_by_album(cls):
        sounds = DBSession.query(Sound).all()
        sorted_dict = {}
        
        for sound in sounds:
            try:
                sorted_dict[sound.album].append([sound.sound_name, sound.data])
            except:
                sorted_dict[sound.album] = [[sound.sound_name, sound.data]]

        return sorted_dict

    @classmethod
    def sort_into_folders(cls, tag):
        if tag == 0:
            music = cls.sort_by_date()
            cls.paste_into_folders(music, 'date')
        elif tag == 1:
            music = cls.sort_by_album()
            cls.paste_into_folders(music, 'album')
        elif tag == 2:
            music = cls.sort_by_genre()
            cls.paste_into_folders(music, 'genre')
        elif tag == 3:
            music = cls.sort_by_artist()
            cls.paste_into_folders(music, 'artist')

    @classmethod
    def paste_into_folders(cls, music, folder):
        tree = 'C:\\Users\\Leafmen\\Desktop\\python\\diploma\\webplayer\\webplayer\\public'
        #shutil.rmtree(tree + '\\sorted\\' + folder, ignore_errors=True)
        
        for tag in music:
            ttag = cls.check_dir(tag)
            for mus in music[tag]:
                try:
                    shutil.copy2(tree + '\\music\\' + mus[1], tree + '\\sorted\\' + folder + '\\' + ttag + '\\' + mus[1])
                except:
                     os.makedirs(tree + '\\sorted\\' + folder + '\\' + ttag)
                     shutil.copy2(tree + '\\music\\' + mus[1], tree + '\\sorted\\' + folder + '\\' + ttag + '\\' + mus[1])
        return 0

    @classmethod
    def check_dir(cls, tag):
        tag = tag.replace(':', ' ')
        tag = tag.replace('\\', ' ')
        tag = tag.replace('/', ' ')
        tag = tag.replace('?', ' ')
        tag = tag.replace('*', ' ')
        tag = tag.replace('"', ' ')
        tag = tag.replace('>', ' ')
        tag = tag.replace('<', ' ')
        tag = tag.replace('|', ' ')
        print tag
        return tag

__all__ = ['Sound']
