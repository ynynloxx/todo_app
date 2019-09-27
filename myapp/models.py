from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    category = models.CharField(_('category'), max_length=200)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.category


class ToDo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name=_('category'), null=True)
    todo_name = models.CharField(_('todo_name'), max_length=200)
    todo_date = models.DateField(_('todo_date'), blank=True)

    class Meta:
        verbose_name = _('todo')
        verbose_name_plural = _('todos')

    def __str__(self):
        return self.todo_name


class Appointment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name=_('category'), null=True)
    appoint_name = models.CharField(_('appoint_name'), max_length=200)
    appoint_date = models.DateField(_('appoint_date'), blank=False)

    class Meta:
        verbose_name = _('appointment')
        verbose_name_plural = _('appointments')

    def __str__(self):
        return self.appoint_name
