import sys
from pwn import *

buf = b'A' * 208
buf += b'\x42' * 8