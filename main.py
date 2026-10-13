atexit = __import__("atexit")
datetime = __import__("datetime").datetime
os = __import__("os")
ft = __import__("flet")

from entities import Game, MyMapClass
from ui_components import (
    BtnMain,
    CardBlock,
    CheckBlock,
    ColBlock,
    ContBlock,
    InpBox,
    LineBlock,
    ListBlock,
    TxtHead,
)

# Данные для отчета
time_in = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
login_user = "UserName"
file_path = os.path.abspath("report.txt")


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


def main(page: ft.Page):
  page.title = "Проект ООП"
  page.theme_mode = "light"
  page.bgcolor = "white"
  page.vertical_alignment = "center"
  page.horizontal_alignment = "center"

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