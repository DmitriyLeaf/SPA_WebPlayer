# -*- coding: utf-8 -*-
"""Player controller module"""

from tg import expose, redirect, validate, flash, url, tmpl_context
# from tg.i18n import ugettext as _
from tg import predicates

from webplayer.lib.base import BaseController
from webplayer.model import DBSession
from webplayer.model.sound import Sound
from webplayer.model.relation import Relation

__all__ = ['PlayerController']

class PlayerController(BaseController):
	allow_only = predicates.not_anonymous()

	def _before(self, *args, **kw):
		tmpl_context.project_name = "SpacePlayer"

	@expose('webplayer.templates.player')
	def index(self, id = 3, previous_sound = 1):
		try:
			sound = DBSession.query(Sound).get(id)
			sound_url = '/music/' + str(sound.sound_id) + '.mp3'
		except:
			redirect('/sound')

		return dict(page='player',
			sound=sound,
			sound_url=sound_url,
			previous_sound=previous_sound)

	@expose()
	def next_button(self, current_time_next, current_id):
		
		redirect('/player', dict(
			id=2))

	@expose()
	def previous_button(self, current_time_pre, current_id):
		
		redirect('/player' , dict(
			id=1))

	@expose()
	def stop_button(self, current_time_stop, current_id, previous_sound):
		try:
			if int(current_time_stop) > 61:
				Relation.increase_own_value(current_id)
		except:
			pass
		redirect('/player' , dict(
			id=current_id,
			previous_sound=previous_sound))