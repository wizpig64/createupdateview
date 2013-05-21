"""CreateUpdateView combines Django's Create and Update generic views.

Built for Django 1.5, but it could work with any other version of django
that uses class based views, assuming library locations haven't moved.

It's very simple code, probably best to just paste it into your project
rather than anybody spending time creating a plugin.

Written by Phillip Marshall, who reserves no rights on this code.

"""


from django.http import Http404
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.views.generic.detail import SingleObjectTemplateResponseMixin


class BaseCreateUpdateView(ModelFormMixin, ProcessFormView):
    """
    Base view for creating an new object instance or updating an existing one.

    Using this base class requires subclassing to provide a response mixin.
    """
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            self.object = None
        return super(BaseCreateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            self.object = None
        return super(BaseCreateUpdateView, self).post(request, *args, **kwargs)


class CreateUpdateView(SingleObjectTemplateResponseMixin, BaseCreateUpdateView):
    """
    View for creating a new object instance or updating an existing one,
    with a response rendered by template.
    """
    template_name_suffix = '_form'

