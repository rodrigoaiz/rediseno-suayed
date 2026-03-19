# AGENTS.md

## Proyecto

Rediseño del sitio **SUAyED Facultad de Medicina UNAM**  
Base de referencia: `https://suayed.facmed.unam.mx/`

---

## 1. Propósito de este documento

Este archivo define el contexto, objetivos, alcance, criterios de trabajo y lineamientos para cualquier agente, asistente o colaborador que participe en el rediseño del sitio de SUAyED FM.

Este proyecto no debe limitarse a replicar el sitio actual. El objetivo es usar el sitio existente como base de análisis para construir una nueva arquitectura de información, una mejor experiencia de usuario y una implementación técnica más clara, mantenible y escalable.

---

## 2. Objetivo general del proyecto

Rediseñar el sitio de SUAyED FM a partir de:

1. Un levantamiento inicial de la estructura actual del sitio.
2. Un inventario de secciones principales y subsecciones.
3. La recuperación de contenido introductorio útil.
4. Una propuesta nueva de arquitectura de información.
5. Una futura implementación visual y técnica del nuevo sitio.

---

## 3. Estado actual del análisis

### 3.1 Hallazgos preliminares del sitio actual

A partir del reconocimiento inicial del sitio, se detectó que:

- El sitio parece estar montado sobre una estructura tipo WordPress.
- Existen rutas con patrón `/index.php/...`.
- Existen archivos servidos desde `/wp-content/uploads/...`.
- La navegación actual contiene varias secciones principales y algunas subsecciones visibles desde menús.

### 3.2 Secciones principales identificadas

Estas son las secciones base detectadas en el levantamiento inicial:

- Inicio
- Aprende en línea
- FundamentaleSS
- Logra tu Meta
- Normatividad
- Acerca de SUAyED FM

### 3.3 Subsecciones identificadas inicialmente

Dentro de **Aprende en línea** se detectaron al menos:

- Comunidad PREMED
- Ponte en Líne@
- Asignaturas modalidad en línea
- Periodos intensivos
- TUFH Talk

Dentro de **Logra tu Meta** se detectaron al menos:

- Facultad de Medicina
- Escuelas Incorporadas

### 3.4 Lectura editorial preliminar del contenido

Interpretación inicial de algunas secciones:

- **Aprende en línea**: hub de acceso a programas, recursos y plataformas educativas.
- **Comunidad PREMED**: parece orientarse a diagnóstico o nivelación de conocimientos previos.
- **Ponte en Líne@**: parece enfocarse en reforzamiento académico mediante tutorías, seminarios y recursos.
- **FundamentaleSS**: parece concentrar materiales digitales de apoyo para alumnado en servicio social.
- **Logra tu Meta**: parece orientado a autoevaluación o preparación académica/profesional.
- **Normatividad**: parece fungir como repositorio de lineamientos y documentos descargables.
- **Acerca de SUAyED FM**: sección institucional.

> Estas interpretaciones son preliminares y deben confirmarse con el contenido recuperado por el script y con revisión manual posterior.

---

## 4. Alcance del proyecto

### Incluye

- Inventario inicial de páginas principales
- Clasificación editorial del contenido
- Propuesta de arquitectura de información
- Definición de jerarquías de navegación
- Propuesta de rediseño UX/UI
- Definición de componentes
- Preparación para implementación técnica

### No incluye por ahora

- Migración completa del contenido
- Auditoría SEO exhaustiva
- Descarga total de todos los assets
- Clonado técnico completo del sitio
- Integración con backend o CMS final

---

## 5. Principios de trabajo

### 5.1 No copiar la estructura actual sin criterio

El sitio actual debe servir como referencia de contenido y organización histórica, pero no debe heredarse automáticamente.

Toda propuesta debe evaluar:

- claridad de navegación,
- intención de usuario,
- agrupación lógica de contenidos,
- mantenibilidad editorial,
- escalabilidad futura.

### 5.2 Priorizar arquitectura orientada al usuario

Siempre que sea posible, reorganizar la información por:

- perfil de usuario,
- tarea principal,
- objetivo académico,
- tipo de recurso,
- frecuencia de uso.

### 5.3 Separar contenido, estructura y presentación

Toda decisión debe distinguir entre:

- contenido existente,
- estructura de información,
- interfaz visual,
- implementación técnica.

---

## 6. Productos esperados

Este proyecto idealmente debe producir, en fases, lo siguiente:

### Fase 1 — Descubrimiento

- inventario base de URLs relevantes
- listado de secciones principales
- resumen de contenido por sección
- mapa preliminar del sitio actual

### Fase 2 — Arquitectura

- propuesta de sitemap nuevo
- agrupación por perfiles o tareas
- prioridades de navegación
- criterios de etiquetado y nomenclatura

### Fase 3 — UX/UI

