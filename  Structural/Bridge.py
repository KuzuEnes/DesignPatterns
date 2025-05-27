# Uygulama kısmı (Implementor)
class TV:
    def on(self):
        pass

    def off(self):
        pass

# Concrete Implementor 1
class SonyTV(TV):
    def on(self):
        print("Sony TV açılıyor.")

    def off(self):
        print("Sony TV kapanıyor.")

# Concrete Implementor 2
class SamsungTV(TV):
    def on(self):
        print("Samsung TV açılıyor.")

    def off(self):
        print("Samsung TV kapanıyor.")

# Soyutlama (Abstraction)
class RemoteControl:
    def __init__(self, tv: TV):
        self.tv = tv

    def turn_on(self):
        self.tv.on()

    def turn_off(self):
        self.tv.off()

# Kullanım
sony = SonyTV()
samsung = SamsungTV()

remote1 = RemoteControl(sony)
remote2 = RemoteControl(samsung)

remote1.turn_on()     # Sony TV açılıyor.
remote2.turn_on()     # Samsung TV açılıyor.

remote1.turn_off()    # Sony TV kapanıyor.
remote2.turn_off()    # Samsung TV kapanıyor.


#TV: Soyut TV sınıfı (uygulama tarafı)
#SonyTV, SamsungTV: Farklı uygulama detaylarını içerir.
#RemoteControl: Soyutlama sınıfı, uygulama sınıfına bir köprü görevi görür.
#tv nesnesi dışarıdan verildiği için soyutlama ve implementasyon birbirinden bağımsız gelişebilir.

#Farklı platformlar (örneğin farklı cihazlar, işletim sistemleri, UI araçları) için ortak bir arabirim sağlamak istiyorsan.
#Hem arayüzü hem de implementasyonu genişletmek gerektiğinde (sınıf patlamasını önler).

