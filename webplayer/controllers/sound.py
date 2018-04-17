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
    	sounds = DBSession.query(Sound).all()
        return dict(page='sound',
        	sounds=sounds)

    @expose('json')
    def gener_test_sounds(self, quantity=1):
    	DBSession.bulk_insert_mappings(Sound, [dict(sound_name='Test Song #%s' % i, data='Test Data #%s' % i) for i in range(int(quantity))])
    	redirect('/sound')

