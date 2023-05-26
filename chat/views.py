from django.shortcuts import render

# Create your views here.

def lobby(request):
    for i in inspect.stack():
        print(i[0].f_locals)
    return render(request, 'chat/lobby.html')



import inspect



# def gets_current_user():
#     return next(
#         (
#             frame_record[0].f_locals['request']
#             for frame_record in inspect.stack()
#             if frame_record[3] == 'dispatch'
#         ),
#         None,
#     )