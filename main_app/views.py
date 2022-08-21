from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Goal:
    def __init__(self, name, description, motivation, measure, start_date, target_date, roadblock):
        self.name = name
        self.description = description
        self.motivation = motivation
        self.measure = measure
        self.start_date = start_date
        self.target_date = target_date
        self.roadblock = roadblock

goals = [
    Goal('Loss Weight', 'Lose ten pounds', 'Look good next summer in bathing suit', 173, '8/20/22', '5/1/23', 'none' ),
    Goal('Eat healthy', 'Reduce sugar to help weight loss goal', 'Look good in a bathing suit next summer', 1200, '8/20/22', '5/1/23', 'none'),
    Goal('Code Better', 'Increase time coding to skill up', 'To get a higher paying job', 25, '8/20/22', '8/20/23', 'none')
]        

def goals_index(request):
    return render(request, 'goals/index.html', {'goals': goals})