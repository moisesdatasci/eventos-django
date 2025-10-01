# 📅 Sistema de Registro de Eventos - Django

Aplicación web desarrollada con Django para la gestión y registro de eventos con participantes. Proyecto académico de Talento digital y Skillnet que implementa formularios con validación personalizada, plantillas reutilizables y el patrón MTV (Model-Template-View).

## 🎯 Objetivo del Proyecto

Desarrollar una aplicación que permita a los usuarios registrar eventos y agregar múltiples participantes a cada evento, con validaciones de datos y una interfaz intuitiva y responsiva.

## ✨ Características Principales

- 📝 **Registro de Eventos** con validación de fechas futuras
- 👥 **Gestión de Participantes** vinculados a eventos
- ✅ **Validaciones personalizadas** en formularios
- 🎨 **Plantillas reutilizables** con herencia de templates
- 📱 **Diseño responsivo** con Bootstrap 5
- 💬 **Sistema de mensajes** para feedback al usuario
- 🔍 **Vista detallada** de eventos con lista de participantes
- 🛡️ **Manejo de errores** con mensajes informativos
- 📊 **Panel de administración** completo

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3.x, Django 4.x
- **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons
- **Base de datos:** SQLite (desarrollo)
- **Validación:** Django Forms con validaciones personalizadas

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/moisesdatasci/eventos-django.git
cd eventos-django
```

### 2. Crear y activar entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install django
```

### 4. Realizar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario (para acceder al admin)

```bash
python manage.py createsuperuser
```
Ingresa un nombre de usuario, email (opcional) y contraseña.

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

### 7. Acceder a la aplicación

- **Aplicación web:** http://127.0.0.1:8000/
- **Panel de administración:** http://127.0.0.1:8000/admin/

## 📁 Estructura del Proyecto

```
eventos-django/
│
├── eventos_web/              
│   ├── settings.py           
│   ├── urls.py              
│   └── wsgi.py               
│
├── eventos/                 
│   ├── models.py           
│   ├── forms.py              
│   ├── views.py              
│   ├── urls.py               
│   ├── admin.py             
│   └── templates/            
│       └── eventos/
│           ├── base.html                 
│           ├── form_template.html        
│           ├── inicio.html               
│           ├── lista_eventos.html        
│           ├── detalle_evento.html       
│           ├── crear_evento.html         
│           └── agregar_participante.html 
│
├── db.sqlite3               
├── manage.py                
└── README.md                 
```

## 📝 Modelos de Datos

### Evento
```python
- nombre (CharField, max 100 caracteres)
- fecha (DateField, debe ser futura)
- ubicacion (CharField, opcional)
- fecha_creacion (DateTimeField, automático)
```

### Participante
```python
- nombre (CharField)
- email (EmailField)
- evento (ForeignKey a Evento)
- fecha_registro (DateTimeField, automático)
```

## 🎨 Funcionalidades Implementadas

### ✅ Formularios con Validación

**EventoForm:**
- ✓ Validación de fecha futura
- ✓ Límite de 100 caracteres en nombre
- ✓ Campo ubicación opcional
- ✓ Widgets personalizados con Bootstrap

**ParticipanteForm:**
- ✓ Validación de email
- ✓ Campos obligatorios
- ✓ Vinculación automática con evento

### ✅ Vistas y Lógica

- **GET:** Muestra formularios vacíos
- **POST:** Procesa y valida datos
- **Manejo de errores:** Mensajes informativos
- **Redirecciones:** Después de acciones exitosas

### ✅ Templates Reutilizables

- **base.html:** Estructura común con navbar y footer
- **form_template.html:** Template genérico para formularios
- Uso de bloques (`{% block %}`) para personalización
- Sistema de herencia de templates

### ✅ Sistema de Mensajes

```python
- messages.success() → Alertas verdes
- messages.error() → Alertas rojas
- messages.info() → Alertas azules
- messages.warning() → Alertas amarillas
```

## 🌐 Rutas de la Aplicación

