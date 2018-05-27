# -*- coding: utf-8 -*-
"""Sort controller module"""

from tg import expose, redirect, validate, flash, url, tmpl_context
# from tg.i18n import ugettext as _
from tg import predicates

from webplayer.lib.base import BaseController
# from webplayer.model import DBSession


class SortController(BaseController):
   	allow_only = predicates.not_anonymous()

   	def _before(self, *args, **kw):
   		tmpl_context.project_name = "SpacePlayer"

   	@expose('webplayer.templates.sort')
   	def index(self, **kw):
   		return dict(page='sort')
