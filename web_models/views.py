from django.shortcuts import render
from web_models import models


# Create your views here.
def index(request):
    # bxslider轮播图
    bxslider_list = models.Bxslider.objects.filter(status=1).values('img', 'href')

    # notice_list 公告的数据
    # status必须是1,保证上线,依据weight权重来拿到前3个数据；
    notice_list = models.Notice.objects.filter(status=1).order_by('-weight').values('title', 'content')[0:3]
    # print(notice_list)
    # course_list 课程的数据
    course_list = models.Course.objects.filter(status=1).order_by('-weight').values('id', 'icon', 'title', 'summary')
    # print(course_list)
    student_list = models.Student.objects.filter(status=1).order_by('-weight').values('id', 'company', 'name', 'salary',
                                                                                      'pic')
    # -weight 表示按照weight的大小降序排序
    # print(student_list)
    student_detail_list = models.StudentDetail.objects.order_by('-weight').values(
        'student__name',
        'student__company',
        'student__salary',
        'student__pic',
        'letter_of_thanks',
    )
    # print(student_detail_list)
    recruit_list = models.Recruit.objects.filter(status=1).order_by('-weight').values(
        'salary',
        'title',
    )
    # print(recruit_list)
    return render(request, 'home/index.html', {
        'bxslider_list': bxslider_list,
        'notice_list': notice_list,
        'course_list': course_list,
        'student_list': student_list,
        'student_detail_list': student_detail_list,
        'recruit_list': recruit_list,
    })


def teacher(request):
    teacher_list = models.Teacher.objects.all()
    return render(request, 'home/teacher.html', {'teacher_list': teacher_list})


def students(request):
    student_detail_list = models.StudentDetail.objects.values().order_by('-weight').values('letter_of_thanks',
                                                                                           'student__pic',
                                                                                           'student__name',
                                                                                           'student__company',
                                                                                           'student__salary')
    # print(student_detail_list)
    return render(request, 'home/students.html', {'student_detail_list': student_detail_list})


def video(request, *args, **kwargs):
    # video_list = models.Video.objects.values('title','summary','href','img')
    # print(video_list)
    condition = {}
    # 用来接受url发送的id值，
    for k, v in kwargs.items():
        print(k, v)
        # classification_id 1
        # direction_id 1
        if v == '0':
            pass
        else:
            condition[k] = v
    print(condition)
    direction_list = models.Direction.objects.values('id', 'name')
    # print(direction_list)
    class_list = models.Classification.objects.values('id', 'name')

    video_list = models.Video.objects.filter(**condition).values('id', 'level', 'title', 'summary', 'img', 'href')
    return render(request, 'home/video.html', {
        'direction_list': direction_list,
        'class_list': class_list,
        'video_list': video_list,

    })


def problems(request):
    return render(request, 'home/problems.html')


def about(request):
    return render(request, 'home/about.html')


def simple(request):
    return render(request, 'home/simpletags.html')
