from django.shortcuts import render


def page_not_found_view(request, exception):
    return render(request, 'page-404.html', status=404)


# def page_server_error_view(request):
#     return render(request, 'page-404.html', status=500)
