import struct

def demo1():
    buf1 = 256
    bin_buf1 = struct.pack('i', buf1)
    ret1, = struct.unpack('i', bin_buf1)
    print bin_buf1, '  <====>  ', ret1

    # buf2 = 3.1415
    # bin_buf2 = struct.pack('d', buf2)
    # ret2 = struct.unpack('d', bin_buf2)
    # print bin_buf2, '  <====>  ', ret2
    #
    # buf3 = 'Hello World'
    # bin_buf3 = struct.pack('11s', buf3)
    # ret3 = struct.unpack('11s', bin_buf3)
    # print bin_buf3, '  <====>  ', ret3
    #
    # # struct header {
    # #   int buf1;
    # #   double buf2;
    # #   char buf3[11];
    # # }
    # bin_buf_all = struct.pack('id11s', buf1, buf2, buf3)
    # ret_all = struct.unpack('id11s', bin_buf_all)
    # print bin_buf_all, '  <====>  ', ret_all


demo1()
