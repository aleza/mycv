from django.db import models
from datetime import date

class Personal(models.Model):
    name    		= models.CharField(max_length=30)
    surname 		= models.CharField(max_length=30)
    dni   			= models.CharField(max_length=8)    
    sex  	 		= models.CharField(max_length=1)
    birth_date  	= models.DateField(default=date.today)
    address 		= models.CharField(max_length=50)
    telephone		= models.CharField(max_length=15)
    email 			= models.CharField(max_length=50)

    def __str__(self):
    	return self.name.capitalize() + " "+ self.surname.capitalize()



class Resume(models.Model):
    personal 	= models.ForeignKey(Personal, on_delete=models.CASCADE)
    resume_text = models.CharField(max_length=200)
        
    def __str__(self):
        return self.resume_text.capitalize()
    
class Education(models.Model):
    personal_e 	= models.ForeignKey(Personal, on_delete=models.CASCADE)
    titles  	= models.CharField(max_length=200)
    edu_date 	= models.DateTimeField('finish date')
    
    def __str__(self):
        return self.titles.capitalize()

class Courses(models.Model):
    personal_c 	= models.ForeignKey(Personal, on_delete=models.CASCADE)
    courses  	= models.CharField(max_length=200)
    cou_date 	= models.DateTimeField('finish date')
    
    def __str__(self):
        return self.courses.capitalize()    

class Hobbies(models.Model):
    personal_h 	= models.ForeignKey(Personal, on_delete=models.CASCADE)
    hobbies  	= models.CharField(max_length=200)
       
    def __str__(self):
        return self.hobbies.capitalize()            



