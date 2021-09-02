import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class ItemCategory(db.Model):
    __tablename__="ItemsCategory"
    ItemCatID = db.Column(db.Integer, primary_key=True)
    ItemCatDesc =db.Column(db.String,nullable=False)
    
class ItemMaster(db.Model):
    __tablename__="ItemMaster"
    ItemID = db.Column(db.Integer, primary_key=True)
    ItemCatID = db.Column(db.Integer,db.ForeignKey("ItemsCategory.ItemCatID"), nullable=False)
    ItemDesc = db.Column(db.String,nullable=False)
    AvailAmt = db.Column(db.Integer,nullable=False)
    itemCat = db.relationship("ItemCategory", backref="itemCat", lazy=True)
    
class AddItem(db.Model):
    __tablename__="AddItems"
    transID=db.Column(db.Integer, primary_key=True)
    ItemID = db.Column(db.Integer,db.ForeignKey("ItemMaster.ItemID"), nullable=False)
    AddQty = db.Column(db.Integer, nullable=False)
    AddDate = db.Column(db.Date,nullable=False)
    VendorName = db.Column(db.String,nullable=False)
    
    
class request_tbl(db.Model):
    __tablename__="request_tbl"
    reqID=db.Column(db.Integer, primary_key=True)
    ReqDeptt=db.Column(db.String,nullable=False)  
    ReqDate =db.Column(db.Date,nullable=False)
    ItemID = db.Column(db.Integer,db.ForeignKey("ItemMaster.ItemID"), nullable=False)
    ReqQty = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer,db.ForeignKey("user_tbl.userID"), nullable=False)
    Status=db.Column(db.String,nullable=False) 
    issueDate=db.Column(db.Date,nullable=False) 
    returnDate=db.Column(db.Date,nullable=False)
    item = db.relationship("ItemMaster", backref="item", lazy=True)
    user = db.relationship("user_tbl", backref="user", lazy=True)
    
class user_tbl(db.Model):
    __tablename__="user_tbl"
    userID=db.Column(db.Integer, primary_key=True)
    userName=db.Column(db.String,nullable=False)  
    pwd=db.Column(db.String,nullable=False)  
    userType=db.Column(db.String,nullable=False) 