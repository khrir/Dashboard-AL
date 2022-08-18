from csv import DictReader
from http.client import ImproperConnectionState
from django.core.management import BaseCommand

from dashboard_app.models import Repasses_Municipios, Despesas_Categoria_Economica, Despesas_favorecidos

class Command(BaseCommand):
    def handle(self, *args, **options):

        # if Repasses_Municipios.objects.exists():
        #     print("O csv de repasses já foi carregado")
        #     return
        
        # if Despesas_Categoria_Economica.objects.exists():
        #     print("O csv de d_ce já foi carregado")
        #     return
        
        # if Despesas_favorecidos.objects.exists():
        #     print("O csv de d_f já foi carregado")
        #     return

        for row in DictReader(open('/home/khrir/Documents/Repositorios/Dashboard-Django/dashboard_app/databases/Repasses_M.csv')):
            rm_row = Repasses_Municipios(codigo=row['CODIGO'], total = row['TOTAL'], nome = row['NOME'])
            rm_row.save()

        for row in DictReader(open('/home/khrir/Documents/Repositorios/Dashboard-Django/dashboard_app/databases/despesas_CE.csv')):
            dce_row = Despesas_Categoria_Economica(custeio = row['CUSTEIO'], nome = row['DESCRICAO_UG'])
            dce_row.save()
        
        for row in DictReader(open('/home/khrir/Documents/Repositorios/Dashboard-Django/dashboard_app/databases/despesas_PF.csv')):
            df_row = Despesas_favorecidos(codigo=row['CODIGO'], total = row['TOTAL'], nome = row['NOME'])
            df_row.save()