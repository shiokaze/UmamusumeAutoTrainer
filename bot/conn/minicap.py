import socket
import sys
import struct

import cv2
from collections import OrderedDict

import numpy


class Banner:
    def __init__(self):
        self.__banner = OrderedDict(
            [('version', 0),
             ('length', 0),
             ('pid', 0),
             ('realWidth', 0),
             ('realHeight', 0),
             ('virtualWidth', 0),
             ('virtualHeight', 0),
             ('orientation', 0),
             ('quirks', 0)
             ])

    def __setitem__(self, key, value):
        self.__banner[key] = value

    def __getitem__(self, key):
        return self.__banner[key]

    def keys(self):
        return self.__banner.keys()

    def __str__(self):
        return str(self.__banner)


class Minicap:
    cur_image = None

    def __init__(self, host, port, banner):
        self.__socket = None
        self.buffer_size = 4096
        self.host = host
        self.port = port
        self.banner = banner

    def start(self):
        self.connect()
        self.start_cap()

    def stop(self):
        self.__socket.close()

    def get_screen(self):
        if self.cur_image is None:
            return None
        return cv2.imdecode(numpy.array(self.cur_image, dtype=numpy.uint8), cv2.COLOR_RGBA2BGR)

    def connect(self):
        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print(e)
            sys.exit(1)
        self.__socket.connect((self.host, self.port))

    def start_cap(self):
        read_banner_bytes = 0
        banner_length = 24
        read_frame_bytes = 0
        frame_body_length = 0
        data = []
        # thread = threading.Thread(target=self.debugFrame)
        # thread.start()
        while not getattr(self.__socket, '_closed'):
            try:
                chunk = self.__socket.recv(self.buffer_size)
            except socket.error as e:
                print(e)
                sys.exit(1)
            cursor = 0
            buf_len = len(chunk)
            while cursor < buf_len:
                if read_banner_bytes < banner_length:
                    map(lambda i, val: self.banner.__setitem__(self.banner.keys()[i], val),
                        [i for i in range(len(self.banner.keys()))], struct.unpack("<2b5ibB", chunk))
                    cursor = buf_len
                    read_banner_bytes = banner_length
                elif read_frame_bytes < 4:
                    frame_body_length += (chunk[cursor] << (read_frame_bytes * 8)) >> 0
                    cursor += 1
                    read_frame_bytes += 1
                else:
                    if buf_len - cursor >= frame_body_length:
                        data.extend(chunk[cursor:cursor + frame_body_length])
                        # save img
                        self.cur_image = data
                        # self.cur_image = cv2.imdecode(numpy.array(data, dtype=numpy.uint8), cv2.COLOR_RGBA2BGR)
                        cursor += frame_body_length
                        frame_body_length = read_frame_bytes = 0
                        data = []
                    else:
                        data.extend(chunk[cursor:buf_len])
                        frame_body_length -= buf_len - cursor
                        read_frame_bytes += buf_len - cursor
                        cursor = buf_len
        print("socket closed")
