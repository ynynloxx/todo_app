from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    category_name = models.CharField(_('category_name'), max_length=200)

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    def __str__(self):
        return self.name


class ToDo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name=_('category_name'), null=True)
    todo_name = models.CharField(_('todo_name'), max_length=200)
    todo_date = models.DateField(_('todo_date'))
