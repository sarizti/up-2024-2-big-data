Attendance by Student
=====================


```python
import pandas as pd
from sqlalchemy import create_engine
```

We use "sqlalchemy" because pandas works best with it. Just follow instructions online.


```python
engine = create_engine(f"mysql+mysqlconnector://up:secret@35.193.209.4/up_2024_2_big_data")
con = engine.connect()
```

Change the alias or student id to get attendance for the student


```python
params = {'student_id': '0224260', 'aka': 'Alex'}

pd.read_sql("""
SELECT s.id, s.aka, concat(c.class_date, ' (', c.id, ')') 'cl', a.status, coalesce(c.question_of_the_day, '') 'q', coalesce(a.answer_of_the_day, '') 'ans'
FROM attendance a
JOIN classes c on c.id = a.class_id
JOIN students s on s.id = a.student_id
WHERE 1
-- AND s.aka = %(aka)s
AND s.id = %(student_id)s
""", params=params, con=con)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>aka</th>
      <th>cl</th>
      <th>status</th>
      <th>q</th>
      <th>ans</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0224260</td>
      <td>Alex</td>
      <td>2024-02-10 (1)</td>
      <td>present</td>
      <td>Algo que no sepan de mí</td>
      <td>No me gusta el plátano</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0224260</td>
      <td>Alex</td>
      <td>2024-02-17 (2)</td>
      <td>absent</td>
      <td>Qué carrera estudiaste</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>0224260</td>
      <td>Alex</td>
      <td>2024-02-24 (3)</td>
      <td>present</td>
      <td>Color Favorito</td>
      <td>green</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0224260</td>
      <td>Alex</td>
      <td>2024-03-02 (4)</td>
      <td>present</td>
      <td>Donde Naciste</td>
      <td>Guadalajara</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0224260</td>
      <td>Alex</td>
      <td>2024-03-09 (5)</td>
      <td>present</td>
      <td>Libro Favorito</td>
      <td>Basta de Historias, Oppenheimer</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0224260</td>
      <td>Alex</td>
      <td>2024-03-16 (6)</td>
      <td>absent</td>
      <td>Cumpleaños</td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td>0224260</td>
      <td>Alex</td>
      <td>2024-03-23 (7)</td>
      <td>present</td>
      <td>Hobby</td>
      <td>Hiking</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0224260</td>
      <td>Alex</td>
      <td>2024-04-13 (8)</td>
      <td>present</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



To convert to markdown run:

```sh
jupyter nbconvert 2024-04-20-class9/school.ipynb --to markdown
```
