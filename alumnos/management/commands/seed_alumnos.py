from django.core.management.base import BaseCommand
from alumnos.models import Alumno
from decimal import Decimal
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Carga datos de ejemplo en la tabla de Alumnos'

    def handle(self, *args, **kwargs):
        # Limpiar datos existentes (opcional)
        Alumno.objects.all().delete()
        self.stdout.write(self.style.WARNING('Datos anteriores eliminados'))

        # Lista de nombres y apellidos chilenos
        nombres = [
            'Matías', 'Sofía', 'Sebastián', 'Valentina', 'Diego', 'Isidora',
            'Tomás', 'Martina', 'Benjamín', 'Florencia', 'Vicente', 'Emilia',
            'Agustín', 'Amanda', 'Lucas', 'Catalina', 'Gabriel', 'Javiera',
            'Nicolás', 'Francisca', 'Felipe', 'Constanza', 'Joaquín', 'Antonia',
            'Cristóbal', 'Victoria', 'Ignacio', 'Maite', 'Manuel', 'Trinidad'
        ]

        apellidos = [
            'González', 'Muñoz', 'Rojas', 'Díaz', 'Pérez', 'Soto',
            'Contreras', 'Silva', 'Martínez', 'Sepúlveda', 'Morales', 'Rodríguez',
            'López', 'Fuentes', 'Hernández', 'Torres', 'Araya', 'Flores',
            'Espinoza', 'Valenzuela', 'Castillo', 'Reyes', 'Gutiérrez', 'Alvarez',
            'Núñez', 'Castro', 'Vargas', 'Ramírez', 'Carrasco', 'Vega'
        ]

        # Carreras disponibles
        carreras = ['informatica', 'administracion', 'mecanica', 'construccion', 'robotica', 'contabilidad']

        # Generar 50 alumnos
        alumnos_creados = 0

        for i in range(50):
            nombre = random.choice(nombres)
            apellido = random.choice(apellidos)
            carrera = random.choice(carreras)

            # Generar notas aleatorias entre 1.0 y 7.0
            nota1 = Decimal(str(round(random.uniform(1.0, 7.0), 1)))
            nota2 = Decimal(str(round(random.uniform(1.0, 7.0), 1)))
            nota3 = Decimal(str(round(random.uniform(1.0, 7.0), 1)))

            # Generar fecha de ingreso aleatoria (últimos 3 años)
            dias_atras = random.randint(0, 1095)  # 3 años en días
            fecha_ingreso = date.today() - timedelta(days=dias_atras)

            # Crear el alumno
            alumno = Alumno.objects.create(
                nombre=nombre,
                apellido=apellido,
                nota1=nota1,
                nota2=nota2,
                nota3=nota3,
                fecha_ingreso=fecha_ingreso,
                carrera=carrera
            )

            alumnos_creados += 1

            if alumnos_creados % 10 == 0:
                self.stdout.write(self.style.SUCCESS(f'{alumnos_creados} alumnos creados...'))

        self.stdout.write(self.style.SUCCESS(f'Seeder completado exitosamente!'))
        self.stdout.write(self.style.SUCCESS(f'Total de alumnos creados: {alumnos_creados}'))
