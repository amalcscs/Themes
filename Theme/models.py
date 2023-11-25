from django.db import models
from django.contrib.auth.models import User,auth

#Admin_data

class Admin_data(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True,default='')
    u_image = models.ImageField(null=True,blank = True,upload_to = 'categorie')
    u_name = models.CharField(max_length=255, null=True,blank=True,default='')
    u_desig = models.CharField(max_length=255,null=True,blank=True,default=0)
    u_username = models.CharField(max_length=255,null=True,blank=True,default='')
    u_password = models.CharField(max_length=255,null=True,blank=True,default='')
   

#  Categorie Table 
class Categorie(models.Model):
    categorie_image = models.ImageField(null=True,blank = True,upload_to = 'categorie')
    categorie_name = models.CharField(max_length=255, null=True,blank=True,default='')
    status = models.CharField(max_length=255,null=True,blank=True,default=0)
    publish_date = models.DateField(max_length=255,null=True,blank=True)
    img_alttag = models.TextField(null=True,blank=True,default='')


class Categorie_details(models.Model):
    categori_details_id = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True,default='')
    details = models.TextField(null=True,blank=True,default='')
    content_position = models.IntegerField(null=True,blank=True,default=0)
    status = models.CharField(max_length=255,null=True,blank=True,default=0)

class Categorie_features(models.Model):
    categori_feature_id = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True,default='')
    feature = models.TextField(null=True,blank=True,default='')
    type_feature = models.CharField(max_length=255, null=True,blank=True,default='')
    status = models.CharField(max_length=255,null=True,blank=True,default=0)

#  Client Table 
class Client(models.Model):
    client_image = models.ImageField(null=True,blank = True,upload_to = 'client')
    client_name = models.CharField(max_length=255, null=True,blank=True,default='')
    client_alttag = models.TextField(null=True,blank=True,default='')

class Templates(models.Model):
    categori_id = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True,default='')
    template_image = models.ImageField(null=True,blank = True,upload_to = 'templates_images')
    template_name = models.CharField(max_length=255, null=True,blank=True,default='')
    template_discription = models.TextField(null=True,blank=True,default='')
    template_status = models.CharField(max_length=255,null=True,blank=True,default='ALTS000')
    template_code = models.CharField(max_length=255,null=True,blank=True,default=0)
    template_publish_date = models.DateField(max_length=255,null=True,blank=True)
    template_img_alttag = models.TextField(null=True,blank=True,default='')
    template_price =models.CharField(max_length=255,null=True,blank=True,default=0)
    template_rating=models.CharField(max_length=255,null=True,blank=True,default=0)
    video_file = models.FileField(upload_to='tempvideo/')


class Testimonials(models.Model):
    testimonial_image = models.ImageField(null=True,blank = True,upload_to = 'testimonial')
    testimonial_name = models.CharField(max_length=255, null=True,blank=True,default='')
    testimonial_position = models.CharField(max_length=255, null=True,blank=True,default='')
    testimonial_discription = models.TextField(null=True,blank=True,default='')
    testimonial_status = models.CharField(max_length=255,null=True,blank=True,default=0)
    testimonial_tag = models.CharField(max_length=255,null=True,blank=True,default=0)


class UploadedFile(models.Model):
    temp_code = models.ForeignKey(Templates, on_delete=models.CASCADE, null=True,default='')
    temp_filename=models.CharField(max_length=255,null=True,blank=True,default='')
    temp_devname=models.CharField(max_length=255,null=True,blank=True,default='')
    zip_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Connect(models.Model):
    messages = models.TextField(null=True,blank=True,default='')
    name =models.CharField(max_length=255,null=True,blank=True,default=0)
    contact_no=models.CharField(max_length=255,null=True,blank=True,default=0)
    email=models.EmailField(null=True,blank=True,default='admin@gmail.com')
    connect_date=models.DateField(auto_now_add=True,blank=False,null=True)
    connect_time=models.TimeField(auto_now_add=True,blank=False,null=True)
    status=models.CharField(max_length=255,null=True,blank=True,default=0)

# Enquiry form ==  Added - Shemeem
class Enquiries(models.Model):
    name = models.CharField(max_length=255)
    enq_date=models.DateField(auto_now_add=True,null=True,auto_now=False)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    company = models.CharField(max_length=255)
    message =  models.TextField()
    status = models.BooleanField(default=0)