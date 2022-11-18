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

        consumed = Consume.objects.all()

        cal_querysetConsumed = []
        for item in consumed:
            cal_querysetConsumed.append(item.food_consumed.calories)
        qsc = cal_querysetConsumed
        total = 0
        for item in qsc:
            total = item + total

        carb_querysetConsumed = []
        for item in consumed:
            carb_querysetConsumed.append(item.food_consumed.carbs)
        qsc = carb_querysetConsumed
        carb_total = 0
        for item in qsc:
            carb_total = item + carb_total

    else:
        foods = Food.objects.all()

        consumed = Consume.objects.all()
        cal_querysetConsumed = []
        for item in consumed:
            cal_querysetConsumed.append(item.food_consumed.calories)
        qsc = cal_querysetConsumed
        total = 0
        for item in qsc:
            total = item + total

        carb_querysetConsumed = []
        for item in consumed:
            carb_querysetConsumed.append(item.food_consumed.carbs)
        qsc = carb_querysetConsumed
        carb_total = 0
        for item in qsc:
            carb_total = item + carb_total

    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'index.html',  {'foods': foods, 'consumed_food': consumed_food, 'total': total, 'carb_total': carb_total})

def count(request,):
    user = request.user
    food_item = Food.objects.all()
    consumed = Consume.objects.all()
    querysetFood=[]
    for food in food_item:
        querysetFood.append(food.calories)
    qs = querysetFood
    querysetConsumed = []
    for item in consumed:
        querysetConsumed.append(item.food_consumed.calories)
    qsc = querysetConsumed
    total = 0
    for item in qsc:
        total = item + total
    context = {
        'user': user,
        'food_item': food_item,
        'consumed': consumed,
        'qs': qs,
        'qsc': qsc,
        'total': total,
    }
    return render(request, 'count.html', context)



def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'delete.html')


