# Ürün sınıfları
class Kedi:
    def konus(self):
        return "Miyav"

class Kopek:
    def konus(self):
        return "Hav hav"

# Factory method
def hayvan_olustur(tur):
    if tur == "kedi":
        return Kedi()
    elif tur == "kopek":
        return Kopek()
    else:
        raise ValueError("Bilinmeyen hayvan türü!")

hayvan1 = hayvan_olustur("kedi")
hayvan2 = hayvan_olustur("kopek")

print(hayvan1.konus())  # Miyav
print(hayvan2.konus())  # Hav hav

#Alt sınıfların hangi nesneyi oluşturacağına karar vermesini sağlar; nesne oluşturma süreci bir metotla soyutlanır.
#hayvan_olustur() fonksiyonu bir factory method gibi çalışarak doğru sınıfın nesnesini üretir.


