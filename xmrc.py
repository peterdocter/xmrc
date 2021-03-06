
class XiaomiRemote:
    '''小米遥控器'''
    def __init__(self,ip,port=6091):
        self.ip = ip
        self.port = port
        self.sb = None

    def connect(self):


        if self.conn():
            self.connectRemote()

    def conn(self):
        try:
            self.sb  =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(10)
            self.sb.connect((self.ip,self.port))
            return True
        except Exception,e:
            return False



    def connectRemote(self):
        self.sb.send("\x05\x00\x2f\x01\x01\x01\x00\x00\x00\x02\x00\x26\x52\x65\x6d\x6f"
            + "\x74\x65\x20\x43\x6f\x6e\x74\x72\x6f\x6c\x6c\x65\x72\x20\x50\x72"
            + "\x6f\x74\x6f\x63\x6f\x6c\x20\x56\x65\x72\x73\x69\x6f\x6e\x20\x31"
            + "\x2e\x30")
        #print repr(self.sb.recv(1024))

    def menu(self):

        data = "\x04\x00\x41\x01\x00\x00\x00\x01\x00\x3a\x01\x00\x00\x00\x00\x02"\
        + "\x00\x00\x00\x00\x03\x00\x00\x00\x52\x04\x00\x00\x00\x00\x05\x00"\
        + "\x00\x00\x00\x06\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00"\
        + "\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x0a\xff\xff\xff\xff\x0b"\
        + "\x00\x00\x00\x00"
        self.sb.send(data)



    def home(self):

        data = "\x04\x00\x41\x01\x00\x00\x00\x01\x00\x3a\x01\x00\x00\x00\x00\x02"\
        + "\x00\x00\x00\x00\x03\x00\x00\x00\x03\x04\x00\x00\x00\x00\x05\x00"\
        + "\x00\x00\x00\x06\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00"\
        + "\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x0a\xff\xff\xff\xff\x0b"\
        + "\x00\x00\x00\x00"
        self.sb.send(data)


    def back(self):

        data = "\x04\x00\x41\x01\x00\x00\x00\x01\x00\x3a\x01\x00\x00\x00\x00\x02"\
        + "\x00\x00\x00\x00\x03\x00\x00\x00\x04\x04\x00\x00\x00\x00\x05\x00"\
        + "\x00\x00\x00\x06\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00"\
        + "\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x0a\xff\xff\xff\xff\x0b"\
        + "\x00\x00\x00\x00"
        self.sb.send(data)


    def left(self):

        data = "\x04\x00\x41\x01\x00\x00\x00\x01\x00\x3a\x01\x00\x00\x00\x00\x02"\
        + "\x00\x00\x00\x00\x03\x00\x00\x00\x15\x04\x00\x00\x00\x00\x05\x00"\
        + "\x00\x00\x00\x06\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00"\
        + "\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x0a\xff\xff\xff\xff\x0b"\
        + "\x00\x00\x00\x00"
        self.sb.send(data)


    def right(self):

        data = "\x04\x00\x41\x01\x00\x00\x00\x01\x00\x3a\x01\x00\x00\x00\x00\x02"\
        + "\x00\x00\x00\x00\x03\x00\x00\x00\x16\x04\x00\x00\x00\x00\x05\x00"\
        + "\x00\x00\x00\x06\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00"\
        + "\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x0a\xff\xff\xff\xff\x0b"\
        + "\x00\x00\x00\x00"
        self.sb.send(data)

    def up(self):

        data = "\x04\x00\x41\x01\x00\x00\x00\x01\x00\x3a\x01\x00\x00\x00\x00\x02"\
        + "\x00\x00\x00\x00\x03\x00\x00\x00\x13\x04\x00\x00\x00\x00\x05\x00"\
        + "\x00\x00\x00\x06\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00"\
        + "\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x0a\xff\xff\xff\xff\x0b"\
        + "\x00\x00\x00\x00"
        self.sb.send(data)


    def down(self):

        data = "\x04\x00\x41\x01\x00\x00\x00\x01\x00\x3a\x01\x00\x00\x00\x00\x02"\
        + "\x00\x00\x00\x00\x03\x00\x00\x00\x14\x04\x00\x00\x00\x00\x05\x00"\
        + "\x00\x00\x00\x06\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00"\
        + "\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x0a\xff\xff\xff\xff\x0b"\
        + "\x00\x00\x00\x00"
        self.sb.send(data)

    def enter(self):

        data = "\x04\x00\x41\x01\x00\x00\x00\x01\x00\x3a\x01\x00\x00\x00\x00\x02"\
        + "\x00\x00\x00\x00\x03\x00\x00\x00\x42\x04\x00\x00\x00\x00\x05\x00"\
        + "\x00\x00\x00\x06\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00"\
        + "\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x0a\xff\xff\xff\xff\x0b"\
        + "\x00\x00\x00\x00"
        self.sb.send(data)


    def close(self):

        data = "\x04\x00\x41\x01\x00\x00\x00\x01\x00\x3a\x01\x00\x00\x00\x00\x02"\
        + "\x00\x00\x00\x00\x03\x00\x00\x00\x1a\x04\x00\x00\x00\x00\x05\x00"\
        + "\x00\x00\x00\x06\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00"\
        + "\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x0a\xff\xff\xff\xff\x0b"\
        + "\x00\x00\x00\x00"
        self.sb.send(data)



#实例化
xmrc = XiaomiRemote('192.168.1.23')
xmrc.connect()

#home键
xmrc.home()
#左
xmrc.left()
#右
xmrc.right()


