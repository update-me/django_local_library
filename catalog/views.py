from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# Create your views here.
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    #context_object_name = 'book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
   # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location




def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    
    num_genres = Genre.objects.count()
    
    the_books_count = Book.objects.filter(title__icontains='the').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'the_books_count': the_books_count,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    
class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 10
    
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
    
class AuthorDetailView(generic.DetailView):
    model = Author
