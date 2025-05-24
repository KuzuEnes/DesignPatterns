# Ürün (Product)
class Burger:
    def __init__(self):
        self.malzemeler = []

    def ekle(self, malzeme):
        self.malzemeler.append(malzeme)

    def goster(self):
        print("Burger hazır! Malzemeler:")
        for m in self.malzemeler:
            print(f" - {m}")

# Builder
class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def et_koy(self):
        self.burger.ekle("Et")

    def peynir_ekle(self):
        self.burger.ekle("Peynir")

    def ketcap_ekle(self):
        self.burger.ekle("Ketçap")

    def al(self):
        return self.burger

# Director (İsteğe bağlı)
class BurgerYapici:
    def __init__(self, builder):
        self.builder = builder

    def klasik_burger_yap(self):
        self.builder.et_koy()
        self.builder.peynir_ekle()
        self.builder.ketcap_ekle()
        return self.builder.al()

# Kullanım

builder = BurgerBuilder()
yapici = BurgerYapici(builder)
hazir_burger = yapici.klasik_burger_yap()
hazir_burger.goster()

#Burger: Nihai ürün (product).
#BurgerBuilder: Burger inşa etmek için adımları tanımlar.
#BurgerYapici (Director): Adımları bir sıraya koyar ve ürünü oluşturur.
#Farklı burger türleri üretmek için aynı yapıcıyı (builder) farklı şekilde çağırabilirsin.

