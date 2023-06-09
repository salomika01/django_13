from django.shortcuts import render
from .models import Reader


def enter_info(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        favorite_book_id = request.POST['favorite_book']

        # Create a new reader object
        reader = Reader.objects.create(name=name, email=email, date_of_birth=date_of_birth,
                                       favorite_book_id=favorite_book_id)

        return render(request, 'reader/thank_you.html', {'reader': reader})
    else:
        return render(request, 'reader/enter_info.html')
