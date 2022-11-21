from main_program import *
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
Builder.load_file('my.kv')
zmiana_liter()

def wybrana_lista(interupt_glowny):

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
        theapp.secscreen.ids.ti_wynik_glowny.text = str('\n\n'.join(map(str, newlist)))
        print("\n")

        #except:
        print("Brak, podaj podaj poprawną wartość")
    print("KONIEC")




def wynik_komplemanatrny():

    if newlist:
        interupt = "coś czego nie ma"

        while interupt != "":
            print("podaj komplementarna")
            interupt = input().lower()
            r = re.compile(".*" + interupt)
            if interupt != "":
                print("\n")
                newlist2 = list(filter(r.match, szukaj2))  # Read Note below
                print(*newlist2, sep='\n')
                print("\n")
                if not newlist2:
                    print("Brak,podaj poprawną warotść")

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
                    Popup(size_hint=(None,None), size=(400,200), title="BŁĄD", auto_dismiss=True, content=show).open()
                    theapp.fscreen.ids.in_first.text = "nie ma"
                    theapp.screenm.current = 'first'
                theapp.fscreen.ids.in_first.text = ""

            except:
                theapp.fscreen.ids.in_first.text = ""
                Popup(size_hint=(None, None), size=(400, 200), title="BŁĄD", auto_dismiss=True,
                      content=show).open()
                theapp.screenm.current = 'first'


    def change_color(self):
        theapp.stop()



class secscreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change(self):
        theapp.screenm.current = 'first'

    def change_color(self):
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
