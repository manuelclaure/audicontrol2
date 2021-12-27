from django.forms import *
from .models import *

TITULO_CHOICES = (
    ('LICENCIADO', 'LICENCIADO'),
    ('ABOGADO', 'ABOGADO'),
    ('INGENIERO', 'INGENIERO'),
    ('CONTADOR PUBLICO AUTORIZADO', 'CONTADOR PUBLICO AUTORIZADO'),
    ('INGENIERO CIVIL', 'INGENIERO CIVIL'),
    ('INGENIERO ELECTRICO', 'INGENIERO ELECTRICO'),  
)

class TiempoDisponibleForm(ModelForm):
    class Meta:
        model = TiempoDisponible
        fields = ['mes', 'sabados_domingos', 'feriados', 'dias_totales', 'dias_habiles', 'gestion']
        labels = {
            'mes': ('Mes'),
            'sabados_domingos': ('Sabados y domingos'),
            'feriados': ('Feriados'),
            'dias_totales': ('Dias totales'),
            'dias_habiles': ('Dias habiles'),
            'gestion': ('Gestion'),
        }
        widgets = {'mes': TextInput(attrs={'readonly': 'readonly'}), 'gestion': TextInput(attrs={'readonly': 'readonly'})}
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'           
         

class PersonalForm(ModelForm):
    class Meta:
        model = Personal
        fields = ['ci', 'nombre', 'a_paterno', 'a_materno', 'usuario', 'sexo','profesion', 'cargo', 'experiencia_sector_publico_anios', 'experiencia_sector_publico_meses', 'experiencia_sector_privado_anios', 'experiencia_sector_privado_meses',
        'experiencia_auditor_sector_publico_anios', 'experiencia_auditor_sector_publico_meses', 'experiencia_auditor_sector_privado_anios', 'experiencia_auditor_sector_privado_meses'
        , 'fecha_incorporacion_entidad', 'fecha_incorporacion_unidad', 'remuneracion_anual', 'titulo_prov_nal', 'nro_registro_deptal', 'nro_registro_nacional', 'dependencia', 'item', 'remuneracion_anual', 'nro_memorandum']
        labels = {
            'experiencia_sector_publico_anios': ('EXPERIENCIA GENERAL EN EL SECTOR PUBLICO Años'),
            'experiencia_sector_publico_meses': ('Meses'),
            'experiencia_sector_privado_anios': ('EXPERIENCIA GENERAL EN EL SECTOR PRIVADO Años'),
            'experiencia_sector_privado_meses': ('Meses'),
            'experiencia_auditor_sector_publico_anios': ('EXPERIENCIA COMO AUDITOR EN EL SECTOR PUBLICO Años'),
            'experiencia_auditor_sector_publico_meses': ('Meses'),
            'experiencia_auditor_sector_privado_anios': ('EXPERIENCIA COMO AUDITOR EN EL SECTOR PRIVADO Años'),
            'experiencia_auditor_sector_privado_meses': ('Meses'),
            'nro_memorandum': ('Nro memorandum'),
        }
        exclude = ['tipopersonal']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
           
        self.fields['experiencia_sector_publico_anios'].required = False
        self.fields['experiencia_sector_publico_meses'].required = False
        self.fields['experiencia_sector_privado_anios'].required = False
        self.fields['experiencia_sector_privado_meses'].required = False
        self.fields['fecha_incorporacion_entidad'].required = False
        self.fields['fecha_incorporacion_unidad'].required = False
        self.fields['remuneracion_anual'].required = False
        self.fields['titulo_prov_nal'].required = False
        self.fields['dependencia'].required = False
        self.fields['nro_registro_deptal'].required = False
        self.fields['nro_registro_nacional'].required = False 

