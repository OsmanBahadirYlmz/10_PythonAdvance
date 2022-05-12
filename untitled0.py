# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:00:37 2022

@author: oby_pc
"""

import firebase_admin
from firebase_admin import credentials, firestore

cred= credentials.Certificate("./key.json")
# app=firebase_admin.initialize_app(cred)

db=firestore.client()

document=db.collection("data").document("test")

a="zczcxcxc"

document.set({
    "veriYazi":a,
    "verisayi":42,
    "veriBool": True
    
    })
