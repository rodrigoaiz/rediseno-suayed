# Rediseño SUAyED FM

Rediseño del sitio web del **Sistema Universidad Abierta y Educación a Distancia de la Facultad de Medicina UNAM**.

Este proyecto no replica el sitio actual — parte de él como referencia de contenido para construir una nueva arquitectura de información, una mejor experiencia de usuario y una implementación técnica más clara y mantenible.

---

## Stack

- [Astro](https://astro.build/) v6
- [Tailwind CSS](https://tailwindcss.com/) v4 (via `@tailwindcss/vite`)
- Node.js ≥ 22.12

## Tipografía y paleta

- **Fraunces** — fuente display/hero (serif óptico-variable, carácter editorial)
- **Plus Jakarta Sans** — fuente de UI y cuerpo (humanista, moderna)
- Paleta OKLCH: navy profundo · oro cálido · neutros pergamino

---

## Inicio rápido

```bash
npm install
npm run dev
```

El servidor de desarrollo levanta en `http://localhost:4321`.

Otros comandos:

```bash
npm run build    # genera el sitio estático en dist/
npm run preview  # previsualiza el build
```

---

## Estructura del proyecto

```
rediseno-suayed/
├── src/
│   ├── components/
│   │   ├── Navbar.astro
│   │   └── Footer.astro
│   ├── layouts/
│   │   ├── Base.astro       # head, fuentes, meta
│   │   └── Site.astro       # envuelve Navbar + main + Footer
│   ├── pages/
│   │   ├── index.astro
│   │   ├── acerca-de.astro
│   │   ├── fundamentaless.astro
│   │   ├── normatividad.astro
│   │   ├── aprende-en-linea/
│   │   │   ├── index.astro
│   │   │   ├── premed.astro
│   │   │   ├── ponte-en-linea.astro
│   │   │   ├── asignaturas.astro
│   │   │   └── periodos-intensivos.astro
│   │   └── logra-tu-meta/
│   │       ├── facultad.astro
│   │       └── incorporadas.astro
│   └── styles/
│       └── global.css       # tokens OKLCH, fuentes, utilidades
├── public/
├── data/
│   └── raw/                 # datos del scraping inicial
├── scripts/
│   └── crawl_suayed.py      # script de levantamiento del sitio actual
├── astro.config.mjs
├── package.json
└── AGENTS.md                # contexto y reglas del proyecto
```

---

## Páginas implementadas

| Ruta | Descripción |
|------|-------------|
| `/` | Home — hero asimétrico, perfiles, estadísticas, programas, misión/visión |
| `/aprende-en-linea` | Hub de programas educativos en línea |
| `/aprende-en-linea/premed` | Comunidad PREMED |
| `/aprende-en-linea/ponte-en-linea` | Ponte en Líne@ |
| `/aprende-en-linea/asignaturas` | Asignaturas en línea (MOLIMOD) |
| `/aprende-en-linea/periodos-intensivos` | Periodos intensivos |
| `/fundamentaless` | FundamentaleSS — recursos para servicio social |
| `/normatividad` | Documentos normativos descargables |
| `/acerca-de` | Historia, trayectoria, misión y visión |
| `/logra-tu-meta/facultad` | Logra tu Meta — egresados Facultad de Medicina |
| `/logra-tu-meta/incorporadas` | Logra tu Meta — escuelas incorporadas |

---

## Ramas

| Rama | Descripción |
|------|-------------|
| `main` | Rediseño editorial — dirección visual activa |
| `diseno-conservador` | Diseño anterior de referencia |

---

## Contexto del proyecto

Ver [`AGENTS.md`](./AGENTS.md) para el contexto completo del proyecto: objetivos, alcance, principios de trabajo, fases, preguntas estratégicas y reglas para agentes que colaboren en el repositorio.
