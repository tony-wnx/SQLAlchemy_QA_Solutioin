# -*- coding: utf-8 -*-
"""
    Copyright (C) 2019 YOYOCLUB
    All rights reserved

    Filename : view.py
    Description : view.py

    Created by yxq at 2019/7/3 14:27
"""
from flask import Blueprint
from app.models_tmp import CircleClasscircle, CircleStory

bp = Blueprint('bp', __name__)


@bp.route("/")
def test():
    baby_id = '57723c14cf7a42e89dbc694b98231e68'

    # story_list = db.session.query(CircleClasscircle,
    #     CircleStory).join(CircleStory,
    #     CircleClasscircle.id == CircleStory.circle_id).filter(
    #     CircleStory.baby_id == baby_id).order_by(
    #     CircleClasscircle.create_date.desc()).first()

    # print(db.session.query(CircleStory).filter(CircleStory.baby_id == baby_id))
    # print(CircleStory.query.all())
    sql = CircleClasscircle.query.join(
        CircleStory, CircleClasscircle.id == CircleStory.circle_id).filter(
        CircleStory.baby_id == baby_id)

    sql2 = CircleClasscircle.query.join(
        CircleStory,
        CircleClasscircle.id == CircleStory.circle_id).filter(
        CircleStory.baby_id == baby_id).with_entities(
            CircleClasscircle.id,
        CircleClasscircle.baby_id)

    print(sql)
    print("===================")
    print(sql2)

    return str(sql)
