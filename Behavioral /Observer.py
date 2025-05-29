# Observer (Gözlemci)
class Subscriber:
    def update(self, news):
        pass

# Concrete Observer
class EmailSubscriber(Subscriber):
    def update(self, news):
        print(f"[E-posta] Yeni haber: {news}")

class SMSSubscriber(Subscriber):
    def update(self, news):
        print(f"[SMS] Yeni haber: {news}")

# Subject (Gözlemlenen)
class NewsAgency:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)

    def notify_all(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)

# Kullanım
agency = NewsAgency()

email_user = EmailSubscriber()
sms_user = SMSSubscriber()

agency.subscribe(email_user)
agency.subscribe(sms_user)

# Haber geldiğinde tüm aboneler bilgilendirilir
agency.notify_all("Deprem meydana geldi!")

#Bir nesne değiştiğinde, bu değişiklikten haberdar olması gereken diğer nesnelere otomatik bildirim gönderilmesini sağlamak.
#Yani: "Bir değişiklik olduğunda haberim olsun!"

