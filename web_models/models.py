from django.db import models

# Create your models here.

#首页轮播表
class Bxslider(models.Model):
    status_choice = (
        (0,'下线'),
        (1,'上线'),
    )
    status = models.IntegerField(choices=status_choice,default=0)
    name = models.CharField(max_length=32,db_index=True,unique=True),
    img = models.ImageField(upload_to='./static/images/focus/')
    href = models.CharField(max_length=256)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Bxslider'
        verbose_name_plural = '首页轮播表'

    def __str__(self):
        return self.href

class Notice(models.Model):
    status_choice = {
        (0,'不显示'),
        (1,'显示'),
    }
    status = models.IntegerField(choices=status_choice,default=0)
    weight = models.IntegerField(default=0)
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=256)
    detail = models.TextField(null=True,blank=True)

    class Meta:
        db_table = 'Notice'
        verbose_name_plural = '最新公告（如：开班信息）'
    def __str__(self):
        """
        __str__方法用来将对象转换为字符串，返回啥就打印啥；
        :return:
        """
        return self.title


class Course(models.Model):
    status_choice = {
        (0,'下线'),
        (1,'上线'),
    }
    status = models.IntegerField(choices=status_choice,default=1)#状态
    weight = models.IntegerField(default=0) #权重
    title = models.CharField(max_length=32,db_index=True,default=None) # 标题db_index=True 快排
    icon = models.ImageField(upload_to='./static/images/icon/',null=True,blank=True)
    summary = models.CharField(max_length=64,default='summary')

    class Meta:
        db_table = 'Course' #该模型所使用的数据库表的名称:
        verbose_name_plural = '课程' #该对象复数形式的名称:

    def __str__(self):
        return self.title

class Student(models.Model):
    status_choice = (
        (0,'下线'),
        (1,'上线'),
    )
    status = models.IntegerField(verbose_name='状态',choices=status_choice,default=1)
    weight = models.IntegerField(verbose_name='权重',default=0)
    pic = models.ImageField(verbose_name='学员头像',upload_to='./static/images/student_pic/')
    name = models.CharField(verbose_name='姓名',max_length=32,db_index=True,unique=True,default=None)
    company = models.CharField(verbose_name='就业公司',max_length=32,default=None)
    salary = models.CharField(verbose_name='薪资',max_length=32,default=None)

    class Meta:
        db_table = 'Student'
        verbose_name_plural = '学生信息'

    def __str__(self):
        return self.name

class StudentDetail(models.Model):
    student = models.OneToOneField('Student',on_delete=models.CASCADE,default=None)
    weight = models.IntegerField(verbose_name='权重',default=0)
    letter_of_thanks = models.CharField(verbose_name='感谢信',max_length=256,default=None)

    class Meta:
        db_table = 'StudentDetail'
        verbose_name_plural = '学生更多信息'

    def __str__(self):
        return self.student.name

class Recruit(models.Model):
    status_choice = (
        (0,'已过期'),
        (1,'招聘中'),
    )
    status = models.IntegerField(verbose_name='状态',choices=status_choice,default=0)
    weight = models.IntegerField(verbose_name='权重',default=0)
    title  = models.CharField(max_length=32,default=None)
    salary = models.CharField(max_length=32,default=None)
    company = models.CharField(max_length=32,default=None)
    detail = models.TextField(default=None)
    # deadline = models.DateField()

    class Meta:
        db_table = 'Recruit'
        verbose_name_plural = '招聘信息'

    def __str__(self):
        return self.title

class Cooperation(models.Model):
    pass

class Teacher(models.Model):
    pic = models.ImageField(verbose_name='老师头像', upload_to='./static/images/teacher_pic/')
    name = models.CharField(verbose_name='姓名', max_length=32, db_index=True, unique=True, default=None)
    summary = models.CharField(verbose_name='简介', max_length=256, default=None)

    class Meta:
        db_table = 'Teacher'
        verbose_name_plural = '老师信息'

    def __str__(self):
        return self.name

class Direction(models.Model):
    weight = models.IntegerField(verbose_name='权重（按从大到小排列）',default=0)
    name = models.CharField(verbose_name='名称',max_length=32)
    classification = models.ManyToManyField('Classification',)

    class Meta:
        db_table = 'Direction'
        verbose_name_plural = '视频方向'

    def __str__(self):
        return self.name

class Classification(models.Model):
    '''视频分类'''
    weight = models.IntegerField(verbose_name='权重',default=0)
    name = models.CharField(verbose_name='名称',max_length=32)

    class Meta:
        db_table = 'Classification'
        verbose_name_plural = '视频分类'

    def __str__(self):
        return self.name


class Video(models.Model):
    status_choice = (
        (0,'下线'),
        (1,'上线'),
    )
    level_choice = (
        (0,'初级'),
        (1,'中级'),
        (2,'高级'),
    )
    status = models.IntegerField(verbose_name='状态',choices=status_choice,default=1)
    level = models.IntegerField(verbose_name='级别',choices=level_choice,default=1)
    classification = models.ForeignKey('Classification',null=True,blank=True,on_delete=models.CASCADE)
    weight = models.IntegerField(verbose_name='权重（按从大到小）',default=0)
    title = models.CharField(verbose_name='视频标题',max_length=32)
    summary = models.CharField(verbose_name='简介',max_length=32)
    img = models.ImageField(verbose_name='视频封面',upload_to='./static/images/Video/')
    href = models.CharField(verbose_name='视频地址',max_length=256)

    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Video'
        verbose_name_plural = "视频"

    def __str__(self):
        return self.title
