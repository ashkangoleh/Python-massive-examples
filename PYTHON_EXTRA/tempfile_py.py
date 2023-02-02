import tempfile


temp = tempfile.TemporaryFile()
try:
    temp.write(b"""
               Ashkan Goleh Pour
               age 33
               bachelor degree
               """)
    temp.seek(0)

    read = temp.read()
    read = read.decode("utf-8")
    print(read)

finally:
    temp.close()
