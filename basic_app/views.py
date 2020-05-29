from django.shortcuts import render
from django.utils.http import is_safe_url
from basic_app.models import hospital , patient
from django.views.generic import TemplateView , ListView, DetailView , View , CreateView ,UpdateView ,DeleteView,FormView , RedirectView
from . import models
from django.urls import reverse_lazy
from django.db.models import F,aggregates
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from basic_app.forms import SignUpForm,Authenticate
from django.contrib.auth import login,logout,REDIRECT_FIELD_NAME
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.

def basic_app_pivot(request):
    return render(request,'basic_app/basic_app_pivot.html',{})
def  pivot_data(request):
    dataset=patient.objects.all()
    data=serializers.serialize('json',dataset)
    return JsonResponse(data,safe=False)

class loginview(FormView):
    form_class=Authenticate
    template_name = 'basic_app/login.html'
    success_url = reverse_lazy('basic_app:hospital_list')
    redirect_field_name=REDIRECT_FIELD_NAME
    def dispatch(self,request,*args,**kwargs):
        request.session.set_test_cookie()
        return super(loginview,self).dispatch(request,*args,*kwargs)
    def form_valid(self,form):
        login(self.request,form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return super(loginview,self).form_valid(form)
    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to,allowed_hosts=self.request.get_host()):
            redirect_to=self.success_url
        return redirect_to
class logoutview(RedirectView):
    success_url = reverse_lazy('basic_app:patient_list')
    def get(self,request,*args,**kwargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('basic_app:index'))

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('basic_app:index')
    template_name = 'basic_app/signup.html'

class index(TemplateView):
    template_name = 'basic_app/index.html'

class created(CreateView):
    fields = ('dname','specality','hospitald')
    model = models.doctors
    template_name = 'basic_app/created.html'
    success_url = reverse_lazy('basic_app:doctors_list')

class createp(CreateView):
    fields = ('name','hospitalname','sex','date_of_birth','Emailid','height','Weight','contact_Number','doctor_assigned','date_of_admited','date_of_discharge','cause')
    model=models.patient
    template_name = 'basic_app/createp.html'
    success_url = reverse_lazy('basic_app:patient_list')

class createh(CreateView):
    fields = ('hname','location','doctor')
    model = models.hospital
    template_name = 'basic_app/createh.html'
    success_url = reverse_lazy('basic_app:hospital_list')

class updatep(UpdateView):
    fields = ('name','age','contact_Number','Emailid' , 'height','Weight','doctor_assigned','date_of_admited','date_of_discharge','cause')
    model=models.patient
    success_url = reverse_lazy('basic_app:patient_list')

class updateh(UpdateView):
    fields = ('hname','location','doctor')
    model=models.hospital

class updated(UpdateView):
    fields = ('dname','specality','hospitald')
    model=models.doctors
    success_url = reverse_lazy('basic_app:doctors_list')
class deletep(DeleteView):
    model=models.patient
    success_url = reverse_lazy('basic_app:patient_list')

class deleteh(DeleteView):
    model = models.hospital
    success_url = reverse_lazy('basic_app:hospital_list')

class deleted(DeleteView):
    model = models.doctors
    success_url = reverse_lazy('basic_app:doctors_list')

class details(DetailView):
    model =models.patient
    template_name = 'basic_app/details.html'

class doctors_list(ListView):
    model = models.doctors
    success_url = reverse_lazy('basic_app:patient_list')

class listp(ListView):

    context_object_name = 'list'
    model = models.patient
    success_url = reverse_lazy('basic_app:patient_list')
    # def get_context_data(self,**kwargs):
    #     context=super(listp , self).get_context_data(**kwargs)
    #     return context
class listh(ListView):

    context_object_name = 'hlist'
    model = models.hospital
    success_url = reverse_lazy('basic_app:patient_list')

class hospital_details(DetailView):
    context_object_name = 'hospital_details'
    model = models.hospital
    template_name='basic_app/hospital_details.html'
