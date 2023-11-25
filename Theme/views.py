from django.shortcuts import render,redirect
from django.core import serializers
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import date
from .models import*
from django.db.models import Q
from django.http import FileResponse
from django.shortcuts import get_object_or_404
import os
import zipfile
import shutil


def HomePage(request):
    title = "Altos Theme Store"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."
    templates = Templates.objects.all()[:6]
    categorie = Categorie.objects.all()
    testimonials = Testimonials.objects.all()
    clients = Client.objects.all()
    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        'templates':templates,'categorie':categorie,
        'testimonials':testimonials,
        'clients':clients
        }
    return render(request,'index.html',context)


def ProductPage(request):
    title = "Our Products & Services"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        }
    return render(request,'product.html',context) 


def categoryPage(request):
    title = "Best Templates for your site"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."
    categorie=Categorie.objects.all()
    templates=Templates.objects.all()
    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        'categorie':categorie,
        'templates':templates
        }
    return render(request,'category.html',context)


def categoryDetailsPage(request,categori_id):
    title = "Best Templates for your site"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."
    categorie=Categorie.objects.get(id=categori_id)
    templates=Templates.objects.filter(categori_id=categorie)
    ctg_details = Categorie_details.objects.filter(categori_details_id = categorie )
    features = Categorie_features.objects.filter(categori_feature_id=categorie)
    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        'categorie':categorie,
        'templates':templates,
        'ctg_details':ctg_details,
        'features':features
        }
    return render(request,'categoryDetails.html',context)


def get_sub_templates(request, category_id):
    title = "Best Templates for your site"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."
    categorie=Categorie.objects.all()
    templates=Templates.objects.filter(categori_id=category_id)
    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        'categorie':categorie,
        'templates':templates
        }
    return render(request,'category.html',context)


def TemplateView(request,pk):
    title = "Template Preview"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."
    categorie=Categorie.objects.all()
    templates=Templates.objects.all()
    template=Templates.objects.get(id=pk)
    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        'categorie':categorie,'template':template,
        'templates':templates
        }
    return render(request,'view_template.html',context)


def PricingPage(request):
    title = "Plan & Pricing"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        }
    return render(request,'pricing.html',context)


def AboutPage(request):
    title = "Look out who we are?"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."
    testimonials = Testimonials.objects.all()
    clients = Client.objects.all()

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        'testimonials':testimonials,
        'clients':clients
        }
    return render(request,'about.html',context)


def ContactPage(request):
    title = "Altos Theme Store\Contact"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        }
    return render(request,'contact.html',context)


def connect_us(request):
    
    if request.method=='POST':

        contact=Connect()
        contact.name=request.POST.get('name')
        contact.email=request.POST.get('email')
        contact.contact_no=request.POST.get('phno')
        contact.messages=request.POST.get('message')
        contact.save()
        return JsonResponse({'status': 'success'})


def BlogPage(request):
    title = "My Page Title"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        }
    return render(request,'blog.html',context)


def FileUpload_admin(request):
    title = "File Upload"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."
    templates=Templates.objects.all()

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,'templates':templates,
        }
    return render(request,'file_upload.html',context)


def upload_zip(request):

    title = "File Upload"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."
    templates=Templates.objects.all()

    if request.method == 'POST':
        zip_file = request.FILES.get('zip_file')
        sl_opt = request.POST.get('select_option_lable')
        dev_name = request.POST['dev_name']
        
       
        temp = Templates.objects.get(id=sl_opt)

        try:

             

            uploaded_file = UploadedFile.objects.get(temp_code=temp)
            uploaded_file.temp_devname = dev_name
            uploaded_file.save()

            if dev_name:
                msg = 'Your Name Updated but Your File is already uploaded .' 
            else:

                msg = ' Oops ! Your File is already uploaded .' 
             
        except UploadedFile.DoesNotExist:

                if zip_file:

                    uploaded_file = UploadedFile()
                    uploaded_file.temp_code = Templates.objects.get(id=int(sl_opt))
                    uploaded_file.temp_devname = dev_name
                    uploaded_file.save()
                    uploaded_file.zip_file = zip_file
                    uploaded_file.temp_filename = f'{temp.template_name}_{temp.template_code}'
                    uploaded_file.save()


            
                    msg = 'Thank you for your time, Your File is uploaded successfull.' 

        context = {
                'title': title,
                'meta_tags': meta_tags,
                'meta_description': meta_description,'templates':templates,
                'msg':msg
                }
        
        return render(request,'file_upload.html',context)
    return redirect('FileUpload')  

