import pymysql
from config.config import db as config

class DB:
    def __init__(self):
        host = config["host"]
        user = config["user"]
        password = config['pass']
        db = config["name"]
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()