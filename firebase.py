import firebase_admin
from firebase_admin import credentials, firestore

cred= credentials.Certificate("./key.json")
# app=firebase_admin.initialize_app(cred)

db=firestore.client()

document=db.collection("data").document("test")

a=input("yazı girdisi : ")

document.set({
    "veriYazi":a,
    "verisayi":42,
    "veriBool": True
    
    })




#read date

data=document.get().to_dict()
data2=document.get()
data3=document.get.to_list()












