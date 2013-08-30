from hashlib import md5
from app import db, app
from flask import url_for
from flask.ext.sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy_searchable import SearchQueryMixin, Searchable
from sqlalchemy_utils.types import TSVectorType



class MemberQuery(BaseQuery, SearchQueryMixin):
    pass

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    net_id = db.Column(db.String(10), unique= True, nullable =False)
    name = db.Column(db.String(90), unique= True, nullable =False)
    password = db.Column(db.String(20),nullable = False)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
    

    def __repr__(self):
        return '< Admin %r>'%self.net_id
    def __str__(self):
        return self.net_id
    
class Member(db.Model):
    query_class = MemberQuery
    
    __searchable_columns__ = ['net_id']
    __search_options__ = {
        'tablename': 'member',
        'search_vector_name': 'search_vector',
        'search_trigger_name': '{table}_search_update',
        'search_index_name': '{table}_search_index',
    }
    __tablename__ = 'member'
    search_vector = db.Column(TSVectorType)
    
    id = db.Column(db.Integer, primary_key = True )
    net_id = db.Column(db.String(10), unique= True, nullable =False)
    name = db.Column(db.String(90), unique= True, nullable =False)
    
    def __repr__(self):
        return '< Member %r>'%self.net_id
    def __str__(self):
        return self.net_id
