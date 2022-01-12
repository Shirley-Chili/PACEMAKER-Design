import types
from typing import Type


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class DOOmode:
    def __init__(self):
        self.lrl = 60
        self.url = 120
        self.aAmp = 5
        self.VAmp = 5
        self.apw = 1
        self.FAD = 150
        self.vpw = 1

    def getLRL(self):
        return self.lrl

    def getURL(self):
        return self.url

    def getaAmp(self):
        return self.aAmp

    def getAPW(self):
        return self.apw

    def getFAD(self):
        return self.FAD

    def getvAmp(self):
        return self.VAmp

    def getVPW(self):
        return self.vpw

    def setLRL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (((int(v) >= 30 and int(v) <= 50 and float(v) % 5 == 0)) or (
                    int(v) >= 90 and int(v) <= 175 and float(v) % 5 == 0) or (
                    int(v) > 50 and int(v) < 90 and float(v) % 1 == 0)):
                self.lrl = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) >= 50 and int(v) <= 175 and int(v) % 5 == 0):
                self.url = int(v)
            else:
                raise IndexError

        else:
            raise TypeError

    def setaAmp(self, v):
        if (is_number(v)):
            if (float(v) <= 5.0 and float(v) >= 0.1 and (float(v) * 10) % 1 == 0):

                self.aAmp = float(v)
                #
            else:
                raise IndexError

        else:
            raise TypeError

    def setAPW(self, v):
        if (is_number(v)):
            if (float(v) >= 1 and float(v) <= 30 and float(v) % 1 == 0):
                self.apw = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVAmp(self, v):
        if (is_number(v)):
            if (float(v) <= 5 and float(v) >= 0.1 and float(v) % 0.5 == 0):

                self.VAmp = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVPW(self, v):
        if (is_number(v)):
            if (float(v) <= 30 and float(v) >= 1 and float(v) % 1 == 0):
                self.vpw = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setFAD(self, v):
        if (is_number(v)):
            if (float(v) >= 70 and float(v) <= 300 and float(v) % 10 == 0):
                self.FAD = v
            else:
                raise IndexError
        else:
            raise TypeError


