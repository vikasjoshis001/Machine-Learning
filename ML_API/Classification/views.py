from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import pickle
import numpy as np 

class Classification(APIView):

    def post(self,request):
        price = request.data.get("price")
        maintenance_cost = request.data.get("maintenance_cost")
        no_of_doors = request.data.get("no_of_doors")
        no_of_peoples = request.data.get("no_of_peoples")
        lug_boot = request.data.get("lug_boot")
        safety = request.data.get("safety")
        data = {
            "price":price,
            "maintenance_cost":maintenance_cost,
            "no_of_doors":no_of_doors,
            "no_of_peoples":no_of_peoples,
            "lug_boot":lug_boot,
            "safety":safety
        }

        price = int(price)
        maintenance_cost = int(maintenance_cost)
        no_of_doors = int(no_of_doors)
        no_of_peoples = int(no_of_peoples)
        lug_boot = int(lug_boot)
        safety = int(safety)

        print(price)

        classifier = pickle.load(open("car evaluation.pk","rb"))
        evaluate = np.array([[price,maintenance_cost,no_of_doors,no_of_peoples,lug_boot,safety]])
        print(evaluate)
        result = classifier.predict(evaluate)
        result = int(result)
        return Response(result)

# for 0 and 1
# vhigh = 3
# high = 0
# med = 2
# low = 1

# for 2
# 3 = 1
# 2 = 0
# 4 = 2
# 5more = 3

# for 3
# more = 2
# 2 = 0
# 4 = 1

# for 4:
# small = 2
# big = 0
# med = 1
    
    
# for 5
# high = 0 
# med = 2
# low = 1

# for result
# unacc = 2
# acc = 0
# good = 1
# vgood = 3

  
