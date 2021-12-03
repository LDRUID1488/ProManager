from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [('migrations', '0001_initial')]

    operations = [
        migrations.DeleteModel('Tribble'),
        migrations.AddField('Author', 'rating', models.IntegerField(default=0)),
    ]




#**************
#1 Users
#2 Project
#3 Exercise
#4 Administrator
#**************

# Користувачі
#      - ім'я
#      - прізвище
#      - дата народження
#      - посада
#      - аватар (опціонально)  




# Проекти
#      - ім'я
#      - опис (для поля застосувати контент едітор, наприклад TinyMCE)
#      - строковий унікальний ідентифікатор (буде використовуватися в url PATH для перегляду проекту)


class Project(models.Model):
    name = models.CharField('Name project',max_length=40)
    description = models.CharField('Description',max_length=220)
    full_descrip = models.TextField('Full description',null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/project/{self.id}'
    


# Задачи
#      - тема
#       - опис
#       - дата початку, дата закінчення завдання
#       - тип завдання (фіча, баг)
#       - пріоритет завдання (нормальний, високий, терміново)
#       - оцінений час в годинах
#       - масив коментарів до задачі
#       - виконавець (зв'язок з таблицею користувачі)
#       - автор (зв'язок з таблицею користувачі), значення встановлюється при створенні завдання, недоступно для редагування
#       - проект (зв'язок з таблицею проект)     


class Exercise(models.Model):
    post = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    topic = models.CharField(max_length=40)
    description = models.TextField(max_length=2000)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    FEATURE = 'FE'
    BAG = 'BA'
    TYPE_OF_EXERCISE = [
        (FEATURE, 'Feature'),
        (BAG, 'Bag'),
    ]
    type_of_exercise = models.CharField('Type exercise',max_length = 2, choices = TYPE_OF_EXERCISE, default = FEATURE )

    def is_upperclass(self):
        return self.type_of_exercise in {self.BAG}
    
    NORMAL = 'NO'
    HIGH = 'HI'
    URGENT = 'UR'
    TASK_OF_PRIORITY = [
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
        (URGENT, 'Urgent')
    ]
    task_of_priority = models.CharField('Task of priority',max_length = 2, choices = TASK_OF_PRIORITY, default = NORMAL)
    def is_upperclass(self):
        return self.task_of_priority in {self.HIGH}
    
    time = models.TimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete= models.CASCADE,null=True)
    
    def __str__(self):
            return self.topic


class Comments(models.Model):
    """Ксласс комментариев к новостям
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    new = models.ForeignKey(
         Exercise,
         verbose_name="Новость",
         on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=False)

    

    def __str__(self):
        return "{}".format(self.user)