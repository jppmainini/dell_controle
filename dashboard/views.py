from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required()
def vwDashboard(request):
    context = {
        'pgHome': ' active'
    }
    return render(request, 'dashboard/dashboard.html', context)