#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """ function that returns an Python data represented by a JSON """
    return json.loads(my_str)
