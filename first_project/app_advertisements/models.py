from django.contrib import admin
from django.db import models
from django.utils.html import format_html

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text="Отметьте, если торг уместен ;)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_at = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_at
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
        
    @admin.display(description="Дата обновления")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_at = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: limegreen; font-weight: bold;">Сегодня в {}</span>', updated_at
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return "{}(id={id}, title={title}, price={price})".format(self.__class__.__name__, **self.__dict__)
    
    class Meta:
        db_table = "advertisements"
