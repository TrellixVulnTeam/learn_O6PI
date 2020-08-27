from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import index, not_found, detail, results, \
   vote, user_register, home, profile, view_product,\
   PostsView, ajax, member, MyRegisterView, CategoryList, CategoryDetail, CategorytUpdate,\
   CategoryDelete, Pdf, stripe_config, create_checkout_session, SuccessView, CancelledView, \
   table, index1

from django.contrib.auth import views
#from .admin import admin_site
from .forms import UserUpdate, BookForm, ChoiceForm
from django.conf.urls import handler404
from django.views.generic import TemplateView

urlpatterns = [
  # path('admin/', admin.site.urls),
   path('social/', TemplateView.as_view(template_name='polls/social.html')),
   path('table/', table, name="TableView"),
   path('index/', index1, name ="Plotly"),
   path('home/', TemplateView.as_view(template_name='home.html')),
   path('config/', stripe_config),
   path('success/', SuccessView.as_view()), # new
   path('cancelled/', CancelledView.as_view()), # new
   path('create-checkout-session/', create_checkout_session),
   path('', home, name = "index"),
   path('accounts/', include('allauth.urls')),
   path('render/pdf/', Pdf.as_view()),
   path('test/', PostsView.as_view(),  name="posts"),
   path('register/', user_register, name = "register"),
   path('classview',login_required(MyRegisterView.as_view(), login_url="login/"), name='original-create-view'), # template_name='other_form.html', form_class='MyOtherForm'
   path('classview1',login_required(MyRegisterView.as_view(template_name='relational.html', form_class=BookForm), login_url="login/"), name='original-create-view'),
   path('classview2',login_required(MyRegisterView.as_view(template_name='relational.html', form_class=ChoiceForm), login_url="login/"), name='original-create-view'),
   path('listview/', CategoryList.as_view(), name = "ListView"),
   path('detailview/<int:pk>', CategoryDetail.as_view(), name = "DetailView"),
   path('delete/<pk>', CategoryDelete.as_view()),
   path('update/<int:pk>', CategorytUpdate.as_view(), name = "UpdateView"),
   path('login/', views.LoginView.as_view(template_name="login.html"), name='login'),
   path('logout/', views.LogoutView.as_view(), name='logout'),
   path('profile/', profile, name='logout'),
   path('product/', view_product, name='logout'),
   path('ajax/', ajax, name='api parse'),
   path('member/', member, name='api parse'),
   path('password-change/', views.PasswordChangeView.as_view(template_name="password_change_form.html"), name='password_change'),
   path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
   path('password-reset/', views.PasswordResetView.as_view(template_name = "password_reset_form.html"), name='password_reset'),
   path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   path('not_found/', not_found, name = "not"),
   path('<int:question_id>/', detail, name='detail'),
   path('<int:question_id>/results/', results, name='results'),
   path('<int:question_id>/vote/', vote, name='vote'),
]


#handler404 = 'polls.views.error_404_view'