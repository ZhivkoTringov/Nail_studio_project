from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views
from Nail_studio.services.models import Service


class ServiceCreateView(auth_mixins.PermissionRequiredMixin, views.CreateView):
    model = Service
    fields = '__all__'
    template_name = 'services/create_service.html'
    permission_required = 'services.manage_services'
    success_url = reverse_lazy('service_list')


class ServiceEditView(auth_mixins.PermissionRequiredMixin, views.UpdateView):
    model = Service
    fields = '__all__'
    template_name = 'services/edit_service.html'
    permission_required = 'services.manage_services'
    success_url = reverse_lazy('service_list')


class ServiceDeleteView(auth_mixins.PermissionRequiredMixin, views.DeleteView):
    model = Service
    fields = '__all__'
    template_name = 'services/delete_service.html'
    permission_required = 'services.manage_services'
    success_url = reverse_lazy('service_list')


class ServiceListView(views.ListView):
    model = Service
    template_name = 'services/services.html'
    context_object_name = 'services'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Service.objects.values_list('categories', flat=True).distinct()
        return context

    def get_queryset(self):
        return Service.objects.all().order_by('-categories')