from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class AdminCustomUser(UserAdmin):
    model = CustomUser
    list_display = ['id','email','registrationNumber','is_active']
    list_display_links = ('id','email','registrationNumber','is_active',)
    fieldsets = (
        (None, {'fields':('email','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
        ('Custom fields', {'fields': ('registrationNumber', 'phoneNumber', 'is_email_verified',)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions',)
        }),
    )
    search_fields = ['email',]
    ordering = ['email']

admin.site.register(CustomUser,AdminCustomUser)

class AdminEnvironments(admin.ModelAdmin):
    list_display = ('id','name','block')
    list_display_links = ('id','name','block',)
    search_fields = ('name','block',)
    list_per_page = 10

admin.site.register(Environments,AdminEnvironments)

class AdminTasks(admin.ModelAdmin):
    list_display = ('id','title','environmentFK', 'creationDate')
    list_display_links = ('id','title','environmentFK', 'creationDate',)
    search_fields = ('title',)
    list_per_page = 10

admin.site.register(Tasks,AdminTasks)

class AdminTasksAssignees(admin.ModelAdmin):
    list_display = ('id','taskFK','assigneeFK')
    list_display_links = ('id','taskFK','assigneeFK',)
    search_fields = ('taskFK',)
    list_per_page = 10

admin.site.register(TasksAssignees,AdminTasksAssignees)

class AdminEquipments(admin.ModelAdmin):
    list_display = ('id','name','code')
    list_display_links = ('id','name','code',)
    search_fields = ('name','code',)
    list_per_page = 10

admin.site.register(Equipments,AdminEquipments)

class AdminTasksStatus(admin.ModelAdmin):
    list_display = ('id','taskFK','status')
    list_display_links = ('id','taskFK','status',)
    search_fields = ('taskFK',)
    list_per_page = 10

admin.site.register(TasksStatus,AdminTasksStatus)

class AdminFilesTasksStatus(admin.ModelAdmin):
    list_display = ('id','taskStatusFK','fileType')
    list_display_links = ('id','taskStatusFK','fileType',)
    search_fields = ('taskStatusFK',)
    list_per_page = 10

admin.site.register(FilesTasksStatus,AdminFilesTasksStatus)

class AdminTasksEquipments(admin.ModelAdmin):
    list_display = ('id','taskFK','equipmentFK')
    list_display_links = ('id','taskFK','equipmentFK',)
    search_fields = ('equipmentFK',)
    list_per_page = 10

admin.site.register(TasksEquipments,AdminTasksEquipments)

class AdminEnviromentsAssignees(admin.ModelAdmin):
    list_display = ('id','environmentFK','assigneeFK')
    list_display_links = ('id','environmentFK','assigneeFK',)
    search_fields = ('environmentFK',)
    list_per_page = 10

admin.site.register(EnviromentsAssignees,AdminEnviromentsAssignees)

class AdminThemes(admin.ModelAdmin):
    list_display = ('id','name','timeLoad')
    list_display_links = ('id','name','timeLoad',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Themes,AdminThemes)

class AdminCourses(admin.ModelAdmin):
    list_display = ('id','name','category', 'durationType', 'area')
    list_display_links = ('id','name','durationType', 'area',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Courses,AdminCourses)

class AdminCoursesThemes(admin.ModelAdmin):
    list_display = ('id','courseFK','themeFK')
    list_display_links = ('id','courseFK','themeFK',)
    search_fields = ('courseFK','themeFK',)
    list_per_page = 10

admin.site.register(CoursesThemes,AdminCoursesThemes)

class AdminClasses(admin.ModelAdmin):
    list_display = ('id','name','courseFK')
    list_display_links = ('id','name','courseFK',)
    search_fields = ('name','courseFK',)
    list_per_page = 10

admin.site.register(Classes,AdminClasses)

class AdminClassesDivision(admin.ModelAdmin):
    list_display = ('id','name','classFK')
    list_display_links = ('id','name','classFK',)
    search_fields = ('name','classFK',)
    list_per_page = 10

admin.site.register(ClassesDivision,AdminClassesDivision)

class AdminTeacherAlocation(admin.ModelAdmin):
    list_display = ('id','classFK','themeFK')
    list_display_links = ('id','classFK','themeFK',)
    search_fields = ('classFK','themeFK',)
    list_per_page = 10

admin.site.register(TeacherAlocation,AdminTeacherAlocation)


class AdminTeacherAlocationDetail(admin.ModelAdmin):
    list_display = ('id','teacherFK','classDivisionFK','alocationStatus')
    list_display_links = ('id','teacherFK','classDivisionFK','alocationStatus',)
    search_fields = ('teacherFK','classDivisionFK',)
    list_per_page = 10

admin.site.register(TeacherAlocationDetail,AdminTeacherAlocationDetail)


class AdminTeacherAlocationDetailEnvironment(admin.ModelAdmin):
    list_display = ('id','teacherAlocationDetailFK','environmentFK')
    list_display_links = ('id','teacherAlocationDetailFK','environmentFK',)
    search_fields = ('teacherAlocationDetailFK','environmentFK',)
    list_per_page = 10

admin.site.register(TeacherAlocationDetailEnvironment,AdminTeacherAlocationDetailEnvironment)


class AdminDeadline(admin.ModelAdmin):
    list_display = ('id','targetDate','category')
    list_display_links = ('id','targetDate','category',)
    search_fields = ('targetDate','category',)
    list_per_page = 10

admin.site.register(Deadline,AdminDeadline)

class AdminSignatures(admin.ModelAdmin):
    list_display = ('id','ownerFK','createdDate')
    list_display_links = ('id','ownerFK','createdDate',)
    search_fields = ('ownerFK',)
    list_per_page = 10

admin.site.register(Signatures,AdminSignatures)

class AdminPlan(admin.ModelAdmin):
    list_display = ('id','teacherFK','courseThemeFK','status')
    list_display_links = ('id','teacherFK','courseThemeFK','status',)
    search_fields = ('teacherFK',)
    list_per_page = 10

admin.site.register(Plan,AdminPlan)

class AdminPlanStatus(admin.ModelAdmin):
    list_display = ('id','planFK','createdDate','status')
    list_display_links = ('id','planFK','createdDate','status',)
    search_fields = ('planFK',)
    list_per_page = 10

admin.site.register(PlanStatus,AdminPlanStatus)


class AdminChatBot(admin.ModelAdmin):
    list_display = ('id','createdDate','scheduledDate')
    list_display_links = ('id','createdDate','scheduledDate',)
    search_fields = ('scheduledDate',)
    list_per_page = 10

admin.site.register(ChatBot,AdminChatBot)


class AdminFileLogs(admin.ModelAdmin):
    list_display = ('id','type','phoneNumber')
    list_display_links = ('id','type','phoneNumber',)
    search_fields = ('type','phoneNumber',)
    list_per_page = 10

admin.site.register(FileLogs,AdminFileLogs)
