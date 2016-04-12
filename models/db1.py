import datetime


STANOWISKO = ('Projektant','Handlowiec','Księgowość','Brygadzista','Monter','Kierownik_Robot','Kierownik_Projektu','Kierownik_Serwisu','Stazysta','Serwisant','Sekretariat')
MIEJSCEPRACY=('Biuro_Warszawa','Oddział_Katowice','Hala_Kozerki','Na_Budowie','Dyrektor')
RODZAJZATRUDNIENIA=('Umowa_o_prace','Umowa_o_dzieło','Umowa_Zlecenie')
RODZAJSPRZETU=('Laptop','Komputer_Stacjonarny','Monitor','Internet_Mobilny','Torba_Na_Laptopa','Drukarka','Aparat','Kamera','Switch','Router','Serwer','Telefon_Komórkowy','Nawigacja','Stacja_Robocza','Dysk_Przenośny','Pendrive','Oprogramowanie',)
GWARANCJA=('Brak','12_Miesiecy','24_Miesiace','36_Miesiecy','48_Miesiecy','60_Miesiecy')
STATUS=('Zajety','Wolny')
AKCEPTACJA=('W trakcie','Zaakceptowano','Odrzucono')


db.define_table('Pracownicy',
                Field('user_id', db.auth_user, writable=True, readable=True),
                Field('Imie','string'),
                Field('Nazwisko','string'),
                Field('Stanowisko',requires=IS_IN_SET(STANOWISKO)),
                Field('Miejsce_Pracy',requires=IS_IN_SET(MIEJSCEPRACY)),
                Field('Rodzaj_Zatrudnienia',requires=IS_IN_SET(RODZAJZATRUDNIENIA)),
                Field('Nr_tel_Prywatny','integer'),
                Field('Nr_tel_Sluzbowy','integer'),
                ),

# db.define_table('Sprzet',
#     Field('Wlasciciel', 'reference auth_user'),
#     format='%(Wlasciciel)s')


db.define_table('Dodaj_Sprzet',
                Field('user_id', db.auth_user, default=auth.user_id, writable=True, label='Pracownik' ),
                Field('Rodzaj_Sprzetu',requires=IS_IN_SET(RODZAJSPRZETU)),
                Field('Model','string',requires=IS_NOT_EMPTY()),
                Field('Serial_Number','string'),
                Field('Nr_Inw','string'),
                Field('Data_Zakupu','string'),
                Field('Nr_Faktury','integer'),
                Field('Gwarancja',requires=IS_IN_SET(GWARANCJA)),
                Field('IMEI','integer'),
                Field('Numer_telefonu','integer'),
                Field('Wlasciciel','reference auth_user', default=auth.user_id),
                Field('Lokalizacja',requires=IS_IN_SET(MIEJSCEPRACY)),
                Field('Status',requires=IS_IN_SET(STATUS),default=0),
                ),
##default=auth.user_id
db.define_table('Zamowienie',
                Field('user_id', db.auth_user, writable=False, readable=False, label='Pracownik' ),
                Field('Rodzaj_Sprzetu',requires=IS_IN_SET(RODZAJSPRZETU)),
                Field('Ilosc','integer',requires=IS_NOT_EMPTY()),
                Field('Dodatkowy_opis','string'),
                Field('Wlasciciel','reference auth_user', default=auth.user_id,writable=False),
                Field('Status',requires=IS_IN_SET(AKCEPTACJA),default=AKCEPTACJA[0],writable=False),
                auth.signature),

db.define_table('Licencje',
                Field('user_id',db.auth_user, label='Uzytkowany przez:'),
                Field('Licencja_na','string',requires=IS_NOT_EMPTY()),
                Field('Wykupiona_dnia','string',requires=IS_NOT_EMPTY()),
                Field('Okres_waznosci',requires=IS_IN_SET(GWARANCJA)),
                Field('Klucz_do_autoryzacji','string'),
                Field('Status',requires=IS_IN_SET(STATUS)),
                Field('Dodatkowe_informacje','string')),





def send_email_realtime(to, subject, message, sender):
        mail.settings.sender = sender
        mail.send(to=to, subject=subject, message=message or '(no message)')

def send_email_deferred(to, subject, message, sender):
    if not isinstance(to, list): to = [to]
    scheduler.queue_task(send_email_realtime,
        pvars=dict(to=to, subject=subject, message=message, sender=sender))

def send_email(to, subject, message, sender):
    if EMAIL_POLICY == 'realtime':
        return send_email_realtime(to, subject, message, sender)
    else:
        return send_email_deferred(to, subject, message, sender)
