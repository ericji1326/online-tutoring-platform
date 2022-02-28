from doctest import DONT_ACCEPT_TRUE_FOR_1
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
            cred = credentials.Certificate({
            "type": "service_account",
            "project_id": "levelup-dcde9",
            "private_key_id": "0d47f42d39765c24ef60b26f2152dcfd730e55ba",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDskgealSh+NorG\nO8MW1K1iYJa3f7ReunXV9p/3BO1S1K0X2KSZShLbeyiQgFVLKMYgtPJpFQDgg+a3\n4AHLsz5Ip4+Gf7b1QUho3NzcgIcDPr56PPS7Rnp5GORUVxPjE8X2c1h7JL/IIx+i\n7fKbWanj75AjwjN2I33zP2c51I1/4jVyrdYcaHQKapYz/YbXiYshS928Ignegf2X\ngLTOUH4YUchKYf/j7Efr4tu+pHeH2beXvETULgtViUYphpofsJ0FI4cmxT3u59Ic\n0L+X21dGK2HupUv8kUMNdPK+pmNzI40Ca1Fa+Q6qyZ8Q2Lf1jrxLKGbtj/6SKv8y\n0fQuo6snAgMBAAECggEAI0+YDKCh8YDbou4trFKPag/nvzkJEltQ67XLDQ3Ht2WL\noUkS0ddGzErsSZwA3zNAANwcE3JGoLx0wNJnV4vddUPJfmEWzTHIM0VwPrDSi49J\n0tNsENNaxDONH/JQGMS395V3n13jYGYEZVyQqf6EB26X0baS2YSVBVdb5ZEOk91F\nlzsODQtcPJUmEd2O5zOYZalkE+aVnSk0RBCINKZI0gq+y4p1+tYsGNc1h6fWHz+W\nU2JqSCm2VnJOj8nYhR20P0NInQW4IL3Q4bi/+3gNX2K8o7OjJEqQSpSldO4KEksZ\nZOV216vfUmq+oZAV1R2NTMKuOfLeQNcbpuGOg1XwQQKBgQD+nuxR1eyUhY7cEzRl\nDzF83FST3LUTd11jIcDmSukHVywhqZvgKMcjPzUdCNh/6qyF/mL1iTxPnAMDgrZS\nXUe/Pd9UB8dt1b/HFvdJWXigT/RRWd5Whgc4OlD6Ho780IWaMgikq/o5QyZEOq3v\nJcRcnhQxWO/7MAMsyogZkjSfQQKBgQDt2hOYm1wv2FtfOLpaGAKTzMFDTh7sSCCi\n2oAmTyNvgWvVpe1Vu+Hx0kXQXGzSsujf9TZsz4AM7SDIBUFM/7CRMmfnPL8xVG/9\ndh63NIXfvIL3To0giDmN12mHv1skYZ+eVBKVYUPECI5emfUMAtwuKbFO/z5qVdv3\n2SrqO6mYZwKBgQDFC/xbALEL56g9TGd55h4oQOL7YwyHOhL9irub/VEFq0Kt8nJ9\nMVGbR2k1RQk3RUeqksnGtyQDf/sdFmU+rI2/xIQ2paaCq660xmMtUp51girTYjcc\nwrCHpSnRxyBlKoKaaCokNit5cSwGFVtR/epOus9puShPPkLWwQ4+q9UpgQKBgD43\neD7IDOI7DxOmbCCa/TmaKsenTLFz4I2Y6EKdGuDVEtcNEzsE7YJrBXYOZyzqPb4v\nj3ABCzbWZGfN8BnrHE2uyL0VB9Ioiy7a0ggMRiSTVBLKymHDIIL44RLwPDAVFUK+\nLSpECgziTBN05EOjD+NHZqkKXVJFaUe419/zgVZrAoGAU29ol3uQfmD80KNtFQbL\nIfKOSYPoYWAOPbDi5YbHLi6WLWNkbZhspApcpNPalctkYbFvLk//Aw7w9IRuoZq/\nv+MeMrOrbmH+QE7/dYXZaOkHPsZ7Ez2Q35PoajDV3i5sfumXjQw59oSaHnva8ZjL\nQ6Pn1PGhmfHVJH5rEAxIlck=\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-c42pu@levelup-dcde9.iam.gserviceaccount.com",
            "client_id": "108836886346364744669",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-c42pu%40levelup-dcde9.iam.gserviceaccount.com"
        })
            
firebase_admin.initialize_app(cred)
db = firestore.client()

#get documents from the firebase
docs = db.collection(u'base64_image_collection').stream()
    
#there is only one doc in the firebase which contains fields
#each field should be a base64 image string    
for doc in docs: 
    img_doc = doc.to_dict()

#print(img_doc)
from PIL import Image
from io import BytesIO
import base64
#img_doc is a dictionary containing a single base64 image string
#there should only be one key
for key in img_doc:
    #marvin decode string, convert to image, pass to model
    image1 = img_doc[key]
    image1 = image1[23:]
    #print(img_doc[key]) #this is how you access the base64 image string
    im = Image.open(BytesIO(base64.b64decode(image1)))
    im.show()