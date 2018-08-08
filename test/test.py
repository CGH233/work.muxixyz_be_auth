import unittest
import os
from work_muxixyz_app import create_app,db
from flask import current_app,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import json

db=SQLAlchemy()

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(os.getenv('FLASK_CONFIG') or 'default')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exist(self):
        self.assertFalse(current_app is None)

# API FOR AUTH START

    def auth_a_signup(self):
        response=self.client.post(
            url_for('api.signup',_external=True),
            data=json.dumps({
                "name": 'test',
                "email": 'test@test.com',
                "avatar": 'https://test/test.png',
                "tel": '11111111111',
            }),
            content_type='application/json'
        )
        self.assertTrue(response.status_code==200)

    def auth_b_login(self):
        response=self.client.post(
            url_for('api.login',_external=True),
            data=json.dumps({
                "username": 'test',
            }),
            content_type='application/json'
        )
        s=json.loads(response.data.decode('utf-8'))['token']
        global TOKEN
        TOKEN=s
        self.assertTrue(response.status_code==200)

    def auth_c_verify(self):
        response=self.client.post(
            url_for('api.verify',_external=True),
            data=jsopn.dumps({
                "token": TOKEN,
            }),
            content_type='application/json'
        )
        s=json.loads(response.data.decode('utf-8'))['uid']
        print ('ID:'+string(s)+ ' ')
        self.assertTrue(resopnse.status_code==200)

# API FOR AUTH END
