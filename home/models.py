from django.db import models
 
class Book(models.Model):
    FANTASY = 1
    MYSTERY = 2
    ROMANCE = 3
    BOOK_TYPES = (
        (FANTASY, 'Fantasy'),
        (MYSTERY, 'Mystery'),
        (ROMANCE, 'Romance'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)
   
    class Meta:
        db_table = 'books' 