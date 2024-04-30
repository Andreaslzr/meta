from django.contrib.auth.models import BaseUserManager
import random

class CustomManager(BaseUserManager):

    def create_user(self, email, password=None, registrationNumber=None, **extra_fields):

        if not email:
            raise  ValueError("Invalid e-mail!")
        
        regNumber = registrationNumber if registrationNumber else random.randint(1,100000)

        email = self.normalize_email(email)
   
        user = self.model(
            email=email,            
            registrationNumber=regNumber,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
        
    def create_superuser(self, email, password=None, registrationNumber=None, **extra_fields):
        #se é criação de super user, então seta estes atributos automaticamente:
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        return self.create_user(email, password, registrationNumber, **extra_fields)
            
        