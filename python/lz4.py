import uuid
import timeit
import lz4     #pip intall lz4
import os
from timeit import Timer

DATA = open("data.txt", "rb").read()
OUTPUT = open("data.lz4", "wb")
LZ4_DATA = lz4.compress(DATA)
OUTPUT.write(LZ4_DATA)
LOOPS = 1

DISK_READ_SPEED = 60 #in MB

print("Data Size:")
print("  Raw: %.2f MB" % (float(len(DATA)) / 1000000))
print("  LZ4: %.2f MB (%.2f percent)" % ((float(len(LZ4_DATA))/1000000), ( len(LZ4_DATA) / float(len(DATA)) * 100 )  ))
print("Benchmark: %d loop(s), Size %.3f GB" % (LOOPS, (LOOPS * float(len(DATA)) / 1000000000)))
print("  LZ4 Compression: %fs" % Timer("lz4.compress(DATA)", "from __main__ import DATA; import lz4").timeit(number=LOOPS))
decompress = Timer("lz4.uncompress(LZ4_DATA)", "from __main__ import LZ4_DATA; import lz4").timeit(number=LOOPS)
print("  LZ4 Decompression: %fs" % decompress)
print("Get 1000 matches from disk (read speed %dMB/s)" % DISK_READ_SPEED)
print("  Raw: %.2f seconds" % ((float(len(DATA)) / 1000000) / DISK_READ_SPEED) )
print("  LZ4: %.2f seconds (%0.2f percent)" % 
		(
			(((float(len( LZ4_DATA )) / 1000000 ) / DISK_READ_SPEED ) + decompress),
			((((float(len( LZ4_DATA )) / 1000000 ) / DISK_READ_SPEED ) + decompress) / ((float(len(DATA)) / 1000000) / DISK_READ_SPEED) * 100)
		)	
	 )










