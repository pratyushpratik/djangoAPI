from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^questions-answers-with-subcategoryID/(?P<pk>[\w:|-]+)/$',
        views.GetLearningCentreQuestionsAnswersWithSubcategoryID.as_view()),
]