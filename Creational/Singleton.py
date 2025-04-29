class Singleton:
    _instance = None  # Sınıf değişkeni (tek örnek burada tutulur)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Yeni nesne oluşturuldu.")
        else:
            print("Var olan nesne döndürüldü.")
        return cls._instance



a = Singleton()
b = Singleton()

print(a is b)  # True -> Aynı nesne

#Bu pattern bir sınfın yalnızca bir nesne örneğine sahip olmasına ve bu örneğe genel bir erişim noktasından erişilmesine olanak tanır.
#Bir sınıf nesnesinin tek bir örneğinin olması bazı paylaşılan kaynaklara erişimin kontrollü sağlanması gerektiğinde işimize yarayacaktır.
#Genelde veri tabanı nesnesinin singleton olarak kullanıldığını görebilirsiniz.