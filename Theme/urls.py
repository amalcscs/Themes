from django.urls import path,re_path 
from.import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [

    path('',views.HomePage,name='HomePage'),
    path('Products',views.ProductPage,name='ProductPage'),
    path('Category',views.categoryPage,name='categoryPage'),
    path('Category-Details/<int:categori_id>/',views.categoryDetailsPage,name='categoryDetailsPage'),
    path('Pricing',views.PricingPage,name='PricingPage'),
    path('About',views.AboutPage,name='AboutPage'),
    path('Contact',views.ContactPage,name='ContactPage'),
    path('Blog',views.BlogPage,name='BlogPage'),
    path('Templates/<int:pk>',views.TemplateView,name='TemplateView'),
    path('Templates/<int:category_id>/', views.get_sub_templates, name='get_sub_templates'),
    path('Contact_Us',views.connect_us,name='connect_us'),
    path('File-Upload-Admin',views.FileUpload_admin,name='FileUpload_admin'),
    path('Upload-zip',views.upload_zip,name='upload_zip'),


    # ================ Admin section ===========

    path('login',views.adminlogin,name='adminlogin'),
    path('logout',views.logout,name='logout'),

    path('LgoinCheck',views.loginCheck,name='loginCheck'),
    path('Dashboard',views.Dashboard,name='Dashboard'),
    path('Categorie_Form',views.categorie_load,name='categorie_load'),
    path('Categorie_Save',views.categorie_save,name='categorie_save'),
    path('categorie_Edit',views.categorie_edit,name='categorie_edit'),
    path('categeori_Edit_Save',views.categeori_edit_save,name='categeori_edit_save'),
    path('Fetch_categories',views.fetch_categori,name='fetch_categori'),
    path('Fetch_Templates_editlist',views.fetch_templates_editlist,name='fetch_templates_editlist'),
    path('Fetch_Templates/<int:pk>',views.fetch_templates,name='fetch_templates'),
    path('categorie_List',views.categorie_list,name='categorie_list'),
    path('Categorie_Remove/<int:pk>',views.categorie_remove,name='categorie_remove'),

    path('category-details-add/<int:pk><int:status>',views.category_details_add,name='category_details_add'),
    path('category-features-add/<int:pk>',views.category_features,name='category_features'),
    path('category-details-save',views.category_details_save,name='category_details_save'),
    path('category-details-Edit/<int:pk>',views.category_details_edit,name='category_details_edit'),
    path('category-details-Edit-save',views.category_details_edit_save,name='category_details_edit_save'),
    path('category-details-Remove/<int:pk>',views.category_details_remove,name='category_details_remove'),
    path('category-feature-save',views.category_feature_save,name='category_feature_save'),
    path('category-feature-Edit/<int:pk>',views.feature_edit,name='feature_edit'),
    path(' category-feature-edit_save',views.category_feature_edit_save,name='category_feature_edit_save'),
    path('category-feature-Delete/<int:pk>',views.feature_remove,name='feature_remove'),

    #=========Template urls=========
    path('Template-Form',views.template_load,name='template_load'),
    path('Template-List',views.template_list,name='template_list'),
    path('Template-Files',views.template_file,name='template_file'),
    path('search_files',views.search_files,name='search_files'),
   
    path('Fetch-Templates-List',views.fetch_templates_list,name='fetch_templates_list'),
    path('Fetch-Templates-File',views.fetch_templates_file,name='fetch_templates_file'),
    path('Template-Edit-List',views.template_editload,name='template_editload'), 
    path('Template-Code-Generate/<int:temp_id_code>',views.template_code_generate,name='template_code_generate'),
    path('Template-Remove/<int:pk>',views.template_remove,name='template_remove'),
    path('Template-save',views.template_save,name='template_save'),
    path('Template-view/<int:pk>',views.template_view,name='template_view'),
    path('Template-Edit-Save',views.template_editsave,name='template_editsave'),


    # clients section 
    path('Client-Settings',views.client_load,name='client_load'),
    path('Client-List',views.client_list,name='client_list'),
    path('Client-Save',views.client_save,name='client_save'),
    path('Client-EditForm/<int:cedit_id>',views.client_edit,name='client_edit'),
    path('Client-Edit-Save',views.client_editsave,name='client_editsave'),
    path('Client-Remove/<int:client_id>',views.client_remove,name='client_remove'),
     

     # Testimonial Section 

    path('Testimonial-Form',views.testimonial_load,name='testimonial_load'),
    path('Testimonial-Save',views.testimonial_save,name='testimonial_save'),
    path('Testimonial-List',views.testimonial_list,name='testimonial_list'),
    path('Testimonial-Remove/<int:testi_remove>',views.testimonial_remove,name='testimonial_remove'),
    path('Testimonial-Edit/<int:testi_edit>',views.testimonial_edit,name='testimonial_edit'),
    path('Testimonial-Edit-Save',views.testimonial_edit_save,name='testimonial_edit_save'),
     

    # Message Section
    path('Message',views.view_allmessage,name='view_allmessage'),
    path('Message-Remove/<int:remove_id>',views.message_remove,name='message_remove'),

    

    path('Account-Settings',views.profile,name='profile'),
    path('Account-Profile-Edit',views.useredit_save,name='useredit_save'),
    path('Account-Profile-Password-Edit',views.user_password_edit,name='user_password_edit'),
    path('Account-Profile-Password',views.userpassword_save,name='userpassword_save'),
    path('Service-enquiry',views.serviceEnquiry, name='serviceEnquiry'),
    path('Save-enquiry',views.saveEnquiry, name='saveEnquiry'),
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)