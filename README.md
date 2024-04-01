# Sistema de invetario.

Autor(s): Jose V.

link: https://excalidraw.com/#json=FhYh7Wq-qCmGXs1r-lfII,aywucHcFzTgZTjf6zLvMsw

Status:

Last Update: 2024-04-01

### Contents
-Introduccion.
-Objetivos
-Requisitos Funcionales.
    -Almacenamiento de datos.
    -Busqueda de productos.
    -Resumen de inventario.
    -Actualizacion Dinamica.
-Arquitectura del sistema.
-Interfaz de Usuario.
-Algoritmo y estructuras de Datos.
-Pruebas.

## Introduction.
El Sistema Simplificado de Inventarios en Python tiene como objetivo proporcionar herramientas de administración básicas para controlar productos y sus cantidades. El sistema almacenará información esencial sobre los productos y permitirá realizar búsquedas, obtener resúmenes del inventario y actualizar la base de datos de manera dinámica.

## Objetive
Almacenar y organizar información sobre productos de manera eficiente, incluyendo nombre, cantidad, precio, ID y categoria.

## Funtional Requeriments.
Almacenamiento de Datos
El sistema almacenará la siguiente información para cada producto: nombre, cantidad, precio, ID numérico y categoría.

Búsqueda de Productos
Los usuarios podrán buscar productos por precio, ID o nombre, obteniendo resultados relevantes..

Resumen del Inventario
El sistema proporcionará un resumen del inventario actual, ordenando las cantidades de productos por categoría.

Actualización Dinámica
La base de datos se actualizará dinámicamente cuando un producto se agote o sea eliminado del sistema.

Arquitectura del Sistema
El sistema estará compuesto por módulos: almacenamiento_datos, busqueda_productos, resumen_inventario, actualizacion_dinamica, etc.
Se utilizará una estructura de base de datos simple (puede ser un diccionario o una base de datos SQLite) para almacenar la información del inventario.

Interfaz de Usuario
Se diseñará una interfaz de usuario para interactuar con el sistema.

Algoritmos y Estructuras de Datos
Se implementarán algoritmos eficientes para la búsqueda de productos y la generación de resúmenes del inventario.
Se utilizarán estructuras de datos adecuadas para almacenar la información del inventario de manera eficiente.

Pruebas
Se llevarán a cabo pruebas exhaustivas para garantizar la funcionalidad y la corrección del sistema.
