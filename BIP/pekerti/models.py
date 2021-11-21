from django.db import models
# from CustomUserAuth.models import User
from pekerti.functions.function import user_directory_path,validate_file_extension,validate_nidn,validate_number

class Peserta(models.Model):

    class Meta:
        verbose_name_plural = "Data Peserta"
    def __str__(self) :
        return str(self.id)

    id              = models.AutoField   ( primary_key=True),
    owner           = models.ForeignKey  ( ("ext_user.User"), related_name='pekerti', on_delete=models.CASCADE)
    nama            = models.CharField   ( ("Nama Peserta")       , max_length=50    )
    nidn            = models.CharField   ( ("NIDN")               , blank= True, max_length=10,validators=[validate_nidn]    )
    institusi_asal  = models.CharField   ( ("Institusi Asal")     , max_length=50    )
    nomer_telp      = models.CharField   ( ("Nomer Telepon")      , max_length=16, validators=[validate_number]    )
    link_transfer   = models.FileField   ( ("Bukti Transfer")     , blank= True, upload_to=user_directory_path,validators=[validate_file_extension])
    link_penugasan  = models.FileField   ( ("Dokumen Penugasan")  , upload_to=user_directory_path,validators=[validate_file_extension])
    link_kesanggupan= models.FileField   ( ("Dokumen Kesanggupan"), blank= True, upload_to=user_directory_path,validators=[validate_file_extension])
    link_sertifikat = models.CharField   ( ("Sertifikat")         , max_length=254   , blank=True )
    is_validated    = models.BooleanField( ("Status Validasi")    , blank= True, default=False)
    gelombang       = models.ForeignKey  ( ("Gelombang")          , verbose_name=("Gelombang"), on_delete=models.CASCADE )
    
class Gelombang(models.Model):

    class Meta:
        verbose_name_plural = "Data Pelaksanaan Gelombang"

    def __str__(self) :
        return "Gelombang " + str(self.id)

    id                  = models.IntegerField   ( ("Gelombang Id")          , primary_key = True)
    start_date          = models.DateField      ( ("Tanggal Mulai")      , auto_now=False, auto_now_add=False)
    end_date            = models.DateField      ( ("Tanggal Berakhir")   , auto_now=False, auto_now_add=False)
    link_kelas          = models.CharField      ( ("Link Kelas")         , blank=True    , max_length=50 )
    kode_akses_kelas    = models.CharField      ( ("Class Access Code")  , blank=True    , max_length=50 )
    jumlah_jam          = models.IntegerField   ( ("Jumlah Jam Pelaksanaan"))
    is_full             = models.BooleanField   ( ("Apakah Sudah Penuh")    , blank= True, default=False)
