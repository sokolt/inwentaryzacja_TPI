from gluon.tools import Mail
# mail = Mail()

#Działające !!!!!
EMAIL_SERVER = 'smtp.gmail.com:587'
EMAIL_SENDER = 'm.mlynarczyk87@gmail.com'
EMAIL_LOGIN = 'm.mlynarczyk87@gmail.com:masterve2015'


# EMAIL_SERVER = 'smtp.mandrillapp.com:587'
# EMAIL_SENDER = 'calantpi@o2.pl'
# EMAIL_LOGIN = 'calantpi@o2.pl:masterve2016'
# EMAIL_POLICY = 'deferred' # or 'realtime'

#http://smtp.mandrillapp.com:587/
#smtp.poczta.o2.pl:587

# mail = Mail()
#587 smtp 
# ##haslo: masterve2016

#from gluon.tools import Mail
# mail = Mail()
# mail.settings.server = 'smtp.poczta.o2.pl:587'
# mail.settings.sender = 'calantpi@tlen.pl'
# mail.settings.login = 'calantpi@tlen.pl:masterve2016'

#def EdycjaSprzet():
#     forma = SQLFORM(db.Dodaj_Sprzet)
#     if forma.process().accepted:
#         response.flash='Zapisano'
#         email = db.auth_user(forma.vars.assigned_to).email
#         mail.settings.sender = EMAIL_SENDER
#         mail.send(to=["m.mlynarczyk24@gazeta.pl"],
#                   subject="Nowy sprzet dodany: %s" % forma.vars.Rodzaj_Sprzetu,
#                   message=forma.vars.Model or'Dodano nowy sprzet'),
#         redirect(URL('Sprzet'))
#     return dict(forma=forma)
