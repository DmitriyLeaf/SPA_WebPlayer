# -*- coding: utf-8 -*-
"""Relation controller module"""

from tg import expose, redirect, validate, flash, url, tmpl_context
# from tg.i18n import ugettext as _
from tg import predicates

from webplayer.lib.base import BaseController
from webplayer.model import DBSession
from webplayer.model.sound import Sound
from webplayer.model.relation import Relation

class RelationController(BaseController):
    allow_only = predicates.not_anonymous()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "SpacePlayer"
    
    @expose('webplayer.templates.relation')
    def index(self, **kw):
        relations = DBSession.query(Relation).all()
        sounds = DBSession.query(Sound).all()
        return dict(page='relation',
        	relations=relations)

    @expose('json')
    def gener_new_relation(self):
    	sounds = DBSession.query(Sound).all()
    	sound_quantity = len(sounds)
    	Relation.generation_new_relation(sound_quantity=sound_quantity)
    	redirect('/relation')
