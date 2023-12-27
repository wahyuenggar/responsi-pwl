import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://wahyudb_titlepoet:c0f10d2d449715ed5a99c03db4642115aad5259a@7xk.h.filess.io:3307/wahyudb_titlepoet'

SQLALCHEMY_TRACK_MODIFICATIONS = False