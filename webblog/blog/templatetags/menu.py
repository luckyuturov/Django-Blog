from atexit import register
from django import template
from blog.models import Category

#Модуль шаблонного тэга
#Здесь мы пишем собственные тэги

register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html') #Декаратор который будет декарировать функцию 
def show_menu(menu_class='menu'):
    categories = Category.objects.all()#Получаем все категории
    return {"categories": categories, "menu_class": menu_class}