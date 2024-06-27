from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        db_table = "todos"
        ordering = ["-updated_at", "-created_at"]

