from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField('カテゴリ', max_length = 100)
    created_at = models.DateTimeField('作成日', default=timezone.now )

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('タイトル', max_length = 250)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default = timezone.now)
    category = models.ForeignKey(
        Category, verbose_name = 'カテゴリ', on_delete = models.PROTECT
    )

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.text[:20]

   
class Comment(models.Model):
    name = models.CharField('お名前',max_length = 50, default='이름을 적어주세요')
    text = models.TextField('コメント内容')
    post = models.ForeignKey(
        Post, verbose_name = '紐づく記事',on_delete = models.PROTECT
    )
    created_at = models.DateTimeField('作成日', default = timezone.now)

    def summary(self):
        return self.text[:10]


  

