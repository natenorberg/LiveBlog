from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from live.models import Update


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = ('text',)

@login_required
def new_update(request):
    if request.POST:
        form = UpdateForm(request.POST)
        if form.is_valid():
            new_update = form.save()
            return HttpResponseRedirect("/live/")
        else:
            form = UpdateForm(request.POST)
    else:
        form = UpdateForm()
    return render_to_response("add.html", {"form": form}, context_instance=RequestContext(request))