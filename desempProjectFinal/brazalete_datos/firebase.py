# firebase.py

import firebase_admin
from firebase_admin import credentials, db

# Ruta correcta al archivo JSON de credenciales
cred = credentials.Certificate('brazalete_datos\\credenciales.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://prueba-android-2d2fc-default-rtdb.firebaseio.com/'
})

