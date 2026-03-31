from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
# import login_required decorator
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import IsTeacherRoleMixin

# Create your views here.
from .models import Announcement
from .forms import AnnouncementForm

# our test function here.
def is_teacher(user):
    # the user object is passed in here by the decorator
    return user.role == 'teacher'


#@method_decorator(login_required, name='dispatch')
class AnnouncementListView(LoginRequiredMixin, ListView):
    template_name = 'announcements/announcement_list.html'
    model = Announcement
    context_object_name = 'announcements'
    ordering = ['-created_at']

    # Can override to filter
    def get_queryset(self):
        return Announcement.objects.filter(
            created_by=self.request.user
        ).order_by('-created_at')

class CreateAnnouncementView(LoginRequiredMixin, IsTeacherRoleMixin, FormView):
    template_name = 'announcements/create_announcement.html'
    form_class = AnnouncementForm
    success_url = reverse_lazy('announcement_list')

    def form_valid(self, form):
            announcement = form.save(commit=False)
            announcement.created_by = self.request.user
            announcement.save()
            return super().form_valid(form)
    
