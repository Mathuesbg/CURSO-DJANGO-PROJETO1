from django.shortcuts import render
from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(
        request,
        template_name='recipes/pages/home.html',
        context={"recipes": recipes}
    )


def category(request, category_id):
    recipes = Recipe.objects.filter(
        is_published=True,
        category__id=category_id
    ).order_by('-id')
    return render(
        request,
        template_name='recipes/pages/category.html',
        context={"recipes": recipes}
    )


def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(
        request,
        template_name='recipes/pages/recipe-view.html',
        context={'recipe': recipe,
                 'is_detail_page': True}
    )
