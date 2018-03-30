# -*- coding: utf-8 -*-
"""Relation controller module"""

from tg import expose, redirect, validate, flash, url
# from tg.i18n import ugettext as _
# from tg import predicates

from webplayer.lib.base import BaseController
# from webplayer.model import DBSession


class RelationController(BaseController):
    # Uncomment this line if your controller requires an authenticated user
    # allow_only = predicates.not_anonymous()
    
    @expose('webplayer.templates.relation')
    def index(self, **kw):
        return dict(page='relation-index')
