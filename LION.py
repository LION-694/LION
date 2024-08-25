import os, sys
try:
    __import__("LION").__menu__()
except Exception as e:
    exit(str(e))
