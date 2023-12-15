from django.shortcuts import render
from recipes.utils.recipes.factory import make_recipe


def home(request):
    return render(
        request,
        template_name='recipes/pages/home.html',
        context={'recipes': [make_recipe() for _ in range(10)], }
    )


def recipe(request, id):
    return render(
        request,
        template_name='recipes/pages/recipe-view.html',
        context={'recipe': make_recipe(),
                 'is_detail_page': True}
    )
