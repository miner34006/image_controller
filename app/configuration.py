# -*- encoding: utf-8 -*-


class Config(object):
	"""
	Configuration base, for all environments.
	"""
	DEBUG = False
	TESTING = False

class ProductionConfig(Config):
	pass

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
