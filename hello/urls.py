from django.urls import path
from hello import views
from hello.models import LogMessage
from .views import SignUpView

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("register/", views.register, name='register'),
    path("booking/", views.booking, name='booking'),
    path("log/", views.log_message, name="log"),
    path("signup/", SignUpView.as_view(), name="signup"),
]