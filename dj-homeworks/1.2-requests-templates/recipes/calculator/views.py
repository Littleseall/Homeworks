from django.shortcuts import render
from django.http import Http404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'rolls': {
        'лосось, кусок': 1,
        'нори, лист': 1,
        'рис, штука': 1,
        'авокадо, кусок': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe_view(request, recipe_name):
    if recipe_name not in DATA:
        raise Http404("Рецепт не найден.")

    servings = request.GET.get('servings', 1)

    try:
        servings = int(servings)
        if servings <= 0:
            raise ValueError
    except (ValueError, TypeError):
        servings = 1


    recipe = {ingredient: amount * servings for ingredient, amount in DATA[recipe_name].items()}

    context = {
        'recipe': recipe,
    }

    return render(request, 'calculator/index.html', context)