from pymongo import MongoClient
from flask import Flask, render_template, request
from database import veritabani
import json
from bson.json_util import dumps

app = Flask(__name__)

arama_deger=["ismi","soyismi","mail","telefon"]


@app.route('/',methods=['POST'])
def post_page():

        if "ekle" in request.form:
            json_data = request.form['ekle']
            try:
                data = json.loads(json_data)
            except Exception :
                return "yanlıs kullanım"

            if set(("ismi", "soyismi", "mail", "telefon")) <= set(data):
                 v.ekle(data["ismi"], data["soyismi"], data["mail"], data["telefon"])
            else:
                return "yanlıs parametre"

        else :
            #Kullanıcı bilgisi aramak icin
            for post_deger in request.form:
                deger = request.form[post_deger]
                #print(deger)
                #print(post_deger)

                if not (post_deger in arama_deger):
                    return "gecersiz deger = %s" % post_deger
                if deger == "":
                    return "bos  deger = %s " % post_deger

                v.bilgiara(post_deger, deger)
        sorgu = list(v.ara())
        #print(sorgu)
        ekran = dumps(sorgu)
        return ekran



if __name__ == '__main__':
    v=veritabani()
    app.run()
