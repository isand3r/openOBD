import socket
import sys

class UDPDevice():
    """OBD Device that can send PIDs and read from the CAN bus"""

    def __init__(self):
        self.host = 'localhost'
        self.port = 8000
        self.ready = False
        self.msg = None
        self.msg_str = None
        self.response = ["",""]
        self.addr = None
        self.s = None
        self.UID = 0
        self.EV = 0
        self.D = 0
        self.T = 0
        self.LT = 0
        self.LN = 0
        self.AL = 0
        self.SP = 0
        self.AC = 0
        self.DC = 0
        self.RP = 0
        self.HD = 0
        self.SV = 0
        self.HP = 0
        self.MI = 0
        self.MG = 0
        self.BV = 0
        self.CQ = 0
        self.GS = 0
        self.GT = 0
        self.FL = 0
        self.XY = 0
        self.FWM = 0
        self.FWO = 0
        self.PF = 0
        self.VN = 0
        self.CP = 0
        self.CN = 0
        self.AX = 0
        self.AY = 0
        self.AZ = 0
        self.SEQ = 0

def connect(self):
    # create dgram udp socket
    try:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setblocking(0)
        self.ready = True 
        self.SEQ = 0
    except socket.error:
        print 'Failed to create socket'

def disconnect(self):
    if(self.ready == True):
        self.s.shutdown()
        self.s.close()
        self.ready = False

def format_msg(self, request):
    """Ignition ON alert"""
    if(request == 6011):
        self.EV = request
        self.SEQ += 1
        self.msg = ['$$', self.UID, self.EV, self.D, self.T, self.LT, self.LN, self.AL, self.SP, self.AC, self.DC, self.RP, self.HD, self.SV, self.HP, self.MI, self,MG, self.BV, self.CQ, self.GS, self.FL, self.GT, self.AX, self.AY, self.AZ, self.SEQ, '##']
    elif(request == (4001 or 4002 or 6001 or 6002 or 6003 or 6005 or 6006 or 6007 or 6008 or 6012 or 6016 or 6017 or 6018 or 6030 or 6031 or 6035 or 6032)):
        """Ignition OFF alert"""
        self.EV == request
        self.SEQ += 1
        self.msg = ['$$', self.UID, self.EV, self.D, self.T, self.LT, self.LN, self.AL, self.SP, self.AC, self.DC, self.RP, self.HD, self.SV, self.HP, self.MI, self,MG, self.BV, self.CQ, self.GS, self.GT, self.FL, self.AX, self.AY, self.AZ, self.SEQ, '##']

    self.msg_str = ','.join(map(str, self.msg))  


def send_udp_msg(self):
     
    if(self.ready == True) :

        #Set the whole string
       
        msg_length = len(self.message)
        recv_length = len(self.response)

        while(int(self.response[recv_length-1]) != int(self.msg[msg_length-1])):
            #send message again if response doesnt not match msg request
         
            try :
                self.s.settimeout(10)
                
                self.s.sendto(self.msg_str, (self.host, self.port))
                 
                # receive data from client (recv, addr)
                recv, addr = s.recvfrom(1024)

                self.response = recv.split(',')
                self.addr = addr

            except socket.timeout:
                print 'No data was recieved for message on UDP Port, sending again.'
                

