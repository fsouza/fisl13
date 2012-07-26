import threading

from django.core import mail


class EnviadorDeEmail(object):

    def enviar_email(self, assunto, remetente, destinatario, mensagem):
        kwargs = {
            "subject": assunto,
            "from_email": remetente,
            "recipient_list": [destinatario],
            "message": mensagem,
        }
        self.t = threading.Thread(target=mail.send_mail, kwargs=kwargs)
        self.t.start()

    def esperar(self, tempo):
        self.t.join(timeout=tempo)
        return not self.t.isAlive()
