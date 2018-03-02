import pymongo
from pymongo import MongoClient

client = None
db = None
class veritabani:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['deneme']
        #dictionary(sozluk) veritabanındaki degerleri tutmak icin
        self.bilgi={}

    #kullanıcı eklemek ıcın
    def ekle(self,ismi,soyismi,mail,tel):
        self.db.Kullanicilar.insert(
            {
                "ismi": ismi,
                "soyismi": soyismi,
                "mail":mail,
                "telefon":tel

            }
        )

    def bilgiara(self,post,deger):
        self.bilgi[post]=deger

    def ara(self):
        bilgi = self.bilgi
        self.bilgi = {}
        return self.db.Kullanicilar.find(bilgi)






