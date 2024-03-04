#!/usr/bin/python3
"""Base model Module"""


class Base:
    """Class Base contains only Id, Creation date, update date."""

    def __init__(self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def save(self):
        """base function for saving"""
        return

    def to_json(self):
        """serilize model to josn object"""
        return {}
