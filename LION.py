import os, sys
try:
    __import__("LION").lion()
except Exception as e:
    exit(str(e))
