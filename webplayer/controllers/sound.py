# -*- coding: utf-8 -*-
"""Song controller module"""

from tg import expose, redirect, validate, flash, url
# from tg.i18n import ugettext as _
# from tg import predicates

from webplayer.lib.base import BaseController
# from webplayer.model import DBSession


class SongController(BaseController):
    allow_only = predicates.not_anonymous()
    
    @expose('webplayer.templates.sound')
    def index(self, **kw):
        return dict(page='sound-index')
