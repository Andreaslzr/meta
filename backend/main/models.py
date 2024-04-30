from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import *
from django.core.validators import FileExtensionValidator

#criando uma classe de usuário customizada para substituir a padrão com
#atributos desejados:
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    registrationNumber = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email" #substituir o login username por e-mail
    REQUIRED_FIELDS = []

    objects = CustomManager()

    def __str__(self):
        return self.email    


BLOCKS = [
    ('A','Bloco A'),
    ('B','Bloco B'),
    ('C','Bloco C'),
]

class Environments(models.Model):
    name = models.CharField(max_length=100)
    block = models.CharField(max_length=30, choices=BLOCKS)

    def __str__(self):
        return self.name

TASKS_TYPE = [
    ('MA','Manutenção'),
    ('ME','Melhoria'),
]

TASKS_STATUS = [
    ('AB','Aberta'),
    ('EA','Em Andamento'),
    ('CA','Cancela'),
    ('CO','Concluída'),
    ('EN','Encerrada'),
]

class Tasks(models.Model):
    environmentFK = models.ForeignKey(Environments, related_name='tasksEnvironments', on_delete=models.CASCADE)
    reporterFK = models.ForeignKey(CustomUser, related_name='tasksCustomUser', on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    diagnostic = models.CharField(max_length=300, null=True, blank=True)
    type = models.CharField(max_length=100,choices=TASKS_TYPE)
    status = models.CharField(max_length=100,choices=TASKS_STATUS)
    #environmentAlocationFK = models.ForeignKey(EnvironmentAlocation, related_name='tasksEnvironmentAlocation', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class TasksAssignees(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name='tasksAssigneesTask', on_delete=models.CASCADE)
    assigneeFK = models.ForeignKey(CustomUser, related_name='tasksAssignees', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.taskFK.title
    
class Equipments(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    assigneeFK = models.ForeignKey(CustomUser, related_name='equipmentsCustomUser', on_delete=models.CASCADE, 
                                   blank=True, null=True)
    
    def __str__(self):
        return self.name

class TasksStatus(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name='tasksStatusTask', on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=TASKS_STATUS)
    creationDate = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.taskFK.title

FILE_TYPE = [
    ('D','Document'),
    ('P', 'Photo')
]

class FilesTasksStatus(models.Model):
    taskStatusFK = models.ForeignKey(TasksStatus, related_name='filesTasksStatusTask', on_delete=models.CASCADE)
    link = models.CharField(max_length=2000)
    fileType = models.CharField(max_length=300, choices=FILE_TYPE)

    def __str__(self):
        return self.fileType
    
class TasksEquipments(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name='tasksEquipmentsTask', on_delete=models.CASCADE)
    equipmentFK = models.ForeignKey(Equipments, related_name='tasksEquipmentsEquipment', on_delete=models.CASCADE)   

    def __str__(self):
        return self.fileType
    
class EnviromentsAssignees(models.Model):
    environmentFK = models.ForeignKey(Environments, related_name='enviromentsAssigneesEnvironment', on_delete=models.CASCADE)
    assigneeFK = models.ForeignKey(CustomUser, related_name='enviromentsAssigneesCustomUser', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.environmentFK.name
    

COURSES_CATEGORY = [
    ('CAI','Aprendizagem Industrial'),
    ('FIC','Formação Continuada'),
    ('CST','Curso Superior Tecnológico'),
    ('CT','Curso Técnico'),
]

DURATION_TYPE = [
    ('H','Horas'),
    ('S','Semestres'),
]

COURSES_AREA = [
    ('TI','Tecnologia da Informação'),
    ('MEC','Mecânica'),
    ('AUT','Automação'),
    ('ELE','Elétrica'),
]

COURSES_MODALITY = [
    ('EAD', 'Ensino à Distância'),
    ('P', 'Presencial'),
    ('H', 'Híbrido'),
]


class Themes(models.Model):
    name = models.CharField(max_length=200)    
    timeLoad = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Courses(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=COURSES_CATEGORY)
    duration = models.IntegerField()
    durationType = models.CharField(max_length=30, choices=DURATION_TYPE)
    area = models.CharField(max_length=100, choices=COURSES_AREA)
    modality = models.CharField(max_length=100, choices=COURSES_MODALITY)
    #themes = models.ManyToManyField(Themes)

    def __str__(self):
        return self.name
    
class CoursesThemes(models.Model):
    courseFK = models.ForeignKey(Courses, related_name='coursesThemesCourse', on_delete=models.CASCADE)
    themeFK = models.ForeignKey(Themes, related_name='coursesThemesTheme', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.courseFK.name

class Classes(models.Model):
    name = models.CharField(max_length=200)
    courseFK = models.ForeignKey(Courses, related_name='classesCourses', on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return self.name

class ClassesDivision(models.Model):
    name = models.CharField(max_length=200)
    classFK = models.ForeignKey(Classes, related_name='classesDivisionClass', on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name
    

class TeacherAlocation(models.Model):
    classFK = models.ForeignKey(Classes, related_name='teacherAlocationClass', on_delete=models.CASCADE)
    themeFK = models.ForeignKey(Classes, related_name='teacherAlocationTheme', on_delete=models.CASCADE)    
    reporterFK = models.ForeignKey(CustomUser, related_name='teacherAlocationReporter', on_delete=models.CASCADE)

    def __str__(self):
        return self.themeFK.name
    
ALOCATION_STATUS = [
    ('1','Rascunho'),
    ('2','Assinalado'),
    ('3','Concluído'),
]

class TeacherAlocationDetail(models.Model):
    teacherFK = models.ForeignKey(CustomUser, related_name='teacherAlocationDetailTeacher', on_delete=models.CASCADE)
    classDivisionFK = models.ForeignKey(ClassesDivision, related_name='teacherAlocationDetailClassDiv', on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    alocationStatus = models.CharField(max_length=30, choices=ALOCATION_STATUS, default='1')

    def __str__(self):
        return self.classDivisionFK.name

WEEK_DAYS = [
    ('Seg','Segunda-Feira'),
    ('Ter','Terça-Feira'),
    ('Qua','Quarta-Feira'),
    ('Qui','Quinta-Feira'),
    ('Sex','Sexta-Feira'),
    ('Sab','Sábado'),
    ('Dom','Domingo'),
]

class TeacherAlocationDetailEnvironment(models.Model):
    teacherAlocationDetailFK = models.ForeignKey(TeacherAlocationDetail, related_name='teacherAlocationDetailEnvTeacher', on_delete=models.CASCADE)
    environmentFK = models.ForeignKey(Environments, related_name='teacherAlocationDetailEnv', on_delete=models.CASCADE)
    weekDay = models.CharField(max_length=30, choices=WEEK_DAYS)
    hourStart = models.TimeField()
    hourEnd = models.TimeField()
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return self.environmentFK.name
    

class Deadline(models.Model):
    targetDate = models.DateTimeField()
    category = models.CharField(max_length=30, choices=COURSES_CATEGORY)

    def __str__(self):
        return self.category
    

class Signatures(models.Model):
    ownerFK = models.ForeignKey(CustomUser, related_name='signaturesOwner', on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    signature = models.CharField(max_length=1000)

    def __str__(self):
        return self.ownerFK.name
    
PLAN_STATUS = [
    ('1','Pendente'),
    ('2','Em Aprovação'),
    ('3','Aprovado'),
    ('4','Em revisão'),
    ('5','Cancelado'),
]
    
class Plan(models.Model):
    teacherFK = models.ForeignKey(CustomUser, related_name='planTeacher', on_delete=models.CASCADE)
    courseThemeFK = models.ForeignKey(CoursesThemes, related_name='planCourseTheme', on_delete=models.CASCADE)    
    status = models.CharField(max_length=30, choices=PLAN_STATUS, default='1')
    signatureFK = models.ForeignKey(Signatures, related_name='planSignature', on_delete=models.CASCADE, blank=True, null=True)
    approverFK = models.ForeignKey(CustomUser, related_name='planApprover', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.teacherFK.email

class PlanStatus(models.Model):
    planFK = models.ForeignKey(Plan, related_name='planStatusPlan', on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=PLAN_STATUS)
    comment = models.CharField(max_length=500)
    file = models.CharField(max_length=1000)

    def __str__(self):
        return self.planFK.teacherFK.email
    

class ChatBot(models.Model):
    file = models.FileField(upload_to='chatbot', validators=[FileExtensionValidator(allowed_extensions=['xlsx'])])
    message = models.TextField(max_length=1000)
    createdDate = models.DateTimeField(auto_now_add=True)
    scheduledDate = models.DateTimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return 'chatBot'


LOG_TYPE = [
    ('1', 'Número Indisponível'),
    ('2', 'Dado Incorreto'),
    ('3', 'API Indisponível'),
    ('4', 'Erro Desconhecido')
]

class FileLogs(models.Model):
    chatbotFK = models.ForeignKey(ChatBot, related_name='fileLogChatBot', on_delete=models.CASCADE)
    response = models.CharField(max_length=1000)
    type = models.CharField(max_length=30, choices=LOG_TYPE)
    row = models.IntegerField()
    phoneNumber = models.CharField(max_length=15)

    def __str__(self):
        return self.phoneNumber

