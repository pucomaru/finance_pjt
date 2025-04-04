from django.db import models

class Comment(models.Model):
    company_name = models.CharField(max_length=100)
    stock_code = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.company_name}({self.stock_code})] {self.content[:30]}"
