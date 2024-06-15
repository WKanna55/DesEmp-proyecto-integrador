from django.shortcuts import render
from .firebase import db
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def help(request):
    return render(request, 'help.html')

def fetch_closest_reminders(request):
    ref = db.reference('/closestReminders')
    data = ref.get()

    # Formatear la fecha
    if data:
        reminder_time = data.get('reminderTime')
        if reminder_time:
            # Convertir el timestamp a una fecha legible
            data['reminderTime'] = datetime.fromtimestamp(reminder_time / 1000).strftime('%d/%m/%Y %H:%M:%S')
    
    context = {
        'data': data
    }
    return render(request, 'closest_reminders.html', context)

