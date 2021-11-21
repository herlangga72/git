# Register your models here.
from django.contrib import admin
from pekerti.models import Peserta,Gelombang
# Register your models here.

@admin.register(Peserta)
class Peserta(admin.ModelAdmin):
    list_display = (
        "id",
        "nama",
        "nidn",
        "institusi_asal",
        "gelombang",
        "nomer_telp",
        "is_validated",
        "link_sertifikat"
        )

    def Sertifikat(self, obj):
        return bool(obj.linkSertifikat)==True
    
    #displayed
    list_filter = ["nama","nidn","institusi_asal","gelombang","nomer_telp","is_validated"]
    search_fields = ["nama","nidn","institusi_asal","gelombang","nomer_telp","is_validated"]
    Sertifikat.boolean = True

@admin.register(Gelombang)
class Gelombang(admin.ModelAdmin):
    list_display=['id', 'start_date', 'end_date', 'link_kelas', 'kode_akses_kelas']
