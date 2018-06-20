# -*- coding: utf-8 -*-
"""Sort controller module"""

from tg import expose, redirect, validate, flash, url, tmpl_context
# from tg.i18n import ugettext as _
from tg import predicates

from webplayer.lib.base import BaseController
from webplayer.model import DBSession

from webplayer.model.sound import Sound

import collections

class SortController(BaseController):
   allow_only = predicates.not_anonymous()
   
   def _before(self, *args, **kw):
      tmpl_context.project_name = "SpacePlayer"

   @expose('webplayer.templates.sort')
   def index(self, **kw):
      return dict(page='sort')

   @expose()
   def into_folders(self, tag=0):
      Sound.sort_into_folders(int(tag))
      redirect('/sort')

   @expose('webplayer.templates.sortby')
   def genre(self, **kw):
      sounds = DBSession.query(Sound).all()
      sorted_dict = {}

      for sound in sounds:
         try:
            sorted_dict[sound.genre].append([sound.sound_name, sound.data])
         except:
            sorted_dict[sound.genre] = [[sound.sound_name, sound.data]]

      sorted_dict = collections.OrderedDict(sorted(sorted_dict.items()))
      keys = sorted_dict.keys()
      return dict(page='sortby',
         sorted_dict=sorted_dict,
         keys=keys,
         tag='Genre')

   @expose('webplayer.templates.sortby')
   def date(self, **kw):
      sounds = DBSession.query(Sound).all()
      sorted_dict = {}

      for sound in sounds:
         try:
            sorted_dict[sound.date].append([sound.sound_name, sound.data])
         except:
            sorted_dict[sound.date] = [[sound.sound_name, sound.data]]

      sorted_dict = collections.OrderedDict(sorted(sorted_dict.items()))
      keys = sorted_dict.keys()
      return dict(page='sortby',
         sorted_dict=sorted_dict,
         keys=keys,
         tag='Date')

   @expose('webplayer.templates.sortby')
   def artist(self, **kw):
      sounds = DBSession.query(Sound).all()
      sorted_dict = {}

      for sound in sounds:
         try:
            sorted_dict[sound.artist].append([sound.sound_name, sound.data])
         except:
            sorted_dict[sound.artist] = [[sound.sound_name, sound.data]]

      sorted_dict = collections.OrderedDict(sorted(sorted_dict.items()))
      keys = sorted_dict.keys()
      return dict(page='artist',
         sorted_dict=sorted_dict,
         keys=keys,
         tag='Artist')

   @expose('webplayer.templates.sortby')
   def album(self, **kw):
      sounds = DBSession.query(Sound).all()
      sorted_dict = {}

      for sound in sounds:
         try:
            sorted_dict[sound.album].append([sound.sound_name, sound.data])
         except:
            sorted_dict[sound.album] = [[sound.sound_name, sound.data]]

      sorted_dict = collections.OrderedDict(sorted(sorted_dict.items()))
      keys = sorted_dict.keys()
      return dict(page='album',
         sorted_dict=sorted_dict,
         keys=keys,
         tag='Album')
