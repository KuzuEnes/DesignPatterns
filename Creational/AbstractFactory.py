# Ürün Arayüzleri
class Klavye:
    def yaz(self):
        pass

class Mouse:
    def tikla(self):
        pass

# Windows Ürünleri
class WindowsKlavye(Klavye):
    def yaz(self):
        return "Windows klavyesiyle yazılıyor..."

class WindowsMouse(Mouse):
    def tikla(self):
        return "Windows mouse tıklandı!"

# Mac Ürünleri
class MacKlavye(Klavye):
    def yaz(self):
        return "Mac klavyesiyle yazılıyor..."

class MacMouse(Mouse):
    def tikla(self):
        return "Mac mouse tıklandı!"

# Abstract Factory
class BilgisayarBilesenleriFabrikasi:
    def klavye_olustur(self):
        pass

    def mouse_olustur(self):
        pass

# Concrete Factories
class WindowsFabrikasi(BilgisayarBilesenleriFabrikasi):
    def klavye_olustur(self):
        return WindowsKlavye()

    def mouse_olustur(self):
        return WindowsMouse()

class MacFabrikasi(BilgisayarBilesenleriFabrikasi):
    def klavye_olustur(self):
        return MacKlavye()

    def mouse_olustur(self):
        return MacMouse()

# Kullanım
def sistem_kur(factory: BilgisayarBilesenleriFabrikasi):
    klavye = factory.klavye_olustur()
    mouse = factory.mouse_olustur()
    print(klavye.yaz())
    print(mouse.tikla())

# Test
print("--- Windows sistemi ---")
sistem_kur(WindowsFabrikasi())

print("\n--- Mac sistemi ---")
sistem_kur(MacFabrikasi())

# Abstract Factory: BilgisayarBilesenleriFabrikasi – ortak ürünleri tanımlar.
# Concrete Factory: WindowsFabrikasi, MacFabrikasi – her biri kendi türünde klavye ve mouse üretir.
# Abstract Factory: Birbirleriyle ilişkili veya bağımlı nesneleri gruplar hâlinde birbirinden bağımsız olarak oluşturmak için kullanılır.