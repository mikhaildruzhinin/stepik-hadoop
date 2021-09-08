# distinct-values-v1
Реализуйте mapper и reducer из фазы 1, а также mapper из фазы 2 задачи Distinct Values v1. 

На фазе 1 mapper принимает на вход строку, содержащую значение и через табуляцию список групп, разделенных запятой. Reducer принимает на вход данные, созданные mapper из предыдущей шага.
На фазе 2 mapper принимает на вход данные, созданные reducer из предыдущей шага.

Sample Input:

```
1	a,b
2	a,d,e
1	b
3	a,b
```

Sample Output:

```
a	1
a	1
a	1
b	1
b	1
d	1
e	1
```

## Запуск
```
sh run.sh
```
