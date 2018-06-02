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
	def index(self, id = 2, previous_id = 1):
		try:
			sound = DBSession.query(Sound).get(id)
			sound_url = '/music/' + str(sound.sound_id) + '.mp3'
		except:
			redirect('/sound')

		return dict(page='player',
			sound=sound,
			sound_url=sound_url,
			previous_id=previous_id)

	@expose()
	def next_button(self, current_time_next, current_id, previous_id):
		next_sound = current_id
		try:
			if int(current_time_next) < 38:
				Relation.reduce_own_value(current_id)
				Relation.reduce_relation(previous_id, current_id)
				
				next_sound = Relation.get_next_sound(previous_id)
			elif int(current_time_next) >= 38 and int(current_time_next) <=61:

				next_sound = Relation.get_next_sound(current_id)
				previous_id = current_id
			elif int(current_time_next) > 61:
				Relation.increase_own_value(current_id)
				Relation.increase_relation(previous_id, current_id)
				
				next_sound = Relation.get_next_sound(current_id)
				previous_id = current_id
		except:
			pass

		redirect('/player', dict(
			id=next_sound,
			previous_id=previous_id))

	@expose()
	def previous_button(self, current_time_pre, current_id, previous_id):
		next_sound = current_id
		try:
			if int(current_time_pre) < 38:
				Relation.reduce_own_value(current_id)
				Relation.reduce_relation(current_id, previous_id)
				
				next_sound = Relation.get_previous_sound(previous_id)
			elif int(current_time_pre) >= 38 and int(current_time_pre) <=61:
				next_sound = Relation.get_previous_sound(current_id)
				previous_id = current_id
			elif int(current_time_pre) > 61:
				Relation.increase_own_value(current_id)
				Relation.increase_relation(current_id, previous_id)
				
				next_sound = Relation.get_previous_sound(current_id)
				previous_id = current_id
		except:
			pass

		redirect('/player', dict(
			id=next_sound,
			previous_id=previous_id))

	@expose()
	def stop_button(self, current_time_stop, current_id, previous_id):
		try:
			if int(current_time_stop) > 61:
				Relation.increase_own_value(current_id)
		except:
			pass
		redirect('/player' , dict(
			id=current_id,
			previous_id=previous_id))