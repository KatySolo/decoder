Дешифратор произвольной перестановочной шифровки
Автор: Katy Solo (Солодовникова Екатерина)

Описание:
Данный дешифратор на вход получает имя директории, в которой лежит текстовый файл с именем input,
содержащий зашифрованный текст,а также имя директории, содержащую текстовые файлы с базовыми словами,
на основе которых будет строиться словарь.
Ны выходе в директории output создается фаил output.txt, содержащий расшифрованный текст.
Программа реализована в двух форматах: консольный и оконный.

Схема работы:
Текст поступает из файла output.txt
"Привет! Я - Катя!"
|
V
Текст разбивается на слова и распределяется в словарь где ключ - длина слова
{1:{"Я"},4:{"Катя"},"6:{"Привет"}}
|
V
Кадому слову в соответсвие ставится маска, формирующаяся
по принципу встречалась ли буква в слове уже или нет.
Все буквы имеют сквозную нумерацию и если буква уже встречалась ранее, то в маске она заменяется
на номер ранее
|
V
{1:{"Я":"0"},4:{"Катя":"0123"},"6:{"Приветик":01234526}}
|
V
Выбирается некоторое достаточно большое колличество слов из словаря базовых слов
и формируется аналогичный предыдущему словарь


Используемые технологии:
Unit-тестирование
TKinter для оконной версии приложения
argparser для консольной версии приложения

