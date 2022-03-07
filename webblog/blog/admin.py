from encodings import search_function
from django.contrib import admin
from .models import * #Из файла models импортируем все
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_as = True #При редактировании статьи вместо кнопки "сохранить и добавить новую" будет "Сохранить как новый объект"
    save_on_top = True #Набор кнопок сверху при редактировании статьи
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo', 'views')
    list_display_links = ('id', 'title')#id и заголовок в админке становятся ссылками
    search_fields = ('title',)#Поиск статьи в админке по заголовкам
    list_filter = ('category', 'tags')#Фильтр в админке по категориям
    readonly_fields = ('views', 'created_at', 'get_photo') #Поля в админке становятся только для чтения
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at') #Какие поля показывать в админке при редактирвании статьи

    #Функция get_photo для отображения фотографии в админке и эту функцию добавляем в list_display
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return '-'
    
    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
