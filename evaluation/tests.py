from django.test import TestCase

# Create your tests here.
from pyecharts import Radar

result = {'常规型C': 5, '现实型R': 4, '研究型I': 6, '管理型E': 7, '社会型S': 10, '艺术型A': 3}
radar = Radar('你的兴趣分布图')
c_schema = []
values = [[]]
for key, value in result.items():
    c_schema.append({'name': key, 'max': 10, 'min': 0})
    values[0].append(value)
radar.config(c_schema=c_schema)
radar.add('你', values)
print(radar.render_embed())
