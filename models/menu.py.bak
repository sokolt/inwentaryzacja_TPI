# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B("Inwentaryzacja Calanabau TPI"),
                  _class="navbar-brand",_href='index',
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################
##(T('STRONA GLOWNA'), False, URL('default', 'index'),[



# response.menu = [
#                 (T('STRONA GLOWNA'), False, URL('default','index'),[
#                  (T('Pracownicy'), False, URL('default','indexx'),[
#                     (T('Dodaj pracownika'), False, URL('default','EdycjaPracownicy')),
#                     (T('Zatrudnieni pracownicy'), False, URL('default','Pracownicy'))]),
#                  (T('Sprzet'), False, URL('default','indexxx'),[
#                     (T('Dodaj sprzet'), False, URL('default','EdycjaSprzet')),
#                     (T('Aktualny sprzet'), False, URL('default','Sprzet')),
#                     (T('Zapotrzebowanie na sprzet'), False, URL('default','Zamowienie'))])])]

response.menu = [
                (T('PRACOWNICY'), False, URL('default','indexx'),[
                    (T('Dodaj pracownika'), False, URL('default','EdycjaPracownicy')),
                    (T('Zatrudnieni pracownicy'), False, URL('default','Pracownicy'))]),
                (T('SPRZET'), False, URL('default','indexxx'),[
                    (T('Dodaj sprzet'), False, URL('default','EdycjaSprzet')),
                    (T('Aktualny sprzet'), False, URL('default','Sprzet')),
                    (T('Twoj sprzet'), False, URL('default','TwojSprzet')),
                    (T('Zapotrzebowanie na sprzet'), False, URL('default','Zamowienie')),
                    (T('Twoje Zamowienia'),False, URL('default','TwojeZamowienia')),
                    (T('Licencje'),False, URL('default','Licencje')),
                    (T('Dodawanie licencji'), False, URL('default','DodawanieLicencji'))])]
