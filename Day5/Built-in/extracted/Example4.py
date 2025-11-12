#Compressed file

import zlib

data = b"Python Standard Library"
compressed = zlib.compress(data)
print('Compressed:',compressed)

#decompress the data
decompressed = zlib.decompress(compressed)
print('Decompressed:',decompressed)

print('Original Size:',len(data))
print('Compressed size:',len(compressed))