class PersonalForm2(ModelForm):
    class Meta:
        model = Personal
        fields = ['id', 'ci', 'nombre', 'a_paterno', 'a_materno', 'usuario', 'sexo','profesion', 'cargo', 'experiencia_sector_publico_anios', 'experiencia_sector_publico_meses', 'experiencia_sector_privado_anios', 'experiencia_sector_privado_meses',
        'experiencia_auditor_sector_publico_anios', 'experiencia_auditor_sector_publico_meses', 'experiencia_auditor_sector_privado_anios', 'experiencia_auditor_sector_privado_meses'
        , 'fecha_incorporacion_entidad', 'fecha_incorporacion_unidad', 'remuneracion_anual', 'titulo_prov_nal', 'nro_registro_deptal', 'nro_registro_nacional', 'dependencia', 'item', 'remuneracion_anual', 'nro_memorandum']
        labels = {
            'experiencia_sector_publico_anios': ('EXPERIENCIA GENERAL EN EL SECTOR PUBLICO Años'),
            'experiencia_sector_publico_meses': ('Meses'),
            'experiencia_sector_privado_anios': ('EXPERIENCIA GENERAL EN EL SECTOR PRIVADO Años'),
            'experiencia_sector_privado_meses': ('Meses'),
            'experiencia_auditor_sector_publico_anios': ('EXPERIENCIA COMO AUDITOR EN EL SECTOR PUBLICO Años'),
            'experiencia_auditor_sector_publico_meses': ('Meses'),
            'experiencia_auditor_sector_privado_anios': ('EXPERIENCIA COMO AUDITOR EN EL SECTOR PRIVADO Años'),
            'experiencia_auditor_sector_privado_meses': ('Meses'),
            'nro_memorandum': ('Nro memorandum'),
        }
        widgets = {'id': TextInput(attrs={'type': 'hidden'})}
        exclude = ['tipopersonal']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
           
        self.fields['experiencia_sector_publico_anios'].required = False
        self.fields['experiencia_sector_publico_meses'].required = False
        self.fields['experiencia_sector_privado_anios'].required = False
        self.fields['experiencia_sector_privado_meses'].required = False
        self.fields['fecha_incorporacion_entidad'].required = False
        self.fields['fecha_incorporacion_unidad'].required = False
        self.fields['remuneracion_anual'].required = False
        self.fields['titulo_prov_nal'].required = False
        self.fields['dependencia'].required = False
        self.fields['nro_registro_deptal'].required = False
        self.fields['nro_registro_nacional'].required = False   
        

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        exclude = []
        widgets = {'fecha_inicio': DateInput(attrs={'type': 'date'})}
        labels = {
            'fecha_inicio': ('Fecha programada'),
            'plazo': ('Plazo Total')}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'        

class AsignacionForm(ModelForm):
    class Meta:
        model = Asignacion
        fields = ['personal', 'tipoauditor', 'proyecto', 'tipoasignacion', 'cargo', 'supervisorpoa', 'plazo_poa', 'plazo_supervisor_poa', 'plazo_director', 'gestion'] 
        labels = {
            'plazo_poa': ('Plazo del Auditor segun POA'),  
            'supervisorpoa':('Supervisor POA'), 
            'plazo_supervisor_poa':('Plazo del supervisor segun POA'), 
            'plazo_director':('Plazo del Director segun POA')      
        }       
        exclude = []
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['tipoauditor'].label = "Tipo de auditor"


class TipoAsignacionForm(ModelForm):
    class Meta:
        model = TipoAsignacion
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

class EtapaForm(ModelForm):
    class Meta:
        model = Etapa
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

class ActividadForm(ModelForm):
    class Meta:
        model = Actividad
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

class TEAForm(ModelForm):
    class Meta:
        model = TEA
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

class UsuarioForm(ModelForm):
    class Meta:
        model = User
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

