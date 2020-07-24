from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import pickle
import numpy as np

class Regression(APIView):

    def post(self,request):
        pcm = request.data.get("pcm")
        maths = request.data.get("maths")
        physics = request.data.get("physics")
        chemistry = request.data.get("chemistry")
        data = {
            "pcm":pcm,
            "maths":maths,
            "physics":physics, 
            "chemistry":chemistry
        }
        regressor = pickle.load(open("rank_predictor.pk","rb"))
        pcm = float(pcm)
        maths = float(maths)
        physics = float(physics)
        chemistry = float(chemistry)
        per = np.array([[pcm,maths,physics,chemistry]])
        rank = regressor.predict(per)
        rank = int(rank)
        return Response({"Your Expected MHTCET Rank is",rank})
