
## Задание 1. Экзамен

Студенты пришли сдавать экзамен. Его принимают одновременно несколько экзаменаторов. Студенты сидят в одной общей очереди. Как только кто-то из экзаменаторов освобождается, к нему сразу заходит первый студент из очереди.

Спустя 30 секунд после начала экзамена экзаменатор имеет право на обед, поэтому заканчивает работу с текущим студентом и в течение случайного времени в интервале от 12 до 18 секунд после этого никого не принимает.

Сдача экзамена происходит следующим образом: студенту по очереди задается три вопроса из банка вопросов. Студент в качестве ответа выбирает наугад любое слово из вопроса. По статистике выходит так, что мальчики вероятнее берут слова, расположенные ближе к началу вопроса, а девочки — к концу. Например, на вопрос «Там стоит стол» мальчик с вероятностью 1/2 ответит «Там», с вероятностью 1/3 ответит «стоит» и с вероятностью 1/6 ответит «стол». Девочка на этот же вопрос с вероятностью 1/2 ответит «стол», с вероятностью 1/3 ответит «стоит» и с вероятностью 1/6 ответит «Там». 

Экзаменатор заранее не знает ответ на свой вопрос, поэтому поступает аналогично, выбирая наугад слова. Верных ответов может быть несколько, потому что, выбрав ответ, экзаменатор может с вероятностью 1/3 выбрать еще один, а затем еще и еще до тех пор, пока не остановится, либо не выберет все слова из вопроса в качестве верных ответов. 

По результатам опроса, экзаменатор принимает окончательное решение, сдал студент экзамен или нет. У экзаменатора с вероятностью 1/8 может быть плохое настроение (тогда экзамен считается несданным), с вероятностью 1/4 может быть хорошее настроение (тогда экзамен считается сданным) и с вероятностью 5/8 настроение нейтральное. Тогда оценка объективная: сдал, если верных ответов больше, чем неверных, иначе не сдал.

Время сдачи экзамена зависит от длины имени экзаменатора. Например, у экзаменатора с именем «Степан» (длина имени 6 символов) экзамен продлится от 5 до 7 секунд (случайное вещественное число из диапазона).

Тебе требуется смоделировать сдачу экзамена.

При запуске программы из файла examiners.txt считывается список экзаменаторов, из файла students.txt считывается список студентов, которые пришли заранее и встали в очередь, а из файла questions.txt считывается банк вопросов. Затем начинается экзамен.

Каждый экзаменатор принимает экзамен на отдельном потоке.

Во время работы программы необходимо поддерживать в консоли актуальную информацию об экзамене, а именно выводить:

1. Таблицу студентов из двух столбцов: «Студент», «Статус» (статус один из трех: «Очередь», «Сдал», «Провалил»). 
   - Таблицу отсортировать по статусу, чтобы в начале были студенты в очереди (в том порядке, в котором они будут сдавать), затем — сдавшие, в конце — провалившие.
2. Таблицу экзаменаторов из пяти столбцов: «Экзаменатор», «Текущий студент», «Всего студентов», «Завалил», «Время работы».
   - Когда экзаменатор обедает или закончил принимать, в столбец «Текущий студент» выводить «-».
3. Отдельной строкой количество оставшихся в очереди студентов из общего числа.
4. Отдельной строкой время с момента начала экзамена.

Необходимо, чтобы при любом изменении данных информация синхронизировалась на месте, а не выводилась новая. В конце работы программы необходимо вместо предыдущей промежуточной информации вывести:

1. Таблицу студентов из двух столбцов: «Студент», «Статус» (статус один из двух: «Сдал», «Провалил»).
   - Таблицу отсортировать по статусу, чтобы в начале были студенты, сдавшие экзамен, в конце — провалившие.
2. Таблицу экзаменаторов из четырех столбцов: «Экзаменатор», «Всего студентов», «Завалил», «Время работы».
3. Отдельной строкой время с момента начала экзамена и до момента и его завершения.
4. Отдельной строкой имена лучших студентов через запятую (студент считается лучшим, если смог быстрее других сдать экзамен).
5. Отдельной строкой имена лучших экзаменаторов через запятую (экзаменатор считается лучшим, если процент заваленных студентов у него ниже, чем у других экзаменаторов).
6. Отдельной строкой имена студентов, которых после экзамена отчислят (исключат тех, кто провалил экзамен, закончив раньше других проваливших).
7. Отдельной строкой лучшие вопросы через запятую (вопрос считается лучшим, если на него верно ответило больше всего студентов).
8. Отдельной строкой вывод, удался экзамен или нет (экзамен удался, если сдало больше 85% студентов).

