# ENAE VET ES — Chatbot de Atención Veterinaria

> Proyecto académico del curso **[Nombre del curso — pendiente]** en **ENAE Business School**.
> MVP: agente conversacional con LangChain para atención al cliente de una clínica veterinaria.

---

## 1. Proyecto

### Visión del producto

Plataforma backend que expone un **chatbot clínico veterinario** accesible vía API HTTP. El agente:

- Orienta a los dueños de mascotas (triage, cuidados, citas).
- **No diagnostica ni prescribe** — deriva al equipo veterinario cuando procede.
- Sigue las reglas de negocio documentadas en `DOCs/`.

### Alcance del MVP (Épica 1)

| Funcionalidad | Estado |
|---|---|
| Chatbot simple (Flask + LangChain + OpenAI) | Hecho |
| README maestro / plantilla viva (VET-2) | En curso |
| Despliegue en Vercel (VET-3) | To Do |
| Sistema de prompt veterinario + disclaimers | To Do |
| RAG sobre documentación interna | To Do |
| Tool de agenda / calendario | To Do |

---

## 2. Equipo

| Nombre | Rol | Contacto |
|---|---|---|
| _Pendiente — completar por cada miembro_ | | |

---

## 3. Jira y control de versiones

- **Tablero Jira:** URL pendiente — responsable: _[nombre]_
- **Repositorio GitHub:** <https://github.com/LuimiGod/ENAE-VET-ES>
- **Rama principal:** `main`
- **Convención de ramas:** `<tipo>/VET-<n>-<descripcion-corta>` (ej. `feat/VET-3-vercel-deploy`)

### Backlog de tickets VET

| Ticket | Resumen | Estado |
|---|---|---|
| VET-1 | Setup inicial del repositorio | Hecho |
| VET-2 | README maestro: estructura y huecos para lo que viene | En curso |
| VET-3 | Despliegue en Vercel | To Do |
| VET-4 | Sistema de prompt veterinario + disclaimers | To Do |
| VET-5 | RAG sobre documentación interna | To Do |
| VET-6 | Tool de agenda / calendario Google | To Do |
| _Épica 2_ | SDD / comandos `enrich` e `implement` | To Do |

---

## 4. Setup local

### Requisitos previos

- Python 3.11+
- `pip` (o Poetry — ver `.cursor/rules/Python-Context.mdc`)

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/LuimiGod/ENAE-VET-ES.git
cd ENAE-VET-ES

# 2. Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## 5. Variables de entorno

Copia el fichero de ejemplo y rellena tus valores:

```bash
cp .env.example .env   # pendiente: crear .env.example en VET-3
```

| Variable | Descripción | Obligatoria |
|---|---|---|
| `OPENAI_API_KEY` | Clave de API de OpenAI | Sí |
| `LLM_MODEL` | Modelo a usar (ej. `gpt-4o-mini`) | No (default: `gpt-4o-mini`) |
| `FLASK_ENV` | Entorno Flask (`development` / `production`) | No |

> `.env.example` se creará en el ticket VET-3 junto con el despliegue.

---

## 6. Cómo ejecutar

### API (modo desarrollo)

```bash
python chatbot_simple.py
# Servidor disponible en http://localhost:5000
```

### UI web básica

Abre `http://localhost:5000` en el navegador — incluye un formulario de prueba.

### API en producción (Vercel)

> URL: **pendiente hasta VET-3**

---

## 7. Documentación de la API

- **OpenAPI / Swagger:** pendiente — se habilitará al migrar a FastAPI (VET-4 o posterior).
- Endpoint actual: `POST /ask_bot` — body form `msg=<texto>`, responde JSON `{"msg": "<respuesta>"}`.

---

## 8. RAG y fuentes de conocimiento

> Pendiente — se implementará en VET-5.

Plan previsto:

- Vector store sobre los documentos de `DOCs/` (reglas de negocio y agenda quirúrgica).
- Posible ingesta de fuentes oficiales veterinarias (URL: pendiente de definir con el equipo).

---

## 9. Tools y calendario

> Pendiente — se implementará en VET-6.

Plan previsto:

- Herramienta LangChain (`@tool`) para consultar y crear citas.
- Integración con Google Calendar u otro backend de agenda.
- Lógica de capacidad diaria según `DOCs/Reglas-de-Negocio-Logica-Agenda.mdc`.

---

## 10. Épica 2 — SDD y comandos avanzados

> Pendiente.

- Comando `enrich`: enriquecimiento de contexto del agente (`.cursor/commands/enrich.md`).
- Comando `implement`: generación guiada de código desde tickets Jira (`.cursor/commands/implement.md`).

---

## 11. Arquitectura de alto nivel

```
Cliente (web / WhatsApp / otros)
        │
        ▼
  API HTTP (Flask → FastAPI)
        │
        ▼
  Capa LangChain
  ├── System prompt veterinario
  ├── Tool: RAG / FAQ (pendiente VET-5)
  ├── Tool: Agenda / Calendar (pendiente VET-6)
  └── LLM: OpenAI / Anthropic (configurable)
        │
        ▼
  Fuentes de datos
  ├── DOCs/ (reglas de negocio)
  └── BD / vector store (pendiente)
```

Principios de diseño:
- **Seguridad clínica**: el chatbot no diagnostica ni prescribe.
- **Separación de responsabilidades**: HTTP, LangChain y reglas de negocio desacopladas.
- **Documentación como fuente única de verdad**: este `README.md` apunta a todos los documentos relevantes.

---

## 12. Índice de documentación

| Documento | Descripción |
|---|---|
| `DOCs/Business-Rules.mdc` | Visión general de las reglas de negocio |
| `DOCs/Reglas-de-Negocio-Logica-Agenda.mdc` | Lógica de agenda quirúrgica (capacidad, ventanas, especies) |
| `.cursor/rules/Python-Context.mdc` | Convenciones Python del equipo |
| `.cursor/rules/repo-context.mdc` | Contexto general del repositorio para Cursor |
| `.cursor/agents/veterinary-langchain-backend.mdc` | Definición del agente LangChain veterinario |
| `.cursor/skills/veterinary-langchain-chatbots/SKILL.md` | Guías de chatbot veterinario (triage, disclaimers, tono) |
| `.cursor/commands/enrich.md` | Comando `enrich` (Épica 2) |
| `.cursor/commands/implement.md` | Comando `implement` (Épica 2) |

---

## 13. Flujo de trabajo (Scrum + Jira)

1. Tomar ticket de Jira → crear rama `<tipo>/VET-<n>-<descripcion>`.
2. Implementar cambios siguiendo `.cursor/rules/Python-Context.mdc`.
3. Abrir Pull Request → solicitar revisión.
4. Merge a `main` una vez aprobado.
5. Actualizar estado del ticket en Jira + enlace al PR.

> Un ticket está **Hecho** cuando su código está mergeado en `main` y el ticket de Jira lo refleja.

---

## 14. Enlaces útiles

| Recurso | URL |
|---|---|
| Repositorio | <https://github.com/LuimiGod/ENAE-VET-ES> |
| Tablero Jira | Pendiente — responsable: _[nombre]_ |
| App en producción (Vercel) | Pendiente hasta VET-3 |
| OpenAPI docs | Pendiente hasta migración a FastAPI |
