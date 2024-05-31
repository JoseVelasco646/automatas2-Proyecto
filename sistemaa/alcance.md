# Sistema de Inventario


### Componentes del Sistema

1. **Backend (API REST)**
    - Implementado en Python usando django.
    - Base de datos en SQLite.


2. **Frontend**
    - Desarrollado en Django.
    - Librerias usadas datatable 1.10, select2 4.0.13, moments 2.25, jquery.
    - Estilos con CSS/Bootstrap.

3. **Documentación**
    - Manual de usuario.
    - Guía de instalación y configuración.
    - Diagrama de arquitectura del sistema.

### Instalación

#### Requisitos Previos

- Python 3.10
- Django 5.0.3


#### Pasos de Instalación

1. Clonar el repositorio:
    ```sh
    git clone https://github.com/JoseVelasco646/automatas2-Proyecto
    cd automas2-Proyecto
    ```

2. Configurar variables de entorno:
    - Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:


3. Instalar dependencias:
    ```sh
    pip install -r requirements.txt
    ```


## Alcance

### Funcionalidades Principales

1. **Creacion de categorias**
    -Crear categoria y descripcion.

2. **Gestión de Productos**
    - Crear, leer, actualizar y eliminar productos.
    - Búsqueda de productos por categoria, nombre del producto o precio.

3. **Creacion de clientes**
    -Crear, editar y eliminar clientes.


4. **Control de Stock**
    - Actualización de cantidades en inventario.

5. **Reportes**
    - Visualizar ventas

### Limitaciones

- El sistema está diseñado para pequeñas y medianas empresas.
- No incluye integración con sistemas externos de contabilidad.
- La escalabilidad está limitada a la capacidad del servidor y la base de datos configurada.

## Proyección

### Mejoras Futuras

1. **Integración con Sistemas Externos**
    - Integrar con ERP y sistemas de contabilidad.

2. **Genear reportes**
    - Generación de reportes de inventario.
    - Exportación de datos a CSV/Excel.

3. **Aplicación Móvil**
    - Desarrollar una versión móvil para la gestión desde dispositivos Android/iOS.

4. **Optimización de Rendimiento**
    - Mejorar la eficiencia de las consultas a la base de datos.
    - Implementar técnicas de caché.

### Escalabilidad

- Migrar a una infraestructura en la nube (AWS, Azure).
- Uso de bases de datos distribuidas y balanceadores de carga.
- Implementar microservicios para descomponer el sistema en componentes más pequeños y manejables.

## Conclusión

El sistema de inventario desarrollado ofrece una solución robusta y fácil de usar para la gestión de productos y stock en pequeñas y medianas empresas. Con las mejoras proyectadas, el sistema puede adaptarse a necesidades más complejas y a un mayor volumen de datos, permitiendo así su uso en entornos empresariales más grandes y exigentes.

---

**Autores**:
- Jose Velasco
