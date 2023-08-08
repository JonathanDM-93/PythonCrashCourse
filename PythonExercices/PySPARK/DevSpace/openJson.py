# Librerias
import json
import pandas as pd
from pandas.io.json._table_schema import build_table_schema
# Cadena de caracteres en formato JSON

json_inicial = """
{
    "start-time":1685148268702392,
    "flags":["rd","edns"],
    "client-port":53034,
    "address-family":6,
    "dns-message":{
        "id":28127,
        "rcode":"noerror",
        "opcode":"query",
        "flags":["qr","rd","ra"],
        "question":[{
            "name":"pull-flv-f77-sg01.tiktokcdn.com.",
            "rdclass":"IN",
            "rdtype":"AAAA"}],
        "answer":[],
        "authority":[],
        "additional":[]},
    "client-address":"2806:2f0:3340:0:5fab:eb33:48b6:b4f7",
    "server-address":"2806:2f0:31:601::2",
    "view":"worldipv6",
    "resolver":"worldipv6",
    "request-length":81,
    "response-length":150,
    "device-id":"ce:f1:9a:95:c7:7e",
    "core-domain":"tiktokcdn.com.",
    "_meta":{
        "timestamp":1685148268,
        "engine-type":"cacheserve",
        "engine-version":"7.6.1.2",
        "node-id":"5b9de68e-7c18-5b23-9d73-04ef1f796e6d"}
}"""

struct_json = {
    "start-time":1685148268702392,
    "flags":["rd","edns"],
    "client-port":53034,
    "address-family":6,
    "dns-message":{
        "id":28127,
        "rcode":"noerror",
        "opcode":"query",
        "flags":["qr","rd","ra"],
        "question":[{
            "name":"pull-flv-f77-sg01.tiktokcdn.com.",
            "rdclass":"IN",
            "rdtype":"AAAA"}],
        "answer":[],
        "authority":[],
        "additional":[]},
    "client-address":"2806:2f0:3340:0:5fab:eb33:48b6:b4f7",
    "server-address":"2806:2f0:31:601::2",
    "view":"worldipv6",
    "resolver":"worldipv6",
    "request-length":81,
    "response-length":150,
    "device-id":"ce:f1:9a:95:c7:7e",
    "core-domain":"tiktokcdn.com.",
    "_meta":{
        "timestamp":1685148268,
        "engine-type":"cacheserve",
        "engine-version":"7.6.1.2",
        "node-id":"5b9de68e-7c18-5b23-9d73-04ef1f796e6d"}}


json_root_2 = {'root':json_inicial}

# Convertir cadena de caracteres JSON a un diccionario / leer una cadena con json.loads
datos_diccionario = json.loads(json_inicial)
#print(datos_diccionario)

# print(type(datos_diccionario))
# #<class 'dict'>

# {'start-time': 1685148268702392,
# 'flags': ['rd', 'edns'],
# 'client-port': 53034,
# 'address-family': 6,
# 'dns-message': {'id': 28127,
#                 'rcode': 'noerror',
#                 'opcode': 'query',
#                 'flags': ['qr', 'rd', 'ra'],
#                 'question': [{'name': 'pull-flv-f77-sg01.tiktokcdn.com.',
#                               'rdclass': 'IN',
#                               'rdtype': 'AAAA'}],
#                 'answer': [],
#                 'authority': [],
#                 'additional': []},
# 'client-address': '2806:2f0:3340:0:5fab:eb33:48b6:b4f7',
# 'server-address': '2806:2f0:31:601::2',
# 'view': 'worldipv6',
# 'resolver': 'worldipv6',
# 'request-length': 81,
# 'response-length': 150,
# 'device-id': 'ce:f1:9a:95:c7:7e',
# 'core-domain': 'tiktokcdn.com.',
# '_meta': {'timestamp': 1685148268,
#           'engine-type': 'cacheserve',
#           'engine-version': '7.6.1.2',
#           'node-id': '5b9de68e-7c18-5b23-9d73-04ef1f796e6d'}}

# Entrar a diccionario para ver los pares llave-valor
"""for llaves, valores in datos_diccionario['dns-message'].items():
    print(llaves, valores)"""

    # id 28127
    # rcode noerror
    # opcode query
    # flags ['qr', 'rd', 'ra']
    # question [{'name': 'pull-flv-f77-sg01.tiktokcdn.com.', 'rdclass': 'IN', 'rdtype': 'AAAA'}]
    # answer []
    # authority []
    # additional []

# Normalizar el JSON
# https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
JSON_Normalizado= pd.json_normalize(struct_json)
print(JSON_Normalizado.info())


print("\n *****    SEPARATOR    ******\n")


# Ver la estructura JSON
#print(json.dumps(datos_diccionario, indent=4))

# {
#     "start-time": 1685148268702392,
#     "flags": [
#         "rd",
#         "edns"
#     ],
#     "client-port": 53034,
#     "address-family": 6,
#     "dns-message": {
#         "id": 28127,
#         "rcode": "noerror",
#         "opcode": "query",
#         "flags": [
#             "qr",
#             "rd",
#             "ra"
#         ],
#         "question": [
#             {
#                 "name": "pull-flv-f77-sg01.tiktokcdn.com.",
#                 "rdclass": "IN",
#                 "rdtype": "AAAA"
#             }
#         ],
#         "answer": [],
#         "authority": [],
#         "additional": []
#     },
#     "client-address": "2806:2f0:3340:0:5fab:eb33:48b6:b4f7",
#     "server-address": "2806:2f0:31:601::2",
#     "view": "worldipv6",
#     "resolver": "worldipv6",
#     "request-length": 81,
#     "response-length": 150,
#     "device-id": "ce:f1:9a:95:c7:7e",
#     "core-domain": "tiktokcdn.com.",
#     "_meta": {
#         "timestamp": 1685148268,
#         "engine-type": "cacheserve",
#         "engine-version": "7.6.1.2",
#         "node-id": "5b9de68e-7c18-5b23-9d73-04ef1f796e6d"
#     }
# }

print("\n *****    SEPARATOR    ******\n")

#############
#json to xml
#############

# Convertir el JSON a un archivo XML el cual se puede mapear a una tabla con REDSHIFT
# Importar libreria para convertir de JSON a XML
import xmltodict
json_to_xml = xmltodict.unparse(json_root_2)
# print(json_to_xml)


