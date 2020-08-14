import socket
import struct

class PixelClient():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    buffer = []
    count = 0;
    packetSize = 0 
    mode = 0
    def __init__(self, host: str, port=5005, mode=0):
        self.host = host
        self.port = port
        self.mode = mode
        if mode == 1:
            self.packetSize = 140
        else:
            self.packetSize = 210
        self.verModeString = self.SetVersionBit(0) + self.SetRGBAMode(mode)

    def _update(self):
        if self.count == self.packetSize:
            self.flush()

    def _send(self, data: bytes):
        """ Send data to the server"""
        self.sock.sendto(data, (self.host, self.port))

    def flush(self):
        """ Send everything that is inside the buffer to the server"""
        self._send(self.verModeString + b"".join(self.buffer))
        self.buffer = []
        self.count = 0

    def RGBPixel(self, x: int, y: int, r: int, g: int, b: int, a=None):
        """Generates the packed data for a pixel"""
        self.count += 1
        if self.mode == 1:
            self.buffer.append(bytes(struct.pack("<2H4B", x, y, r, g, b, a)))
        else:
            self.buffer.append(bytes(struct.pack("<2H3B", x, y, r, g, b)))
        self._update()

    @staticmethod
    def SetRGBAMode(mode: int) -> bytes:
        """
            Generate the rgb/rgba bit
            0 for RGB and 1 for RGBA
        """
        return struct.pack("<?", mode)

    @staticmethod
    def SetVersionBit(protocol=0) -> bytes:
        """Generate the Version bit"""
        return struct.pack("<B", protocol)

