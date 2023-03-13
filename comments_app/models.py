from django.db import models
    

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f'{self.user_name} - {self.created_at}'
