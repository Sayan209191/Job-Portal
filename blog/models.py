from django.db import models

from django.contrib.auth.models import User
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    isUpdated = models.BooleanField(default=False)
    updated_at = models.DateTimeField(default=None)
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
class LikeDislike(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    CHOICE = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.CharField(max_length=7, choices=CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('article', 'user')

    def __str__(self):
        return f"{self.user.username} {self.choice}d {self.article.title}"