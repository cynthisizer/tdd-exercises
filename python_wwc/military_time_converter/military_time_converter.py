__author__ = 'cwu'


class MilitaryTimeConverter():

    hour = 1;    # Hour boundaries: 1-12
    minute = 0;  # Minute boundaries: 0 - 59
    dayType = 0; # 0 > AM | 1> PM

    milit_hour = 0;
    milit_min  = 0;

    def __init__(self):
        self;

    def hour(self, hour):
        if h
        self.hour = hour

        self.hour = self.sanitize_payload("HOUR", hour)
        return self.hour

    #Throw a Value Exception if improper
    def sanitize_payload(self,param1, param2):
        if param1.__eq__("HOUR"):
            temp = int(param2)
            if 1 <= temp <= 12:
                return temp
        return 0