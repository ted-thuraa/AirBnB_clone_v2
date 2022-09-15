#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")


if (storage_engine == "db"):
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
