import os
from flask_restful import Api, Resource, reqparse
import pandas as pd
from scipy.misc import face

from Mask2Former.demo.facebookModel import Model
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
#? This takes in 3 playlists and generates a numpy array 
#? to describe them based on spotify metadata (3 rows pertaining to playlist)
#? call this function when a new user submits 3 playlists

#? each playlist vector for other users is plotted in n-D space
#? each vector is retrieved from the database (excluding your own playlists)
#? find nearest 2 neighbours for each of your playlists (input into KNN model)
#? you will have 6 potential matches, your top 2 soulmates should be the majority of your 6 matches
#? retrieve thir Uid's send to eric so he can display their emails

class model2_loader(Resource):
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
            im.save("/tmp/2.jpg")
        # Get string from firebase

        # Model takes in a string
        a = Model("/tmp/2.jpg")
        #!testing flask
        return {
        '1': a
        }
    
        
        
    def post(self):
        print(self)
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

        return final_ret    
            

    