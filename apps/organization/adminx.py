# _*_ coding:utf-8 _*_

import xadmin

from .models import CityDict,CourseOrg,Teacher


class CityDictAdmin(object):
    list_display=['name','desc','add_time']
    search_fields=['name','desc']
    list_filter=['name','desc','add_time']
    model_icon = 'fa fa-university'


class CourseOrgAdmin(object):
    list_display=['name','desc','click_num','fav_nums','image','address','city','add_time']
    search_fields=['name','desc','click_num','fav_nums','image','address']
    list_filter=['name','desc','click_num','fav_nums','image','address','city','add_time']
    model_icon = 'fa fa-university'
    #在后台管理系统中，将课程机构的下拉框改成搜索框
    relfield_style='fk-ajax'


class TeacherAdmin(object):
    list_display=['org','name','work_years','work_company','work_position','points','click_num','fav_nums','add_time']
    search_fields=['org','name','work_years','work_company','work_position','points','click_num','fav_nums']
    list_filter=['org','name','work_years','work_company','work_position','points','click_num','fav_nums','add_time']
    model_icon = 'fa fa-graduation-cap'


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
