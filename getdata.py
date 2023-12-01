import pprint
import xml.etree.ElementTree as ET
import json

tree = ET.parse('stok_hareketleri_kisa.xml')
root = tree.getroot()
list = []
for str in root:
    list.append(dict(
        status       = str[0].text,
        fyear        = str[1].text,
        fmon         = str[2].text,
        evrak_tarihi = str[3].text,
        rec_id       = str[4].text,
        cari_kod     = str[5].text,
        urun_kodu    = str[6].text,
        urun_grubu   = str[7].text,
        miktar       = str[8].text
        ))

kisi = "10079"
#kisi = "20588"


def faturalar(id):
    #kişinin faturalarını döndürür
    if(len(list)==0):
        print("Satis islemlerinde bulunamadi.")

    fatura_ids =[]
    for i in list:
        if(i["cari_kod"]==id):
            if(i["rec_id"] not in fatura_ids):
                fatura_ids.append(i["rec_id"])

    return fatura_ids


def fatura_icerik(fatura_id):
    #Fatura İçeriğini Döndürür
    urun_ids =[]
    for i in list:
        if(i["rec_id"]==fatura_id):
            if(i["urun_kodu"] not in urun_ids and i["urun_kodu"] != None):
                urun_ids.append(i["urun_kodu"])
    if(len(urun_ids)==0):
        print("İçerik Bulunamadı")
    return urun_ids

urun_miktarlari = {}
def fatura_icerik_miktar(fatura_id):
    #Fatura İçeriğini Döndürür
  
    for i in list:
        if(i["rec_id"]==fatura_id):
                if urun_miktarlari.get('urun_kodu') == None:
                      print("Not Present")
                      urun_miktarlari[i["urun_kodu"]]= int(i["miktar"])
                else:
                      print("Present")
                      print("Benim kodum duplicate bul beni",['urun_kodu'])
                      onceki_miktar +=int( i["miktar"])
                      urun_miktarlari.update(dict.fromkeys(["urun_kodu"],str(onceki_miktar+int( i["miktar"]))))
                
    return urun_miktarlari


def clients_Most_Purchased_Items(kisi):
    #müşterinin en çok aldığı 20 ürünü tespit eder ve sıralar.

    for p in range( len(faturalar(kisi))):

        fatura_icerik_miktar(faturalar(kisi)[p])
    sorted_urun_miktarlari =dict(sorted(urun_miktarlari.items(), key=lambda x:x[1], reverse=True))
    
    pretty_dict = json.dumps(sorted_urun_miktarlari, indent=4)
    
    return pretty_dict

def clients_Least_Purchased_Items(kisi):
    #müşterinin en az aldığı 20 ürünü tespit eder ve sıralar.

    for p in range( len(faturalar(kisi))):

        fatura_icerik_miktar(faturalar(kisi)[p])
    sorted_urun_miktarlari =dict(sorted(urun_miktarlari.items(), key=lambda x:x[1], reverse=False))
   
    pretty_dict = json.dumps(sorted_urun_miktarlari, indent=4)
    
    return pretty_dict


if(len(faturalar(kisi)) == 0):
    print("fatura bulunamadı")
else:
   # print(kisi,"kişisinin",faturalar(kisi)[0],"no'lu faturasının içeriği=",fatura_icerik(faturalar(kisi)[0]))
  
   
    print(clients_Most_Purchased_Items(kisi))


    
    #env/Scripts/activate.ps1
    #set FLASK_ENV=development
    #flask run

