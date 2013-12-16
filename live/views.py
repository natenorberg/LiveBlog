from django.contrib.auth import logout
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import ListView
from live.models import Update


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/live/")


class UpdateListView(ListView):
    model = Update

    def get_context_data(self, **kwargs):
        context = super(UpdateListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def updates_after(request, id):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(serializers.serialize("json",
                                         Update.objects.filter(pk__gt=id)))
    return response