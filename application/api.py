""" This module contains the apis """
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Investissement
from .serializers import InvSerializer


#Using Viewset to creat API
class All_inv_api_filter_vset(viewsets.ModelViewSet): # pylint: disable=too-many-ancestors
    """ This class contains the apis viewsets"""
    serializer_class = InvSerializer

    
    def get_queryset(self):
        """  This function lists the investments 'METHODE 01': using Viewset """
        all_inv = Investissement.objects.all()
        return all_inv

    def retrieve(self, request, *args, **kwargs):
        """  This function lists investments filtered by ville or by etat_d_avancement """
        params = kwargs
        print(params['pk'])
        params_list = params['pk'].split('-')
        invests = Investissement.objects.filter(
            Q(ville=params_list[0]) | Q(etat_d_avancement=params_list[1] ))
        serializer = InvSerializer(invests, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def all_inv_api(request):
    """  This function lists all the investments 'METHODE 02': using api_view""" 
    all_inv = Investissement.objects.all()
    data = InvSerializer(all_inv, many=True).data
    return Response(data)



@api_view(['GET'])
def inv_detail_api(request, id):
    """  This function gets a single investment by id"""
    inv_detail = Investissement.objects.get(id = id)
    data = InvSerializer(inv_detail).data
    return Response({'data': data})



#METHODE 03 Using APIView to create API
class InvAPIView(APIView):

    def get(self, *args, **kwargs):
        """  This function lists all the investments 'METHODE 03': using APIView"""
        investissements = Investissement.objects.all()
        serializer = InvSerializer(investissements, many = True)
        return Response(serializer.data)
