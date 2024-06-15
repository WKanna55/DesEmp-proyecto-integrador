# firebase.py

import firebase_admin
from firebase_admin import credentials, db

# Ruta correcta al archivo JSON de credenciales
cred = credentials.Certificate('brazalete_datos\\prueba-android-2d2fc-firebase-adminsdk-p14z7-04148ab8e7.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://prueba-android-2d2fc-default-rtdb.firebaseio.com/'
})

