from django.db import models
from django.urls import reverse

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    # This method name: 'get_absolute_url()' is reserved in django
    # def get_absolute_url(self):
    #     return reverse("employee_app:edit", kwargs={"employee_id": self.pk})

    def get_absolute_url_edit(self):
        return reverse("employee_app:edit", kwargs={"employee_id": self.pk})

    def get_absolute_url_delete(self):
        return reverse("employee_app:delete", kwargs={"employee_id": self.pk})
