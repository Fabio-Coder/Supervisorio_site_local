from django.shortcuts import render
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyBFlqcoYQ07Xjpc3Bfbhuu799TYyhJI_V0",
    'authDomain': "esp32-autocom.firebaseapp.com",
    'databaseURL': "https://esp32-autocom-default-rtdb.firebaseio.com",
    'projectId': "esp32-autocom",
    'storageBucket': "esp32-autocom.appspot.com",
    'messagingSenderId': "37325631743",
    'appId': "1:37325631743:web:9cce453397844572141cca"
}

config = firebaseConfig
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def index(request):

    maquina_14003 = database.child('Status').child('14003').child('IdentificacaoMaquina').get().val()
    producao_14003 = database.child('Status').child('14003').child('Contador').get().val()
    status_14003 = database.child('Status').child('14003').child('Status').get().val()
    maquina_11001 = database.child('Status').child('11001').child('IdentificacaoMaquina').get().val()
    producao_11001 = database.child('Status').child('11001').child('Contador').get().val()
    status_11001 = database.child('Status').child('11001').child('Status').get().val()
    maquina_20001 = database.child('Status').child('20001').child('IdentificacaoMaquina').get().val()
    producao_20001 = database.child('Status').child('20001').child('Contador').get().val()
    status_20001 = database.child('Status').child('20001').child('Status').get().val()
    return render(request, 'static/index.html', {
        'maquina_14003': maquina_14003,
        'producao_14003': producao_14003,
        'status_14003': status_14003,
        'maquina_11001': maquina_11001,
        'producao_11001': producao_11001,
        'status_11001': status_11001,
        'maquina_20001': maquina_20001,
        'producao_20001': producao_20001,
        'status_20001': status_20001,
    })
