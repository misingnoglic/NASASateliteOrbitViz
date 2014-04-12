class Orbit:
    def __init__(self,n,s1,s2):
        #first line
        self.name = n
        self.number = int(s1[2:7])
        self.classification = s1[7]
        self.internationaldesignatoryr = int(s1[9:11])
        self.internationaldesignatorln = s1[11:14]
        self.internationaldesignatorpiece = s1[14:17].strip()
        self.epochyear = s1[17:20].strip()
        self.epoch = float(s1[20:32])
        self.firsttimederivativeofmean = float(s1[33:43])
        self.secondtimederivativeofmean = num(s1[44:52])
        self.bstardragterm = num(s1[53:61]) #change to e-
        self.zero = int(s1[62:63])
        self.elemsetnum = s1[64:68].strip()
        self.checksum = int(s1[68])

        #second line
        self.number2 = int(s2[2:7])
        self.inclination = float(s2[8:16]) #degrees
        self.rightascention = float(s2[17:25]) #degrees
        self.eccentricity = float("0."+s2[26:33])
        self.argumentofperigee = float(s2[34:42])
        self.meananomaly = float(s2[43:51]) #degrees
        self.meanmotion = float(s2[52:53])
        self.revnumberatepoch = int(s2[63:68])
        self.checksum2 = int(s2[68])

    def printstuff(self):
        #To test the fields
        print [self.name,self.number,self.classification,self.internationaldesignatoryr,
               self.internationaldesignatorln,self.internationaldesignatorpiece,self.epochyear,
               self.epoch,self.firsttimederivativeofmean,self.secondtimederivativeofmean,self.bstardragterm,
               self.zero,self.elemsetnum, self.checksum]
        print [self.number2,self.inclination,self.rightascention,self.eccentricity,
               self.argumentofperigee,self.meananomaly,self.meanmotion,self.revnumberatepoch,
               self.checksum]
        
        
def num(s):
    temp = s[:-2].strip()
    temp = "0."+temp
    return float(temp)*(10**int(s[-2:]))
