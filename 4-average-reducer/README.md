# average-reducer
Реализуйте reducer в задаче подсчета среднего времени, проведенного пользователем на странице.

Mapper передает в reducer данные в виде key / value, где key - адрес страницы, value - число секунд, проведенных пользователем на данной странице.

Среднее время на выходе приведите к целому числу.

Sample Input:

```
www.facebook.com	100
www.google.com	10
www.google.com	5
www.google.com	15
www.stepic.org	60
www.stepic.org	100
```

Sample Output:

```
www.facebook.com	100
www.google.com	10
www.stepic.org	80
```

## Запуск
```
sh run.sh
```
