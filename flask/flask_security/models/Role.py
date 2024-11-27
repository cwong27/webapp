from sqlalchemy import Column, Integer, String
from main.app import fsqla, db

class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = "role"
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))