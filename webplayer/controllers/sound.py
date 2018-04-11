# -*- coding: utf-8 -*-
"""Sound controller module"""

from tg import expose, redirect, validate, flash, url, tmpl_context
# from tg.i18n import ugettext as _
from tg import predicates

from webplayer.lib.base import BaseController
from webplayer.model import DBSession
from webplayer.model.sound import Sound

__all__ = ['SoundController']

class SoundController(BaseController):
    allow_only = predicates.not_anonymous()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "SpacePlayer"
    
    @expose('webplayer.templates.sound')
    def index(self):
    	#sound_test = DBSession.query(Sound).get(1)
        return dict(page='sound')
        	#sound=sound_test)
