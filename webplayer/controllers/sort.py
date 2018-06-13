# -*- coding: utf-8 -*-
"""Sort controller module"""

from tg import expose, redirect, validate, flash, url, tmpl_context
# from tg.i18n import ugettext as _
from tg import predicates

from webplayer.lib.base import BaseController
from webplayer.model import DBSession

from webplayer.model.sound import Sound


class SortController(BaseController):
   	allow_only = predicates.not_anonymous()

   	def _before(self, *args, **kw):
   		tmpl_context.project_name = "SpacePlayer"

   	@expose('webplayer.templates.sort')
   	def index(self, **kw):
   		return dict(page='sort')

   	@expose()
   	def into_folders(self, tag=0):
   		Sound.sort_into_folders(int(tag))
   		redirect('/sort')
