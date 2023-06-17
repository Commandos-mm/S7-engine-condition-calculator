# Задание 1
Предсказать performance значения для каждого полетного цикла.
![alt text](/contents/img/tech_task.jpeg)

# Решение задания 1
Для решения данной задачи, в первую очередь, необходимо провести разведочный анализ и предобработку данных. Предобработка данных заключается в разбиении исходного датасета на 6 датасетов, соответствующие различным комбинациям семейств двигателей и типа полета.
Первый этап работы изложен в нескольких ноутбуках:

eda_full_merged_6parts_nonan (2).ipynb - разведочный анализ данных с использованием библиотеки pandas_profiling на разбитом датасете

eda_s7_baseline.ipynb - корреляционная матрица для одного из шести новых датасетов (является промежуточным этапом)

s7_input_corr.ipynb - корреляционная матрица входных параметров для разбитого датасета

s7_output_corr.ipynb - матрица корреляций между входными и выходными параметрами

Зависимости параметров.pdf - аналитика зависимостей на основе корреляционных матриц

Характеристики.pdf - результаты теоретического исследования предметной области с целью получения более подробной информации о параметрах

Следующий этап состоит в подборе модели. Были изучены следующие модели:

s7_catboost_splited.ipynb - катбуст (базовое решение) на разбитом датасете

s7_gd_cb_GSCV.ipynb - gridsearch

s7_perceptron_mine_trained.ipynb - perceptron

s7_pure_data_cb_lgbm.ipynb - GB модели


# Как запускать

Сменить директорию на app.
```
cd app
```

Собрать docker образ с решением можно при помощи команды: 

```
make build
```

Установить необходимые зависимости локально (**Необходимо наличие pip 3 версии**):
```
make install
```

Собрать приложение локально:
```
make run-local
```

