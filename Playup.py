import os, sys
try:
    __import__("LION1").lion()
except Exception as e:
    exit(str(e))
