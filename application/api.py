from .models import Investissement
from .serializers import InvSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



#List all the investments
@api_view(['GET'])
def all_inv_api(request):
    all_inv = Investissement.objects.all()
    data = InvSerializer(all_inv, many=True).data
    return Response(data)



#List investments filtered by ville and/or by etat_d_avancement





#Get a single investment by id
@api_view(['GET'])
def inv_detail_api(request, id):
    inv_detail = Investissement.objects.get(id = id)
    data = InvSerializer(inv_detail).data
    return Response({'data': data})