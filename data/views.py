from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Create your views here.
#from .myfun import myfun
from django.views import View
from .forms import VariableForm
from .myfun import myfun
from .myfun import *

class CourseFunc(View):

    def get(self, request):

        form = VariableForm()

        return render(request ,  'data/searchhome.html' , {'form': form})

    def post(self , request):

        form = VariableForm(request.POST)

        if form.is_valid():

            x =form.cleaned_data['X']

            lust = [x]
            myfun(lust , clean )


            context = {'pred': myfun(lust , clean ) }
            return render(request ,  'data/result.html' , context=context )


