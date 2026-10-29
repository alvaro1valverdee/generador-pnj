# 🛡️ Generador de PNJ (Personajes No Jugables)

Aplicación web interactiva desarrollada con **Flask** que genera personajes no jugables aleatorios para juegos de rol (como D&D o rol de mesa), combinando razas, oficios, personalidades, rasgos, intenciones y secretos guardados en un origen de datos estructurado en JSON.

🔗 **Enlace en producción**: [https://generador-pnj.onrender.com](https://generador-pnj.onrender.com)

---

## 🚀 Características Principales

* **Generación aleatoria dinámica**: Crea perfiles únicos combinando múltiples variables de forma procedural.
* **Interfaz responsiva**: Diseño moderno en modo oscuro adaptado tanto para ordenadores como para dispositivos móviles y tablets.
* **Preparado para producción**: Configurado con **Gunicorn** como servidor WSGI y optimizado para despliegues en la nube.

---

## 🛠️ Tecnologías Utilizadas

* **Backend**: Python, Flask
* **Servidor de Producción**: Gunicorn
* **Datos**: JSON estructurado
* **Frontend**: HTML5, CSS3 / Framework de diseño adaptativo
* **Despliegue**: Render

---

## 📦 Ejecución Local

Si deseas clonar y ejecutar este proyecto en tu entorno local, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone [https://github.com/alvaro1valverdee/generador-pnj.git](https://github.com/alvaro1valverdee/generador-pnj.git)
2. Entra en la carpeta del proyecto:
   ```bash
   cd generador-pnj
3. Crea y activa un entorno virtual:
   ```bash
    python -m venv .venv

    # En Windows:
    .venv\Scripts\activate

    # En macOS/Linux:
    source .venv/bin/activate
4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
5. Ejecuta la aplicación:
    ```bash
    python app.py

💡 Próximas Mejoras (Roadmap)

    [ ] Contenerización de la aplicación utilizando Docker.

    [ ] Ampliación del catálogo de razas y secretos en el archivo JSON.

    [ ] Añadir persistencia de personajes guardados mediante base de datos.

👨‍💻 Autor
Desarrollado por Alvaro Valverde.