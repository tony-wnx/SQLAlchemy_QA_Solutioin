# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Float, Index, String, TIMESTAMP, Table, Text, VARBINARY, \
    text, create_engine
from sqlalchemy.dialects.mysql import BIGINT, CHAR, INTEGER, MEDIUMINT, MEDIUMTEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import scoped_session, sessionmaker
from app import db


# engine = create_engine(
#     "mysql+pymysql://xxxxxx:xxxxxx@xxxxxx.mysql.xxxxxx.aliyuncs.com:3306/xxxxxx")
#
#
# class MyBase(object):
#     query = scoped_session(
#         sessionmaker().configure(
#             bind=engine)).query_property()
#
#
# Base = declarative_base(cls=MyBase)

# class CircleClasscircle(AbstractConcreteBase, db.Model):


class CircleClasscircle(db.Model):
    __tablename__ = 'circle_classcircle'

    id = Column(String(64), primary_key=True)
    class_id = Column(String(64))
    author = Column(String(64))
    author_id = Column(String(64))
    like_num = Column(INTEGER(10), server_default=text("'0'"))
    comment_num = Column(INTEGER(10), server_default=text("'0'"))
    share_num = Column(INTEGER(10), server_default=text("'0'"))
    content = Column(String(2000))
    type = Column(CHAR(1), server_default=text("'0'"))
    create_by = Column(String(64))
    create_date = Column(DateTime)
    update_by = Column(String(64))
    update_date = Column(DateTime)
    remarks = Column(String(255))
    del_flag = Column(CHAR(1), server_default=text("'0'"))
    category = Column(CHAR(1), server_default=text("'1'"))
    release_type = Column(CHAR(1), server_default=text("'1'"))
    Ann_title = Column(String(255))
    baby_id = Column(String(64))
    pdtecher = Column(String(10), server_default=text("'0'"))


class CircleStory(db.Model):
    __tablename__ = 'circle_story'

    id = Column(String(64), primary_key=True)
    circle_id = Column(String(64))
    baby_id = Column(String(64))
    is_read = Column(CHAR(1), server_default=text("'0'"))
    create_date = Column(DateTime)
    update_date = Column(DateTime)
