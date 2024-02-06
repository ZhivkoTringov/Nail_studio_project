from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views
from Nail_studio.services.models import Service


class ServiceCreateView(auth_mixins.PermissionRequiredMixin, views.CreateView):
    """
     A view for creating a new service.

    This view allows authorized users to create new service entries in the system.
    """

    model = Service
    fields = '__all__'
    template_name = 'services/create_service.html'
    permission_required = 'services.manage_services'
    success_url = reverse_lazy('service_list')


class ServiceEditView(auth_mixins.PermissionRequiredMixin, views.UpdateView):
    """
    A view for editing an existing service.

    This view allows authorized users to edit existing service entries in the system.
    """

    model = Service
    fields = '__all__'
    template_name = 'services/edit_service.html'
    permission_required = 'services.manage_services'
    success_url = reverse_lazy('service_list')


class ServiceDeleteView(auth_mixins.PermissionRequiredMixin, views.DeleteView):
    """
     A view for deleting an existing service.

    This view allows authorized users to delete existing service entries in the system.
    """

    model = Service
    fields = '__all__'
    template_name = 'services/delete_service.html'
    permission_required = 'services.manage_services'
    success_url = reverse_lazy('service_list')


class ServiceListView(views.ListView):
    """
     A view for listing all available services.

    This view lists all the services available in the system.
    """

    model = Service
    template_name = 'services/services.html'
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        """
        dd categories to the context.

        This method adds a list of distinct service categories to the context.
        :param kwargs: Arbitrary keyword arguments.
        :return: A dictionary containing the context data.
        """

        context = super().get_context_data(**kwargs)
        context['categories'] = Service.objects.values_list('categories', flat=True).distinct()
        return context

    def get_queryset(self):
        """
         Get the queryset of services.

        This method returns the queryset of services ordered by category in descending order.
        :return: The queryset of services.
        """

        return Service.objects.all().order_by('-categories')
