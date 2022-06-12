class Config:
    DEBUG = True

    SQL_ALCHEMY_DATABASE_URI = 'postgresql+psycopg2://smilecook:smilecook@192.168.1.5/smilecook'
    #SQL_ALCHEMY_DATABASE_URI = 'sqlite://///Users/apollo/Desktop/PYTHON/API/smilecook/smilecook.db'
    SQL_ALCHEMY_TRACK_MODIFICATION = False

