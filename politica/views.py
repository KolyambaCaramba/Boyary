from django.views.generic.base import TemplateView


class PoliticView(TemplateView):
    template_name = 'politica/polit.html'