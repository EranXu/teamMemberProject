'''
author: Yiran Xu
'''
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.forms import MemberForm
from .serializers import TeamsSerializer
from .models import TeamMember
from api import serializers

def getTeams(request):
    # read all elements in database
    teams =TeamMember.objects.all()
    # count the number of elements in database
    # add one because of the admin
    cnt= TeamMember.objects.all().count()+1
    serializer = TeamsSerializer(teams, many = True)
    return render(request, 'index.html', {'teams':teams, 'cnt':cnt})

def getTeam(request, pk):
    # get one element in db according to the pk
    team = TeamMember.objects.get(id = pk)
    return render(request, 'contact-profile.html', {'team': team})

def createMember(request):
    form = MemberForm()
    # catch POST response
    if request.method == 'POST':
        if 'canDelete' in request.POST:
            bol1 = True
        else:
            bol1 = False
        # add the content of model accoring to the POST name
        
        team = TeamMember(
            fullName = request.POST['fullName'],
            phone = request.POST['phone'],
            email = request.POST['email'],
            canDelete = bol1
        )
        # save in databsae
        form = MemberForm(request.POST, instance=team)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
        # team.save()
        # back to the home page
    return render(request,'add.html', {'form': form})
    

def editMember(request, pk):
    form = MemberForm()
    # get one element in db according to the pk
    team = TeamMember.objects.get(id = pk)
    # catch POST response
    if request.method == 'POST':
        if 'canDelete' in request.POST:
            bol2 = True
        else:
            bol2 = False
        # if user press the update(save) button
        # we'll catch the response of POST with name 'update'
        if 'update' in request.POST:
            team.fullName = request.POST['fullName']
            team.phone = request.POST['phone']
            team.email = request.POST['email']
            team.canDelete = bol2
            # save and back
            form = MemberForm(request.POST, instance=team)
            if form.is_valid():
                form.save()
                return redirect('/')
        # if user press the delete button
        # we'll catch the response of POST with name 'delete'
        if 'delete' in request.POST:
            # check if this member can be deleted by user
            if team.canDelete:
                team.delete()
                return redirect('/')
            # if not, no delete operation
            else:
                return redirect('/')
    return render(request, 'edit.html', {'form': form})