### Входные данные

| examiners.txt |
| ------ |
| Степан М <br/>Дарья Ж <br/>Михаил М |

| students.txt |
| ------ |
| Петр М<br/>Сергей М<br/>Варвара Ж<br/>Иван М<br/>Екатерина Ж<br/>Александра Ж<br/>Алексей М |

| questions.txt |
| ------ |
| Там стоит стол<br/>Человек собаке друг<br/>Солнечные затмения влияют на людей<br/>Программирование интересное занятие |

### Выходные данные

Во время работы

```
+------------+----------+
| Студент    |  Статус  |
+------------+----------+
| Алексей    | Очередь  |
| Петр       |   Сдал   |
| Иван       |   Сдал   |
| Екатерина  |   Сдал   |
| Сергей     | Провалил |
| Варвара    | Провалил |
| Александра | Провалил |
+------------+----------+

+-------------+-----------------+-----------------+---------+--------------+
| Экзаменатор | Текущий студент | Всего студентов | Завалил | Время работы |
+-------------+-----------------+-----------------+---------+--------------+
| Степан      | Алексей         |        1        |    0    |    12.31     |
| Дарья       | -               |        3        |    2    |    12.14     |
| Михаил      | -               |        2        |    1    |     7.21     |
+-------------+-----------------+-----------------+---------+--------------+

Осталось в очереди: 1 из 7
Время с момента начала экзамена: 12.31
```

После работы

```
+------------+----------+
| Студент    |  Статус  |
+------------+----------+
| Петр       |   Сдал   |
| Иван       |   Сдал   |
| Екатерина  |   Сдал   |
| Сергей     | Провалил |
| Варвара    | Провалил |
| Александра | Провалил |
| Алексей    | Провалил |
+------------+----------+

+-------------+-----------------+---------+--------------+
| Экзаменатор | Всего студентов | Завалил | Время работы |
+-------------+-----------------+---------+--------------+
| Степан      |        2        |    1    |    12.35     |
| Дарья       |        3        |    2    |    12.14     |
| Михаил      |        2        |    1    |     7.21     |
+-------------+-----------------+---------+--------------+

Время с момента начала экзамена и до момента и его завершения: 12.35
Имена лучших студентов: Иван
Имена лучших экзаменаторов: Степан, Михаил
Имена студентов, которых после экзамена отчислят: Варвара
Лучшие вопросы: Там стоит стол, Человек собаке друг
Вывод: экзамен не удался
```

## Задание 2. Скачивание изображений

Напиши обработчик ссылок, который будет просить пользователя ввести ссылку на изображение, а затем асинхронно скачивать его. Предполагается, что сразу после ввода первой ссылки пользователя будут просить ввести следующую до тех пор, пока он не введет пустую строку. Если к этому моменту не все изображения будут загружены, выводи соответствующее сообщение, а программу завершай только после того, как все будет загружено.

При возникновении любой ошибки не завершай выполнение программы сразу. Сохраняй состояние для вывода в конце. В самом начале пользователь вводит путь, по которому следует сохранять загруженные изображения.

Если введен некорректный путь или у программы нет доступа для сохранения по этому пути, попроси пользователя ввести другой путь. 

Перед завершением программы выведи сводку об успешных и неуспешных загрузках.

### Входные данные

```
./img
https://images2.pics4learning.com/catalog/s/swamp_15.jpg
https://bad-link-no-website-here.strange/img.png
https://images2.pics4learning.com/catalog/p/parrot.jpg

```

### Выходные данные

Сводка об успешных и неуспешных загрузках

```
+----------------------------------------------------------+--------+
| Ссылка                                                   | Статус |
+----------------------------------------------------------+--------+
| https://images2.pics4learning.com/catalog/s/swamp_15.jpg | Успех  |
| https://bad-link-no-website-here.strange/img.png         | Ошибка |
| https://images2.pics4learning.com/catalog/p/parrot.jpg   | Успех  |
+----------------------------------------------------------+--------+
```
