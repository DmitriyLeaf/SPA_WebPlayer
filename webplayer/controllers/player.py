# -*- coding: utf-8 -*-
"""Player controller module"""

from tg import expose, redirect, validate, flash, url, tmpl_context
# from tg.i18n import ugettext as _
from tg import predicates

from webplayer.lib.base import BaseController
from webplayer.model import DBSession
from webplayer.model.sound import Sound

__all__ = ['PlayerController']

class PlayerController(BaseController):
	allow_only = predicates.not_anonymous()

	def _before(self, *args, **kw):
		tmpl_context.project_name = "SpacePlayer"

	@expose('webplayer.templates.player')
	@expose('webplayer.templates.player.css')
	def index(self):
		sound = DBSession.query(Sound).get(1)
		return dict(page='player',
			player_css='player.css',
			sound=sound)
