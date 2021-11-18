from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from random import randint
from generate_text import generate


class MyApp(App):

    def __init__(self):
        super().__init__()


        self.map = [

            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]

        ]
        self.lesnik = Button(text="поговорить с лесником")
        self.dom = Button(text="зайти в дом")
        self.drevo = Button(text="осмотреть дерево")
        self.top = Button(text="осмотреть топор")
        self.oz = Button(text="осмотреть озеро")
        self.lesnikn = Label(text="Походу он очень устал, лучше не буду тревожить")
        self.domn = Label(text="Довольно маленький, но уютный")
        self.topn = Label(text="Наверно его потерял лесник")
        self.drevon = Label(text="Очень сильно отражает свет, может источник энергии")
        self.ozn = Label(text="В нём видно параллельное измерение")

        self.glava = Button(text="Поговорить с главой населения")
        self.mudrez = Button(text="Подойти к мудрецу")
        self.dom_sov = Button(text="Осмотреть дом совета местных")
        self.yama = Button(text="Осмотреть яму")
        self.kolodez = Button(text="осмотреть колодец")
        self.glavatext = Label(text="Глава:'я очень занят, не мешай пожалуйста'")
        self.mudreztext = Label(text="Ты должен выбрать свой путь...")
        self.dom_sovtext = Label(text="Довольно старое здание")
        self.yamatext = Label(text="слишком глубокая")
        self.kolodeztext = Label(text="Неужели это святая вода?")

        self.kor_demonov = Button(text="Поговорить с главой демонов")
        self.doch = Button(text="Подойти с дочери короля-демонов")
        self.turma = Button(text="Осмотреть тюрьму местных")
        self.soputch = Button(text="Поговорить с сопутчицей")
        self.vray = Button(text="Осмотреть портал в рай")
        self.kor_demonov_text = Label(text="Ты не смеешь приближаться ко мне")
        self.dochtext = Label(text="Отец мне не разрешает говорить с незнакомцами")
        self.turmatext = Label(text="Слишком страшное место")
        self.soputchtext = Label(text="Нет времени на разговоры, пора за работу...")
        self.vraytext = Label(text="Туда попадают, только искупившие грехи")

        self.kapsula = Button(text="Осмотреть капсулу, чтобы наблюдать за миром будучи духом")
        self.posoch = Button(text="Подобрать посох")
        self.sobranie_ray = Button(text="Узнать в чём дело")
        self.umerznak = Button(text="Поговорить со знакомым")
        self.siyanie = Button(text="Что за сияние?")
        self.kapsulatext = Label(text="Не пойму, как с ней работать")
        self.posochtext = Label(text="Походу его уронил Зевс")
        self.sobranie_raytext = Label(text="Мы не довольны правилами это мира...")
        self.umerznaktext = Label(text="Извини, не хочу говорить")
        self.sianyetext = Label(text="Это аура богов")

        self.gnom = Button(text="Поговорить с гномом")
        self.vagon = Button(text="Посмотреть, что в мешке")
        self.avantur = Button(text="Узнать, что с ним")
        self.slomport = Button(text="Осмотреть портал")
        self.samovar = Button(text="Подойти к самовару")
        self.gnomtext = Label(text="Я слишком занять, подойди позже")
        self.vagontext = Label(text="Хм... Там пусто")
        self.avanturtext = Label(text="Меня предали...")
        self.slomporttext = Label(text="Интересно, что будет если его собрать")
        self.samovartext = Label(text="Такой вкусный чай...")

        self.verticalBox = BoxLayout(orientation='vertical')
        self.location = 0

        self.label2 = Label(text="Выберите локацию:")

        self.label = Label(text="Hello World")

        self.menu_select_1 = Button(text="Лес")
        self.menu_select_1.bind(on_press=self.save_1)

        self.menu_select_2 = Button(text="Деревня")
        self.menu_select_2.bind(on_press=self.save_2)

        self.menu_select_3 = Button(text="Ад")
        self.menu_select_3.bind(on_press=self.save_3)

        self.menu_select_4 = Button(text="Рай")
        self.menu_select_4.bind(on_press=self.save_4)

        self.menu_select_5 = Button(text="Шахта")
        self.menu_select_5.bind(on_press=self.save_5)

        self.generate = Button(text="Сгенерировать")
        self.generate.bind(on_press=self.prt)

    def save_1(self, *args):

        self.location = 1
        print(self.location)

    def save_2(self, *args):

        self.location = 2
        print(self.location)

    def save_3(self, *args):

        self.location = 3
        print(self.location)

    def save_4(self, *args):

        self.location = 4
        print(self.location)

    def save_5(self, *args):

        self.location = 5
        print(self.location)


    def prt(self, *args):

        while True:
            try:
                finish_str = generate(self.location)
            except IndexError:
                continue
            finish_str = finish_str[1].upper() + finish_str[2:-1] + "."
            j = 0
            d = 0
            while d < len(finish_str):
                try:
                    if finish_str[d] == ".":
                        finish_str = finish_str[0:d+2] + finish_str[d+2].upper() + finish_str[d+3:len(finish_str)]
                        print(finish_str)

                except IndexError:
                    None
                if j >= 50 and j <= 100 and finish_str[d] == " ":
                    finish_str = finish_str[0:d] + "\n" + finish_str[d+1:len(finish_str)]
                    j = 0
                j += 1
                d += 1
            if finish_str == "f":
                continue
            else:
                self.label.text = finish_str

                break
        if self.location == 1:
            try:
                
                try:
                    self.verticalBox.remove_widget(self.siyanie)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.lesnikn)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.domn)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.drevon)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.topn)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.ozn)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.glavatext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.mudreztext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.yamatext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.kolodeztext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.dom_sovtext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.soputchtext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.kor_demonov_text)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.dochtext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.turmatext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.vraytext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.sianyetext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.sobranie_raytext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.posochtext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.umerznaktext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.kapsulatext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.vagontext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.gnomtext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.avanturtext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.samovartext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.slomporttext)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.lesnik)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.dom)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.drevo)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.top)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.oz)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.glava)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.mudrez)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.yama)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.kolodez)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.dom_sov)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.soputch)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.kor_demonov)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.doch)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.turma)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.vray)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.sianye)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.sobranie_ray)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.posoch)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.umerznak)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.kapsula)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.vagon)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.gnom)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.avantur)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.samovar)
                except Exception:
                    None
                try:
                    self.verticalBox.remove_widget(self.slomport)
                except Exception:
                    None
                self.verticalBox.remove_widget(self.lesnik)
                self.verticalBox.remove_widget(self.dom)
                self.verticalBox.remove_widget(self.drevo)
                self.verticalBox.remove_widget(self.top)
                self.verticalBox.remove_widget(self.oz)
            except Exception:
                None
            try:
                self.lesnik.bind(on_press=self.lesniks)
                self.verticalBox.add_widget(self.lesnik)
            except Exception:
                None
            
            try:
                self.dom.bind(on_press=self.doms)
                self.verticalBox.add_widget(self.dom)
            except Exception:
                None
            
            try:
                self.drevo.bind(on_press=self.drevos)
                self.verticalBox.add_widget(self.drevo)
            except Exception:
                None
            
            try:
                self.top.bind(on_press=self.tops)
                self.verticalBox.add_widget(self.top)
            except Exception:
                None

            try:
                self.oz.bind(on_press=self.ozs)
                self.verticalBox.add_widget(self.oz)
            except Exception:
                None

        elif self.location == 2:
            try:
                self.verticalBox.remove_widget(self.siyanie)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.lesnikn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.domn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.drevon)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.topn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.ozn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.glavatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.mudreztext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.yamatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kolodeztext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dom_sovtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.soputchtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kor_demonov_text)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dochtext)
            except Exception:
                    None
            try:
                self.verticalBox.remove_widget(self.turmatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vraytext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sianyetext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sobranie_raytext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.posochtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.umerznaktext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kapsulatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vagontext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.gnomtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.avanturtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.samovartext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.slomporttext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.lesnik)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dom)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.drevo)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.top)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.oz)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.glava)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.mudrez)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.yama)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kolodez)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dom_sov)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.soputch)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kor_demonov)
            except Exception:
                    None
            try:
                self.verticalBox.remove_widget(self.doch)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.turma)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vray)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sianye)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sobranie_ray)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.posoch)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.umerznak)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kapsula)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vagon)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.gnom)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.avantur)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.samovar)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.slomport)
            except Exception:
                None
                    
            try:
                self.glava.bind(on_press=self.glavas)
                self.verticalBox.add_widget(self.glava)
            except Exception:
                None
            
            try:
                self.mudrez.bind(on_press=self.mudrezs)
                self.verticalBox.add_widget(self.mudrez)
            except Exception:
                None
            
            try:
                self.dom_sov.bind(on_press=self.dom_sovs)
                self.verticalBox.add_widget(self.dom_sov)
            except Exception:
                None
            
            try:
                self.yama.bind(on_press=self.yamas)
                self.verticalBox.add_widget(self.yama)
            except Exception:
                None

            try:
                self.kolodez.bind(on_press=self.kolodezs)
                self.verticalBox.add_widget(self.kolodez)
            except Exception:
                None
        elif self.location == 3:
            try:
                self.verticalBox.remove_widget(self.siyanie)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.lesnikn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.domn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.drevon)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.topn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.ozn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.glavatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.mudreztext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.yamatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kolodeztext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dom_sovtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.soputchtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kor_demonov_text)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dochtext)
            except Exception:
                    None
            try:
                self.verticalBox.remove_widget(self.turmatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vraytext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sianyetext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sobranie_raytext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.posochtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.umerznaktext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kapsulatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vagontext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.gnomtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.avanturtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.samovartext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.slomporttext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.lesnik)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dom)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.drevo)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.top)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.oz)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.glava)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.mudrez)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.yama)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kolodez)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dom_sov)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.soputch)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kor_demonov)
            except Exception:
                    None
            try:
                self.verticalBox.remove_widget(self.doch)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.turma)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vray)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sianye)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sobranie_ray)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.posoch)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.umerznak)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kapsula)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vagon)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.gnom)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.avantur)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.samovar)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.slomport)
            except Exception:
                None
            try:
                self.kor_demonov.bind(on_press=self.kor_demonovs)
                self.verticalBox.add_widget(self.kor_demonov)
            except Exception:
                None
            
            try:
                self.doch.bind(on_press=self.dochs)
                self.verticalBox.add_widget(self.doch)
            except Exception:
                None
            
            try:
                self.turma.bind(on_press=self.turmas)
                self.verticalBox.add_widget(self.turma)
            except Exception:
                None
            
            try:
                self.soputch.bind(on_press=self.soputchs)
                self.verticalBox.add_widget(self.soputch)
            except Exception:
                None

            self.vray.bind(on_press=self.vrays)
            self.verticalBox.add_widget(self.vray)
        elif self.location == 4:
            try:
                self.verticalBox.remove_widget(self.siyanie)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.lesnikn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.domn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.drevon)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.topn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.ozn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.glavatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.mudreztext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.yamatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kolodeztext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dom_sovtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.soputchtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kor_demonov_text)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dochtext)
            except Exception:
                    None
            try:
                self.verticalBox.remove_widget(self.turmatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vraytext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sianyetext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sobranie_raytext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.posochtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.umerznaktext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kapsulatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vagontext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.gnomtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.avanturtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.samovartext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.slomporttext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.lesnik)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dom)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.drevo)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.top)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.oz)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.glava)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.mudrez)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.yama)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kolodez)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dom_sov)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.soputch)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kor_demonov)
            except Exception:
                    None
            try:
                self.verticalBox.remove_widget(self.doch)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.turma)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vray)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sianye)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sobranie_ray)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.posoch)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.umerznak)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kapsula)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vagon)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.gnom)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.avantur)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.samovar)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.slomport)
            except Exception:
                None
            try:
                self.posoch.bind(on_press=self.posochs)
                self.verticalBox.add_widget(self.posoch)
            except Exception:
                None
            
            try:
                self.siyanie.bind(on_press=self.siyanies)
                self.verticalBox.add_widget(self.siyanie)
            except Exception:
                None
            
            try:
                self.sobranie_ray.bind(on_press=self.sobranie_rays)
                self.verticalBox.add_widget(self.sobranie_ray)
            except Exception:
                None
            
            try:
                self.umerznak.bind(on_press=self.umerznaks)
                self.verticalBox.add_widget(self.umerznak)
            except Exception:
                None
    
            try:
                self.kapsula.bind(on_press=self.kapsulas)
                self.verticalBox.add_widget(self.kapsula)
            except Exception:
                None
        elif self.location == 5:
            try:
                self.verticalBox.remove_widget(self.siyanie)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.lesnikn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.domn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.drevon)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.topn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.ozn)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.glavatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.mudreztext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.yamatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kolodeztext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dom_sovtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.soputchtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kor_demonov_text)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dochtext)
            except Exception:
                    None
            try:
                self.verticalBox.remove_widget(self.turmatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vraytext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sianyetext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sobranie_raytext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.posochtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.umerznaktext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kapsulatext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vagontext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.gnomtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.avanturtext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.samovartext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.slomporttext)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.lesnik)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dom)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.drevo)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.top)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.oz)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.glava)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.mudrez)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.yama)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kolodez)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.dom_sov)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.soputch)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kor_demonov)
            except Exception:
                    None
            try:
                self.verticalBox.remove_widget(self.doch)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.turma)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vray)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sianye)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.sobranie_ray)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.posoch)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.umerznak)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.kapsula)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.vagon)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.gnom)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.avantur)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.samovar)
            except Exception:
                None
            try:
                self.verticalBox.remove_widget(self.slomport)
            except Exception:
                None
            try:
                self.avantur.bind(on_press=self.avanturs)
                self.verticalBox.add_widget(self.avantur)
            except Exception:
                None
            
            try:
                self.gnom.bind(on_press=self.gnoms)
                self.verticalBox.add_widget(self.gnom)
            except Exception:
                None
            
            try:
                self.samovar.bind(on_press=self.samovars)
                self.verticalBox.add_widget(self.samovar)
            except Exception:
                None
            
            try:
                self.slomport.bind(on_press=self.slomports)
                self.verticalBox.add_widget(self.slomport)
            except Exception:
                None
    
            try:
                self.vagon.bind(on_press=self.vagons)
                self.verticalBox.add_widget(self.vagon)
            except Exception:
                None
    def glavas(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.glavatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.mudreztext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.yamatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kolodeztext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.dom_sovtext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.glava)
        self.verticalBox.remove_widget(self.mudrez)
        self.verticalBox.remove_widget(self.dom_sov)
        self.verticalBox.remove_widget(self.yama)
        self.verticalBox.remove_widget(self.kolodez)
        try:
            self.verticalBox.add_widget(self.glava)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.glavatext)
        except Exception:
            None  
        try:
            self.verticalBox.add_widget(self.mudrez)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.dom_sov)
        except Exception:
            None   
        
        try:
            self.verticalBox.add_widget(self.yama)
        except Exception:
            None 
        
        try:
            self.verticalBox.add_widget(self.kolodez)
        except Exception:
            None
    def mudrezs(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.glavatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.mudreztext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.yamatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kolodeztext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.dom_sovtext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.glava)
        self.verticalBox.remove_widget(self.mudrez)
        self.verticalBox.remove_widget(self.dom_sov)
        self.verticalBox.remove_widget(self.yama)
        self.verticalBox.remove_widget(self.kolodez)
        try:
            self.verticalBox.add_widget(self.glava)
        except Exception:
            None
       
        try:
            self.verticalBox.add_widget(self.mudrez)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.mudreztext)
        except Exception:
            None  
        try:
            self.verticalBox.add_widget(self.dom_sov)
        except Exception:
            None   
        
        try:
            self.verticalBox.add_widget(self.yama)
        except Exception:
            None 
        
        try:
            self.verticalBox.add_widget(self.kolodez)
        except Exception:
            None
    def dom_sovs(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.glavatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.mudreztext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.yamatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kolodeztext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.dom_sovtext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.glava)
        self.verticalBox.remove_widget(self.mudrez)
        self.verticalBox.remove_widget(self.dom_sov)
        self.verticalBox.remove_widget(self.yama)
        self.verticalBox.remove_widget(self.kolodez)
        try:
            self.verticalBox.add_widget(self.glava)
        except Exception:
            None
       
        try:
            self.verticalBox.add_widget(self.mudrez)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.dom_sov)
        except Exception:
            None   
        try:
            self.verticalBox.add_widget(self.dom_sovtext)
        except Exception:
            None  
        try:
            self.verticalBox.add_widget(self.yama)
        except Exception:
            None 
        
        try:
            self.verticalBox.add_widget(self.kolodez)
        except Exception:
            None
    def yamas(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.glavatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.mudreztext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.yamatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kolodeztext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.dom_sovtext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.glava)
        self.verticalBox.remove_widget(self.mudrez)
        self.verticalBox.remove_widget(self.dom_sov)
        self.verticalBox.remove_widget(self.yama)
        self.verticalBox.remove_widget(self.kolodez)
        try:
            self.verticalBox.add_widget(self.glava)
        except Exception:
            None
       
        try:
            self.verticalBox.add_widget(self.mudrez)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.dom_sov)
        except Exception:
            None   
        try:
            self.verticalBox.add_widget(self.yama)
        except Exception:
            None 
        try:
            self.verticalBox.add_widget(self.yamatext)
        except Exception:
            None  
        try:
            self.verticalBox.add_widget(self.kolodez)
        except Exception:
            None
        
    def kolodezs(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.glavatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.mudreztext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.yamatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kolodeztext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.dom_sovtext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.glava)
        self.verticalBox.remove_widget(self.mudrez)
        self.verticalBox.remove_widget(self.dom_sov)
        self.verticalBox.remove_widget(self.yama)
        self.verticalBox.remove_widget(self.kolodez)
          
        
        
        try:
            self.verticalBox.add_widget(self.glava)
        except Exception:
            None
       
        try:
            self.verticalBox.add_widget(self.mudrez)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.dom_sov)
        except Exception:
            None   
        try:
            self.verticalBox.add_widget(self.yama)
        except Exception:
            None 
        
        try:
            self.verticalBox.add_widget(self.kolodez)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.kolodeztext)
        except Exception:
            None  
    def dochs(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.soputchtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kor_demonov_text)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.dochtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.turmatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.vraytext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.kor_demonov)
        self.verticalBox.remove_widget(self.soputch)
        self.verticalBox.remove_widget(self.turma)
        self.verticalBox.remove_widget(self.doch)
        self.verticalBox.remove_widget(self.vray)
        try:
            self.verticalBox.add_widget(self.kor_demonov)
        except Exception:
            None    
        
        try:
            self.verticalBox.add_widget(self.soputch)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.turma)
        except Exception:
            None
       
        try:
            self.verticalBox.add_widget(self.doch)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.dochtext)
        except Exception:
            None   
        try:
            self.verticalBox.add_widget(self.vray)
        except Exception:
            None 
    def kor_demonovs(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.soputchtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kor_demonov_text)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.dochtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.turmatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.vraytext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.kor_demonov)
        self.verticalBox.remove_widget(self.soputch)
        self.verticalBox.remove_widget(self.turma)
        self.verticalBox.remove_widget(self.doch)
        self.verticalBox.remove_widget(self.vray)
        try:
            self.verticalBox.add_widget(self.kor_demonov)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.kor_demonov_text)
        except Exception:
            None   
        try:
            self.verticalBox.add_widget(self.soputch)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.turma)
        except Exception:
            None
       
        try:
            self.verticalBox.add_widget(self.doch)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.vray)
        except Exception:
            None 
    def turmas(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.soputchtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kor_demonov_text)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.dochtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.turmatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.vraytext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.kor_demonov)
        self.verticalBox.remove_widget(self.soputch)
        self.verticalBox.remove_widget(self.turma)
        self.verticalBox.remove_widget(self.doch)
        self.verticalBox.remove_widget(self.vray)
        try:
            self.verticalBox.add_widget(self.kor_demonov)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.soputch)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.turma)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.turmatext)
        except Exception:
            None   
        try:
            self.verticalBox.add_widget(self.doch)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.vray)
        except Exception:
            None
        
    def vrays(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.soputchtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kor_demonov_text)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.dochtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.turmatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.vraytext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.kor_demonov)
        self.verticalBox.remove_widget(self.soputch)
        self.verticalBox.remove_widget(self.turma)
        self.verticalBox.remove_widget(self.doch)
        self.verticalBox.remove_widget(self.vray)
        try:
            self.verticalBox.add_widget(self.kor_demonov)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.soputch)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.turma)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.doch)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.vray)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.vraytext)
        except Exception:
            None 
    def soputchs(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.soputchtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kor_demonov_text)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.dochtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.turmatext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.vraytext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.kor_demonov)
        self.verticalBox.remove_widget(self.soputch)
        self.verticalBox.remove_widget(self.turma)
        self.verticalBox.remove_widget(self.doch)
        self.verticalBox.remove_widget(self.vray)
        try:
            self.verticalBox.add_widget(self.kor_demonov)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.soputch)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.soputchtext)
        except Exception:
            None 
        try:
            self.verticalBox.add_widget(self.turma)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.doch)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.vray)
        except Exception:
            None
        
        
    def posochs(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.sianyetext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.sobranie_raytext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.posochtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.umerznaktext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kapsulatext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.posoch)
        self.verticalBox.remove_widget(self.sobranie_ray)
        self.verticalBox.remove_widget(self.siyanie)
        self.verticalBox.remove_widget(self.umerznak)
        self.verticalBox.remove_widget(self.kapsula)
        try:
            self.verticalBox.add_widget(self.posoch)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.posochtext)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.sobranie_ray)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.siyanie)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.umerznak)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.kapsula)
        except Exception:
            None 
        
    def kapsulas(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.sianyetext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.sobranie_raytext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.posochtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.umerznaktext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kapsulatext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.posoch)
        self.verticalBox.remove_widget(self.sobranie_ray)
        self.verticalBox.remove_widget(self.siyanie)
        self.verticalBox.remove_widget(self.umerznak)
        self.verticalBox.remove_widget(self.kapsula)
        try:
            self.verticalBox.add_widget(self.posoch)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.sobranie_ray)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.siyanie)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.umerznak)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.kapsula)
        except Exception:
            None 
        try:
            self.verticalBox.add_widget(self.kapsulatext)
        except Exception:
            None
    def sobranie_rays(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.sianyetext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.sobranie_raytext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.posochtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.umerznaktext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kapsulatext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.posoch)
        self.verticalBox.remove_widget(self.sobranie_ray)
        self.verticalBox.remove_widget(self.siyanie)
        self.verticalBox.remove_widget(self.umerznak)
        self.verticalBox.remove_widget(self.kapsula)
        try:
            self.verticalBox.add_widget(self.posoch)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.sobranie_ray)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.sobranie_raytext)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.siyanie)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.umerznak)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.kapsula)
        except Exception:
            None 
    def umerznaks(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.sianyetext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.sobranie_raytext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.posochtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.umerznaktext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kapsulatext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.posoch)
        self.verticalBox.remove_widget(self.sobranie_ray)
        self.verticalBox.remove_widget(self.siyanie)
        self.verticalBox.remove_widget(self.umerznak)
        self.verticalBox.remove_widget(self.kapsula)
        try:
            self.verticalBox.add_widget(self.posoch)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.sobranie_ray)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.siyanie)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.umerznak)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.umerznaktext)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.kapsula)
        except Exception:
            None 
    def siyanies(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.sianyetext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.sobranie_raytext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.posochtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.umerznaktext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.kapsulatext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.posoch)
        self.verticalBox.remove_widget(self.sobranie_ray)
        self.verticalBox.remove_widget(self.siyanie)
        self.verticalBox.remove_widget(self.umerznak)
        self.verticalBox.remove_widget(self.kapsula)
        try:
            self.verticalBox.add_widget(self.posoch)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.sobranie_ray)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.sianyetext)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.umerznak)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.kapsula)
        except Exception:
            None
        

        
    def gnoms(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.vagontext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.gnomtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.avanturtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.samovartext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.slomporttext)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.gnom)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.gnomtext)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.avantur)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.samovar)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.slomport)
        except Exception:
            None
        

        try:
            self.verticalBox.add_widget(self.vagon)
        except Exception:
            None
    def avanturs(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.vagontext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.gnomtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.avanturtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.samovartext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.slomporttext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.gnom)
        self.verticalBox.remove_widget(self.avantur)
        self.verticalBox.remove_widget(self.samovar)
        self.verticalBox.remove_widget(self.slomport)
        self.verticalBox.remove_widget(self.vagon)
        try:
            self.verticalBox.add_widget(self.gnom)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.avantur)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.avanturtext)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.samovar)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.slomport)
        except Exception:
            None
        

        try:
            self.verticalBox.add_widget(self.vagon)
        except Exception:
            None
    def samovars(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.vagontext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.gnomtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.avanturtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.samovartext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.slomporttext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.gnom)
        self.verticalBox.remove_widget(self.avantur)
        self.verticalBox.remove_widget(self.samovar)
        self.verticalBox.remove_widget(self.slomport)
        self.verticalBox.remove_widget(self.vagon)
        try:
            self.verticalBox.add_widget(self.gnom)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.avantur)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.samovar)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.samovartext)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.slomport)
        except Exception:
            None
        

        try:
            self.verticalBox.add_widget(self.vagon)
        except Exception:
            None
    def slomports(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.vagontext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.gnomtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.avanturtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.samovartext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.slomporttext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.gnom)
        self.verticalBox.remove_widget(self.avantur)
        self.verticalBox.remove_widget(self.samovar)
        self.verticalBox.remove_widget(self.slomport)
        self.verticalBox.remove_widget(self.vagon)
        try:
            self.verticalBox.add_widget(self.gnom)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.avantur)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.samovar)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.slomport)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.slomporttext)
        except Exception:
            None

        try:
            self.verticalBox.add_widget(self.vagon)
        except Exception:
            None
        
    def vagons(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.vagontext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.gnomtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.avanturtext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.samovartext)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.slomporttext)
        except Exception:
            None
        self.verticalBox.remove_widget(self.gnom)
        self.verticalBox.remove_widget(self.avantur)
        self.verticalBox.remove_widget(self.samovar)
        self.verticalBox.remove_widget(self.slomport)
        self.verticalBox.remove_widget(self.vagon)
        try:
            self.verticalBox.add_widget(self.gnom)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.avantur)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.samovar)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.slomport)
        except Exception:
            None

        try:
            self.verticalBox.add_widget(self.vagon)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.vagontext)
        except Exception:
            None
    def lesniks(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.lesnikn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.domn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.drevon)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.topn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.ozn)
        except Exception:
            None
        self.verticalBox.remove_widget(self.lesnik)
        self.verticalBox.remove_widget(self.dom)
        self.verticalBox.remove_widget(self.drevo)
        self.verticalBox.remove_widget(self.top)
        self.verticalBox.remove_widget(self.oz)
        try:
            self.verticalBox.add_widget(self.lesnik)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.lesnikn)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.dom)
        except Exception:
            None
        
        try:
            self.verticalBox.add_widget(self.drevo)
        except Exception:
            None

        try:
            self.verticalBox.add_widget(self.top)
        except Exception:
            None
    def doms(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.lesnikn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.domn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.drevon)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.topn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.ozn)
        except Exception:
            None
        self.verticalBox.remove_widget(self.lesnik)
        self.verticalBox.remove_widget(self.dom)
        self.verticalBox.remove_widget(self.drevo)
        self.verticalBox.remove_widget(self.top)
        self.verticalBox.remove_widget(self.oz)
        try:
            self.verticalBox.add_widget(self.lesnik)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.dom)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.domn)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.drevo)
        except Exception:
            None

        try:
            self.verticalBox.add_widget(self.top)
        except Exception:
            None

    def drevos(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.lesnikn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.domn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.drevon)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.topn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.ozn)
        except Exception:
            None
        self.verticalBox.remove_widget(self.lesnik)
        self.verticalBox.remove_widget(self.dom)
        self.verticalBox.remove_widget(self.drevo)
        self.verticalBox.remove_widget(self.top)
        self.verticalBox.remove_widget(self.oz)
        try:
            self.verticalBox.add_widget(self.lesnik)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.dom)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.drevo)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.drevon)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.top)
        except Exception:
            None

        try:
            self.verticalBox.add_widget(self.oz)
        except Exception:
            None

    def tops(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.lesnikn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.domn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.drevon)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.topn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.ozn)
        except Exception:
            None
        self.verticalBox.remove_widget(self.lesnik)
        self.verticalBox.remove_widget(self.dom)
        self.verticalBox.remove_widget(self.drevo)
        self.verticalBox.remove_widget(self.top)
        self.verticalBox.remove_widget(self.oz)
        try:
            self.verticalBox.add_widget(self.lesnik)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.dom)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.drevo)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.top)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.topn)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.oz)
        except Exception:
            None
        

    def ozs(self, *args):
        try:
            self.verticalBox.remove_widget(self.siyanie)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.lesnikn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.domn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.drevon)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.topn)
        except Exception:
            None
        try:
            self.verticalBox.remove_widget(self.ozn)
        except Exception:
            None
        self.verticalBox.remove_widget(self.lesnik)
        self.verticalBox.remove_widget(self.dom)
        self.verticalBox.remove_widget(self.drevo)
        self.verticalBox.remove_widget(self.top)
        self.verticalBox.remove_widget(self.oz)
        try:
            self.verticalBox.add_widget(self.lesnik)
        except Exception:
            None    
        try:
            self.verticalBox.add_widget(self.dom)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.drevo)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.top)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.oz)
        except Exception:
            None
        try:
            self.verticalBox.add_widget(self.ozn)
        except Exception:
            None
        

     

    ###func_generate
    def generate_map(self, location, instance, *args):
        op = []
        while True:
            try:
                s = 1
                all_i = 0
                allf = 0

                while s < 6:

                    random_x = randint(0, 8)
                    random_y = randint(0, 6)


                    if random_x != 4 and random_y != 3:
                        if random_x == 8 and random_y == 6:

                            if self.map[random_y][random_x] != 0 or self.map[random_y-1][random_x] != 0 or self.map[random_y-1][random_x-1] != 0 or self.map[random_y][random_x-1] != 0:
                                
                                continue

                        elif random_x == 8 and random_y == 0:

                            if self.map[random_y+1][random_x] != 0 or self.map[random_y][random_x] != 0 or self.map[random_y][random_x-1] != 0 or self.map[random_y+1][random_x-1] != 0:
                                
                                continue

                        elif random_x == 0 and random_y == 0:

                            if self.map[random_y+1][random_x] != 0 or self.map[random_y][random_x] != 0 or self.map[random_y+1][random_x+1] != 0 or self.map[random_y][random_x+1] != 0:
                                
                                continue

                        elif random_x == 0 and random_y == 6:

                            if self.map[random_y][random_x] != 0 or self.map[random_y-1][random_x+1] != 0 or self.map[random_y-1][random_x] != 0 or self.map[random_y][random_x+1] != 0:
                            
                                continue
                        elif random_y == 0:

                            if self.map[random_y+1][random_x] != 0 or self.map[random_y][random_x] != 0 or self.map[random_y+1][random_x+1] != 0 or self.map[random_y][random_x-1] != 0 or self.map[random_y+1][random_x-1] != 0 or self.map[random_y][random_x+1] != 0:
                            
                                continue

                        elif random_y == 6:

                            if self.map[random_y][random_x] != 0 or self.map[random_y-1][random_x+1] != 0 or self.map[random_y-1][random_x] != 0 or self.map[random_y-1][random_x-1] != 0 or self.map[random_y][random_x-1] != 0 or self.map[random_y][random_x+1] != 0:
                         
                                continue

                        elif random_x == 0:

                            if self.map[random_y+1][random_x] != 0 or self.map[random_y][random_x] != 0 or self.map[random_y+1][random_x+1] != 0 or self.map[random_y-1][random_x+1] != 0 or self.map[random_y-1][random_x] != 0 or self.map[random_y][random_x+1] != 0:
                            
                                continue

                        elif random_x == 8:

                            if self.map[random_y+1][random_x] != 0 or self.map[random_y][random_x] != 0 or self.map[random_y-1][random_x] != 0 or self.map[random_y-1][random_x-1] != 0 or self.map[random_y][random_x-1] != 0 or self.map[random_y+1][random_x-1] != 0:
                        
                                continue

                        

                        else:

                            if self.map[random_y+1][random_x] != 0 or self.map[random_y][random_x] != 0 or self.map[random_y+1][random_x+1] != 0 or self.map[random_y-1][random_x+1] != 0 or self.map[random_y-1][random_x] != 0 or self.map[random_y-1][random_x-1] != 0 or self.map[random_y][random_x-1] != 0 or self.map[random_y+1][random_x-1] != 0 or self.map[random_y][random_x+1] != 0:

                                continue

                        self.map[random_y][random_x] = s

                        s += 1
                    else:
                        break
                   
                        
                
                for t in self.map:

                    print(t)

            

                Y = 0
                X = 0
                sinonims_ryadom = ["рядком", "рядышком", "около тебя", "поблизости", "близко" "невдали", "вплотную", "вблизи", "подле", "возле", "близехонько", "близешенько", "накоротке", "недалеко", "рядом", "близостно", "по соседству", "невдалеке", "невдалече"]
                sinonims_sprava = ["справа", "по правую руку от тебя", "по правую сторону", "с правой стороны"]
                sinonims_sleva = ["слева", "по левую руку от тебя", "по левую сторону", "с левой стороны"]
                sinonims_speredy = ["спереди", "впереди", "прямо", "на первых рядах"]
                sinonims_szady = ["сзади", "позади", "сзаду", "в тылу", "за спиной", "на задах", "возле спины", "у затылка"]
                sinonims_daleko = ["далеко", "вдалеке", "вдали", "неблизко", "далековато", "далеконько", "на почтительном расстоянии", "далеко-далеко"]
                spawn_str = ["Ты находишься в", "Ты в", "Ты появился в", "Место прибытия"]
                slovar_polochenia = ["", " находится", " располагается", " пребывает", " размещается"]

                Allowed_slovars = []
                prototip_Allowed_slovars = []

                finish_str = ""
                


                if location == 1:
                    

                    rand_spawn_words = spawn_str[randint(0, len(spawn_str)-1)]
                    if rand_spawn_words == "Место прибытия":

                        finish_str += rand_spawn_words+" лес."

                    else:

                        finish_str += rand_spawn_words+" лесу."

                    random_items = []


                    saved = []
                    s = 1
                    while s <= 5:
                        ran = randint(1, 5)
                        if ran not in saved:
                            random_items.append(ran)
                            saved.append(ran)
                            s += 1
                        else:
                            continue

                    saved_slovars = {1: [], 2: [], 3: [], 4: [], 5: []}
                    for u in random_items:
                        for i in range(0, len(self.map)):

                            try:
                                
                                Y = i
                                X = self.map[i].index(u)
                                break
                            except ValueError:
                                None
                            

                        if X > 4:

                            Allowed_slovars.append(sinonims_sprava)
                            prototip_Allowed_slovars.append(sinonims_sprava)

                        elif X < 4:

                            Allowed_slovars.append(sinonims_sleva)
                            prototip_Allowed_slovars.append(sinonims_sleva)

                        if Y > 3:

                            Allowed_slovars.append(sinonims_szady)
                            prototip_Allowed_slovars.append(sinonims_szady)

                        elif Y < 3:

                            Allowed_slovars.append(sinonims_speredy)
                            prototip_Allowed_slovars.append(sinonims_speredy)

                        if X >= 2 and X <= 6 and Y >= 2 and Y <= 4:

                            Allowed_slovars.append(sinonims_ryadom)
                            prototip_Allowed_slovars.append(sinonims_ryadom)

                        else:

                            Allowed_slovars.append(sinonims_daleko)
                            prototip_Allowed_slovars.append(sinonims_daleko)
        
                   
                        rand_num_for_allowed_slovar = randint(0, 3)
                    
                        if rand_num_for_allowed_slovar != 3:

                            del Allowed_slovars[rand_num_for_allowed_slovar]
                        

                    
                        
                        
                        if u == 1:
                            t = False
                            
                            for i in range(1, 6):
                                
                                if i == 1:
                                    continue

                                if saved_slovars[i] == []:
                                    continue

                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                             
                                    if all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]] + " с домиком лесника." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и домик лесника." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с домиком лесника." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    all_i += 1
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " домик лесника."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " домик лесника."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None   
                                    
                            if t == False:
                                print("t")
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None      
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" домик лесника."
                                del slovar_polochenia[ju-1]
                     
                            saved_slovars[1].append(prototip_Allowed_slovars)
                            saved_slovars[1].append(finish_str.index("лесника.")+len("лесника."))  


                        elif u == 2:
                            t = False
                            
                            for i in range(1, 6):
                                
                                t = False
                                if saved_slovars[i] == []:
                                    continue
                                if i == 2:
                                    continue

                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и лесник." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с лесником." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с лесником." + finish_str[saved_slovars[i][1]:len(finish_str)] 
                                    all_i += 1   
                                    t = True
                                    break
                          
                                
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " лесник."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " лесник."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" лесник."
                                del slovar_polochenia[ju-1]
                     
                            saved_slovars[2].append(prototip_Allowed_slovars)
                            try:
                                saved_slovars[2].append(finish_str.index("лесник.")+len("лесник.")) 
                            except ValueError:
                                saved_slovars[2].append(finish_str.index("лесником.")+len("лесником."))

                        elif u == 3:
                            t = False
                            
                            for i in range(1, 6):
                                
                                if i == 3:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и изумрудное дерево." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с изумрудным деревом." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с изумрудным деревом." + finish_str[saved_slovars[i][1]:len(finish_str)]  
                                    all_i += 1      
                                    t = True
                                    break
              
                                

                            
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " изумрудное дерево."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " изумрудное дерево."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None
 

                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" изумрудное дерево."
                                del slovar_polochenia[ju-1]
                        
                            saved_slovars[3].append(prototip_Allowed_slovars)
                            try:
                                saved_slovars[3].append(finish_str.index("дерево.")+ len("дерево."))    
                            except ValueError:
                                saved_slovars[3].append(finish_str.index("деревом.")+ len("деревом."))    

                        elif u == 4:
                            t = False
                            
                            for i in range(1, 6):
                                
                                if i == 4:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и топор лесника." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с топором лесника." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с топором лесника." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    all_i += 1
                                    t = True
                                    break
                            
                                
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " топор лесника."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " топор лесника."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" топор лесника."
                                del slovar_polochenia[ju-1]

                            saved_slovars[4].append(prototip_Allowed_slovars)

                            saved_slovars[4].append(finish_str.index("лесника.")+ len("лесника."))


                        elif u == 5:
                            t = False
                            
                            for i in range(1, 6):
                                
                                if i == 5:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и странное озеро." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " со странным озером." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе со странным озером." + finish_str[saved_slovars[i][1]:len(finish_str)]    
                                    t = True
                                    all_i += 1
                                    break
                           
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " странное озеро."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " странное озеро."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" странное озеро."
                                del slovar_polochenia[ju-1]

                            saved_slovars[5].append(prototip_Allowed_slovars)
                            try:
                                saved_slovars[5].append(finish_str.index("странное озеро.")+ len("странное озеро."))
                            except ValueError:
                                saved_slovars[5].append(finish_str.index("озером.")+ len("озером."))
                        Allowed_slovars = []
                        prototip_Allowed_slovars = []
                    
                    return finish_str

                    
                        

                if location == 2:

                    rand_spawn_words = spawn_str[randint(0, len(spawn_str)-1)]
                    if rand_spawn_words == "Место прибытия":

                        finish_str += rand_spawn_words+" деревня."

                    else:

                        finish_str += rand_spawn_words+" деревне."

                    random_items = []

                    saved = []
                    s = 1
                    while s <= 5:
                        ran = randint(1, 5)
                        if ran not in saved:
                            random_items.append(ran)
                            saved.append(ran)
                            s += 1
                        else:
                            continue

                    saved_slovars = {1: [], 2: [], 3: [], 4: [], 5: []}
                    for u in random_items:
                        for i in range(0, len(self.map)):

                            try:
                                
                                Y = i
                                X = self.map[i].index(u)
                                break
                            except ValueError:
                                None
                        print(X, Y)        

                        if X > 4:

                            Allowed_slovars.append(sinonims_sprava)
                            prototip_Allowed_slovars.append(sinonims_sprava)

                        elif X < 4:

                            Allowed_slovars.append(sinonims_sleva)
                            prototip_Allowed_slovars.append(sinonims_sleva)

                        if Y > 3:

                            Allowed_slovars.append(sinonims_szady)
                            prototip_Allowed_slovars.append(sinonims_szady)

                        elif Y < 3:

                            Allowed_slovars.append(sinonims_speredy)
                            prototip_Allowed_slovars.append(sinonims_speredy)

                        if X >= 2 and X <= 6 and Y >= 2 and Y <= 4:

                            Allowed_slovars.append(sinonims_ryadom)
                            prototip_Allowed_slovars.append(sinonims_ryadom)

                        else:

                            Allowed_slovars.append(sinonims_daleko)
                            prototip_Allowed_slovars.append(sinonims_daleko)
        
                        print(Allowed_slovars)
                        rand_num_for_allowed_slovar = randint(0, 3)
                    
                        if rand_num_for_allowed_slovar != 3:

                            del Allowed_slovars[rand_num_for_allowed_slovar]
                        

                    
                        
                        
                        if u == 1:
                            t = False
                            
                            for i in range(1, 6):
                                
                                if i == 1:
                                    continue

                                if saved_slovars[i] == []:
                                    continue

                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    print("d")
                                    if all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с главой жителей." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и глава жителей." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с главой жителей." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    all_i += 1
                                    t = True
                                    break
                            
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " глава жителей."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " глава жителей."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None   
                            if t == False:
                                print("t")
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None      
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" глава жителей."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[1].append(prototip_Allowed_slovars)
                            saved_slovars[1].append(finish_str.index("жителей.")+len("жителей."))  


                        elif u == 2:
                            t = False
                            
                            for i in range(1, 6):
                                
                                if i == 2:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и центральный дом совета местных." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с центральным домом совета местных." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с центральным домом совета местных." + finish_str[saved_slovars[i][1]:len(finish_str)] 
                                    all_i += 1   
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " житель-мудрец."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " житель-мудрец."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None   
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" центральный дом совета местных."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[2].append(prototip_Allowed_slovars)
                            saved_slovars[2].append(finish_str.index("местных.")+len("местных."))    

                        elif u == 3:
                            t = False
                            
                            for i in range(1, 6):
                                
                                if i == 3:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и житель-мудрец." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с жителем-мудрецом." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с жителем-мудрецом." + finish_str[saved_slovars[i][1]:len(finish_str)]  
                                    all_i += 1      
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " житель-мудрец."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " житель-мудрец."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None   
                            
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" житель-мудрец."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[3].append(prototip_Allowed_slovars)
                            try:
                                saved_slovars[3].append(finish_str.index("житель-мудрец.")+ len("житель-мудрец."))  
                            except ValueError:
                                saved_slovars[3].append(finish_str.index("мудрецом.")+ len("мудрецом."))

                        elif u == 4:
                            t = False
                            
                            for i in range(1, 6):
                                
                                if i == 4:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и волшебный колодец." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с волшебным колодцем." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с волшебным колодцем." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    all_i += 1
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " волшебный колодец."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " волшебный колодец."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None   
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" волшебный колодец."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[4].append(prototip_Allowed_slovars)
                            try:
                                saved_slovars[4].append(finish_str.index("колодец.")+ len("колодец."))
                            except ValueError:
                                saved_slovars[4].append(finish_str.index("колодцем.")+ len("колодцем."))

                        elif u == 5:
                            t = False
                            
                            for i in range(1, 6):
                                
                                if i == 5:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и мистическая бездонная яма." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с мистической бездонной ямой." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с мистической бездонной ямой." + finish_str[saved_slovars[i][1]:len(finish_str)]    
                                    t = True
                                    all_i += 1
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " мистическая бездонная яма."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " мистическая бездонная яма."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None   
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" мистическая бездонная яма."
                                del slovar_polochenia[ju-1]
                                print(finish_str)
                            saved_slovars[5].append(prototip_Allowed_slovars)
                            try:
                                saved_slovars[5].append(finish_str.index("яма.")+ len("яма."))
                            except ValueError:
                                saved_slovars[5].append(finish_str.index("ямой.")+ len("ямой."))
                        Allowed_slovars = []
                        prototip_Allowed_slovars = []

                    j = 0
                    
                    return finish_str

                if location == 3:

                    rand_spawn_words = spawn_str[randint(0, len(spawn_str)-1)]
                    if rand_spawn_words == "Место прибытия":

                        finish_str += rand_spawn_words+" ад."

                    else:

                        finish_str += rand_spawn_words+" аду."

                    random_items = []

                    saved = []
                    s = 1
                    while s <= 5:
                        ran = randint(1, 5)
                        if ran not in saved:
                            random_items.append(ran)
                            saved.append(ran)
                            s += 1
                        else:
                            continue

                    saved_slovars = {1: [], 2: [], 3: [], 4: [], 5: []}
                    for u in random_items:
                        for i in range(0, len(self.map)):

                            try:
                                
                                Y = i
                                X = self.map[i].index(u)
                                break
                            except ValueError:
                                None
                        print(X, Y)        

                        if X > 4:

                            Allowed_slovars.append(sinonims_sprava)
                            prototip_Allowed_slovars.append(sinonims_sprava)

                        elif X < 4:

                            Allowed_slovars.append(sinonims_sleva)
                            prototip_Allowed_slovars.append(sinonims_sleva)

                        if Y > 3:

                            Allowed_slovars.append(sinonims_szady)
                            prototip_Allowed_slovars.append(sinonims_szady)

                        elif Y < 3:

                            Allowed_slovars.append(sinonims_speredy)
                            prototip_Allowed_slovars.append(sinonims_speredy)

                        if X >= 2 and X <= 6 and Y >= 2 and Y <= 4:

                            Allowed_slovars.append(sinonims_ryadom)
                            prototip_Allowed_slovars.append(sinonims_ryadom)

                        else:

                            Allowed_slovars.append(sinonims_daleko)
                            prototip_Allowed_slovars.append(sinonims_daleko)
        
                        print(Allowed_slovars)
                        rand_num_for_allowed_slovar = randint(0, 3)
                    
                        if rand_num_for_allowed_slovar != 3:

                            del Allowed_slovars[rand_num_for_allowed_slovar]
                        

                    
                        
                        
                        if u == 1:
                            t = False
                            
                            for i in range(1, 6):
                                
                                if i == 1:
                                    continue

                                if saved_slovars[i] == []:
                                    continue

                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    print("d")
                                    if all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с неизвестной сопутчицей." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и неизвестная сопутчица." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с неизвестной сопутчицей." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    all_i += 1
                                    t = True
                                    break

                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " неизвестная сопутчица."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " неизвестная сопутчица."
                                                allf += 1
                                                t = True
                                                break    
                                except IndexError:
                                    None  
                            if t == False:
                                print("t")
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None      
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" неизвестная сопутчица."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[1].append(prototip_Allowed_slovars)
                            try:
                                saved_slovars[1].append(finish_str.index("сопутчица.")+len("сопутчица."))  
                            except ValueError:
                                saved_slovars[1].append(finish_str.index("сопутчицей.")+len("сопутчицей."))  

                        elif u == 2:
                            t = False
                            
                            for i in range(1, 6):
                               
                                if i == 2:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и главный демон." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с главным демоном." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с главным демоном." + finish_str[saved_slovars[i][1]:len(finish_str)] 
                                    all_i += 1   
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " главный демое."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " главный демон."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None  
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" главный демон."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[2].append(prototip_Allowed_slovars)
                            try:
                                saved_slovars[2].append(finish_str.index("демон.")+len("демон."))  
                            except ValueError:
                                saved_slovars[2].append(finish_str.index("демоном.")+len("демоном."))      

                        elif u == 3:

                            t = False
                            for i in range(1, 6):
                                
                                if i == 3:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и тюрьма грешников." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с тюрьмой грешников." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с тюрьмой грешников." + finish_str[saved_slovars[i][1]:len(finish_str)]  
                                    all_i += 1      
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " тюрьма грешников."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " тюрьма грешников."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None  

                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" тюрьма грешников."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[3].append(prototip_Allowed_slovars)
                            saved_slovars[3].append(finish_str.index("грешников.")+ len("грешников."))    

                        elif u == 4:

                            t = False
                            for i in range(1, 6):
                               
                                if i == 4:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и дочь демона короля." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с дочерью демона короля." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с дочерью демона короля." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    all_i += 1
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " дочь короля демонов."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " дочь короля демонов."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None  
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" дочь демона короля."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[4].append(prototip_Allowed_slovars)
                            saved_slovars[4].append(finish_str.index("короля.")+ len("короля."))

                        elif u == 5:

                            t = False
                            for i in range(1, 6):
                                
                                if i == 5:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и портал в рай." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с порталом в рай." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с порталом в рай." + finish_str[saved_slovars[i][1]:len(finish_str)]    
                                    t = True
                                    all_i += 1
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " портал в рай."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " портал в рай."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None  
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" портал в рай."
                                del slovar_polochenia[ju-1]
                                print(finish_str)
                            saved_slovars[5].append(prototip_Allowed_slovars)
                            saved_slovars[5].append(finish_str.index("рай.")+ len("рай."))
                        Allowed_slovars = []
                        prototip_Allowed_slovars = []

                    
                    return finish_str

                if location == 4:

                    rand_spawn_words = spawn_str[randint(0, len(spawn_str)-1)]
                    if rand_spawn_words == "Место прибытия":

                        finish_str += rand_spawn_words+" рай."

                    else:

                        finish_str += rand_spawn_words+" раю."

                    random_items = []

                    saved = []
                    s = 1
                    while s <= 5:
                        ran = randint(1, 5)
                        if ran not in saved:
                            random_items.append(ran)
                            saved.append(ran)
                            s += 1
                        else:
                            continue

                    saved_slovars = {1: [], 2: [], 3: [], 4: [], 5: []}
                    for u in random_items:
                        for i in range(0, len(self.map)):

                            try:
                                
                                Y = i
                                X = self.map[i].index(u)
                                break
                            except ValueError:
                                None
                        print(X, Y)        

                        if X > 4:

                            Allowed_slovars.append(sinonims_sprava)
                            prototip_Allowed_slovars.append(sinonims_sprava)

                        elif X < 4:

                            Allowed_slovars.append(sinonims_sleva)
                            prototip_Allowed_slovars.append(sinonims_sleva)

                        if Y > 3:

                            Allowed_slovars.append(sinonims_szady)
                            prototip_Allowed_slovars.append(sinonims_szady)

                        elif Y < 3:

                            Allowed_slovars.append(sinonims_speredy)
                            prototip_Allowed_slovars.append(sinonims_speredy)

                        if X >= 2 and X <= 6 and Y >= 2 and Y <= 4:

                            Allowed_slovars.append(sinonims_ryadom)
                            prototip_Allowed_slovars.append(sinonims_ryadom)

                        else:

                            Allowed_slovars.append(sinonims_daleko)
                            prototip_Allowed_slovars.append(sinonims_daleko)
        
                        print(Allowed_slovars)
                        rand_num_for_allowed_slovar = randint(0, 3)
                    
                        if rand_num_for_allowed_slovar != 3:

                            del Allowed_slovars[rand_num_for_allowed_slovar]
                        

                    
                        
                        
                        if u == 1:

                            t = False
                            for i in range(1, 6):
                                
                                if i == 1:
                                    continue

                                if saved_slovars[i] == []:
                                    continue

                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    print("d")
                                    if all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с капсулой, чтобы наблюдать за миром будучи духом." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и капсула, чтобы наблюдать за миром будучи духом." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с капсулой, чтобы наблюдать за миром будучи духом." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    all_i += 1
                                    t = True
                                    break
                                    
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " капсула, чтобы наблюдать за миром будучи духом."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " капсула, чтобы наблюдать за миром будучи духом."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None 
                            if t == False:
                                print("t")
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None      
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" капсула, чтобы наблюдать за миром будучи духом."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[1].append(prototip_Allowed_slovars)
                            saved_slovars[1].append(finish_str.index("духом.")+len("духом."))  


                        elif u == 2:
                            
                            t = False
                            for i in range(1, 6):
                                
                                if i == 2:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и посох зевса." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с посохом зевса." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с посохом зевса." + finish_str[saved_slovars[i][1]:len(finish_str)] 
                                    all_i += 1   
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " посох зевса."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " посох зевса."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None 
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" посох зевса."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[2].append(prototip_Allowed_slovars)
                            saved_slovars[2].append(finish_str.index("зевса.")+len("зевса."))    

                        elif u == 3:
                            t  = False
                            
                            for i in range(1, 6):
                               
                                if i == 3:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и собрание жителей рая." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с собранием жителей рая." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с собранием жителей рая." + finish_str[saved_slovars[i][1]:len(finish_str)]  
                                    all_i += 1      
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " собрание жителей рая."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " собрание жителей рая."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None 
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" собрание жителей рая."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[3].append(prototip_Allowed_slovars)
                            saved_slovars[3].append(finish_str.index("рая.")+ len("рая."))    

                        elif u == 4:

                            t = False
                            for i in range(1, 6):
                                
                                if i == 4:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и умерший знакомый." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с умершим знакомым." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с умершим знакомым." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    all_i += 1
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " умерший знакомый."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " умерший знакомый."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None 
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" умерший знакомый."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[4].append(prototip_Allowed_slovars)
                            try:
                                saved_slovars[4].append(finish_str.index("знакомый.")+ len("знакомый."))
                            except ValueError:
                                saved_slovars[4].append(finish_str.index("знакомым.")+ len("знакомым."))

                        elif u == 5:

                            t = False
                            for i in range(1, 6):
                                
                                if i == 5:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и странное сияние сверху." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " со странным сиянием сверху." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе со странным сиянием сверху." + finish_str[saved_slovars[i][1]:len(finish_str)]    
                                    t = True
                                    all_i += 1
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " странное сияние сверху."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " странное сияние сверху."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None 
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" странное сияние сверху."
                                del slovar_polochenia[ju-1]
                                print(finish_str)
                            saved_slovars[5].append(prototip_Allowed_slovars)
                            saved_slovars[5].append(finish_str.index("сверху.")+ len("сверху."))
                        Allowed_slovars = []
                        prototip_Allowed_slovars = []

                    
                    return finish_str

                if location == 5:

                    rand_spawn_words = spawn_str[randint(0, len(spawn_str)-1)]
                    if rand_spawn_words == "Место прибытия":

                        finish_str += rand_spawn_words+" шахта."

                    else:

                        finish_str += rand_spawn_words+" шахте."

                    random_items = []

                    saved = []
                    s = 1
                    while s <= 5:
                        ran = randint(1, 5)
                        if ran not in saved:
                            random_items.append(ran)
                            saved.append(ran)
                            s += 1
                        else:
                            continue

                    saved_slovars = {1: [], 2: [], 3: [], 4: [], 5: []}
                    for u in random_items:
                        for i in range(0, len(self.map)):

                            try:
                                
                                Y = i
                                X = self.map[i].index(u)
                                break
                            except ValueError:
                                None
                        print(X, Y)        

                        if X > 4:

                            Allowed_slovars.append(sinonims_sprava)
                            prototip_Allowed_slovars.append(sinonims_sprava)

                        elif X < 4:

                            Allowed_slovars.append(sinonims_sleva)
                            prototip_Allowed_slovars.append(sinonims_sleva)

                        if Y > 3:

                            Allowed_slovars.append(sinonims_szady)
                            prototip_Allowed_slovars.append(sinonims_szady)

                        elif Y < 3:

                            Allowed_slovars.append(sinonims_speredy)
                            prototip_Allowed_slovars.append(sinonims_speredy)

                        if X >= 2 and X <= 6 and Y >= 2 and Y <= 4:

                            Allowed_slovars.append(sinonims_ryadom)
                            prototip_Allowed_slovars.append(sinonims_ryadom)

                        else:

                            Allowed_slovars.append(sinonims_daleko)
                            prototip_Allowed_slovars.append(sinonims_daleko)
        
                        print(Allowed_slovars)
                        rand_num_for_allowed_slovar = randint(0, 3)
                    
                        if rand_num_for_allowed_slovar != 3:

                            del Allowed_slovars[rand_num_for_allowed_slovar]
                        

                    
                        
                        
                        if u == 1:

                            t = False
                            for i in range(1, 6):
                                
                                if i == 1:
                                    continue

                                if saved_slovars[i] == []:
                                    continue

                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    print("d")
                                    if all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с главным гномом шахтёром." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и главный гном шахтёр." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с главным гномом шахтёром." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    all_i += 1
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " главный гном шахтёр."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " главный гном шахтёр."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None 
                                    
                            if t == False:
                                print("t")
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None      
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" главный гном шахтёр."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[1].append(prototip_Allowed_slovars)
                            try:
                                saved_slovars[1].append(finish_str.index("шахтёр.")+len("шахтёр."))
                            except ValueError:  
                                saved_slovars[1].append(finish_str.index("шахтёром.")+len("шахтёром."))

                        elif u == 2:
                            
                            t = False
                            for i in range(1, 6):
                                
                                if i == 2:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и вагонетка с фиолетовым мешком." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с вагонеткой с фиолетовым мешком." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с вагонеткой с фиолетовым мешком." + finish_str[saved_slovars[i][1]:len(finish_str)] 
                                    all_i += 1   
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " вагонетка с фиолетовым мешком."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " вагонетка с фиолетовым мешком."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None 
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" вагонетка с фиолетовым мешком."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[2].append(prototip_Allowed_slovars)
                            saved_slovars[2].append(finish_str.index("с фиолетовым мешком.")+len("с фиолетовым мешком."))    

                        elif u == 3:

                            t = False
                            for i in range(1, 6):
                               
                                if i == 3:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и брошенный авантюрист." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с брошенным авантюристом." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с брошенным авантюристом." + finish_str[saved_slovars[i][1]:len(finish_str)]  
                                    all_i += 1      
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " брошенный авантюрист."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " брошенный авантюрист."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None 
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" брошенный авантюрист."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[3].append(prototip_Allowed_slovars)
                            try:

                                saved_slovars[3].append(finish_str.index("авантюрист.")+ len("авантюрист."))    
                            except ValueError:
                                saved_slovars[3].append(finish_str.index("авантюристом.")+ len("авантюристом."))    

                        elif u == 4:

                            t = False
                            for i in range(1, 6):
                                
                                if i == 4:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и сломанный портал." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " со сломанным порталом." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе со сломанным порталом." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    all_i += 1
                                    t = True
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " сломанный портал."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " сломанный портал."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None 
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" сломанный портал."
                                del slovar_polochenia[ju-1]
                            print(finish_str)
                            saved_slovars[4].append(prototip_Allowed_slovars)
                            try:

                                saved_slovars[4].append(finish_str.index("портал.")+ len("портал."))
                            except:
                                saved_slovars[4].append(finish_str.index("порталом.")+ len("порталом."))    

                        elif u == 5:

                            t = False
                            for i in range(1, 6):
                                
                                if i == 5:
                                    continue

                                if saved_slovars[i] == []:
                                    continue
                                o = 0
                                for m in saved_slovars[i][0]:
                                    
                                    if m not in prototip_Allowed_slovars:

                                        t = False
                                        break
                                    else:
                                        o += 1
                                if o == len(prototip_Allowed_slovars):
                                    if all_i == 0:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " и самовар." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 1:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " с самоваром." + finish_str[saved_slovars[i][1]:len(finish_str)]
                                    elif all_i == 2:
                                        finish_str = finish_str[0:saved_slovars[i][1]-1] + " вместе с самоваром." + finish_str[saved_slovars[i][1]:len(finish_str)]    
                                    t = True
                                    all_i += 1
                                    break
                                try:
                                    if "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "справа" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "справа" in prototip_Allowed_slovars[0] or "справа" in prototip_Allowed_slovars[1] or "справа" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " самовар."
                                                allf += 1
                                                t = True
                                                break
            
                                    elif "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][0] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][1] or "слева" in saved_slovars[random_items[random_items.index(u)-1]][0][2]:
                                        if "слева" in prototip_Allowed_slovars[0] or "слева" in prototip_Allowed_slovars[1] or "слева" in prototip_Allowed_slovars[2] and allf == 0 and t == False:
                                            storon = ["в том же направлении", "в этом же направлении", "в таком же направлении", "в той же стороне"]
                                            if storon[0] not in finish_str and storon[1] not in finish_str and storon[2] not in finish_str and storon[3] not in finish_str:
                                                finish_str += " " + storon[randint(0, len(storon)-1)] + ", но " + ["ближе", "поближе", "на меньшем расстоянии"][randint(0, 2)] + " самовар."
                                                allf += 1
                                                t = True
                                                break
                                except IndexError:
                                    None 
                            if t == False:
                                used_words = []
                                for i in Allowed_slovars:
                                    ke = randint(0, len(i)-1)
                                    finish_str += " "+i[ke]
                                    used_words.append(i[ke])
                                for x in used_words:
                                    try:
                                        del sinonims_daleko[sinonims_daleko.index(x)]
                                    except ValueError:
                                        None

                                    try:
                                        del sinonims_ryadom[sinonims_ryadom.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sleva[sinonims_sleva.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_speredy[sinonims_speredy.index(x)]
                                    except ValueError:
                                        None    

                                    try:
                                        del sinonims_sprava[sinonims_sprava.index(x)]
                                    except ValueError:
                                        None      

                                    try:
                                        del sinonims_szady[sinonims_szady.index(x)]
                                    except ValueError:
                                        None  
                                    
                                ju = randint(0, len(slovar_polochenia))
                                finish_str += slovar_polochenia[ju-1]+" самовар."
                                del slovar_polochenia[ju-1]
                                print(finish_str)
                            saved_slovars[5].append(prototip_Allowed_slovars)
                            try:
                                saved_slovars[5].append(finish_str.index("самовар.")+ len("самовар."))
                            except ValueError:
                                saved_slovars[5].append(finish_str.index("самоваром.")+ len("самоваром."))

                        Allowed_slovars = []
                        prototip_Allowed_slovars = []
                    
                    return finish_str
                break
            except ValueError:
                print("f")
                return "f"
               
            
        self.map = [

            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]

        ]
    #ef rotate(self):


    def build(self):
        
        superBoxB = BoxLayout(orientation='horizontal')

        box_rot = BoxLayout(orientation="horizontal")
        
        but_rot = Button(text="поменять местами")

        box_rot.add_widget(but_rot)
        
        
        superBox = BoxLayout(orientation='horizontal')



        box = BoxLayout(orientation='vertical')
        box.size_hint = (0.5, 1)
        box.pos = (1, 1)

        box.add_widget(self.label2)
        box.add_widget(self.menu_select_1)
        box.add_widget(self.menu_select_2)
        box.add_widget(self.menu_select_3)
        box.add_widget(self.menu_select_4)
        box.add_widget(self.menu_select_5)
        box.add_widget(self.generate)

        

        verb = BoxLayout(orientation="vertical")

        verb.add_widget(self.label)
        bx = BoxLayout(orientation="vertical")
        bx.add_widget(verb)
        bx.add_widget(self.verticalBox)

        superBox.add_widget(bx)

        superBox.add_widget(box)


        return superBox
        

        

if __name__ == "__main__":
    MyApp().run()

#лес, деревня, ад, рай, шахта