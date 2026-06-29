from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Report
from .forms import ReportForm

def home(request):
    reports = Report.objects.all()[:12]
    return render(request, 'home.html', {'reports': reports})

def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш отчёт успешно добавлен! Спасибо!')
            return redirect('home')
    else:
        form = ReportForm()
    return render(request, 'submit.html', {'form': form})

def all_reports(request):
    reports = Report.objects.all()
    return render(request, 'reports.html', {'reports': reports})
