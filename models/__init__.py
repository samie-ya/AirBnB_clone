#!/usr/bin/python3
"""This function will run reload when console is called"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
