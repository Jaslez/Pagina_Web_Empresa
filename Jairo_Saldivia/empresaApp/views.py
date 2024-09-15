from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'logo': 'logooo.png',
        'titulo': 'Reseña de la Empresa',
        'contenido': 'SkillMasters es una empresa líder en el desarrollo y potenciación del talento humano a través de programas de formación diseñados para fomentar el crecimiento personal y profesional. Con un enfoque innovador, dinámico y adaptable, ofrece una amplia gama de talleres y cursos dirigidos a diversas industrias, brindando conocimientos actualizados y herramientas prácticas que permiten a las personas enfrentar con confianza los complejos desafíos del mercado laboral actual y cambiante.',
        'img1': 'imagen_resena.jpg',
        'titulo_vision': 'Visión',
        'contenido_vision': 'Ser la empresa de referencia en Latinoamérica, especializada en formación y capacitación profesional de alta calidad. Buscamos transformar el talento humano en el motor clave del cambio y el desarrollo sostenible, impactando positivamente tanto a empresas como a personas. Nuestra meta es contribuir de manera significativa al progreso de la sociedad, promoviendo un crecimiento inclusivo, equitativo y responsable, que fomente oportunidades para todos.',
        'img2': 'imagen_vision.jpg',
        'titulo_mision': 'Misión',
        'contenido_mision': 'Capacitar y desarrollar a personas y equipos con los más altos estándares de calidad, empleando metodologías innovadoras y tecnología avanzada. Nuestro objetivo es que adquieran las habilidades esenciales para enfrentar con éxito los grandes retos y demandas del futuro laboral. Promovemos el crecimiento integral de nuestros clientes, fomentando su progreso continuo y sostenible. También nos enfocamos en el bienestar general de la comunidad y su entorno.',
        'img3': 'imagen_mision.jpg',
    }
    return render(request, 'index.html', data)

def instructores(request):
    data_2 = {
        'logo': 'logooo.png',
        'nombre_seccion': 'Instructores',
        'nombre': 'Carlos Ramírez',
        'especialidad': 'Desarrollo de Software y Arquitectura Web',
        'descripcion': 'Carlos Ramírez tiene más de 15 años de experiencia en el sector tecnológico, especializado en el desarrollo de aplicaciones a gran escala. Ha trabajado en empresas internacionales y se destaca por su enfoque práctico en la enseñanza de software moderno, simplificando conceptos complejos como Java, Python y microservicios para sus estudiantes.',
        'img1': 'hugh_1.jpg',
        'img2': 'hugh_2.jpg',
        'nombre_2': 'María Sánchez',
        'especialidad_2': 'Inteligencia Artificial y Machine Learning',
        'descripcion_2': 'María Sánchez es una experta en inteligencia artificial con amplia experiencia en investigación y desarrollo de soluciones basadas en machine learning. Ha trabajado en startups y empresas tecnológicas de vanguardia, enfocándose en la automatización y análisis de grandes volúmenes de datos. Como instructora, combina teoría y práctica para formar ingenieros en IA.',
        'img3': 'lawrence_1.jpg',
        'img4': 'lawrence_2.jpg',
        'nombre_3': 'Rodrigo Fernández',
        'especialidad_3': 'Ciberseguridad',
        'descripcion_3': 'Rodrigo Fernández es un especialista en ciberseguridad con más de 10 años de experiencia. Ha liderado equipos en empresas multinacionales, protegiendo datos y sistemas contra amenazas cibernéticas. Como instructor, enseña mejores prácticas de seguridad y casos reales, ayudando a los estudiantes a desarrollar habilidades en gestión de vulnerabilidades, criptografía y respuesta a incidentes.',
        'img5': 'downey_11.jpg',
        'img6': 'downey_22.jpg',
    }
    return render(request, 'informacion.html', data_2)

def cursos(request):
    data_3 = {
        'logo': 'logooo.png',
        'nombre_seccion2': 'Cursos',
        'nombre_curso': 'Desarrollo de Aplicaciones Web',
        'duracion': 'Duracion: 12 semanas',
        'resena': 'En este curso, los estudiantes aprenderán a crear aplicaciones web interactivas utilizando tecnologías modernas como HTML, CSS, JavaScript y frameworks como React. Se abordarán conceptos clave como el diseño responsivo, la integración de APIs, y la gestión de bases de datos. El curso incluye proyectos prácticos para desarrollar habilidades aplicadas.',
        'img1': 'img_curso1.png',
        'img2': 'img_curso11.png',
        'nombre_curso2': 'Introducción a la Inteligencia Artificial',
        'duracion_2': 'Duracion: 10 semanas',
        'resena_2': 'Este curso ofrece una introducción completa al mundo de la inteligencia artificial y el machine learning. Los estudiantes aprenderán sobre algoritmos, procesamiento de datos y cómo implementar modelos de IA utilizando Python. Además, se explorarán casos de uso reales para entender el impacto de la IA en diversas industrias.',
        'img3': 'img_curso2.jpg',
        'img4': 'img_curso22.jpg',
        'nombre_curso3': 'Ciberseguridad y Gestión de Riesgos',
        'duracion_3': 'Duracion: 8 semanas',
        'resena_3': 'Este curso cubre los principios fundamentales de la ciberseguridad, desde la identificación de amenazas hasta la implementación de estrategias de mitigación. Los estudiantes aprenderán a gestionar riesgos, asegurar redes y sistemas, y aplicar técnicas de criptografía. Además, se trabajará con estudios de caso para entender cómo responder ante incidentes de seguridad reales.',
        'img5': 'img_curso3.jpg',
        'img6': 'img_curso33.jpg',

    }
    return render(request, 'informacion.html', data_3)

def egresados(request):
    data_4 = {
        'logo': 'logooo.png',
        'nombre_seccion3': 'Egresados',
        'nombre_egresado': 'Andrés Muñoz',
        'empresa': 'Empresa: SecureTech Corp',
        'opinion': ' "Gracias al curso de Ciberseguridad, obtuve una comprensión profunda de cómo proteger sistemas y redes en entornos empresariales. Las clases prácticas y los estudios de caso me ayudaron a aplicar los conceptos directamente en mi trabajo en SecureTech Corp, donde ahora lidero un equipo de seguridad"',
        'img1': 'dicaprio_1.jpg',
        'img2': 'dicaprio_2.jpg',
        'nombre_egresado2': 'Carla Gómez',
        'empresa_2': 'Empresa: TechNow Global',
        'opinion_2': ' "El curso de Inteligencia Artificial me ayudó a desarrollar las habilidades técnicas que necesitaba para sobresalir en el sector tecnológico. Los proyectos prácticos y el enfoque en la resolución de problemas reales me permitieron aplicar mis conocimientos de manera efectiva en TechNow Global" ',
        'img3': 'portman1.jpg',
        'img4': 'portman2-.jpg',
        'nombre_egresado3': 'Juan Pérez',
        'empresa_3': 'Empresa: Innovatech Solutions',
        'opinion_3': ' "El curso de Desarrollo de Aplicaciones Web me brindó las herramientas necesarias para enfrentar desafíos en mi trabajo. Los instructores se enfocan en aspectos prácticos que son aplicables al entorno laboral. Gracias a esta formación, logré obtener un puesto clave en Innovatech Solutions" ',
        'img5': 'freeman1.jpg',
        'img6': 'freeman2.jpg',
    }
    return render(request, 'informacion.html', data_4)
