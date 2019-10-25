# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:47:30 2019

@author: Sachi
"""

from sqlalchemy import Column, String

from models.base import Base

class User(Base):
    __tablename__ = "userLogs"

    username = Column(String, primary_key=True)
    timeStamp = Column(DateTime)

    def get_userId(self):
        return self.userId

    def get_timeStamp(self, i):
        return self.timeStamp
    
def create_user(db, userId, timeStamp):
    user = User(
        userId=userId,
        timeStamp=timeStamp
    )
    db.add(user)
    return user

def get_user(db, userId):
    return db.query(User).filter_by(userId=userId).first()