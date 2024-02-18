from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import UserSerialzier, PurchaseSerialzier
from .models import Users, Purchases
from rest_framework.response import Response
import datetime
import json
@api_view(['POST'])
def createUser(request):
    user_data = UserSerialzier(data=request.data)
    
    if user_data.is_valid():
        users = Users.objects.filter(username=user_data.validated_data['username'])
        if users.count() == 0:
            user_data.save()
            return Response({"userCreated" : "true"})
    else:
        return Response({"userCreated" : "false"})
    

@api_view(['GET'])
def getPurchases(request):
    user_data = request.data 
    
    try:
        username = user_data['username']
    except KeyError:
        return Response({"dataFetched": "false", "reason":"KeyError"})
    
    purchases = Purchases.objects.filter(user_id=username)
    purchase_obj = []
    
    for purchase in purchases:
        obj = {
        "purhcase_amount": purchase.purchase,
        "date": f"{purchase.purchase_date}",
        }
        
        purchase_obj.append(obj)
        

    return Response(purchase_obj)
    

@api_view(['POST'])
def createPurchase(request):
    purchase_data = request.data
    
    try:
        purchase_amount = purchase_data['purchase']
        username_ = purchase_data['username']
    except KeyError:
        return Response({"purchaseCreated": "false", "reason": "KeyError"})
    
    getUser = None
    users = Users.objects.filter(username=username_)
    if users.count() == 0:
       return Response({"purchaseCreated": "false", "reason": "NoUserToLink"})
    elif users.count() == 1:
        getUser = users[0]
        purchase_obj = Purchases(user=getUser, purchase=purchase_amount, purchase_date=datetime.datetime.now())
        purchase_obj.save()        
        return Response({"purchaseCreated": "true",})
        
            
    else:
        return Response({"purchaseCreated": "false", "reason": "somethingUnexpectedHappened"})
        
        