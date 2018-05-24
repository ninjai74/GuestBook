from django.shortcuts import render, redirect

from .models import Comment
from .forms import CommentForm

# Views for the guestbook
#Function for the index page of the guestbook

def index(request):
    # to get the comments from the database
    # '-date_added' is used to display the latest comment
    comments = Comment.objects.order_by('-date_added')

    # to display the comments
    context = {'comments' : comments}

    return render(request, 'guestbook/index.html', context)


#Function for the sign page of the guestbook
def sign(request):
    if request.method == 'POST':
        # instanciate the form with the data from the request
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')
    else:
        # instansiate the form to create the form
        form = CommentForm()

    # created to pass the context to the template
    context = {'form' : form}
    return render(request, 'guestbook/sign.html', context)    
