# -*- coding: utf-8 -*-
"""Date controller module"""

from tg import expose, redirect, validate, flash, url, tmpl_context
# from tg.i18n import ugettext as _
from tg import predicates

from webplayer.lib.base import BaseController
from webplayer.model import DBSession
from webplayer.model.sound import Sound

import collections

class DateController(BaseController):
    allow_only = predicates.not_anonymous()

    def _before(self, *args, **kw):
    	tmpl_context.project_name = "SpacePlayer"

    @expose('webplayer.templates.date')
    def index(self, **kw):
    	sorted_dict = Sound.sort_by_date()
    	sorted_dict = collections.OrderedDict(sorted(sorted_dict.items()))
    	keys = sorted_dict.keys()
    	return dict(page='date',
    		sorted_dict=sorted_dict,
    		keys=keys)
