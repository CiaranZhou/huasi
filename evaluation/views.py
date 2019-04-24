from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import csrf
from .models import *
from pyecharts import Radar


# Create your views here.
def holland_test(request):
    m_data = Question.objects.order_by('id')
    return render(request, 'holland_test.html', {'lst': m_data})


def holland_result(request):
    request.encoding = 'utf-8'
    ctx = {'result': ''}
    if request.POST:
        # 判断是否完成
        for i in range(60):
            if 'choice-'+str(i+1) not in request.POST:
                ctx['result'] = '您没有完成全部题目，我们无法进行评价'
                return render(request, 'holland_result.html', ctx)
        # 如果完成了则返回对应的结果
        m_data = Question.objects.order_by('id')
        result = {'常规型C': 0, '现实型R': 0, '研究型I': 0, '管理型E': 0, '社会型S': 0, '艺术型A': 0}
        for i in range(60):
            if m_data[i].choice == int(request.POST['choice-'+str(i+1)]):
                result[m_data[i].interest.name] += 1
        # 生成雷达图
        radar = Radar('你的兴趣分布图')
        c_schema = []
        values = [[]]
        for key, value in result.items():
            c_schema.append({'name': key, 'max': 10, 'min': 0})
            values[0].append(value)
        radar.config(c_schema=c_schema)
        radar.add('', values)
        # 生成霍兰德类型
        s = sorted(result, key=result.__getitem__, reverse=True)
        for i in range(3):
            if result[s[i]] == 0:
                break
        s = ''.join([i[-1] for i in s[:3]])
        return render(request, 'holland_result.html', {'result': s, 'radar': radar.render_embed()})
    else:
        message = '非法访问'
        return HttpResponse(message)
