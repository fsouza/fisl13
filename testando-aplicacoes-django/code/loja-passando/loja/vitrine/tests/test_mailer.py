from django import test
from django.core import mail

from loja.vitrine import mailer


class MailerTestCase(test.TestCase):

    def test_deve_enviar_email_de_forma_assincrona(self):
        m = mailer.EnviadorDeEmail()
        m.enviar_email(
            assunto=u"Contato",
            remetente=u"algumacoisa@fisl.org.br",
            destinatario=u"algumacoisa@fisl.org.br",
            mensagem=u"Mensagem de teste"
        )
        self.assertTrue(m.esperar(5))
        email = mail.outbox[0]
        self.assertEqual(u"Contato", email.subject)
        self.assertEqual(u"algumacoisa@fisl.org.br", email.from_email)
        self.assertEqual([u"algumacoisa@fisl.org.br"], email.to)
        self.assertEqual(u"Mensagem de teste", email.body)
