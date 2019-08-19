import argparse
import collections
import configparser
import hashlib
import os
import re
import sys
import zlib

argparser = argparse.ArgumentParser(description="Test")
argsubparser = argparser.add_subparsers(title="Commands", dest="command")
argsubparser.required = True