from django.shortcuts import render
from ITD_App.models import InternalTopic
def home(request):
    all_topic = InternalTopic.objects.all()
    return render(request, 'index.html', {'InternalTopics': all_topic})

'''
def topic_list(request):
    # This now works because DjangoTopic is a Model
    all_topics = DjangoTopic.objects.all()
    return render(request, 'index.html', {'topics': all_topics})
'''