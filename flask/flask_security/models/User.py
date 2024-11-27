import uuid
from sqlalchemy import Boolean, DateTime, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from main.app import fsqla, db

class User(db.Model, fsqla.FsUserMixin):
    # __tablename__ = "user"
    # id = Column(Integer(), primary_key=True)
    # email = Column(String(255), unique=True)
    # username = Column(String(255), unique=True, nullable=True)
    # password = Column(String(255), nullable=False)
    # last_login_at = Column(DateTime())
    # current_login_at = Column(DateTime())
    # last_login_ip = Column(String(100))
    # current_login_ip = Column(String(100))
    # login_count = Column(Integer)
    # active = Column(Boolean())
    # premium = Column(Boolean())
    fs_uniquifier = Column(String(255), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    # confirmed_at = Column(DateTime())
    # roles = relationship(
    #     "Role", secondary="roles_users", backref=backref("users", lazy="dynamic")
    # )
