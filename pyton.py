# def password(request):
#     myPassword=''
#     characters=list('abcdefghijklmnopqrstuvwxyz')
#     length=int(request.Get.get('length'))
#     for x in range(length):
#         myPassword+=random.choice(characters) 
#     return (request ,'generate/password.html',{password:'myPassword'})

# def password(request):
#        # return HttpResponse('our first django page')
#    myPassword=''
#    characters= list('abcdefghijklmnopqrstuvwxyz')
#    length =int(request.GET.get('length'))
#    if request.GET.get('uppercase'):
#           characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
#    if request.GET.get('numbers'):
#           characters.extend(list("0123456789"))
#    if request.GET.get('specials'):
#           characters.extend(list("~!@#$%^&*()_+{}[]:<>?"))

#    for x in range(length):
#           myPassword += random.choice(characters)
#    return render(request, 'generator/password.html', {"password":myPassword})
