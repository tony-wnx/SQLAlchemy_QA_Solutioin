# #-*-coding:utf-8-*-

import os


class Config:
    SITE_NAME = u'YOYOCLUB'
    SQLALCHEMY_POOL_RECYCLE = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class DevelopmentConfig(Config):

    HOST = '127.0.0.1'
    PORT = 5000
    DEBUG = True
    SECRET_KEY = ''
    SQLALCHEMY_ECHO = False
    MYSQL_USER = 'xxxxxx'
    MYSQL_PASS = 'xxxxxx'
    MYSQL_HOST = 'xxxxxx.xxxxxx.xxxxxx.aliyuncs.com'
    MYSQL_PORT = '3306'
    MYSQL_DB = 'xxxxxx'
    MYSQL_DB2 = 'log'
    SQLALCHEMY_BINDS = {
        'xxxxxx': 'mysql+pymysql://%s:%s@%s:%s/%s' % (MYSQL_USER,
                                                        MYSQL_PASS,
                                                        MYSQL_HOST,
                                                        MYSQL_PORT,
                                                        MYSQL_DB),
        'log': 'mysql+pymysql://%s:%s@%s:%s/%s' % (MYSQL_USER,
                                                   MYSQL_PASS,
                                                   MYSQL_HOST,
                                                   MYSQL_PORT,
                                                   MYSQL_DB2)}
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
        MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
}
