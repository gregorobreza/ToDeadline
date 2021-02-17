from django import template
from ..models import Task

register = template.Library()

@register.simple_tag
def total_tasks_todo():
    return Task.objects.all().filter(complete=False).count()

@register.filter(name='importance')
def in_level(tasks, level):
    return tasks.filter(level=level)