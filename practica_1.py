import datetime

class mascotas:
    def __init__(self):
        self.__name = ""
        self.__id = 0
        self.__type = ""
        self.__weight = 0
        self.__date = datetime.datetime().strftime("%m/%d/%Y")
        self.__dic_medicine = {}

    def getname(self):
        return self.__name
    def getid(self):
        return self.__id
    def gettype(self):
        return self.__type
    def getweight(self):
        return self.__weight
    def getdate(self):
        return self.__date
    def getdicmedicine(self):
        return self.__dic_medicine
    
    def setname(self,name):
        self.__name = name
    def setid(self,id):
        self.__id = id
    def settype(self,type):
        self.__type
    def getweight (self,weight):
        self.__weight = weight
    def getdate(self,date):
        self.__date = date
    def getdicmedicine(self,dic_medicine):
        self.__dic_medicine = dic_medicine

class medicamento:
    def __init__(self):
        self.__name = ""
        self.__dosis = 0
    
    def getname (self):
        return self.__name
    def getdosis (self):
        return self.__dosis
    
    def setname(self,name):
        self.__name = name
    def setdosis(self,dosis):
        self.__dosis = dosis

class sistema:
    def __init__(self):
        self.__dic_mascotas = {}
        