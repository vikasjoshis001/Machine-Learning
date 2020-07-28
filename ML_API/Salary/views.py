from django.shortcuts import render
from rest_framework.views import APIView
import pickle
from rest_framework.response import Response

class Salary(APIView):

    def post(self,request):
        experience = request.data.get("experience")
        data = {
            "experience":experience
        }
        regressor = pickle.load(open("salary_predictor.pk","rb"))
        experience = float(experience)
        salary = regressor.predict([[experience]])
        salary = int(salary)
        return Response(salary)