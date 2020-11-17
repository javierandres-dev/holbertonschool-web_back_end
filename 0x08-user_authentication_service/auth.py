#!/usr/bin/env python3
""" Hash password, Register user """
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from typing import TypeVar


def _hash_password(password: str) -> str:
    """ takes in a password string arguments and returns a string
        The returned string is a salted hash of the input password,
        hashed with bcrypt.hashpw """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ constructor """
        self._db = DB()

    def register_user(self, email: str, password: str) -> TypeVar('User'):
        """ take mandatory email and password string arguments and
            return a User object """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user
        else:
            raise ValueError('User {email} already exists')