- wireframes
- propuesta de home
- layouts de secciones internas
- sistema de componentes

### Fase 4 — Implementación

- stack técnico elegido
- estructura de proyecto
- componentes reutilizables
- contenido estructurado

---

## 7. Script de levantamiento base

Se cuenta con un script inicial en Python cuyo objetivo es:

- entrar al home del sitio,
- detectar enlaces internos relevantes,
- recuperar título de página,
- recuperar encabezado visible,
- recuperar fragmentos introductorios de contenido,
- exportar resultados a CSV y JSON.

### Propósito del script

El script no pretende hacer un scraping total ni un clonado del sitio. Su función es generar una base de trabajo para el rediseño editorial y estructural.

### Archivos esperados

- `suayed_sitemap_base.csv`
- `suayed_sitemap_base.json`

### Uso sugerido

1. Ejecutar el script.
2. Revisar resultados.
3. Depurar páginas irrelevantes o repetidas.
4. Clasificar por sección.
5. Proponer nueva IA.

---

## 8. Reglas para agentes que trabajen en este proyecto

Cualquier agente que participe en este repositorio debe seguir estas reglas:

### 8.1 Sobre el análisis

- No asumir que la estructura actual del sitio es correcta.
- Distinguir entre navegación visible y arquitectura real.
- Señalar duplicidades, vacíos y ambigüedades.

### 8.2 Sobre el contenido

- Resumir sin alterar el sentido institucional.
- Detectar páginas desactualizadas o redundantes.
- Marcar recursos externos y documentos descargables.

### 8.3 Sobre UX/UI

- Priorizar claridad, jerarquía y orientación al usuario.
- Evitar menús sobrecargados.
- Proponer rutas principales de entrada al contenido.
- Tener presente que es un sitio institucional-académico.

### 8.4 Sobre implementación

- Favorecer componentes reutilizables.
- Mantener separación entre contenido y layout.
- Documentar decisiones.
- Evitar acoplar la nueva arquitectura a limitaciones heredadas del sitio antiguo.

---

## 9. Preguntas estratégicas que deben guiar el rediseño

Estas preguntas deben revisarse durante el proyecto:

1. ¿Quiénes son los usuarios principales del sitio?
2. ¿Qué tareas vienen a resolver?
3. ¿Qué secciones son informativas y cuáles son puertas de acceso a otros sistemas?
4. ¿Qué contenidos necesitan resumirse y cuáles necesitan visibilidad inmediata?
5. ¿Qué recursos están enterrados en la arquitectura actual?
6. ¿Qué cosas deberían agruparse por perfil de usuario en lugar de por nombre histórico del programa?
7. ¿Qué documentos deberían seguir descargándose y cuáles deberían volverse contenido web?
8. ¿Qué parte del sitio debe ser institucional y cuál operativa?

---

## 10. Propuesta preliminar de reorganización

Esta propuesta es inicial y deberá refinarse.

### Opción base de arquitectura futura

- Inicio
- Oferta y programas
- Recursos de aprendizaje
- Evaluación y autoestudio
- Normatividad
- Acerca de SUAyED FM
- Contacto / apoyo / enlaces clave

### Alternativa orientada a usuario

- Aspirantes
- Estudiantes
- Docentes
- Recursos académicos
- Plataformas y programas
- Normatividad
- Acerca de

Los agentes deben evaluar cuál enfoque funciona mejor con base en el contenido real recuperado.

---

## 11. Stack técnico sugerido

Esto aún no está cerrado, pero para futuras propuestas se prioriza:

- frontend moderno y mantenible
- componentes reutilizables
- buen manejo de contenido estructurado
- facilidad de despliegue institucional
- posibilidad de crecimiento editorial

### Opciones viables a evaluar

- Astro
- WordPress desacoplado
- WordPress con tema nuevo
- sitio estático con contenido estructurado
- híbrido estático + CMS editorial

No tomar una decisión final de stack sin antes cerrar la arquitectura de información.

---

## 12. Estructura sugerida del repositorio

```txt
/
├─ AGENTS.md
├─ README.md
├─ docs/
│  ├─ discovery/
│  │  ├─ sitemap-actual.md
│  │  ├─ inventario-contenido.md
│  │  └─ hallazgos.md
│  ├─ ia/
│  │  ├─ propuesta-sitemap-v1.md
│  │  ├─ propuesta-sitemap-v2.md
│  │  └─ taxonomia.md
│  └─ ux/
│     ├─ wireframes.md
│     └─ componentes.md
├─ scripts/
│  └─ crawl_suayed.py
├─ data/
│  ├─ raw/
│  │  ├─ suayed_sitemap_base.csv
│  │  └─ suayed_sitemap_base.json
│  └─ processed/
│     └─ contenido_clasificado.json
└─ src/
