from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class Alumno(models.Model):
      
      nombre = models.CharField(max_length=32)
      apellido = models.CharField(max_length=32)
      
      nota1 = models.DecimalField(max_digits=2, 
                                  decimal_places=1, 
                                  validators=[
                                        MaxValueValidator(Decimal('7.0')), 
                                        MinValueValidator(Decimal('1.0'))
                                              ]
                                  )
      
      nota2 = models.DecimalField(max_digits=2,
                                   
                                  decimal_places=1, 
                                  
                                  validators=[
                                        MaxValueValidator(Decimal('7.0')), 
                                        MinValueValidator(Decimal('1.0'))]
                                  )
      
      nota3 = models.DecimalField(max_digits=2, 
                                  decimal_places=1, 
                                  validators=[
                                        MaxValueValidator(Decimal('7.0')), 
                                        MinValueValidator(Decimal('1.0'))]
                                  )
      
      fecha_ingreso = models.DateField()

      CARRERAS = [
            
            ('informatica', 'Informatica'),
            ('administracion', 'Administrador'),
            ('mecanica', 'Cajero'),
            ('construccion', 'Construcción'),
            ('robotica', 'Robotica'),
            ('contabilidad', 'Contabilidad'),   
      ]

      carrera = models.CharField(max_length=32, choices=CARRERAS)
      
      class Meta:
            verbose_name = 'Alumno'
            verbose_name_plural = 'Alumnos'
            
      def __str__(self):
            return f"{self.id} - {self.nombre} {self.apellido}"