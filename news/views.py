from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import NewsModel


class MainPage(ListView):
    model = NewsModel
    template_name = 'general_api/news/news.html'

    def get(self, request, *args, **kwargs):
        news = self.model.objects.all().order_by('-created')[:3]
        return render(request, self.template_name, {'data': news})


class NewsView(DetailView):
    model = NewsModel
    template_name = 'general_api/news/pk_news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'news_id': self.model.objects.get(id=self.kwargs['pk'])})
        return context
