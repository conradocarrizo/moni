### Moni Desafío Back ###
Este proyecto es una aplicación web para registrar pedidos de préstamos de usuarios que acceden al sitio y para los administradores un CRUD de los mismos.

===
### Tecnologías utilizadas ###

Utilicé el patrón por defecto de Django MTV (MVC) con las vistas y los templates en HTML.
Docker y Docker Compose para el desarrollo.
Pytest para las pruebas.
GitHub Actions en el deploy para verificar Pytest, Black y Flake8.
Celery para tareas en segundo plano.
Flower para monitorear las tareas.
PostgreSQL como base de datos.

===
### Vistas ###
* LandingPage

* Inicio de sesión

* Lista de Préstamos

* Eliminación de Préstamos

* Actualización de Préstamos

* Flower

* Detalle de la tarea