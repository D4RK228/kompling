# KompLing
## KompLing and nothing else
* Это репризиторий для дз :octocat:
* **Котик ушел грустить в другой место, теперь здесь только дз**
import pymorphy2


  text = "Не стоит бояться перемен, чаще всего они случаются в тот момент, когда они необходимы"

  text_split = text.split(" ")



  morph = pymorphy2.MorphAnalyzer()
  for a in text_split:

    parse = morph.parse(a)[0] #метод morph.analyzer возвращает все разборы, с [0] главное

    result = parse.normalized #нормальная форма, не работает без [0] выше

    sklon = parse.inflect({"gent"})

    lex = parse.lexeme

    print("Простой разбор", parse)

    print("Нормализовано: ", result)

    print("Склонение в родительном: ", sklon)

    print("Лексемы: ", lex)

    print("#################")
Это ссылка на оригинал котика: http://edinstvennaya.ua/pictures/article/9315_max.jpg