| Página | URL | Descripción |
|--------|-----|-------------|
| Inicio | `/` | Página principal con eventos recientes |
| Lista de Eventos | `/eventos/` | Todos los eventos registrados |
| Crear Evento | `/evento/crear/` | Formulario para nuevo evento |
| Detalle Evento | `/evento/<id>/` | Información completa y participantes |
| Agregar Participante | `/evento/<id>/participante/` | Formulario para nuevo participante |
| Admin | `/admin/` | Panel de administración Django |

## 💡 Uso de la Aplicación

### Crear un Evento

1. Ve a "Crear Evento" en el menú
2. Completa el formulario:
   - Nombre del evento (obligatorio, máx. 100 caracteres)
   - Fecha (obligatoria, debe ser futura)
   - Ubicación (opcional)
3. Haz clic en "Crear Evento"
4. Si hay errores, se mostrarán debajo de cada campo

### Agregar Participantes

1. Desde la lista de eventos, haz clic en "Ver Detalles"
2. Clic en "Agregar Participante"
3. Completa el formulario:
   - Nombre del participante (obligatorio)
   - Correo electrónico (obligatorio, formato válido)
4. Haz clic en "Agregar Participante"

### Ver Detalles de un Evento

1. En la página de inicio o lista de eventos
2. Haz clic en "Ver Detalles"
3. Verás:
   - Información completa del evento
   - Lista de todos los participantes registrados
   - Opciones para agregar más participantes

## ⚠️ Validaciones Implementadas

### Validaciones del Formulario de Eventos

- ❌ **Fecha pasada:** "La fecha del evento debe ser futura."
- ❌ **Nombre muy largo:** "El nombre no puede superar los 100 caracteres."
- ❌ **Campos vacíos:** "Este campo es obligatorio."

### Validaciones del Formulario de Participantes

- ❌ **Email inválido:** "Ingrese un correo electrónico válido."
- ❌ **Campos vacíos:** "Este campo es obligatorio."

## 🎓 Requisitos Académicos Cumplidos

- ✅ Formulario de registro de eventos con validaciones
- ✅ Formulario de participantes vinculado a eventos
- ✅ Uso de FormClass (ModelForm) de Django
- ✅ Vistas que manejan GET y POST
- ✅ Manejo de errores con mensajes
- ✅ Plantillas reutilizables con herencia
- ✅ Validación de fecha futura
- ✅ Validación de longitud de campos
- ✅ Múltiples participantes por evento
- ✅ Diseño responsivo con Bootstrap

## 🔧 Configuración del Admin

El panel de administración incluye:

- **Eventos:**
  - Lista con nombre, fecha, ubicación y cantidad de participantes
  - Filtros por fecha
  - Búsqueda por nombre y ubicación
  - Jerarquía por fecha

- **Participantes:**
  - Lista con nombre, email y evento
  - Filtros por evento y fecha de registro
  - Búsqueda por nombre y email

## 🎨 Personalización

### Cambiar colores del tema

Edita las clases de Bootstrap en los templates:
- `bg-primary` → Color principal
- `bg-success` → Color de éxito
- `btn-primary` → Botones principales

### Agregar más campos al modelo

1. Edita `eventos/models.py`
2. Agrega el campo al modelo
3. Actualiza `eventos/forms.py` para incluirlo
4. Ejecuta migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
## 👥 Equipo de Desarrollo

- Moisés Ortega - Sin grupo - Desarrollo completo

## 📚 Recursos de Aprendizaje

- [Documentación oficial de Django](https://docs.djangoproject.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)
- [Django Forms](https://docs.djangoproject.com/en/4.2/topics/forms/)
- [Django Templates](https://docs.djangoproject.com/en/4.2/topics/templates/)

## 📄 Licencia

Este proyecto es de uso académico para el curso de Backend Python de Talento Digital.

## 📞 Contacto

Para preguntas o sugerencias:
- Email: moises.ortega@usach.cl
- GitHub: [@tu-usuario](https://github.com/moisesdatasci)

---

⭐ **Si este proyecto te fue útil, no olvides darle una estrella en GitHub!**
