from gluon import *
me = auth.user_id
##print "To jest moje id %s", me

def index():
    ##wrt = db.executesql('SELECT Pracownicy.imie FROM Pracownicy WHERE Pracownicy.id == ?;', (me,))
    ## db.auth_user.id==db.Pracownicy.Zarejestrowany_Uzytkownik
    return locals()

#Panel admin dla Pracownikow /Widoczne Dodaj Pracownika
@auth.requires_login()
def indexA():
    if auth.user.id != 5:
        redirect(URL('indexx'))
    return dict(message=T('Panel Administratora'))

##auth.user == db.auth_user.id==5:
@auth.requires_login()
def indexx():
    if auth.user.id == 5:
        redirect(URL('indexA'))
    else:
        redirect(URL('Pracownicy'))
    ##Dla pracownikow
    return locals()

@auth.requires_login()
def indexxx():
    ##Dla sprzetu
    if auth.user.id == 5:
        redirect(URL('indexxxA'))
    return locals()

#Panel Admin dla sprzet / Widoczne Dodaj Sprzet
@auth.requires_login()
def indexxxA():
    if auth.user.id!=5:
        redirect(URL('indexxx'))
    xyz = db().select(db.auth_user.first_name)
    return dict(xyz=xyz)

#Wyswietla liste pracownikow dodanych
@auth.requires_login()
def Pracownicy():
    tabela = db().select(db.Pracownicy.ALL)
    wrt = db().select(db.Dodaj_Sprzet.ALL)
    abc = db.executesql('SELECT Dodaj_Sprzet.Model FROM Dodaj_Sprzet WHERE Dodaj_Sprzet.user_id IN(SELECT user_id FROM Pracownicy);')
    ##SQLFORM.smartgrid(db.Pracownicy)
    return dict(tabela=tabela,wrt=wrt,abc=abc)

#Edycja Pracownikow, sa wpisane juz dane
@auth.requires_login()
def EdycjaPracownicyx():
    if auth.user.id !=5:
        redirect(URL('Pracownicy'))
        response.flash = T("Brak uprawnien!")
    id = request.args(0,cast=int)
    formd = SQLFORM(db.Pracownicy, id, showid=False).process(next='Pracownicy/[id]')
    return dict(formd=formd)

#Edycja sprzetu, sa wpisane juz dane
@auth.requires_login()
def EdycjaSprzetx():
    if auth.user.id != 5:
        redirect(URL('Sprzet'))
        response.flash = T("Brak uprawnien!")
    id = request.args(0,cast=int)
    formd = SQLFORM(db.Dodaj_Sprzet, id, showid=False).process(next='Sprzet/[id]')
    return dict(formd=formd)

def xaxaxa():
    sprzet = db().select(db.Dodaj_Sprzet.ALL)
    return dict(sprzet=sprzet)

#def Pracownicy():
#     par=P()
#     Pracownicy = db(db.Pracownicy.id>0).select()
#     for pracownicy in Pracownicy:
#         par.append(pracownicy['Imie'])
#         par.append(pracownicy['Nazwisko'])
#         par.append(pracownicy['NumerIdentyfikacji'])
#         par.append(pracownicy['Stanowisko'])
#         par.append(pracownicy['Miejsce_Pracy'])
#         par.append(pracownicy['Rodzaj_Zatrudnienia'])
#         par.append(pracownicy['Nr_tel_Prywatny'])
#         par.append(pracownicy['Nr_tel_Sluzbowy'])
#     return dict(par=par)

##@auth.requires_membership('Szef')

#Tworzenie Wpisu nie edycja
@auth.requires_login()
def EdycjaPracownicy():
    form = SQLFORM(db.Pracownicy,deletable=False, editable=False, details=False)
    if form.process().accepted:
        response.flash='Zapisano'
        redirect(URL('Pracownicy'))
    return dict(form=form)

@auth.requires_login()
def Oczekujace():
    xyz = db().select(db.auth_user.ALL)
    sprzet = db().select(db.Zamowienie.ALL)
    return dict(sprzet=sprzet,xyz=xyz)
##{{ for abc in auth: }}{{db.executesql('SELECT aut_user.first_name FROM auth_user WHERE ? = ;',(abc.id, new.Wlasciciel))}}

#Wyswietla caly sprzet
def Sprzet():
    wrt = db().select(db.Pracownicy.ALL)
    sprzet = db().select(db.Dodaj_Sprzet.ALL)
    return dict(sprzet=sprzet,wrt=wrt)

@auth.requires_login()
def TwojeZamowienia():
    mee = auth.user_id
    zam = db().select(db.Zamowienie.ALL)
    return dict(zam=zam, mee=mee)

