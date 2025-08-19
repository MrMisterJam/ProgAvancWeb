class DefaultConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'nosso-segredinho'

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    TESTING = True
    ENV = 'development'

class ProductionConfig(DefaultConfig):
    DEBUG = False
    ENV = 'production'        