# #views.py
# from django.shortcuts import render, redirect
  
# from django.http import HttpResponse
# from home.resources import MemberResource
 
 
# def export(request):
#     member_resource = MemberResource()
#     dataset = member_resource.export()
#     #response = HttpResponse(dataset.csv, content_type='text/csv')
#     #response['Content-Disposition'] = 'attachment; filename="member.csv"'
#     #response = HttpResponse(dataset.json, content_type='application/json')
#     #response['Content-Disposition'] = 'attachment; filename="persons.json"'
#     response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="persons.xls"'
#     return response