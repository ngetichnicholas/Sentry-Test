from django.urls.conf import path
import sentry_test_app.views as app_views

urlpatterns = [
    path('',app_views.index,name='home'),
    path('my_task_test', app_views.my_task_test, name="my_task_test")
]
