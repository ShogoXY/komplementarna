from main_program import *
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window


Window.softinput_mode="below_target"


Builder.load_file('my.kv')
zmiana_liter()

def wybrana_lista(interupt_glowny):
    global lista_nowa2
    print("podaj glowny")
    interupt_glowny = str(theapp.fscreen.ids.in_first.text)
    lista_nowa = list(
        (bol_g, wlosy_g, grypa_odpornosc_g, opryszczka_masc_g, opryszcza_odpornosc_g, nogi_g,
         hemoroidy_masc_g, hemoroidy_czopki_g, furagina_zurawina_g, alergia_calcium_g,
         alergia_inne_g, antybiotyk_g, biegunka_elektrolity_g))
    lista_nowa2 = list(
        (bol_k, wlosy_k, grypa_odpornosc_k, opryszczka_masc_k, opryszcza_odpornosc_k, nogi_k,
         hemoroidy_masc_k, hemoroidy_czopki_k, furagina_zurawina_k, alergia_calcium_k,
         alergia_inne_k, antybiotyk_k, biegunka_elektrolity_k))
    global i
    i = 0
    l = 0

    if interupt_glowny != "":
        while l == 0:
            global szukaj2
            szukaj = lista_nowa[i]
            szukaj2 = lista_nowa2[i]
            r = re.compile(".*" + interupt_glowny)

            new = list(filter(r.match, szukaj))  # Read Note belo
            l = len(new)
            i = i + 1

        print("\n")
        # print(szukaj)
        global newlist
        newlist = list(filter(r.match, szukaj))  # Read Note below
        gotowe=print(*newlist, sep='\n')
        print(gotowe)
        theapp.secscreen.ids.lb_wynik_glowny.text = str('\n\n'.join(map(str, newlist)))
        print("\n")

        #except:
        print("Brak, podaj podaj poprawną wartość")
    print("KONIEC")




def wynik_komplemanatrny(interupt):

    if newlist:
        
        # print("to jest I ",i, "to jest szukaj2 ", szukaj2)
        # if interupt != "":
        print("podaj komplementarna")
        interupt = theapp.secscreen.ids.ti_komplementarna.text
        r = re.compile(".*" + interupt)
        if interupt != "":
            print("\n")
            newlist2 = list(filter(r.match, szukaj2))  # Read Note below
            print(*newlist2, sep='\n')
            theapp.secscreen.ids.lb_komplementarna.text = str('\n\n'.join(map(str, newlist2)))
            print("\n")
            if not newlist2:
                theapp.secscreen.ids.ti_komplementarna.text = ""
                Popup(size_hint=(None, None), size=(500, 600), title="BŁĄD", auto_dismiss=True,
                      content=show).open()

class P(FloatLayout):
    pass


class fscreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def change(self):
        show=P()
        if True:

            try:
                wybrana_lista(theapp.fscreen.ids.in_first.text)
                theapp.screenm.current = 'second'
                if theapp.fscreen.ids.in_first.text == "":
                    Popup(size_hint=(None,None), size=(500,600), title="BŁĄD", auto_dismiss=True, content=show).open()
                    theapp.fscreen.ids.in_first.text = "nie ma"
                    theapp.screenm.current = 'first'
                theapp.fscreen.ids.in_first.text = ""

            except:
                theapp.fscreen.ids.in_first.text = ""
                Popup(size_hint=(None, None), size=(500, 600), title="BŁĄD", auto_dismiss=True,
                      content=show).open()
                theapp.screenm.current = 'first'


    

    def exit(self):
        theapp.stop()


class secscreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change(self):
        theapp.screenm.current = 'first'

    def change_color(self):
        # theapp.stop()
        show=P()
        if True:

            try:
                wynik_komplemanatrny(theapp.secscreen.ids.ti_komplementarna.text)
                if theapp.secscreen.ids.ti_komplementarna.text == "":
                    Popup(size_hint=(None,None), size=(500,600), title="BŁĄD", auto_dismiss=True, content=show).open()
                    theapp.secscreen.ids.ti_komplementarna.text = "nie ma"
                    # theapp.screenm.current = 'second'
                theapp.secscreen.ids.ti_komplementarna.text = ""

            except:
                theapp.secscreen.ids.ti_komplementarna.text = ""
                Popup(size_hint=(None, None), size=(500, 600), title="BŁĄD", auto_dismiss=True,
                      content=show).open()
                # theapp.screenm.current = 'first'
    def exit(self):
        theapp.stop()


class theapp(App):
    def build(self):
        self.screenm = ScreenManager()
        self.fscreen = fscreen()
        screen = Screen(name="first")
        screen.add_widget(self.fscreen)
        self.screenm.add_widget(screen)

        self.secscreen = secscreen()
        screen = Screen(name="second")
        screen.add_widget(self.secscreen)
        self.screenm.add_widget(screen)

        return self.screenm


if __name__ == "__main__":
    theapp = theapp()
    theapp.run()
