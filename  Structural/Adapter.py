# Eski sistemdeki sınıf
class OldPrinter:
    def old_print(self, text):
        print(f"Eski yazıcı: {text}")

# Yeni sistemin beklediği arayüz
class NewPrinterInterface:
    def print_text(self, text):
        pass

# Adapter sınıfı
class PrinterAdapter(NewPrinterInterface):
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print_text(self, text):
        # Eski metoda yönlendirme yapıyor
        self.old_printer.old_print(text)

# Kullanım
old_printer = OldPrinter()
adapter = PrinterAdapter(old_printer)

# Yeni sistem, Adapter üzerinden eski sistemi kullanabiliyor
adapter.print_text("Merhaba Dünya!")

#OldPrinter: Var olan ama uyumsuz bir sınıf.
#PrinterAdapter: Yeni sisteme uygun arayüzü sağlar ama aslında eski sınıfı kullanır.
#adapter.print_text(...): Artık yeni arayüzle uyumlu çağrı yapılabilir.