@auth.requires_membership('Administrator')
def OczekujaceZamowienia():
    sprzet = db().select(db.Zamowienie.ALL)
    return dict(sprzet=sprzet)

#Tworzenie Wpisu nie edycja
@auth.requires_login()
def EdycjaSprzet():
    forma = SQLFORM(db.Dodaj_Sprzet)
    if forma.process().accepted:
        redirect(URL('Sprzet'))
        response.flash='Zapisano'
        abc = db.executesql('SELECT auth_user.email FROM auth_user WHERE forma.user_id IN (SELECT auth_user.id FROM auth_user);')
        email = db.auth_user(forma.vars.Wlasciciel).email
        mail.send(to=[abc],
                  subject="Dostales nowy sprzet: %s" % forma.vars.Rodzaj_Sprzetu,
                  message="""
                  <html>
                   <table style="width:600">
                   <tr>
                      <td  align="right"><strong>Rodzaj Sprzetu:</strong></td><td align="left">{}</td>
                   </tr>
                   <tr>
                      <td  align="right"><strong>Model:</strong></td><td align="left">{}</td>
                   </tr>
                   <tr>
                      <td  align="right"><strong>Serial number:</strong></td><td align="left">{}</td>
                   </tr>
                   <tr>
                      <td  align="right"><strong>Lokalizacja:</strong></td><td align="left">{}</td>
                   </tr>
                      <td align="right"><strong>Przekierowanie na strone</strong></td><td align="left"><a href="http://127.0.0.1:8000/Inw/default/Oczekujace"><button>Oczekujace</button></a></td>
                   </table>
                   </html>
                   """.format(forma.vars.Rodzaj_Sprzetu,
                              forma.vars.Model,
                              forma.vars.Nr_Inw,
                              forma.vars.Lokalizacja),
                  )
        redirect(URL('Sprzet'))
    return dict(forma=forma)

@auth.requires_login()
def Zamowienie():
    wrt = SQLFORM(db.Zamowienie)
    if wrt.process().accepted:
        response.flash='Zapisano'
        message=T('Zgloszenie wyslano')
        email = db.auth_user(wrt.vars.Wlasciciel).email
        mail.send(to=["m.mlynarczyk24@gazeta.pl"],
                  subject="Zlozono zapotrzebowanie na nowy sprzet",
                  message="""
                  <html>
                   <table style="width:600">
                   <tr>
                      <td  align="right"><strong>Potrzebny sprzet:</strong></td><td align="left">{}</td>
                   </tr>
                   <tr>
                      <td  align="right"><strong>Ilosc:</strong></td><td align="left">{}</td>
                   </tr>
                   <tr>
                      <td  align="right"><strong>Osoba skladajaca zamowienie:</strong></td><td align="left">{}{}</td>
                   </tr>
                   <tr>
                      <td  align="right"><strong>Dodatkowy opis:</strong></td><td align="left">{}</td>
                   </tr>
                      <td align="right"><strong>Przekierowanie na strone</strong></td><td align="left"><a href="http://127.0.0.1:8000/Inw/default/Oczekujace"><button>Oczekujace</button></a></td>
                   </table>
                   </html>
                   """.format(wrt.vars.Rodzaj_Sprzetu,
                              wrt.vars.Ilosc,
                              db.executesql('SELECT auth_user.first_name FROM auth_user WHERE ? ==auth_user.id;', (me,)),
                              db.executesql('SELECT auth_user.last_name FROM auth_user WHERE ? ==auth_user.id;', (me,)),
                              wrt.vars.Dodatkowy_opis),
                  )
        redirect(URL('index'))
    return dict(wrt=wrt)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

@auth.requires_login()
def DodawanieLicencji():
    ##Dodawnie licencji do bazy danych
    if auth.user.id!=5:
        redirect(URL('index'))
        response.flash = T("Brak uprawnien!")
    wrt = SQLFORM(db.Licencje)
    if wrt.process().accepted:
        response.flash='Zapisano'
        redirect(URL('Licencje'))
    return dict(wrt=wrt)

@auth.requires_login()
def Licencje():
    ##Wyswietlanie stanu licencji:
    if auth.user.id!=5:
        redirect(URL('index'))
        response.flash = T("Brak uprawnien!")
    wrt = db().select(db.Licencje.ALL)
    return dict(wrt=wrt)

@auth.requires_login()
def TwojSprzet():
    ##Wyswietla sprzet przypisany do zalogowanego uzytkownika
    wrt = db().select(db.Dodaj_Sprzet.ALL)
    return dict(wrt=wrt)
