import copy

# Ürün sınıfı
class Kedi:
    def __init__(self, isim, renk):
        self.isim = isim
        self.renk = renk

    def konus(self):
        print(f"{self.isim} diyor ki: Miyav!")

# Kopyalama yapan sınıf
class PrototipYonetici:
    def __init__(self):
        self._ornekler = {}

    def kaydet(self, isim, nesne):
        self._ornekler[isim] = nesne

    def kopyala(self, isim):
        return copy.deepcopy(self._ornekler[isim])

# Kullanım

orijinal_kedi = Kedi("Minnoş", "Beyaz")

yonetici = PrototipYonetici()
yonetici.kaydet("temel_kedi", orijinal_kedi)

kopya_kedi = yonetici.kopyala("temel_kedi")
kopya_kedi.isim = "Pamuk"

# Test
orijinal_kedi.konus()   # Minnoş diyor ki: Miyav!
kopya_kedi.konus()      # Pamuk diyor ki: Miyav!

#copy.deepcopy kullanarak nesnenin tüm alt verileriyle birlikte derin kopyasını çıkarıyoruz.
#PrototipYonetici: birden fazla prototip nesnesini saklar ve istenileni kopyalayarak üretir.
#Bu desen özellikle nesne oluşturma maliyetli olduğunda kullanışlıdır.