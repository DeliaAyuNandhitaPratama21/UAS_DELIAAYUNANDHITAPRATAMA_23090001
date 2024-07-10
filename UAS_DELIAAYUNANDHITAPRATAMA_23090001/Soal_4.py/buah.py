class Buah:
    def __init__(self, nama, warna, rasa):
        self.__nama = nama
        self.__warna = warna
        self.__rasa = rasa

    def getNama(self, namaBaru):
        self.__nama = namaBaru

    def getWarna(self, warnaBaru):
        self.__warna = warnaBaru

    def getRasa(self, rasaBaru):
        self.__rasa = rasaBaru
    
    def setNama(self, namaBaru):
        self.__nama = namaBaru

    def setWarna(self, warnaBaru):
        self.__warna = warnaBaru

    def setRasa(self, rasaBaru):
        self.__rasa = rasaBaru

    def infoBuah(self):
        return f'Nama Buah : {self.getNama()}, Warna Buah : {self.getWarna()}, Rasa Buah : {self.getRasa()}'
    
class Mangga(Buah):
    def __init__(self, vitamin, nama, warna, rasa):
        super().__init__(nama, warna, rasa)
        self.__vitamin = vitamin

    def getVitamin(self):
        return self.__vitamin
    
    def setVitamin(self, vitaminBaru):
        self.__ukuranFile = vitaminBaru

    def info_Mangga(self):
        return f'{self.infoBuah()}, Vitamin : {self.getVitamin()}'