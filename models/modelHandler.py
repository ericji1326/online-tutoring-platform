import os
from flask_restful import Api, Resource, reqparse
import pandas as pd
from scipy.misc import face

# from Mask2Former.demo.facebookModel import Model
from facial_expression.home import model
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from collections import Counter
from os.path import join, dirname, realpath
from PIL import Image
from io import BytesIO
import base64

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class model_loader(Resource):
    def __init__(self):
        pass
    def get(self):
        db = firestore.client()

        #get documents from the firebase
        docs = db.collection(u'base64_image_collection').stream()
    
        #there is only one doc in the firebase which contains fields
        #each field should be a base64 image string    
        for doc in docs: 
            img_doc = doc.to_dict()

        #print(img_doc)

        #img_doc is a dictionary containing a single base64 image string
        #there should only be one key
        for key in img_doc:
            #marvin decode string, convert to image, pass to model
            image1 = img_doc[key]
            image1 = image1[23:]
            #print(img_doc[key]) #this is how you access the base64 image string
            im = Image.open(BytesIO(base64.b64decode(image1)))
            im.save("/tmp/1.jpg")
        b = model("/tmp/1.jpg")
        if b == "No Face":
            return {'expression':b}
        mood = ["Angry","Disgust","Fear","Happy","Sad","Surprise","Neutral"]
        #!testing flask
        return {
        'expression': mood[int(b)]
        }
    
        
        
    def post(self):
        #request.files['image']
        
        """ print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)

        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        request_type = args['type']
        request_json = args['message']
        # ret_status, ret_msg = ReturnData(request_type, request_json)
        # currently just returning the req straight
        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            message = "Your Message Requested: {}".format(ret_msg)
        else:
            message = "No Msg"
        
        final_ret = {"status": "Success", "message": message}

        return final_ret   """  
            

    