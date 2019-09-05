# -*- encoding: utf-8 -*-

from flask import Flask


app = Flask(__name__)

#Configuration of application, see configuration.py, choose one and uncomment.
app.config.from_object('app.configuration.ProductionConfig')
# app.config.from_object('app.configuration.DevelopmentConfig')
#app.config.from_object('app.configuration.TestingConfig')

from app import views