class UsuariocpForm(ModelForm):
    class Meta:
        model = User
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active','date_joined','groups', 'user_permissions']
        fields = ['username', 'password','first_name', 'last_name']
        labels = {
            'username': ('Nombre de usuario'),
            'password': ('Contraseña'),
            'first_name': ('Nombres'),            
            'last_name': ('Apellidos'),
        }
        widgets = {'username': TextInput(attrs={'type': 'text', 'readonly':'readonly'}), 'first_name': TextInput(attrs={'type': 'text', 'readonly':'readonly'}), 'last_name': TextInput(attrs={'type': 'text', 'readonly':'readonly'})}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'


class PoaPersonalForm(ModelForm):
    class Meta:
        model = PoaPersonal
        exclude = []
        widgets = {'fecha': DateInput(attrs={'type': 'date'})}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

class TipoAuditorForm(ModelForm):
    class Meta:
        model = TipoAuditor
        exclude = []        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

class GestionForm(ModelForm):
    class Meta:
        model = Gestion
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'        

class AmpliacionForm(ModelForm):
    class Meta:
        model = Ampliacion
        exclude = []
        labels = {
            'asignacion': ('Codigo'),
            'tiempo': ('Plazo Total'),
            'tiempoauditor': ('Plazo p/ auditor'),
        }
        widgets = {'asignacion': TextInput(attrs={'readonly':'readonly', 'placeholder': '', 'data-toggle' : 'modal', 'data-target' : '.bs-example-modal-lg'})}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control' 

class AsignacionMemoForm(ModelForm):
    class Meta:
        model = Asignacion
        fields = ['personal', 'tipoauditor', 'proyecto', 'tipoasignacion', 'nro_memorandum', 'fecha_memorandum', 'gestion_memorandum', 'cargo', 'supervisor', 'supervisorpoa', 'plazo', 'plazo_poa', 'plazo_supervisor_memo', 'numero_memorandum_supervisor','plazo_director', 'plazo_supervisor_poa', 'plazo_supervisor_memo', 'fecha_memorandum_supervisor'] 
        labels = {
            'plazo': ('Plazo Auditor segun MEMO'), 
            'plazo_poa': ('Plazo Auditor segun POA'), 
            'plazo_supervisor_poa': ('Plazo Supervisor segun POA'), 
            'plazo_supervisor_memo': ('Plazo Supervisor segun Memorandum') , 
            'numero_memorandum_supervisor': ('Numero de memorandum del Supervisor')
        }    
        widgets = {'personal': Select(attrs={'type': 'text', 'readonly':'readonly'}), 'proyecto': Select(attrs={'type': 'text', 'readonly':'readonly'}), 'tipoasignacion': Select(attrs={'type': 'text', 'readonly':'readonly'}), 'tipoauditor': Select(attrs={'type': 'text', 'readonly':'readonly'}), 'cargo': TextInput(attrs={'type': 'text', 'readonly':'readonly'}), 'supervisorpoa': Select(attrs={'type': 'text', 'readonly':'readonly'}), 'plazo_poa': TextInput(attrs={'type': 'text', 'readonly':'readonly'}), 'plazo_director': TextInput(attrs={'type': 'text', 'readonly':'readonly'}), 'plazo_supervisor_poa': TextInput(attrs={'type': 'text', 'readonly':'readonly'})}   
        exclude = []
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['tipoauditor'].label = "Tipo de auditor"
        self.fields['nro_memorandum'].required = False
        self.fields['fecha_memorandum'].required = False
        self.fields['gestion_memorandum'].required = False
        self.fields['supervisor'].required = False
        self.fields['plazo'].required = False
        self.fields['plazo_director'].required = False
        self.fields['plazo_supervisor_poa'].required = False
        self.fields['personal'].readonly = True
        self.fields['proyecto'].readonly = True
        self.fields['tipoauditor'].readonly = True
        self.fields['cargo'].readonly = True
        self.fields['supervisorpoa'].readonly = True
        self.fields['plazo_poa'].readonly = True
        self.fields['plazo_director'].readonly = True
        self.fields['plazo_supervisor_poa'].readonly = True
        self.fields['plazo_poa'].required = False
        self.fields['cargo'].required = False
        #self.fields['personal'].hidden = True
       