class AOORmode:
    def __init__(self):
        self.lrl = 60
        self.url = 120
        self.MSR = 120
        self.aAmp = 5
        self.apw = 1
        '''self.aT='''
        self.reactionT = 30
        self.RF = 8
        self.recoveryT = 5

    def getLRL(self):
        return self.lrl

    def getURL(self):
        return self.url

    def getaAmp(self):
        return self.aAmp

    def getAPW(self):
        return self.apw

    def getMSR(self):
        return self.MSR

    '''def getAT(self):
            return self.AT'''

    def getRF(self):
        return self.RF

    def getReactionT(self):
        return self.reactionT

    def getRecoveryT(self):
        return self.recoveryT

    def setLRL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (((int(v) >= 30 and int(v) <= 50 and float(v) % 5 == 0)) or (
                    int(v) >= 90 and int(v) <= 175 and float(v) % 5 == 0) or (
                    int(v) > 50 and int(v) < 90 and float(v) % 1 == 0)):
                self.lrl = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) >= 50 and int(v) <= 175 and int(v) % 5 == 0):
                self.url = int(v)
            else:
                raise IndexError

        else:
            raise TypeError

    def setaAmp(self, v):
        if (is_number(v)):
            if (float(v) <= 5.0 and float(v) >= 0.1 and (float(v) * 10) % 1 == 0):

                self.aAmp = float(v)
                #
            else:
                raise IndexError

        else:
            raise TypeError

    def setAPW(self, v):
        if (is_number(v)):
            if (float(v) >= 1 and float(v) <= 30 and float(v) % 1 == 0):
                self.apw = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setMSR(self, v):
        if (is_number(v)):
            if (float(v) <= 175 and float(v) >= 50 and float(v) % 5 == 0):

                self.MSR = int(v)

            else:
                raise IndexError

        else:
            raise TypeError

    '''def AT(self,v):
        if(is_number(v)):
            if (float(v)<=175 and float(v)>=50 and float(v)%5==0):

                self.aT=float(v)

            else:
                raise IndexError

        else:
            raise TypeError'''

    def setReactionT(self, v):
        if (is_number(v)):
            if (float(v) <= 50 and float(v) >= 10 and float(v) % 10 == 0):

                self.reactionT = float(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setRF(self, v):
        if (is_number(v)):
            if (float(v) <= 16 and float(v) >= 1 and (float(v) * 10) % 10 == 0):

                self.RF = float(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setRecoveryT(self, v):
        if (is_number(v)):
            if (float(v) <= 16 and float(v) >= 2 and (float(v) * 10) % 10 == 0):

                self.recoveryT = float(v)

            else:
                raise IndexError

        else:
            raise TypeError


class VOORmode:
    def __init__(self):
        self.lrl = 60
        self.url = 120
        self.MSR = 120
        self.FAD = 150
        self.vAmp = 5
        self.vpw = 1
        '''self.aT='''
        self.reactionT = 30
        self.RF = 8
        self.recoveryT = 5

    def getLRL(self):
        return self.lrl

    def getURL(self):
        return self.url

    def getvAmp(self):
        return self.vAmp

    def getFAD(self):
        return self.FAD

    def getVPW(self):
        return self.vpw

    def getMSR(self):
        return self.MSR

    def getRF(self):
        return self.RF

    '''def getAT(self):
            return self.AT'''

    def getReactionT(self):
        return self.reactionT

    def getRecoveryT(self):
        return self.recoveryT

    def setLRL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (((int(v) >= 30 and int(v) <= 50 and float(v) % 5 == 0)) or (
                    int(v) >= 90 and int(v) <= 175 and float(v) % 5 == 0) or (
                    int(v) > 50 and int(v) < 90 and float(v) % 1 == 0)):
                self.lrl = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) >= 50 and int(v) <= 175 and int(v) % 5 == 0):
                self.url = int(v)
            else:
                raise IndexError

        else:
            raise TypeError

    def setVAmp(self, v):
        if (is_number(v)):
            if (float(v) <= 5 and float(v) >= 0.1 and float(v) % 0.5 == 0):

                self.VAmp = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVPW(self, v):
        if (is_number(v)):
            if (float(v) <= 30 and float(v) >= 1 and float(v) % 1 == 0):
                self.vpw = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setFAD(self, v):
        if (is_number(v)):
            if (float(v) >= 70 and float(v) <= 300 and float(v) % 10 == 0):
                self.FAD = v
            else:
                raise IndexError
        else:
            raise TypeError

    def setMSR(self, v):
        if (is_number(v)):
            if (float(v) <= 175 and float(v) >= 50 and float(v) % 5 == 0):

                self.MSR = int(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setReactionT(self, v):
        if (is_number(v)):
            if (float(v) <= 50 and float(v) >= 10 and float(v) % 10 == 0):

                self.reactionT = float(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setRF(self, v):
        if (is_number(v)):
            if (float(v) <= 16 and float(v) >= 1 and (float(v) * 10) % 10 == 0):

                self.RF = float(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setRecoveryT(self, v):
        if (is_number(v)):
            if (float(v) <= 16 and float(v) >= 2 and (float(v) * 10) % 10 == 0):

                self.recoveryT = float(v)

            else:
                raise IndexError

        else:
            raise TypeError


class AAIRmode:
    def __init__(self):
        self.lrl = 60
        self.url = 120
        self.aAmp = 5
        self.apw = 1
        self.MSR = 120
        '''self.aT='''
        self.AS=0
        self.reactionT = 30
        self.RF = 8
        self.recoveryT = 5
        self.arp = 250

    def getLRL(self):
        return self.lrl

    def getRF(self):
        return self.RF

    def getURL(self):
        return self.url

    def getaAmp(self):
        return self.aAmp

    def getAPW(self):
        return self.apw

    def getMSR(self):
        return self.MSR

    def getAS(self):
            return self.AS

    def getReactionT(self):
        return self.reactionT

    def getRecoveryT(self):
        return self.recoveryT

    def getARP(self):
        return self.arp

    def setMSR(self, v):
        if (is_number(v)):
            if (float(v) <= 175 and float(v) >= 50 and float(v) % 5 == 0):

                self.MSR = int(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setLRL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (((int(v) >= 30 and int(v) <= 50 and float(v) % 5 == 0)) or (
                    int(v) >= 90 and int(v) <= 175 and float(v) % 5 == 0) or (
                    int(v) > 50 and int(v) < 90 and float(v) % 1 == 0)):
                self.lrl = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) >= 50 and int(v) <= 175 and int(v) % 5 == 0):
                self.url = int(v)
            else:
                raise IndexError

        else:
            raise TypeError

    def setaAmp(self, v):
        if (is_number(v)):
            if (float(v) <= 5.0 and float(v) >= 0.1 and (float(v) * 10) % 1 == 0):

                self.aAmp = float(v)
                #
            else:
                raise IndexError

        else:
            raise TypeError

    def setARP(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) >= 150 and int(v) <= 500 and float(v) % 10 == 0):
                self.arp = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setAPW(self, v):
        if (is_number(v)):
            if (float(v) >= 1 and float(v) <= 30 and float(v) % 1 == 0):
                self.apw = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setReactionT(self, v):
        if (is_number(v)):
            if (float(v) <= 50 and float(v) >= 10 and float(v) % 10 == 0):

                self.reactionT = float(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setRF(self, v):
        if (is_number(v)):
            if (float(v) <= 16 and float(v) >= 1 and (float(v) * 10) % 10 == 0):

                self.RF = float(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setRecoveryT(self, v):
        if (is_number(v)):
            if (float(v) <= 16 and float(v) >= 2 and (float(v) * 10) % 10 == 0):

                self.recoveryT = float(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setAS(self, v):
        if (is_number(v)):
            if (float(v) <= 5 and float(v) >= 0 and (float(v) * 10) % 1 == 0):

                self.AS = float(v)

            else:
                raise IndexError

        else:
            raise TypeError


class VVIRmode:
    def __init__(self):
        self.lrl = 60
        self.url = 120
        self.VAmp = 5
        self.vpw = 1
        self.MSR = 120
        '''self.aT='''
        self.reactionT = 30
        self.RF = 8
        self.recoveryT = 5
        self.VS=0
        self.vrp = 320

    def getVRP(self):
        return self.vrp

    def getMSR(self):
        return self.MSR

    def getLRL(self):
        return self.lrl

    def getURL(self):
        return self.url

    def getVAmp(self):
        return self.VAmp

    def getVPW(self):
        return self.vpw

    '''def getAT(self):
            return self.AT'''

    def getRF(self):
        return self.RF

    def getReactionT(self):
        return self.reactionT

    def getRecoveryT(self):
        return self.recoveryT

    def getVS(self):
        return self.VS

    def setVRP(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) >= 150 and int(v) <= 500 and float(v) % 10 == 0):
                self.vrp = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setMSR(self, v):
        if (is_number(v)):
            if (float(v) <= 175 and float(v) >= 50 and float(v) % 5 == 0):

                self.MSR = int(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setLRL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (((int(v) >= 30 and int(v) <= 50 and float(v) % 5 == 0)) or (
                    int(v) >= 90 and int(v) <= 175 and float(v) % 5 == 0) or (
                    int(v) > 50 and int(v) < 90 and float(v) % 1 == 0)):

                self.lrl = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) <= 175 and int(v) >= 50 and int(v) % 5 == 0):
                self.url = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVAmp(self, v):
        if (is_number(v)):
            if (float(v) <= 5 and float(v) >= 0.1 and float(v) % 0.5 == 0):

                self.VAmp = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVPW(self, v):
        if (is_number(v)):
            if (float(v) <= 30 and float(v) >= 1 and float(v) % 1 == 0):
                self.vpw = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setReactionT(self, v):
        if (is_number(v)):
            if (float(v) <= 50 and float(v) >= 10 and float(v) % 10 == 0):

                self.reactionT = float(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setRF(self, v):
        if (is_number(v)):
            if (float(v) <= 16 and float(v) >= 1 and (float(v) * 10) % 10 == 0):

                self.RF = float(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setRecoveryT(self, v):
        if (is_number(v)):
            if (float(v) <= 16 and float(v) >= 2 and (float(v) * 10) % 10 == 0):

                self.recoveryT = float(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setVS(self, v):
        if (is_number(v)):
            if (float(v) >= 0 and float(v) <= 5 and (float(v)*10) % 1 == 0):
                self.VS = float(v)
            else:
                raise IndexError
        else:
            raise TypeError


class DOORmode:
    def __init__(self):
        self.lrl = 60
        self.url = 120
        self.aAmp = 5
        self.VAmp = 5
        self.apw = 1
        self.FAD = 150
        self.MSR = 120
        self.vpw = 1
        self.reactionT = 30
        self.RF = 8
        self.recoveryT = 5

    def getLRL(self):
        return self.lrl

    def getURL(self):
        return self.url

    def getaAmp(self):
        return self.aAmp

    def getAPW(self):
        return self.apw

    def getvAmp(self):
        return self.VAmp

    def getMSR(self):
        return self.MSR

    def getVPW(self):
        return self.vpw

    def getFAD(self):
        return self.FAD

    def getRF(self):
        return self.RF

    def getReactionT(self):
        return self.reactionT

    def getRecoveryT(self):
        return self.recoveryT

    def setLRL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (((int(v) >= 30 and int(v) <= 50 and float(v) % 5 == 0)) or (
                    int(v) >= 90 and int(v) <= 175 and float(v) % 5 == 0) or (
                    int(v) > 50 and int(v) < 90 and float(v) % 1 == 0)):
                self.lrl = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) >= 50 and int(v) <= 175 and int(v) % 5 == 0):
                self.url = int(v)
            else:
                raise IndexError

        else:
            raise TypeError

    def setaAmp(self, v):
        if (is_number(v)):
            if (float(v) <= 5.0 and float(v) >= 0.1 and (float(v) * 10) % 1 == 0):

                self.aAmp = float(v)
                #
            else:
                raise IndexError

        else:
            raise TypeError

    def setAPW(self, v):
        if (is_number(v)):
            if (float(v) >= 1 and float(v) <= 30 and float(v) % 1 == 0):
                self.apw = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVAmp(self, v):
        if (is_number(v)):
            if (float(v) <= 5 and float(v) >= 0.1 and float(v) % 0.5 == 0):

                self.VAmp = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVPW(self, v):
        if (is_number(v)):
            if (float(v) <= 30 and float(v) >= 1 and float(v) % 1 == 0):
                self.vpw = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setFAD(self, v):
        if (is_number(v)):
            if (float(v) >= 70 and float(v) <= 300 and float(v) % 10 == 0):
                self.FAD = v
            else:
                raise IndexError
        else:
            raise TypeError

    def setMSR(self, v):
        if (is_number(v)):
            if (float(v) <= 175 and float(v) >= 50 and float(v) % 5 == 0):

                self.MSR = int(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setReactionT(self, v):
        if (is_number(v)):
            if (float(v) <= 50 and float(v) >= 10 and float(v) % 10 == 0):

                self.reactionT = float(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setRF(self, v):
        if (is_number(v)):
            if (float(v) <= 16 and float(v) >= 1 and (float(v) * 10) % 10 == 0):

                self.RF = float(v)

            else:
                raise IndexError

        else:
            raise TypeError

    def setRecoveryT(self, v):
        if (is_number(v)):
            if (float(v) <= 16 and float(v) >= 2 and (float(v) * 10) % 10 == 0):

                self.recoveryT = float(v)

            else:
                raise IndexError

        else:
            raise TypeError


class AOOmode:
    def __init__(self):
        self.lrl = 60
        self.url = 120
        self.aAmp = 5
        self.apw = 1

    def getLRL(self):
        return self.lrl

    def getURL(self):
        return self.url

    def getaAmp(self):
        return self.aAmp

    def getAPW(self):
        return self.apw

    def setLRL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (((int(v) >= 30 and int(v) <= 50 and float(v) % 5 == 0)) or (
                    int(v) >= 90 and int(v) <= 175 and float(v) % 5 == 0) or (
                    int(v) > 50 and int(v) < 90 and float(v) % 1 == 0)):
                self.lrl = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) >= 50 and int(v) <= 175 and int(v) % 5 == 0):
                self.url = int(v)
            else:
                raise IndexError

        else:
            raise TypeError

    def setaAmp(self, v):
        if (is_number(v)):
            if (float(v) <= 5.0 and float(v) >= 0.1 and (float(v) * 10) % 1 == 0):

                self.aAmp = float(v)
                #
            else:
                raise IndexError

        else:
            raise TypeError

    def setAPW(self, v):
        if (is_number(v)):
            if (float(v) >= 1 and float(v) <= 30 and float(v) % 1 == 0):
                self.apw = float(v)
            else:
                raise IndexError
        else:
            raise TypeError


class VOOmode:
    def __init__(self):
        self.lrl = 60
        self.url = 120
        self.VAmp = 5
        self.vpw = 1

    def getLRL(self):
        return self.lrl

    def getURL(self):
        return self.url

    def getVAmp(self):
        return self.VAmp

    def getVPW(self):
        return self.vpw

    def setLRL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (((int(v) >= 30 and int(v) <= 50 and float(v) % 5 == 0)) or (
                    int(v) >= 90 and int(v) <= 175 and float(v) % 5 == 0) or (
                    int(v) > 50 and int(v) < 90 and float(v) % 1 == 0)):

                self.lrl = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) <= 175 and int(v) >= 50 and int(v) % 5 == 0):
                self.url = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVAmp(self, v):
        if (is_number(v)):
            if (float(v) <= 5 and float(v) >= 0.1 and float(v) % 0.5 == 0):

                self.VAmp = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVPW(self, v):
        if (is_number(v)):
            if (float(v) <= 30 and float(v) >= 1 and float(v) % 1 == 0):
                self.vpw = float(v)
            else:
                raise IndexError
        else:
            raise TypeError


class AAImode:
    def __init__(self):
        self.lrl = 60
        self.url = 120
        self.aAmp = 5
        self.apw = 1
        self.arp = 250
        self.AS=0

    def getAS(self):
        return self.AS
    def getLRL(self):
        return self.lrl

    def getURL(self):
        return self.url

    def getaAmp(self):
        return self.aAmp

    def getAPW(self):
        return self.apw

    def getARP(self):
        return self.arp

    def setAS(self, v):
        if (is_number(v)):
            if (float(v) <= 5 and float(v) >= 0 and (float(v) * 10) % 1 == 0):

                self.AS = float(v)

            else:
                raise IndexError

        else:
            raise TypeError
    def setLRL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (((int(v) >= 30 and int(v) <= 50 and float(v) % 5 == 0)) or (
                    int(v) >= 90 and int(v) <= 175 and float(v) % 5 == 0) or (
                    int(v) > 50 and int(v) < 90 and float(v) % 1 == 0)):

                self.lrl = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) >= 50 and int(v) <= 175 and float(v) % 5 == 0):
                self.url = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setaAmp(self, v):
        if (is_number(v)):
            if (float(v) <= 5.0 and float(v) >= 0.1 and (float(v) * 10) % 1 == 0):

                self.aAmp = float(v)
                #
            else:
                raise IndexError

        else:
            raise TypeError

    def setAPW(self, v):
        if (is_number(v)):
            if (float(v) >= 1 and float(v) <= 30 and float(v) % 1 == 0):
                self.apw = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setARP(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) >= 150 and int(v) <= 500 and float(v) % 10 == 0):
                self.arp = int(v)
            else:
                raise IndexError
        else:
            raise TypeError


