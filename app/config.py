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
    SECRET_KEY = '0\xd4H\x08\x80gQ\xa3\x9c\xeaO\x01\xb8\xd3\xb5B\xd6\xd6e%\xf3\xe3\xd0\xc4'
    SQLALCHEMY_ECHO = False
    MYSQL_USER = 'haierzhongyou'
    MYSQL_PASS = 'dKLLLbcQ2a4Nl41MallT'
    MYSQL_HOST = 'rdsx63p8l175ukqi9120o.mysql.rds.aliyuncs.com'
    MYSQL_PORT = '3306'
    MYSQL_DB = 'yoyoclub'
    MYSQL_DB2 = 'log'
    SQLALCHEMY_BINDS = {
        'yoyoclub': 'mysql+pymysql://%s:%s@%s:%s/%s' % (MYSQL_USER,
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
