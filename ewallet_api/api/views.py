from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import UserSerializer, HistorySerializer
from .models import User, History

import datetime
import time

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/user-list/',
        'Create': '/user-create/'
    }
    return Response(api_urls)


@api_view(['GET'])
def ShowAll(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({'status': 200, 'data': serializer.data})


@api_view(['GET'])
def ShowAllHistory(request):
    histories = History.objects.all()
    serializer = HistorySerializer(histories, many=True)
    return Response({'status': 200, 'data': serializer.data})


@api_view(['POST'])
def CreateProduct(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        print('valid')
        serializer.save()

    return Response({'status': 201, 'message': 'Success creating new user!',
                     'data': serializer.data})


@api_view(['PUT'])
def topUpUser(request, pk):
    user = User.objects.get(id=pk)
    # ini balance setelah ditopup
    balance = user.balance + int(request.data.get('topup'))

    serializer = UserSerializer(
        instance=user, data={"balance": balance}, partial=True)

    serializerHistory = HistorySerializer(
        data={'userId': pk, 'description': 'Top up amount {} by user with ID : {}'.format(request.data.get('topup'), pk)})

    if serializer.is_valid() and serializerHistory.is_valid():
        print('valid')
        serializer.save()
        serializerHistory.save()
        return Response({'status': 200, 'message': 'Top-Up Success!', 'data':serializer.data})
    else:
        print('invalid')
        return Response('Top-Up Gagal!')


@api_view(['PUT'])
def transferUser(request, pk):
    userFrom = User.objects.get(id=pk)
    userTo = User.objects.get(id=request.data.get('idTo'))

    if userFrom.balance < int(request.data.get('amount')):
        return Response('Insufficient balance!')

    balanceFrom = userFrom.balance - int(request.data.get('amount'))
    balanceTo = userTo.balance - int(request.data.get('amount'))

    serializerFrom = UserSerializer(instance=userFrom, data={
                                    "balance": balanceFrom}, partial=True)
    serializerTo = UserSerializer(
        instance=userTo, data={"balance": balanceTo}, partial=True)
    serializerHistory = HistorySerializer(data={'userId': pk, 'description': 'Transfer amount of {} from User with ID : {} to User with ID : {}'.format(
        request.data.get('amount'), pk, request.data.get('idTo'))})

    if serializerFrom.is_valid() and serializerTo.is_valid() and serializerHistory.is_valid():
        print('valid')
        serializerFrom.save()
        serializerTo.save()
        serializerHistory.save()
        return Response({'status': 200, 'message': 'Success transferring {} from User with ID : {} to User with ID : {}'.format(
        request.data.get('amount'), pk, request.data.get('idTo'))})
    else:
        print('invalid')
        return Response('Transfer Gagal!')
