import flet as ft


# 10 кастомных компонентов окна
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