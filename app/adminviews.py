from app import app, admin, db, models
from flask import Flask
from flask.ext.admin import BaseView, expose
from flask import g
from flask.ext.admin.contrib.sqla import ModelView, fields
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op
from config import SUPERUSERS
from wtforms import validators

path = op.join(op.dirname(__file__), 'static')


class MyBase(ModelView):
    pass
##    def is_accessible(self):
##        return g.user.is_authenticated() and (g.user.net_id in SUPERUSERS)

   


class Admin(MyBase):
    can_create = True

class Member(MyBase):
    can_create = True

class StaticFilesAdmin(FileAdmin):
    pass

admin.add_view(Member(models.Member, db.session))
admin.add_view(Admin(models.Admin, db.session))
