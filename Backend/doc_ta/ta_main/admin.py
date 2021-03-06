# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models as ta_models

class TableDefAdmin(admin.ModelAdmin):
    list_display = ["start_hour","end_hour","title"]

class SavedTableAdmin(admin.ModelAdmin):
    list_display = ['name','table_size']


class DayDefAdmin(admin.ModelAdmin):
    list_display = ["day_string","day_asp"]


class TimeslotAdmin(admin.ModelAdmin):
    list_display = ['day', 'hour']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['code', 'title', 'hours', 'population_estimate']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_name', 'room_size']


class LectureClassAdmin(admin.ModelAdmin):
    list_display = ['room', 'subject', 'time_slot','save_it_belongs_to']


class ClassTermAdmin(admin.ModelAdmin):
    list_display = ["term", "subject"]


class TermAdmin(admin.ModelAdmin):
    list_display = ["name","number_of_weeks"]


class LecturerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "surname"]


class TeachesAdmin(admin.ModelAdmin):
    list_display = ["lecturer", "subject"]


class CourseYearAdmin(admin.ModelAdmin):
    list_display = ["name"]


class SubjectsCoursesAdmin(admin.ModelAdmin):
    list_display = ["courseyear", "subject"]


class ClashAdmin(admin.ModelAdmin):
    list_display = ["subject1","subject2"]

class SlotBlockerAdmin(admin.ModelAdmin):
    list_display = ["subject","day","start","end","owner"]

# Register your models here.
admin.site.register(ta_models.TableSizeDef,TableDefAdmin)
admin.site.register(ta_models.SavedTable, SavedTableAdmin)
admin.site.register(ta_models.DayDef, DayDefAdmin)
admin.site.register(ta_models.Timeslot, TimeslotAdmin)
admin.site.register(ta_models.Subject, SubjectAdmin)
admin.site.register(ta_models.Room, RoomAdmin)
admin.site.register(ta_models.LectureClass, LectureClassAdmin)
admin.site.register(ta_models.Term, TermAdmin)
admin.site.register(ta_models.ClassTerm, ClassTermAdmin)
admin.site.register(ta_models.Lecturer, LecturerAdmin)
admin.site.register(ta_models.Teaches, TeachesAdmin)
admin.site.register(ta_models.CourseYear, CourseYearAdmin)
admin.site.register(ta_models.SubjectsCourses, SubjectsCoursesAdmin)
admin.site.register(ta_models.Clash, ClashAdmin)
admin.site.register(ta_models.SlotBlocker, SlotBlockerAdmin)
