from django.shortcuts import render, redirect
from .models import Food, Consume


# Create your views here.
def index(request):
    if request.method =="POST":
        food_consumed = request.POST['food_consumed'] # pobiera co wybral uzytkownik (to jest tylko tekst a nie obiekt)
        consume = Food.objects.get(name=food_consumed) # tworzy obiekt ktory nazywa sie food_consumed czyli to co podal uzytkownik
        user = request.user #tworzy obiekt uzytkownik (czyli kto zalogowany zjadl produkt)
        consume = Consume(user=user, food_consumed=consume)#tworze obiekt dla klasy Consume
        consume.save()
        foods = Food.objects.all()
    else:
        foods = Food.objects.all()
    return render(request, 'index.html', {'foods': foods})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'delete.html')