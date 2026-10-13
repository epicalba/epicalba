from abc import ABC, abstractmethod
import atexit
from datetime import datetime
import os
import flet as ft

# Данные для отчета
time_in = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
login_user = "UserName"
file_path = os.path.abspath("report.txt")


# Аккуратный и красивый формат отчета при выходе
def save_report_on_exit():
  time_out = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
  report = (
      "+-------------------------------------------------------------+\n"
      "| login    | time_in             | time_out              |\n"
      "+-------------------------------------------------------------+\n"
      f"| {login_user.ljust(8)} | {time_in} | {time_out} |\n"
      "+-------------------------------------------------------------+\n"
  )
  with open(file_path, "w", encoding="utf-8") as f:
    f.write(report)
  print(f"Отчет успешно создан: {file_path}")


atexit.register(save_report_on_exit)


# Свой маппинг вместо dict, строго по методичке[cite: 5]
class MyMapClass:

  def __init__(self):
    self.k_list = []
    self.v_list = []

  def put(self, k, v):
    if k in self.k_list:
      i = self.k_list.index(k)
      self.v_list[i] = v
    else:
      self.k_list.append(k)
      self.v_list.append(v)

  def get(self, k):
    if k in self.k_list:
      i = self.k_list.index(k)
      return self.v_list[i]
    return None

  def __len__(self):
    return len(self.k_list)


# Абстрактный класс[cite: 5]
class ParentEntity(ABC):

  def __init__(self, title):
    self._title = title

  @property
  def title(self):
    return self._title

  @title.setter
  def title(self, val):
    self._title = val

  @abstractmethod
  def info(self):
    pass


# Пользовательский класс со спецметодами, геттерами и сеттерами[cite: 5]
class Game(ParentEntity):

  def __init__(self, title, rating, desc):
    super().__init__(title)
    self._rating = rating
    self._desc = desc

  @property
  def rating(self):
    return self._rating

  @rating.setter
  def rating(self, val):
    self._rating = val

  @property
  def desc(self):
    return self._desc

  @desc.setter
  def desc(self, val):
    self._desc = val

  def info(self):
    return f"{self._title} - Рейтинг: {self._rating}"

  def __str__(self):
    return self._title

  def __repr__(self):
    return f"Game('{self._title}', {self._rating})"

  def __eq__(self, other):
    if not isinstance(other, Game):
      return False
    return self._title == other._title and self._rating == other._rating

  def __lt__(self, other):
    return self._rating < other._rating

  def __len__(self):
    return len(self._title)

  @staticmethod
  def check_rt(r):
    return r > 0


# 10 кастомных компонентов окна[cite: 5]
class TxtHead(ft.Text):

  def __init__(self, val):
    super().__init__(val, size=18, weight="bold", color="black")


class BtnMain(ft.Button):

  def __init__(self, text, func):
    super().__init__(content=ft.Text(text), on_click=func)


class InpBox(ft.TextField):

  def __init__(self, hint):
    super().__init__(
        label=hint, width=280, color="black", label_style={"color": "black"}
    )


class ColBlock(ft.Column):

  def __init__(self, lst):
    super().__init__(
        controls=lst, alignment="center", horizontal_alignment="center"
    )


class RowBlock(ft.Row):

  def __init__(self, lst):
    super().__init__(controls=lst, alignment="center")


class ContBlock(ft.Container):

  def __init__(self, elem):
    super().__init__(content=elem, padding=20, border_radius=10, bgcolor="white")


class CardBlock(ft.Card):

  def __init__(self, elem):
    super().__init__(
        content=ft.Container(content=elem, padding=10), bgcolor="blue_grey_50"
    )


class ListBlock(ft.ListView):

  def __init__(self):
    super().__init__(expand=1, spacing=5, padding=10)


class LineBlock(ft.Divider):

  def __init__(self):
    super().__init__(height=20, thickness=2)


class CheckBlock(ft.Checkbox):

  def __init__(self, txt, fn):
    super().__init__(
        label=txt, value=False, on_change=fn, label_style={"color": "black"}
    )


# Главная функция программы
def main(page: ft.Page):
  page.title = "Проект ООП"
  page.theme_mode = "light"
  page.bgcolor = "white"
  page.vertical_alignment = "center"
  page.horizontal_alignment = "center"

  # 10 объектов в коллекции list[cite: 5]
  games = [
      Game("Cyberpunk 2077", 8.5, "РПГ в открытом мире"),
      Game("Witcher 3", 9.5, "История про ведьмака"),
      Game("GTA V", 9.0, "Криминальный город"),
      Game("Minecraft", 9.2, "Строительство из блоков"),
      Game("Dota 2", 7.8, "Командная моба"),
      Game("CS 2", 7.5, "Шутер"),
      Game("RDR 2", 9.8, "Вестерн про бандитов"),
      Game("Skyrim", 9.1, "Драконы и магия"),
      Game("FIFA 23", 6.5, "Футбол"),
      Game("Portal 2", 9.6, "Головоломки с порталами"),
  ]

  my_map = MyMapClass()
  for g in games:
    my_map.put(g.title, g.desc)

  t1 = TxtHead("Каталог игр")
  inp = InpBox("Введите название игры")
  st = TxtHead("Статус: ждем ввода")

  list_v = ListBlock()

  def show_all(arr):
    list_v.controls.clear()
    for item in arr:
      list_v.controls.append(ft.Text(item.info(), color="black"))
    page.update()

  show_all(games)

  def filter_chk(e):
    if chk.value:
      res = [x for x in games if x.rating >= 9.0]
      show_all(res)
      st.value = "Показаны топ игры"
    else:
      show_all(games)
      st.value = "Весь список"

  chk = CheckBlock("Только топ (9.0+)", filter_chk)

  def find_game(e):
    name = inp.value.strip()
    res_desc = my_map.get(name)
    if res_desc:
      st.value = f"Описание: {res_desc}"
    else:
      st.value = "Игра не найдена"
    page.update()

  btn = BtnMain("Узнать информацию", find_game)

  ui_col = ColBlock(
      [t1, LineBlock(), chk, inp, btn, st, LineBlock(), CardBlock(list_v)]
  )
  page.add(ContBlock(ui_col))


if __name__ == "__main__":
  ft.run(main)