def my_cp(request):
    user = request.user
    return {'user': user}