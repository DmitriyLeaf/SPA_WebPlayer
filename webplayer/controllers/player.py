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
	def index(self, id = 1):
		try:
			sound = DBSession.query(Sound).get(id)
			sound_url = '/music/' + str(sound.sound_id) + '.mp3'
			icon = 'play'
		except:
			redirect('/sound')

		return dict(page='player',
			sound=sound,
			sound_url=sound_url,
			icon=icon)

	@expose()
	def next_button(self, current_time_next):
		
		redirect('/player', dict(
			id=2))

	@expose()
	def previous_button(self, current_time_pre):
		
		redirect('/player' , dict(
			id=1))
