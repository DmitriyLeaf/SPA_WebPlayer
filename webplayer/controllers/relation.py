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

        #relations_table = []
        
        #relations_table = [[0 for i in range(0, len(sounds))] for j in range(0, len(sounds))]
        
        try:
            relations_table = []
            relations_table = [[0 for i in range(0, len(sounds))] for j in range(0, len(sounds))]
            for i in relations:
                relations_table[i.left_sound_id-1][i.right_sound_id-1] = i.weight
        except:
            pass
        
        return dict(page='relation',
        	relations=relations,
            relations_table=relations_table)

    @expose('json')
    def gener_new_relation(self):
    	sounds = DBSession.query(Sound).all()
    	Relation.generation_new_relation(len(sounds))
    	redirect('/relation')

    @expose('json')
    def gener_null_relation(self):
        sounds = DBSession.query(Sound).all()
        Relation.generation_null_relation(len(sounds))
        redirect('/relation')