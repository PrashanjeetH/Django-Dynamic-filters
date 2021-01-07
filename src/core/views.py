from django.db.models import Q
from django.shortcuts import render
from .models import Journal, Category
# Create your views here.


def get_verified_param(query):
    return query != '' and query is not None


def BootstrapFilterView(request):
    query_set = Journal.objects.all()
    category = Category.objects.all()
    if request.method == "POST":
        title_contains_query = request.POST.get('title_contains')
        title_or_author_query = request.POST.get('title_or_author')
        category_query = request.POST.get('category')
        reviewed_query = request.POST.get('reviewed')
        not_reviewed_query = request.POST.get('not_reviewed')
        min_views_query = request.POST.get('min_views')
        max_views_query = request.POST.get('max_views')
        min_date_query = request.POST.get('min_date')
        max_date_query = request.POST.get('max_date')

        if get_verified_param(title_contains_query):
            query_set = query_set.filter(title__icontains=title_contains_query)
        elif get_verified_param(title_or_author_query):
            query_set = query_set.filter(Q(title__icontains=title_or_author_query)
                                         | Q(author__name__icontains=title_or_author_query))

        if get_verified_param(category_query):
            query_set = query_set.filter(categories__name=category_query)

        if get_verified_param(min_views_query):
            query_set = query_set.filter(views__gte=min_views_query)

        if get_verified_param(max_views_query):
            query_set = query_set.filter(views__lt=max_views_query)

        if get_verified_param(min_date_query):
            query_set = query_set.filter(publish_date__gte=min_date_query)

        if get_verified_param(max_date_query):
            query_set = query_set.filter(publish_date__lt=max_date_query)

        if reviewed_query == 'on':
            query_set = query_set.filter(reviewed=True)
        elif not_reviewed_query == 'on':
            query_set = query_set.filter(reviewed=False)

        context = {
            'journals': query_set,
            'categories': category,
        }
    else:
        context = {
            'journals': query_set,
            'categories': category,
        }
    return render(request, "index.html", context)
