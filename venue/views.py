from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import View
from .forms.exampleform import EForm
# Create your views here.


class EView(View):


    def get(self, request):

        f = EForm()

        context = RequestContext(request)
        return render_to_response('venue/etemplate.html', {'form': f}, context)

    def post(self, request):

        f = EForm(request.POST)
        if not f.is_valid():
            context = RequestContext(request)
            return render_to_response('venue/etemplate.html', {'form': f}, context)

        data = f.cleaned_data

        return render_to_response('venue/result.html', {'data': data})
