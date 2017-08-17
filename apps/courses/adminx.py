# _*_ coding:utf-8 _*_

import xadmin

from .models import Course,Lesson,Video,CourseResource


class LessonInline(object):
    model=Lesson
    extra=0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree','learn_time','students','fav_nums','image','click_nums','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree','students','fav_nums','image','click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree','learn_time','students','fav_nums','image','click_nums','add_time']
    #设置图表
    model_icon = 'fa fa-window-restore'
    #设置默认排序
    ordering=['-click_nums']
    #设置只读
    readonly_fields=['click_nums']
    #设置不显示  注：readonly_fields与exclude是冲突的
    exclude=['fav_nums']
    #添加课程时，直接在同一个页面添加课程，避免再跳出才能添加
    inlines=[LessonInline]


class LessonAdmin(object):
    list_display=['course','name','add_time']
    search_fields=['course','name']
    list_filter=['course__name','name','add_time']
    model_icon = 'fa fa-bookmark-o'


class VideoAdmin(object):
    list_display=['lesson','name','add_time']
    search_fields=['lesson','name']
    list_filter=['lesson','name','add_time']
    model_icon = 'fa fa-eye'


class CourseResourceAdmin(object):
    list_display=['course','name','download','add_time']
    search_fields=['course','name','download']
    list_filter=['course','name','download','add_time']
    model_icon = 'fa fa-file'


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)

