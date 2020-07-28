from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import pickle
import numpy as np

class Clustering(APIView):

    def post(self,request):
        # annual_income = request.data.get("annual_income")
        # spending_score = request.data.get("spending_score")
        # data = {
        #     "annual_income":annual_income,
        #     "spending_score":spending_score
        # }
        # annual_income = int(annual_income)
        # spending_score = int(spending_score)
        cluster = pickle.load(open("customer_profit.pk","rb"))
        # Data = np.array([[annual_income,spending_score],[annual_income,spending_score],[annual_income,spending_score],[annual_income,spending_score],[annual_income,spending_score]])
        # print(Data)
        profit = cluster.fit_predict(Data)
        print(profit)
        profit = int(profit)
        return Response(profit)



