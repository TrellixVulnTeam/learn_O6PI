import stripe
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.utils.translation import gettext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.base import View, TemplateView
from django.contrib.auth.decorators import login_required
from .models import Category
from .forms import RegisterForm, UserUpdate, MemberForm, BookForm
from .models import Question
# Create your views here.
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

def index1(request):
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "index1.html", context={'plot_div': plot_div})

# List View
from .models import Category
# Page Not Found



# List View
from .render import Render


class CategoryList(ListView):
    # specify the model for list view
    model = Category
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        qs = super(CategoryList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs


# Detail View
class CategoryDetail(DetailView):
    # specify the model for list view
    model = Category

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetail,
                        self).get_context_data(*args, **kwargs)
        # add extra field
        context["category"] = "MISC"
        return context


class CategorytUpdate(UpdateView):
    model = Category
    # specify the fields
    fields = '__all__'

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = "/"


# Delete View
class CategoryDelete(DeleteView):
    # specify the model you want to use
    model = Category

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/"


# Generic View
class MyRegisterView(View):
    template_name = 'register1.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # form.save()
            return HttpResponse("Form Submit Done !")
        else:
            return render(request, self.template_name, {'form': form})


class PostsView(ListView):
    model = Category
    paginate_by = 4
    context_object_name = 'posts'
    template_name = 'test.html'
    ordering = ['name']

def table(request):
    return render(request,"test.html")


def index(request):
    # create a dictionary to pass
    # data to the template
    context = {
        "data": "Gfg is the best",
        "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    # return response with template and context
    return render(request, "index.html", context)


def ajax(request):
    return render(request, "ajax.html")


def home(request):
    return render(request, "base.html")


def not_found(request):
    # q = Question(question_text="Second Question?", pub_date=timezone.now())
    return HttpResponseNotFound('<h1>Page Not Found  !</h1>')


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def member(request):
    return render(request, "member.html", {"form": MemberForm()})


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect('/')

    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})


def profile(request):
    # if this is a POST request we need to process the form data
    template = 'profile.html'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect('/')

    # No post data availabe, let's just show the page.
    else:

        # form = RegisterForm(initial={"username": "mit"})
        user_data = User.objects.get(username=request.user.username)
        form = UserUpdate(initial={"first_name": user_data.first_name,
                                   "last_name": user_data.last_name})

    return render(request, template, {'form': form})


def view_product(request):
    return render(request, "view_product.html")

class Pdf(View):

    def get(self, request):
        sales = Category.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'sales': sales,
            'request': request
        }
        return Render.render('pdf.html', params)

def done(request):
    return HttpResponse("Your Are Loggin With Google !")

# Strip Payment Gateway
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - lets capture the payment later
            # [customer_email] - lets you prefill the email input in the form
            # For full details see https:#stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'Ramayan',
                        'quantity': 1,
                        'currency': 'inr',
                        'amount': '10000',
                    },
                    {
                        'name': 'Mahabharat',
                        'quantity': 1,
                        'currency': 'inr',
                        'amount': '10000',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

class SuccessView(TemplateView):
    template_name = 'success.html'

class CancelledView(TemplateView):
    template_name = 'cancelled.html'