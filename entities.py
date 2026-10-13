from abc import ABC, abstractmethod


# Свой маппинг вместо dict
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


# Абстрактный класс
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


# Пользовательский класс со спецметодами, геттерами и сеттерами
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