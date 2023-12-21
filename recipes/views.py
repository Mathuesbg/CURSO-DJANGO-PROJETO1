from django.shortcuts import render, get_list_or_404, get_object_or_404
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

    recipes = get_list_or_404(
        Recipe.objects.filter(
            is_published=True,
            category__id=category_id
        ).order_by('-id')
    )

    return render(request, template_name='recipes/pages/category.html',
                  context={
                      "recipes": recipes,
                      "title": f"Category - {recipes[0].category.name}",
                  })


def recipe(request, id):

    recipe = get_object_or_404(Recipe, is_published=True, id=id)

    return render(
        request,
        template_name='recipes/pages/recipe-view.html',
        context={'recipe': recipe,
                 'is_detail_page': True}
    )
