from django.shortcuts import render
import pyrebase
from django.template.defaulttags import register
from collections import namedtuple
from django.utils.safestring import SafeString

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


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    maquina_5002 = database.child('Status').child('5002').child('IdentificacaoMaquina').get().val()
    producao_5002 = database.child('Status').child('5002').child('Contador').get().val()
    status_5002 = database.child('Status').child('5002').child('Status').get().val()

    maquina_5001 = database.child('Status').child('5001').child('IdentificacaoMaquina').get().val()
    producao_5001 = database.child('Status').child('5001').child('Contador').get().val()
    status_5001 = database.child('Status').child('5001').child('Status').get().val()

    maquina_9003 = database.child('Status').child('9003').child('IdentificacaoMaquina').get().val()
    producao_9003 = database.child('Status').child('9003').child('Contador').get().val()
    status_9003 = database.child('Status').child('9003').child('Status').get().val()

    maquina_9002 = database.child('Status').child('9002').child('IdentificacaoMaquina').get().val()
    producao_9002 = database.child('Status').child('9002').child('Contador').get().val()
    status_9002 = database.child('Status').child('9002').child('Status').get().val()

    maquina_5003 = database.child('Status').child('5003').child('IdentificacaoMaquina').get().val()
    producao_5003 = database.child('Status').child('5003').child('Contador').get().val()
    status_5003 = database.child('Status').child('5003').child('Status').get().val()

    maquina_11001 = database.child('Status').child('11001').child('IdentificacaoMaquina').get().val()
    producao_11001 = database.child('Status').child('11001').child('Contador').get().val()
    status_11001 = database.child('Status').child('11001').child('Status').get().val()

    maquina_9001 = database.child('Status').child('9001').child('IdentificacaoMaquina').get().val()
    producao_9001 = database.child('Status').child('9001').child('Contador').get().val()
    status_9001 = database.child('Status').child('9001').child('Status').get().val()

    maquina_11002 = database.child('Status').child('11002').child('IdentificacaoMaquina').get().val()
    producao_11002 = database.child('Status').child('11002').child('Contador').get().val()
    status_11002 = database.child('Status').child('11002').child('Status').get().val()

    maquina_5004 = database.child('Status').child('5004').child('IdentificacaoMaquina').get().val()
    producao_5004 = database.child('Status').child('5004').child('Contador').get().val()
    status_5004 = database.child('Status').child('5004').child('Status').get().val()

    maquina_20001 = database.child('Status').child('20001').child('IdentificacaoMaquina').get().val()
    producao_20001 = database.child('Status').child('20001').child('Contador').get().val()
    status_20001 = database.child('Status').child('20001').child('Status').get().val()

    maquina_16001 = database.child('Status').child('16001').child('IdentificacaoMaquina').get().val()
    producao_16001 = database.child('Status').child('16001').child('Contador').get().val()
    status_16001 = database.child('Status').child('16001').child('Status').get().val()

    maquina_16002 = database.child('Status').child('16002').child('IdentificacaoMaquina').get().val()
    producao_16002 = database.child('Status').child('16002').child('Contador').get().val()
    status_16002 = database.child('Status').child('16002').child('Status').get().val()

    maquina_14001 = database.child('Status').child('14001').child('IdentificacaoMaquina').get().val()
    producao_14001 = database.child('Status').child('14001').child('Contador').get().val()
    status_14001 = database.child('Status').child('14001').child('Status').get().val()

    maquina_14002 = database.child('Status').child('14002').child('IdentificacaoMaquina').get().val()
    producao_14002 = database.child('Status').child('14002').child('Contador').get().val()
    status_14002 = database.child('Status').child('14002').child('Status').get().val()

    maquina_14003 = database.child('Status').child('14003').child('IdentificacaoMaquina').get().val()
    producao_14003 = database.child('Status').child('14003').child('Contador').get().val()
    status_14003 = database.child('Status').child('14003').child('Status').get().val()

    maquina_1000 = database.child('Status').child('1000').child('IdentificacaoMaquina').get().val()
    producao_1000 = database.child('Status').child('1000').child('Contador').get().val()
    status_1000 = database.child('Status').child('1000').child('Status').get().val()

    maquina_1200 = database.child('Status').child('1200').child('IdentificacaoMaquina').get().val()
    producao_1200 = database.child('Status').child('1200').child('Contador').get().val()
    status_1200 = database.child('Status').child('1200').child('Status').get().val()

    maquina_20002 = database.child('Status').child('20002').child('IdentificacaoMaquina').get().val()
    producao_20002 = database.child('Status').child('20002').child('Contador').get().val()
    status_20002 = database.child('Status').child('20002').child('Status').get().val()

    maquina_20003 = database.child('Status').child('20003').child('IdentificacaoMaquina').get().val()
    producao_20003 = database.child('Status').child('20003').child('Contador').get().val()
    status_20003 = database.child('Status').child('20003').child('Status').get().val()

    maquinas = {'maquina_5002': maquina_5002,
                'producao_5002': producao_5002,
                'status_5002': status_5002,
                'maquina_5001': maquina_5001,
                'producao_5001': producao_5001,
                'status_5001': status_5001,
                'maquina_9003': maquina_9003,
                'producao_9003': producao_9003,
                'status_9003': status_9003,
                'maquina_9002': maquina_9002,
                'producao_9002': producao_9002,
                'status_9002': status_9002,
                'maquina_5003': maquina_5003,
                'producao_5003': producao_5003,
                'status_5003': status_5003,
                'maquina_11001': maquina_11001,
                'producao_11001': producao_11001,
                'status_11001': status_11001,
                'maquina_9001': maquina_9001,
                'producao_9001': producao_9001,
                'status_9001': status_9001,
                'maquina_11002': maquina_11002,
                'producao_11002': producao_11002,
                'status_11002': status_11002,
                'maquina_5004': maquina_5004,
                'producao_5004': producao_5004,
                'status_5004': status_5004,
                'maquina_20001': maquina_20001,
                'producao_20001': producao_20001,
                'status_20001': status_20001,
                'maquina_16001': maquina_16001,
                'producao_16001': producao_16001,
                'status_16001': status_16001,
                'maquina_16002': maquina_16002,
                'producao_16002': producao_16002,
                'status_16002': status_16002,
                'maquina_14001': maquina_14001,
                'producao_14001': producao_14001,
                'status_14001': status_14001,
                'maquina_14002': maquina_14002,
                'producao_14002': producao_14002,
                'status_14002': status_14002,
                'maquina_14003': maquina_14003,
                'producao_14003': producao_14003,
                'status_14003': status_14003,
                'maquina_1000': maquina_1000,
                'producao_1000': producao_1000,
                'status_1000': status_1000,
                'maquina_1200': maquina_1200,
                'producao_1200': producao_1200,
                'status_1200': status_1200,
                'maquina_20002': maquina_20002,
                'producao_20002': producao_20002,
                'status_20002': status_20002,
                'maquina_20003': maquina_20003,
                'producao_20003': producao_20003,
                'status_20003': status_20003}

    return render(request, 'static/index.html', maquinas)
