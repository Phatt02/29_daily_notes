# config.py
class Config:
    SECRET_KEY = 'your-secret-key'
    JWT_SECRET_KEY = 'your-jwt-secret'
    MONGODB_SETTINGS = {
        'db': 'mario_notes02',#ยังไม่ได้ใช้
        'host': 'localhost02',
        'port': 27017
    }
    