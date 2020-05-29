from django.db import models
from django.urls import reverse
from django.db.models import F,aggregates
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class doctors(models.Model):
    dname = models.CharField(max_length = 100 , unique = True)
    specality=models.CharField(max_length = 100 , null = True)
    hospitald=models.ForeignKey('basic_app.hospital' ,  on_delete=models.CASCADE , related_name = 'hdoctors' , null=True)
    def __str__(self):
        return self.dname
class hospital(models.Model):
    hname = models.CharField(max_length = 100 , null = True)
    location = models.CharField(max_length = 100 , null = True)
    doctor = models.ForeignKey(doctors ,  on_delete=models.CASCADE , related_name = 'doctord')

    class Meta:
        app_label='basic_app'
        managed = True

    def __str__(self):
        return self.hname

    # def get_absolute_url(self):
    #     return reverse('basic_app:hospital_details' , kwargs = {'pk': self.pk})
GENDER_CHOICES = (
('M','Male'),
('F','Female')
)
cause_choices = (
('A','accident'),('B', 'surgery'),('C','pneumonia'),('D','Infection'),('E','Cardiac Arrhythmiac')
)

class patient(models.Model):
    name = models.CharField(max_length = 100 , null = True)
    Emailid = models.EmailField()
    sex =  models.CharField(max_length = 1 , choices = GENDER_CHOICES )
    date_of_birth = models.DateField(max_length = 8)
    age = models.IntegerField(null = True)
    height = models.FloatField()
    Weight = models.FloatField()
    contact_Number = PhoneNumberField()
    hospitalname = models.ForeignKey(hospital ,  on_delete=models.CASCADE , related_name = 'patients')
    bmi = models.FloatField(null = True)
    doctor_assigned =  models.ForeignKey(doctors ,  on_delete=models.CASCADE , to_field='dname' , related_name = 'doctorh')
    cause = models.CharField(max_length = 1 , choices = cause_choices )
    date_of_admited= models.DateField(max_length = 8)
    date_of_discharge= models.DateField(max_length = 8)
    daysadmited= models.IntegerField(null = True)

    class Meta:
        app_label='basic_app'
        managed = True

    def age_calculate(self):
        age = int((datetime.now().date() - self.date_of_birth).days/365.25)
        return age
    def days_admited(self):
        daysadmited = int((self.date_of_discharge - self.date_of_admited).days)
        return daysadmited

    def calculate_BMI(self):
        bmi = self.Weight/(self.height*self.height)
        return bmi
    def save(self, *args, **kwargs):
        self.bmi=self.calculate_BMI()
        self.age=self.age_calculate()
        self.daysadmited=self.days_admited()
        super().save(*args , **kwargs)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:details' , kwargs = {'pk': self.pk})
