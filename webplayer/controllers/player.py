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
	def index(self):
		sound = DBSession.query(Sound).get(1)
		icon = 'play'
		return dict(page='player',
			sound=sound,
			icon=icon)

	@expose()
	def play_pause_button(self, icon):
		if icon == 'play':
			icon = 'pause'
		else:
			icon = 'play'
		return dict(icon=icon)
