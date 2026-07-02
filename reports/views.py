from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Report, ReportPhoto
from .forms import ReportForm


def home(request):
    reports = Report.objects.all()[:12]
    return render(request, 'home.html', {'reports': reports})


def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = Report.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
            )
            for photo in form.cleaned_data['photos']:
                ReportPhoto.objects.create(report=report, image=photo)
            messages.success(request, 'Ваш отчёт успешно добавлен! Спасибо!')
            return redirect('home')
    else:
        form = ReportForm()
    return render(request, 'submit.html', {'form': form})


def all_reports(request):
    reports = Report.objects.all()
    return render(request, 'reports.html', {'reports': reports})


def report_detail(request, slug):
    report = get_object_or_404(Report, slug=slug)
    return render(request, 'detail.html', {'report': report})