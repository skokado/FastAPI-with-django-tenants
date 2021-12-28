from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('著者名', max_length=127)

    class Meta:
        db_table = 'authors'


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='blogs')
    title = models.CharField('タイトル', max_length=127)
    body = models.TextField('本文', null=True, default='')

    class Meta:
        db_table = 'blogs'
