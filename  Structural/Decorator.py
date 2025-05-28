# Temel arayüz (Component)
class Notifier:
    def send(self, message):
        pass

# Temel sınıf (Concrete Component)
class EmailNotifier(Notifier):
    def send(self, message):
        print(f"E-posta gönderildi: {message}")

# Dekoratör (Base Decorator)
class NotifierDecorator(Notifier):
    def __init__(self, notifier):
        self.notifier = notifier

    def send(self, message):
        self.notifier.send(message)

# Concrete Decorator: SMS
class SMSDecorator(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"SMS gönderildi: {message}")

# Concrete Decorator: Slack
class SlackDecorator(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Slack bildirimi gönderildi: {message}")

# Kullanım
notifier = EmailNotifier()
notifier = SMSDecorator(notifier)       # E-posta + SMS
notifier = SlackDecorator(notifier)     # E-posta + SMS + Slack

notifier.send("Sistem uyarısı!")

#Bir Notifier sınıfın var. İlk başta sadece e-posta gönderiyor. Sonra SMS ve Slack ile de bildirim göndermek istiyorsun.
#Decorator Pattern sayesinde bu işlevleri dinamik olarak ekleyebilirsin.

#Yeni işlevler eklemek için sınıfı değiştirmene gerek yok.
#İstediğin kadar decorate edebilirsin.
#open/closed principle (açık/kapalı prensibi)'ni uygular.