class VVImode:
    def __init__(self):
        self.lrl = 60
        self.url = 120
        self.VAmp = 5
        self.vpw = 1
        self.vrp = 320
        self.VS = 0

    def getLRL(self):
        return self.lrl

    def getURL(self):
        return self.url

    def getVAmp(self):
        return self.VAmp

    def getVPW(self):
        return self.vpw

    def getVRP(self):
        return self.vrp

    def getVS(self):
        return self.VS

    def setLRL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (((int(v) >= 30 and int(v) <= 50 and float(v) % 5 == 0)) or (
                    int(v) >= 90 and int(v) <= 175 and float(v) % 5 == 0) or (
                    int(v) > 50 and int(v) < 90 and float(v) % 1 == 0)):

                self.lrl = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) >= 50 and int(v) <= 175 and float(v) % 5 == 0):

                self.url = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVAmp(self, v):
        if (is_number(v)):
            if (float(v) <= 5 and float(v) >= 0.1 and float(v) % 0.5 == 0):

                self.VAmp = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVPW(self, v):
        if (is_number(v)):
            if (float(v) <= 30 and float(v) >= 1 and float(v) % 1 == 0):
                self.vpw = float(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVRP(self, v):
        if (is_number(v) and float(v) % 1 == 0):
            if (int(v) >= 150 and int(v) <= 500 and float(v) % 10 == 0):
                self.vrp = int(v)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVS(self, v):
        if (is_number(v)):
            if (float(v) >= 0 and float(v) <= 5 and (float(v)*10) % 1 == 0):
                self.VS = float(v)
            else:
                raise IndexError
        else:
            raise TypeError