#================= User Section End ===============================



#================= Admin section ===================================


def adminlogin(request):
    return render(request,'admin/login.html')

def loginCheck(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
    
        
        if user is not None:
            request.session["uid"]=user.id
            auth.login(request,user) 
            success='Your are login successful.'   
            categori_count=Categorie.objects.count()
            template_count = Templates.objects.count()
            info=None
            admin=None
            if request.session.has_key('uid'):
                    uid = request.session['uid']
                    user=User.objects.get(id=uid)

                    try:
                        admin=Admin_data.objects.get(u_id=user)
                    except Admin_data.DoesNotExist:
                        admin_create=Admin_data()
                        admin_create.u_id=User.objects.get(id=uid)
                        admin_create.u_name='Admin'
                        admin_create.u_desig='Admin'
                        admin_create.save()
                        info='Please update your profile.'

            else:
                    return redirect('adminlogin')
            
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()

            page_name='Dashboard'
            return render(request,'admin/dashboard.html',{'page_name':page_name,
                         'categori_count':categori_count,'template_count':template_count, 'admin':admin,
                         'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count,'success':success,'info':info})
        else:
            msg='Invalid Username or Password ! Try Again.'
            return render(request, 'admin/login.html',{'msg':msg})


def Dashboard(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
        else:
            return redirect('adminlogin')
        categori_count=Categorie.objects.count()
        template_count = Templates.objects.count()
        user_messages=Connect.objects.filter(connect_date=date.today())[:3]
        user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
        user_tmessages_count=Connect.objects.count()

        page_name='Dashboard'
        return render(request,'admin/dashboard.html',{'page_name':page_name,
                        'categori_count':categori_count,'template_count':template_count,'admin':admin,
                        'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    
    
def categorie_load(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()

        else:
            return redirect('adminlogin')
        page_name='Categorie'
        return render(request,'admin/categorie_add.html',{'page_name':page_name,'admin':admin,
                        'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    

def categorie_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()

        else:
            return redirect('adminlogin')
       
        if request.method=='POST':
        
            categorie=Categorie()
            categorie.categorie_name=request.POST['categori_name']
            categorie.status=request.POST.get('visibility_opt')
            categorie.publish_date=request.POST['publish_date']
            categorie.img_alttag=request.POST['tag_name']
            categorie.categorie_image=request.FILES.get('categori_img')
            categorie.save()
            done=True
            return redirect(category_details_add,categorie.id,done)

    else:
        return redirect('adminlogin')
    

def category_details_add(request,pk,status):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()

        else:
            return redirect('adminlogin')
        
        categorie=Categorie.objects.get(id=pk)
    
        if status == True:
            success= 'Category saved successfully. Now you can add details to category'
        else:
            success=False
        ctg_details = Categorie_details.objects.filter(categori_details_id = categorie )
        features = Categorie_features.objects.filter(categori_feature_id=categorie)
        page_name='Categorie Details'
        return render(request,'admin/categorie_details.html',{'page_name':page_name,'success':success,'admin':admin,
                                                                'user_messages':user_messages,'features':features,
                            'user_messages_count':user_messages_count,
                            'user_tmessages_count':user_tmessages_count,'categorie':categorie,'ctg_details':ctg_details})
    

def category_details_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()

        else:
            return redirect('adminlogin')
        
       
        if request.method=='POST':
            categorie=Categorie.objects.get(id=int(request.POST['categori_id']))
            details=Categorie_details()
            details.categori_details_id=categorie
            details.details=request.POST['categori_descrip']
            details.content_position=request.POST['visibility_opt']
            details.save()
    
            success= 'Category Details successfully.'
            ctg_details = Categorie_details.objects.filter(categori_details_id = categorie )
            features = Categorie_features.objects.filter(categori_feature_id=categorie)
            page_name='Categorie Details'
            return render(request,'admin/categorie_details.html',{'page_name':page_name,'success':success,'admin':admin,
                                                                    'user_messages':user_messages,'features':features,
                                'user_messages_count':user_messages_count,
                                'user_tmessages_count':user_tmessages_count,'categorie':categorie,'ctg_details':ctg_details})
        else:
            return redirect('Dashboard')
        

def category_details_edit(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
 
            ctg_details = Categorie_details.objects.get(id=pk )

            page_name='Categorie Details'
            return render(request,'admin/categorie_details_edit.html',{'page_name':page_name,'admin':admin,
                                                                    'user_messages':user_messages,
                                'user_messages_count':user_messages_count,
                                'user_tmessages_count':user_tmessages_count,'ctg_details':ctg_details})
        


def category_details_edit_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()

        else:
            return redirect('adminlogin')
        
       
        if request.method=='POST':
            
            details=Categorie_details.objects.get(id=int(request.POST['up_id']))
            categorie=Categorie.objects.get(id=details.categori_details_id.id)
            details.categori_details_id=categorie
            details.details=request.POST['categori_descrip']
            details.content_position=request.POST['visibility_opt']
            details.save()
    
            success= 'Category Details edited successfully.'
            ctg_details = Categorie_details.objects.filter(categori_details_id = categorie )
            features = Categorie_features.objects.filter(categori_feature_id=categorie)
            page_name='Categorie Details'
            return render(request,'admin/categorie_details.html',{'page_name':page_name,'success':success,'admin':admin,
                                                                    'user_messages':user_messages,'features':features,
                                'user_messages_count':user_messages_count,
                                'user_tmessages_count':user_tmessages_count,'categorie':categorie,'ctg_details':ctg_details})
        else:
            return redirect('Dashboard')


    
def category_details_remove(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()

        else:
            return redirect('adminlogin')
        
        catg=Categorie_details.objects.get(id=pk)
        categorie=Categorie.objects.get(id=catg.categori_details_id.id)
        catg.delete()
        success= 'Category details removed.'
 
        ctg_details = Categorie_details.objects.filter(categori_details_id = categorie )
        features = Categorie_features.objects.filter(categori_feature_id=categorie)
        page_name='Categorie Details'
        return render(request,'admin/categorie_details.html',{'page_name':page_name,'success':success,'admin':admin,
                                                                'user_messages':user_messages,'features':features,
                            'user_messages_count':user_messages_count,'success':success,
                            'user_tmessages_count':user_tmessages_count,'categorie':categorie,'ctg_details':ctg_details})


        
def category_features(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()

        else:
            return redirect('adminlogin')
        categorie=Categorie.objects.get(id=pk)
        
        features = Categorie_features.objects.filter(categori_feature_id=categorie)
        page_name='Categorie Features and Customization Options'
        return render(request,'admin/categorie_feature.html',{'page_name':page_name,'admin':admin,'features':features,
                                                                    'user_messages':user_messages,
                                'user_messages_count':user_messages_count,
                                'user_tmessages_count':user_tmessages_count,'categorie':categorie})
    


def feature_remove(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()

        else:
            return redirect('adminlogin')
        
        f=Categorie_features.objects.get(id=pk)
        categorie=Categorie.objects.get(id=f.categori_feature_id.id)
        f.delete()
        success= 'Category feature removed.'
 
        ctg_details = Categorie_details.objects.filter(categori_details_id = categorie )
        features = Categorie_features.objects.filter(categori_feature_id=categorie)
        page_name='Categorie Details'
        return render(request,'admin/categorie_details.html',{'page_name':page_name,'success':success,'admin':admin,
                                                                'user_messages':user_messages,'features':features,
                            'user_messages_count':user_messages_count,'success':success,
                            'user_tmessages_count':user_tmessages_count,'categorie':categorie,'ctg_details':ctg_details})
  
    
def category_feature_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()

        else:
            return redirect('adminlogin')
        if request.method=='POST':
            categorie=Categorie.objects.get(id=int(request.POST['categori_id']))
            feature=Categorie_features()
            feature.categori_feature_id=categorie
            feature.feature=request.POST['feature_descrip']
            feature.type_feature=request.POST['type_opt']
            feature.save()
            success= 'Feature  successfully added .'
            features = Categorie_features.objects.filter(categori_feature_id=categorie)
         
            page_name='Categorie Features and Customization Options'
            return render(request,'admin/categorie_feature.html',{'page_name':page_name,'admin':admin,'success':success,
                                                                    'user_messages':user_messages,
                                'user_messages_count':user_messages_count,'features':features,
                                'user_tmessages_count':user_tmessages_count,'categorie':categorie})


def feature_edit(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
 
            features = Categorie_features.objects.get(id=pk)

            page_name='Categorie Details feature'
            return render(request,'admin/categorie_feature_edit.html',{'page_name':page_name,'admin':admin,
                                                                    'user_messages':user_messages,
                                'user_messages_count':user_messages_count,
                                'user_tmessages_count':user_tmessages_count,'features':features})


def category_feature_edit_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()

        else:
            return redirect('adminlogin')
        
       
        if request.method=='POST':
            
            features=Categorie_features.objects.get(id=int(request.POST['up_id']))
            categorie=Categorie.objects.get(id=features.categori_feature_id.id)
            features.categori_feature_id=categorie
            features.feature=request.POST['feature_descrip']
            features.type_feature=request.POST['type_opt']
            features.save()
    
            success= 'Feature edited successfully.'
            ctg_details = Categorie_details.objects.filter(categori_details_id = categorie )
            features = Categorie_features.objects.filter(categori_feature_id=categorie)
            page_name='Categorie Details'
            return render(request,'admin/categorie_details.html',{'page_name':page_name,'success':success,'admin':admin,
                                                                    'user_messages':user_messages,'features':features,
                                'user_messages_count':user_messages_count,
                                'user_tmessages_count':user_tmessages_count,'categorie':categorie,'ctg_details':ctg_details})
        else:
            return redirect('Dashboard')




def categorie_edit(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.all()
        page_name='Categorie'
        return render(request,'admin/categorie_edit.html',{'page_name':page_name,'categories':categories,'admin':admin,
                                                           'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')

def fetch_categori(request):
    value = request.GET.get('value')
    categorie=Categorie.objects.get(id=value)
    image_url = Categorie.objects.values_list('categorie_image', flat=True).get(id=value)
    
    response = {
        'categorie_name': categorie.categorie_name,
        'categorie_tag': categorie.img_alttag,
        'image': image_url,
        'radioValue': int(categorie.status),
        'categorie_date':categorie.publish_date,
        
        
    }
    return JsonResponse(response)


def categeori_edit_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')

        categories=Categorie.objects.all()
        page_name='Categorie'

        if request.method=='POST':
            categorie=Categorie.objects.get(id=request.POST['slect_categori'])
            categorie.categorie_name=request.POST['categori_name']
            categorie.status=request.POST.get('visibility_opt')
            categorie.publish_date=request.POST['publish_date']
            categorie.img_alttag=request.POST['tag_name']
            if request.FILES.get('categori_img'):
                categorie.categorie_image=request.FILES.get('categori_img')
            else:
                categorie.categorie_image = categorie.categorie_image

            categorie.save()
            success= 'Category updated successfully.'
            return render(request,'admin/categorie_edit.html',{'page_name':page_name,'categories':categories,
                                                               'success':success,'admin':admin,
                                                               'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})

        else:
    
            return render(request,'admin/categorie_edit.html',{'page_name':page_name,'categories':categories,'admin':admin})
    else:
        return redirect('adminlogin')


def categorie_list(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.all()
        page_name='Categorie'
        return render(request,'admin/categorie_list.html',{'page_name':page_name,'categories':categories,'admin':admin,
                                                           'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    

def categorie_remove(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.get(id=pk)
        categories.delete()
        danger="Category deleted successfully."
        categories=Categorie.objects.all()
        page_name='Categorie'
        return render(request,'admin/categorie_list.html',{'page_name':page_name,'categories':categories,'danger':danger,
                                                           'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count,'admin':admin})
    else:
        return redirect('adminlogin')



def template_load(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.all()
        page_name='Template'
        return render(request,'admin/template_load.html',{'page_name':page_name,'categories':categories,'admin':admin,
                                                          'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')


def template_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        
        if request.method=='POST':
        
            template=Templates()
            template.categori_id=Categorie.objects.get(id=int(request.POST['slect_categori']))
            template.template_name=request.POST['temp_name']
            template.template_discription=request.POST['temp_discription']
            template.template_status=request.POST.get('visibility_opt')
            template.template_publish_date=request.POST['publish_date']
            template.template_img_alttag=request.POST['tag_name']
            template.template_rating=request.POST.get('rating_opt')
            template.template_price=request.POST['temp_price']
            template.template_image=request.FILES.get('temp_img')
            template.video_file = request.FILES['temp_video']
            template.save()
            template.template_code = 'ALTS00' + str(template.id)
            template.save()
            success= 'Template saved successfully.'
            page_name='Template'
            categories=Categorie.objects.all()
            return render(request,'admin/template_load.html',{'page_name':page_name,'success':success,'categories':categories,'admin':admin,
                                                              'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')


def template_editload(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.all()
        templates=Templates.objects.all()
        page_name='Template'
        return render(request,'admin/template_editlist.html',{'page_name':page_name,
                        'categories':categories,'templates':templates,'admin':admin,
                        'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    


def template_code_generate(request,temp_id_code):
    template=Templates.objects.get(id=temp_id_code)
    template.template_code = 'ALTS00' + str(template.id)
    template.save()
    
    return redirect('template_editload')

def template_remove(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.all()
        temp_remove=Templates.objects.get(id=pk)
        temp_remove.delete()
        danger="Template deleted successfully."
        templates=Templates.objects.all()
        page_name='Template'
        return render(request,'admin/template_editlist.html',{'page_name':page_name,'categories':categories,
                                                              'templates':templates,'danger':danger,'admin':admin,
                                                              'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    

def fetch_templates_editlist(request):
    
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        
        categories=Categorie.objects.all()
        try:
            cate_check=Categorie.objects.get(id=int(request.POST['slect_categori']))
            templates=fetch_templates(cate_check.id)

        except Categorie.DoesNotExist:
            templates=None

        page_name='Template'
        return render(request,'admin/template_editlist.html',{'page_name':page_name,
                    'categories':categories,'templates':templates,'admin':admin,
                    'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')


# reuseble for featching template

def fetch_templates(pk):    
    cate_check=Categorie.objects.get(id=pk)
    templates=Templates.objects.filter(categori_id=cate_check)
    return templates


def template_list(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.all()
        templates=Templates.objects.all()
        page_name='Template'
        return render(request,'admin/template_list.html',{'page_name':page_name,'categories':categories,
                            'templates':templates,'admin':admin,'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    


def template_file(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.all()
        uploadfile = UploadedFile.objects.all() 
       
        page_name='Template File'
        return render(request,'admin/template_files.html',{'page_name':page_name,'categories':categories,
                        'uploadfile':uploadfile,'admin':admin,'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    


def search_files(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        
        categories=Categorie.objects.all()

        if request.method =='POST':
            search_value = request.POST['file_search']
            uploadfile = UploadedFile.objects.filter(Q(temp_filename__icontains=search_value) | Q(temp_devname__icontains=search_value) )
        else:
             uploadfile = UploadedFile.objects.all()

       
       
        page_name='Template File'
        return render(request,'admin/template_files.html',{'page_name':page_name,'categories':categories,
                        'uploadfile':uploadfile,'admin':admin,'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    
    

    

def fetch_templates_list(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        
        categories=Categorie.objects.all()
        try:
            cate_check=Categorie.objects.get(id=int(request.POST['slect_categori']))
            templates=fetch_templates(cate_check.id)

        except Categorie.DoesNotExist:
            templates=None

        page_name='Template'
        return render(request,'admin/template_list.html',{'page_name':page_name,'categories':categories,
                                'templates':templates,'admin':admin,'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    



def fetch_templates_file(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        
        categories=Categorie.objects.all()
        try:
            cate_check=Categorie.objects.get(id=int(request.POST['slect_categori']))
            temp =Templates.objects.filter(categori_id=cate_check)
            uploadfile=UploadedFile.objects.filter(temp_code__in=temp)
            
           
            page_name='Template File'
            return render(request,'admin/template_files.html',{'page_name':page_name,'categories':categories,
                            'uploadfile':uploadfile,'admin':admin,'user_messages':user_messages,
                            'user_messages_count':user_messages_count,
                            'user_tmessages_count':user_tmessages_count})

        except Categorie.DoesNotExist:
            uploadfile=None

        page_name='Template File'
        return render(request,'admin/template_files.html',{'page_name':page_name,'categories':categories,
                                'uploadfile':uploadfile,'admin':admin,'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
        
def template_view(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
       
        template=Templates.objects.get(id=pk)
        categories=Categorie.objects.exclude(id=template.categori_id.id)
        page_name='Template View'
        return render(request,'admin/template_view.html',{'page_name':page_name,'template':template,'admin':admin,
                                                          'user_messages':user_messages,'categories':categories,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    

def template_editsave (request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        if request.method=='POST':
        
            template=Templates.objects.get(id=int(request.POST['temp_id']))
            template.categori_id=Categorie.objects.get(id=int(request.POST['slect_categori']))
            template.template_name=request.POST['temp_name']
            template.template_discription=request.POST['temp_discription']
            template.template_status=request.POST.get('visibility_opt')
            template.template_publish_date=request.POST['publish_date']
            template.template_img_alttag=request.POST['tag_name']
            template.template_rating=request.POST.get('rating_opt')
            template.template_price=request.POST['temp_price']

            if request.FILES.get('temp_img'):
                template.template_image=request.FILES.get('temp_img')
            else:
                template.template_image=template.template_image

            if request.FILES.get('temp_video'):

                template.video_file = request.FILES.get('temp_video')
            else:
                template.video_file = template.video_file
            template.save()
            success= 'Template updated successfully.'
            page_name='Template'
            categories=Categorie.objects.all()
            templates=Templates.objects.all()
            return render(request,'admin/template_editlist.html',{'page_name':page_name,'success':success,'categories':categories,'admin':admin,
                        'user_messages':user_messages,'templates':templates,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')



# =============== Clients section ================

def client_load(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        
        page_name='Client'
        return render(request,'admin/client_Form.html',{'page_name':page_name,'admin':admin,
                                                        'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    

def client_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        
        if request.method=='POST':

            client_save=Client()
            client_save.client_image=request.FILES.get('client_img')
            client_save.client_name=request.POST['client_name']
            client_save.client_alttag=request.POST['client_tag_name']
            client_save.save()
            success="Client saved successfully."
        
        page_name='Client'
        return render(request,'admin/client_Form.html',{'page_name':page_name,'admin':admin,'success':success,
                                                        'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')


def client_list(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        
        clients=Client.objects.all()
    
        page_name='Clients '
        return render(request,'admin/client_list.html',{'page_name':page_name,'admin':admin,'clients':clients,
                                                        'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    
    
def client_edit(request,cedit_id):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        
        client=Client.objects.get(id=cedit_id)
        page_name='Clients '
        return render(request,'admin/client_editForm.html',{'page_name':page_name,'admin':admin,
                                                        'client':client,
                                                        'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    

def client_editsave(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        
        if request.method=='POST':

            client=Client.objects.get(id=int(request.POST['client_id']))
            if request.FILES.get('client_img'):

                client.client_image=request.FILES.get('client_img')
            else:
                client.client_image=client.client_image
            client.client_name=request.POST['client_name']
            client.client_alttag=request.POST['client_tag_name']
            client.save()
            clients=Client.objects.all()
            success="Client data updated successfully."
        
        
        page_name='Clients '
        return render(request,'admin/client_list.html',{'page_name':page_name,'admin':admin,
                                                        'client':client,
                                                        'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count,'success':success,'clients':clients})
    else:
        return redirect('adminlogin')
    

def client_remove(request,client_id):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        
        client=Client.objects.get(id=client_id)
        client.delete()
        clients=Client.objects.all()
        danger='Client data deleted successfully.'
        page_name='Clients '
        return render(request,'admin/client_list.html',{'page_name':page_name,'admin':admin,
                                                        'clients':clients,'danger':danger,
                                                        'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')

    

#============ Message Section =============

def view_allmessage(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
            user_all_message=Connect.objects.all().order_by('-id')
        else:
            return redirect('adminlogin')
        
        page_name='Messages'
        return render(request,'admin/messageForm.html',{'page_name':page_name,'admin':admin,
                            'user_all_message':user_all_message,'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')


    
def message_remove(request,remove_id):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user) 

            message_remove=Connect.objects.get(id=remove_id)
            message_remove.delete()
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
            user_all_message=Connect.objects.all().order_by('-id')
        else:
            return redirect('adminlogin')
        
        page_name='Messages'
        return render(request,'admin/messageForm.html',{'page_name':page_name,'admin':admin,
                            'user_all_message':user_all_message,'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')



# Testimonial 

def testimonial_load(request):
  
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
       
        user=User.objects.get(id=uid)
        admin=Admin_data.objects.get(u_id=user)
        user_messages=Connect.objects.filter(connect_date=date.today())[:3]
        user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
        user_tmessages_count=Connect.objects.count()

        page_name='Testimonials '
        return render(request,'admin/testimonialForm.html',{'page_name':page_name,'admin':admin,
                        'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')
    

def testimonial_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
       
        user=User.objects.get(id=uid)
        admin=Admin_data.objects.get(u_id=user)
        user_messages=Connect.objects.filter(connect_date=date.today())[:3]
        user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
        user_tmessages_count=Connect.objects.count()
        
        if request.method=='POST':

            testimonials_save=Testimonials()
            testimonials_save.testimonial_image=request.FILES.get('testi_img')
            testimonials_save.testimonial_name=request.POST['testi_name']
            testimonials_save.testimonial_discription=request.POST['testi_discription']
            testimonials_save.testimonial_status=1
            testimonials_save.testimonial_tag=request.POST['testi_tag']
            testimonials_save.save()
            success="Testimonial saved successfully"
        

        page_name='Testimonials '
        return render(request,'admin/testimonialForm.html',{'page_name':page_name,'admin':admin,'success':success,
                        'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')


def testimonial_list(request):
  
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
       
        user=User.objects.get(id=uid)
        admin=Admin_data.objects.get(u_id=user)
        user_messages=Connect.objects.filter(connect_date=date.today())[:3]
        user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
        user_tmessages_count=Connect.objects.count()

        testimonials=Testimonials.objects.all()
        page_name='Testimonials '
        return render(request,'admin/testimonialList.html',{'page_name':page_name,'admin':admin,
                            'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count,'testimonials':testimonials})
    else:
        return redirect('adminlogin')


def testimonial_remove(request,testi_remove):
  
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
       
        user=User.objects.get(id=uid)
        admin=Admin_data.objects.get(u_id=user)
        user_messages=Connect.objects.filter(connect_date=date.today())[:3]
        user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
        user_tmessages_count=Connect.objects.count()

        testimonial=Testimonials.objects.get(id=testi_remove)
        testimonial.delete()
        danger="Testimonial data deleted successfully."

        testimonials=Testimonials.objects.all()
        page_name='Testimonials '
        return render(request,'admin/testimonialList.html',{'page_name':page_name,'admin':admin,'danger':danger,
                            'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count,'testimonials':testimonials})
    else:
        return redirect('adminlogin')
    

def testimonial_edit(request,testi_edit):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
       
        user=User.objects.get(id=uid)
        admin=Admin_data.objects.get(u_id=user)
        user_messages=Connect.objects.filter(connect_date=date.today())[:3]
        user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
        user_tmessages_count=Connect.objects.count()

        testimonial=Testimonials.objects.get(id=testi_edit)

        page_name='Testimonials '
        return render(request,'admin/testimonial_editForm.html',{'page_name':page_name,'admin':admin,
                        'user_messages':user_messages,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count,'testimonial':testimonial})
    else:
        return redirect('adminlogin')
    

def testimonial_edit_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
       
        user=User.objects.get(id=uid)
        admin=Admin_data.objects.get(u_id=user)
        user_messages=Connect.objects.filter(connect_date=date.today())[:3]
        user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
        user_tmessages_count=Connect.objects.count()
        
        if request.method=='POST':

            testimonials_save=Testimonials.objects.get(id=int(request.POST['testi_id']))

            if request.FILES.get('testi_img'):
                testimonials_save.testimonial_image=request.FILES.get('testi_img')
            else:
                testimonials_save.testimonial_image= testimonials_save.testimonial_image
            testimonials_save.testimonial_name=request.POST['testi_name']
            testimonials_save.testimonial_discription=request.POST['testi_discription']
            testimonials_save.testimonial_status=1
            testimonials_save.testimonial_tag=request.POST['testi_tag']
            testimonials_save.save()
            success="Testimonial data updated successfully."

        
        testimonials=Testimonials.objects.all()
        page_name='Testimonials '
        return render(request,'admin/testimonialList.html',{'page_name':page_name,'admin':admin,'success':success,
                        'user_messages':user_messages,'testimonials':testimonials,
                         'user_messages_count':user_messages_count,
                         'user_tmessages_count':user_tmessages_count})
    else:
        return redirect('adminlogin')


# Admin Account Settings 

def profile(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        user_id=User.objects.get(id=uid)
        try:
            user_check= Admin_data.objects.get(u_id=user_id)

        except Admin_data.DoesNotExist:
            user_check=User.objects.get(id=uid)
        page_name='Account Setting'
        return render(request,'admin/profile.html',{'page_name':page_name,'user_check':user_check,
                                                    'admin':admin,
                        'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
        
    else:
        return redirect('adminlogin')


def useredit_save(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
         
        if request.method=='POST':

            user_id=User.objects.get(id=uid)
            try:
                user_check= Admin_data.objects.get(u_id=user_id)
                user_check.u_name=request.POST['fullName']
                user_check.u_desig=request.POST['desig']

                if request.FILES.get('u_img'):
                    user_check.u_image=request.FILES.get('u_img')
                else:
                    user_check.u_image=user_check.u_image
                
                user_check.save()
                success='Successfully updated.'
                admin=Admin_data.objects.get(u_id=user)

            except Admin_data.DoesNotExist:
               user_check=Admin_data()
               user_check.u_id=user_id
               user_check.u_name=request.POST['fullName']
               user_check.u_desig=request.POST['desig']
               user_check.u_image=request.FILES.get('u_img')
               user_check.save()
               
        page_name='Account Setting'
        return render(request,'admin/profile.html',{'page_name':page_name,'user_check':user_check,
                                                    'admin':admin,'success':success,
                        'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
        
    else:
        return redirect('adminlogin')


def user_password_edit(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
        
        user_id=User.objects.get(id=uid)

        try:
            user_check= Admin_data.objects.get(u_id=user_id)
                
        except Admin_data.DoesNotExist:
                user_check=User.objects.get(id=uid)
        page_name='Account Setting'
        return render(request,'admin/password.html',{'page_name':page_name,'user_check':user_check,
                                                     'admin':admin,
                        'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
        
    else:
        return redirect('adminlogin')


def userpassword_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
            user=User.objects.get(id=uid)
            admin=Admin_data.objects.get(u_id=user)
            user_messages=Connect.objects.filter(connect_date=date.today())[:3]
            user_messages_count=Connect.objects.filter(connect_date=date.today()).count()
            user_tmessages_count=Connect.objects.count()
        else:
            return redirect('adminlogin')
         
        if request.method =='POST':

            user_id=User.objects.get(id=uid)
            try:
                user_check= Admin_data.objects.get(u_id=user_id)
                user_id.set_password(request.POST.get('newpassword'))
                user_id.save()
                user_check.u_password=request.POST.get('newpassword')
                user_check.save()

                success = "Password updated successfully!"
                
            
            except Admin_data.DoesNotExist:
                user_check=User.objects.get(id=uid)
           
            
        page_name='Account Setting'
        return render(request,'admin/password.html',{'page_name':page_name,'user_check':user_check,
                                                     'admin':admin,'success':success,
                        'user_messages':user_messages,
                        'user_messages_count':user_messages_count,
                        'user_tmessages_count':user_tmessages_count})
        
    else:
        return redirect('adminlogin')


def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    
    return redirect('HomePage')
    
    
def serviceEnquiry(request):
    return render(request, 'enquiry_form.html')

def saveEnquiry(request):
    if request.method == 'POST':
        try:
            uName=request.POST['Name']
            uEmail=request.POST['Email']
            uPhone=request.POST['Phone']
            uCompany = request.POST['Company']
            uMessage=request.POST['message']

            enq=Enquiries(name=uName,email=uEmail,phone=uPhone,message=uMessage,company = uCompany)
            enq.save()
            messages.success(request,"We will reach out to you soon..")
            return redirect('ProductPage')
        except Exception as e:
            print(e)
            messages.error(request, 'Something went wrong, Please try again.')
            return redirect('ProductPage')
    else:
        return redirect('ProductPage')