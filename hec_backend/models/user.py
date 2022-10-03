from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.contrib.auth.hashers import make_password 
# esto me sirve para hashear un password. pero me funciona con el admin de Django


#CUSTOM MANAGER USUARIO

class UserManager(BaseUserManager):

    def create_user(self, email, tipo_usuario, password = None):
        """
        Crea y Guarda un usuario con el correo y password.
        """
    
        if not email:
            raise ValueError('Usuario debe tener un correo')
    
        user = self.model(email = self.normalize_email(email))
        
        user.tipo_usuario = tipo_usuario.upper()
        user.set_password(password)
        if tipo_usuario.upper() == 'MEDICO' or tipo_usuario.upper() == 'ENFERMERO':
            user.is_staff = True         
        user.save(using = self._db)

        return user
        
    def create_superuser(self, email, password = None):
        """
        Crea y Guarda un usuario con el correo y password.
        """
        user = self.create_user(email, tipo_usuario = 'AUXILIAR', password=password)
        user.is_active=True
        user.is_staff= True
        user.is_superuser = True
   
        user.save(using = self._db)

        return user



#MODELO CUSTOM USUARIO

class User(AbstractBaseUser, PermissionsMixin):

    class Roles(models.TextChoices):
        PACIENTE ='PACIENTE', 'Paciente'
        FAMILIAR = 'FAMILIAR', 'Familiar'
        MEDICO = 'MEDICO', 'Medico'
        ENFERMERO = 'ENFERMERO', 'Enfermero'
        AUXILIAR = 'AUXILIAR', 'Auxiliar'
    
    base_rol = Roles.AUXILIAR

    
    email = models.EmailField(max_length= 100, unique= True)  
    password =  models.CharField(max_length=250)
    tipo_usuario = models.CharField(max_length=10, choices=Roles.choices)

    is_active =  models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
   

    objects = UserManager()


    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [     
        
    ]

    # Al definir otro password con el hasher no lo reconoce el admin cutom que tenemos.
    # Creo que se debe hacer un custom backend para que reconozca el password.

    def save(self, *args, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
     
        return super().save(*args, **kwargs)


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_staff
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.is_staff
    







class FamiliarManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(rol = User.Roles.FAMILIAR)

class Familiarproxy(User):  

    base_rol = User.Roles.FAMILIAR
    familiar = FamiliarManager()    
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.rol = self.base_rol
        return super().save(*args, **kwargs)


class MedicoManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(rol = User.Roles.MEDICO)

class Medicoproxy(User):  

    base_rol = User.Roles.MEDICO
    medico = MedicoManager()    
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.rol = self.base_rol
        return super().save(*args, **kwargs)

class EnfermeroManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(rol = User.Roles.ENFERMERO)

class Enfermeroproxy(User):  

    base_rol = User.Roles.ENFERMERO
    enfermero = EnfermeroManager()    
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.rol = self.base_rol
        return super().save(*args, **kwargs)


class PacienteManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(rol = User.Roles.PACIENTE)

class Pacienteproxy(User):  

    base_rol = User.Roles.PACIENTE
    paciente = PacienteManager()    
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.rol = self.base_rol
        return super().save(*args, **kwargs)

    








