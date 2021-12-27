from .models import Investissement
from .serializers import InvSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets



#Using Viewset to creat API
class All_inv_api_filter_vset(viewsets.ModelViewSet):
    serializer_class = InvSerializer

    #List all the investments 'METHODE 01': using Viewset
    def get_queryset(self):
        all_inv = Investissement.objects.all()
        return all_inv

    #List investments filtered by ville and/or by etat_d_avancement
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        invests = Investissement.objects.filter(ville=params['pk'])
        serializer = InvSerializer(invests, many=True)
        return Response(serializer.data)













#List all the investments 'METHODE 02': using api_view
@api_view(['GET'])
def all_inv_api(request):
    all_inv = Investissement.objects.all()
    data = InvSerializer(all_inv, many=True).data
    return Response(data)



#Get a single investment by id
@api_view(['GET'])
def inv_detail_api(request, id):
    inv_detail = Investissement.objects.get(id = id)
    data = InvSerializer(inv_detail).data
    return Response({'data': data})