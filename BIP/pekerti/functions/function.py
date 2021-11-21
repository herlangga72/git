import os
from django.core.exceptions import ValidationError
from django.conf import settings
from django.conf.urls.static import static

# simplify using python 3.6 formating syntax
def user_directory_path(instance, filename):
    return f'pekerti/peserta/{filename}'

# invalidate format except (pdf, jpg, jpeg, and png ) 
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf','.jpg', '.png', '.jpeg' ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_number(value,length=0):
    temp=[]
    print('start')
    for i in list(value):
        try:
            temp_b=int(i)
            if temp_b:
                temp.append(temp_b)
                print(f'im good{temp_b}')
            else:
                raise ValidationError('Input Salah')
        except:
            raise ValidationError('Input Salah')

    if length:
        if len(temp) != length:
            raise ValidationError('Input Salah')
def validate_nidn(value):
    validate_number(value,10)