# yandexTest
Задания, которые опубликованы https://habr.com/ru/post/353662/
Задача 1. Ошибка

Условия задания

Вы обслуживаете сайт и отслеживаете возникающие проблемы. Клиент получил ошибку после того, как попытался добавить свой пост в систему. Вы хотите понять на каком из серверов эта ошибка произошла.

Есть n серверов, на i-й из них приходится ai процентов запросов, из которых bi процентов завершаются с ошибкой. Для каждого сервера найдите вероятность того, что ошибка произошла именно на нём.

Формат ввода

В первой строке входного файла содержится одно целое число n (1 ≤n≤ 100) — количество серверов.

В каждой из следующих n строк содержится два целых числа ai bi (0 ≤ ai, bi ≤ 100) — вероятность того что запрос пойдет на i-й сервер в процентах и вероятность того что на i-м сервере случится ошибка в процентах.

Гарантируется, что сумма всех ai равна 100 и ошибка в системе может произойти.

Формат вывода

Выведите n строк. В каждой строке должно находиться одно вещественное число (0 ≤ pi ≤ 1) — вероятность, что ошибка произошла на соответствующем сервере.

Абсолютная или относительная погрешность каждого из ответов не должна превышать 10-9.
Пример 1.
Ввод

2
50 1
50 2
Вывод
0.333333333333
0.666666666667

Пример 2.
Ввод

3
10 100
30 10
60 2
Вывод
0.704225352113
0.211267605634
0.084507042254

Задача 2. Встречи

Условия задания
Чтобы не мешать коллегам на рабочем месте громкими обсуждениями, ребята назначают встречи на определенное время и бронируют переговорки. При бронировании нужно указать дату и время встречи, её длительность и список участников. Если у кого-то из участников получается две встречи в один и тот же момент времени, то в бронировании будет отказано с указанием списка людей, у которых время встречи пересекается с другими встречами. Вам необходимо реализовать прототип такой системы.

Формат ввода
В первой строке входного файла содержится одно число n (1 ≤ n ≤ 1000) — число запросов.

В следующих n строках содержатся запросы по одному в строке. Запросы бывают двух типов:

APPOINT day time duration k names1 names2… namesk
PRINT day name
day — номер дня в 2018 году (1 ≤ day ≤ 365)

time — время встречи, строка в формате HH:MM (08 ≤ HH ≤ 21, 00 ≤ MM ≤ 59)

duration — длительность встречи в минутах (15 ≤ duration ≤ 120)

k — число участников встречи (1 ≤ k ≤ 10)

namesi, name — имена участников, строки, состоящие из маленьких латинских букв (1 ≤ |name| ≤ 20). У всех коллег уникальные имена. Кроме того гарантируется, что среди участников одной встречи ни одно имя не встречается дважды.

Формат вывода
Если удалось назначить встречу (первый тип запросов), выведите OK.

Иначе выведите в первой строке FAIL, а в следующей строке через пробел список имен участников, для которых время встречи пересекается с другими встречами, в том порядке, в котором имена были даны в запросе.

Для второго типа запросов выведите для данного дня и участника список всех событий на данный момент в этот день в хронологическом порядке, по одному в строке, в формате

HH:MM duration names1 names2 … namesk

где имена участников следуют в том же порядке, что и в исходном описании встречи. Если событий в данный день для этого человека нет, то ничего выводить не нужно.
Пример 1.
Ввод
7
APPOINT 1 12:30 30 2 andrey alex
APPOINT 1 12:00 30 2 alex sergey
APPOINT 1 12:59 60 2 alex andrey
PRINT 1 alex
PRINT 1 andrey
PRINT 1 sergey
PRINT 2 alex
Вывод
OK
OK
FAIL
alex andrey
12:00 30 alex sergey
12:30 30 andrey alex
12:30 30 andrey alex
12:00 30 alex sergey
