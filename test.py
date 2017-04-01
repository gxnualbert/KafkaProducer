import struct

# topic="ttr"
# clientconnected_msg="gggggg"
#
# print "!cqi%dsi%ds"%(len(topic),len(clientconnected_msg))


tt=struct.pack("!hhl",1,2,3)
print tt
print repr(tt)

