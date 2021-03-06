# -*- coding: utf-8 -*-
"""
Formularios para la app globales
"""
# Librerias Standard
import re
from datetime import date

# Librerias Django
from django import forms
# Django Library
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.files import File
from django.forms import EmailInput, ModelForm, NumberInput, Select, TextInput

# Librerias de terceros
from PIL import Image

# Librerias en carpetas locales
from .models import Persona


class PerfilForm(ModelForm):
    """Clase para actualizar el perfil del usuario en el sistema
    """
    class Meta:
        model = Persona
        fields = (
            'avatar',
            'first_name',
            'otros_nombres',
            'last_name',
            'otros_apellidos',
            'email_secundario',
            'letra_cedula_identidad',
            'cedula_identidad',
            'telefono',
            'celular',
            'fecha_nacimiento',
            'sexo',
        )
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'otros_nombres': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'otros_apellidos': TextInput(attrs={'class': 'form-control'}),
            'email_secundario': TextInput(attrs={'class': 'form-control'}),
            'letra_cedula_identidad': Select(attrs={'class': 'form-control'}),
            'cedula_identidad': NumberInput(attrs={'class': 'form-control'}),
            'telefono': TextInput(attrs={'class': 'form-control'}),
            'celular': TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': TextInput(attrs={'class': 'form-control'}),
            'sexo': Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        super().clean()
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        cedula_identidad = str(self.cleaned_data.get('cedula_identidad'))

        # Validamos que la persona tiene menos de diez y ocho(18) años
        fecha_actual = date.today()
        print('Fecha: %s' % fecha_nacimiento)
        edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        if edad < 18:
            self.add_error('fecha_nacimiento', "Disculpe, debe ser mayor de edad para poder registrarse en\
                             el sistema")

        #  Si la persona tiene nueve(9) años o mas, validamos la cédula tenga la forma 99999999
        patron_mayor_edad = re.compile('^\d{5,8}$')
        if edad >= 9 and patron_mayor_edad.match(cedula_identidad) is None:
            self.add_error('cedula_identidad', "La cédula de identidad de las personas mayores o iguales\
                             a nueve (9) años de edad, debe comenzar con V ó E, seguido de hasta ocho (8) \
                             digitos correspondientes al número de la cédula")

    def clean_telefono(self):
        """
        Validamos que el teléfono cumpla con el formato
        """
        diccionario_limpio = self.cleaned_data
        telefono = diccionario_limpio.get('telefono')
        patron = re.compile('^\+58\s\(\d{3}\)\s\d{3}\-\d{2}\-\d{2}$')
        if telefono:
            if patron.match(telefono) is None:
                raise forms.ValidationError("El número de teléfono local debe\
                                                cumplir con la forma +58 (999)\
                                                999-99-99")
        return telefono

    def clean_celular(self):
        """
        Validamos que el celular cumpla con el formato
        """
        diccionario_limpio = self.cleaned_data
        celular = diccionario_limpio.get('celular')
        patron = re.compile('^\+58\s\(\d{3}\)\s\d{3}\-\d{2}\-\d{2}$')
        if celular:
            if patron.match(celular) is None:
                raise forms.ValidationError(
                    "El número de teléfono celular debe cumplir con la forma +58 (999) 999-99-99")
        return celular


class PersonaChangeForm(UserChangeForm):
    """Para algo sera esto
    """
    class Meta(UserChangeForm.Meta):
        model = Persona
        fields = (
            'username',
            'is_superuser',
            'is_staff',
            'is_active',
            'last_login',
            'date_joined',
            'first_name',
            'last_name',
        )


class PersonaCreationForm(UserCreationForm):
    """Con esta clase de formulario se renderiza la plantilla de registro de ususarios
    """
    class Meta(UserCreationForm.Meta):
        model = Persona
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder':'Primer nombre'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder':'Primer apellido'}),
            'username': TextInput(attrs={'class': 'form-control', 'placeholder':'Usuario'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder':'Coreo electrónico'}),
        }





# class AvatarForm(ModelForm):
#     """Clase para actualizar el perfil del usuario en el sistema
#     """
#     class Meta:
#         model = Persona
#         fields = (
#             'avatar',
#         )
#     def clean_avatar(self):
#         avatar = self.cleaned_data['avatar']

#         try:
#             w, h = get_image_dimensions(avatar)

#             #validate dimensions
#             max_width = max_height = 100
#             if w > max_width or h > max_height:
#                 raise forms.ValidationError(
#                     u'Please use an image that is '
#                      '%s x %s pixels or smaller.' % (max_width, max_height))

#             #validate content type
#             main, sub = avatar.content_type.split('/')
#             if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
#                 raise forms.ValidationError(u'Please use a JPEG, '
#                     'GIF or PNG image.')

#             #validate file size
#             if len(avatar) > (20 * 1024):
#                 raise forms.ValidationError(
#                     u'Avatar file size may not exceed 20k.')

#         except AttributeError:
#             """
#             Handles case when we are updating the user profile
#             and do not supply a new avatar
#             """
#             pass

#         return avatar






class AvatarForm(ModelForm):
    """Clase para actualizar el perfil del usuario en el sistema
    """
    # x = forms.FloatField(widget=forms.HiddenInput())
    # y = forms.FloatField(widget=forms.HiddenInput())
    # width = forms.FloatField(widget=forms.HiddenInput())
    # height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Persona
        fields = (
            'avatar',
        )

    # def save(self):
    #     photo = super(AvatarForm, self).save()

    #     x = self.cleaned_data.get('x')
    #     y = self.cleaned_data.get('y')
    #     w = self.cleaned_data.get('width')
    #     h = self.cleaned_data.get('height')

    #     image = Image.open(photo.avatar)
    #     cropped_image = image.crop((x, y, w+x, h+y))
    #     resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
    #     resized_image.save(photo.avatar.path)

    #     return photo
