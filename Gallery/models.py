from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class Picture(models.Model):
    index = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to='pictures_main/')
    preview_image = models.ImageField(upload_to='pictures_preview/')
    likes = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.index}: "{self.name}" by "{self.publisher.name}"'


class SubmitPictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['main_image', 'name']

    def __init__(self, *args, **kwargs):
        super(SubmitPictureForm, self).__init__(*args, **kwargs)
        self.fields['main_image'].widget.attrs.update({'class': 'form__main-image'})
        self.fields['name'].widget.attrs.update({'class': 'form__image-name'})