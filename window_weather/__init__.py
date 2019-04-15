#! ../venv/bin/python
from get_data import sfg
from view import ViewMessage #, message
import os
# print(os.)
t = sfg()
print(t)
print(t, file = ViewMessage())
