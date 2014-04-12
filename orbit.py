class Orbit:
    def __init__(self,n,s1,s2):
        #first line
        self.name = n
        self.number = s1[2:7]
        self.classification = s1[7]
        self.internationaldesignatoryr = s1[9:11]
        self.internationaldesignatorln = s1[11:14]
        self.internationaldesignatorpiece = s1[14:17]
        self.epochyear = s1[17:20]
        self.epoch = s1[20:32]
        self.firsttimederivativeofmean = s1[33:43]
        self.secondtimederivativeofmean = s1[44:52]
        self.bstardragterm = s1[53:61]
        self.zero = s1[62:63]
        self.elemsetnum = s1[64:68]
        self.checksum = s1[68]

        #second line
        self.number2 = s2[2:7]
        self.inclination = s2[8:16] #degrees
        self.rightascention = s2[17:25] #degrees
        self.eccentricity = s2[26:33]
        self.argumentofperigee = s2[34:42]
        self.meananomaly = s2[43:51] #degrees
        self.meanmotion = s2[52:53] 
        self.revnumberatepoch = s2[63:68]
        self.checksum = s2[68]

    def printstuff(self):
        print [self.name,self.number,self.classification,self.internationaldesignatoryr,
               self.internationaldesignatorln,self.internationaldesignatorpiece,self.epochyear,
               self.epoch,self.firsttimederivativeofmean,self.secondtimederivativeofmean,self.bstardragterm,
               self.zero,self.elemsetnum, self.checksum]
        print [self.number2,self.inclination,self.rightascention,self.eccentricity,
               self.argumentofperigee,self.meananomaly,self.meanmotion,self.revnumberatepoch,
               self.checksum]
        
        
