# Daftar Isi

1. [Dependency dan Dokumentasi Terkait](#dependency)

2. [Struktur Folder](#files)

3. [Env Config](#env)

4. [Feature](#feature)

5. [Known Problem] (#problem)
## Dependency

1. Django==3.2.9
2. django-cors-headers==3.10.0
3. djangorestframework==3.12.4
4. django-filters==21.1
5. drf-spectacular==0.20.2
6. social-auth-app-django==5.0.0

## Files

1. [BIP](./BIP) = Adalah root dari Django. brikut dengan admin.site setting hardcoded.
2. [ext_user](./ext_user) = manajeman user user extended for futher use jadi tidak perlu mengobrak abrik kedepannya bila user manajemen ingin di ubah. hal ini juga masuk kedalap manajemen scope social auth disini. saat ini avatar disini
3. [manajemen_sessions](./manajemen_sessions) = manajemen session base terletak disini logout, user info rest api dan status autentikasi disini
4. [pekerti](./pekerti) = aplikasi pekerti

## Env
Penjelasan tiap variable sudah aada di [sini](./config.ini)

## Feature
1. Create Read Patch Delete pada APP PEKERTI dan juga filternya
2. PATCH User model based on serializer
3. Hanya Menggunakan ModelViewSet dan juga modelSerializer tujuan minimalisir import
4. Manajemen Session Menggunakan APIView sehingga lebih tertata di banding memaksa menggunakan dekorator

## Problem
