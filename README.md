# ENAE-VET-ES

Plataforma backend de soporte a la atención veterinaria para la clínica ENAE VET, centrada en un **agente conversacional basado en LangChain** y en reglas de negocio claramente documentadas.

---

## 1. Arquitectura de alto nivel

### 1.1 Vista general del sistema

El sistema ENAE VET se concibe como una plataforma compuesta por los siguientes bloques principales:

- **Cliente / Interfaces de consumo**
  - Aplicación web interna (backoffice de la clínica) u otros clientes que consuman la API.
  - Integraciones futuras con chatbot web / WhatsApp u otros canales (solo se documenta la intención; la implementación se hará en otros tickets).

- **Backend de aplicación (Python)**
  - API HTTP (por ejemplo, `FastAPI` o framework equivalente en Python).
  - Endpoints para:
    - Gestionar conversaciones con el chatbot.
    - Consultar estados de agenda / reglas de negocio.
    - Integrarse con sistemas externos (p. ej. CRM, Google Calendar u otros).

- **Capa de IA / LangChain**
  - Agente conversacional diseñado específicamente para **atención al cliente veterinaria**.
  - Sigue las reglas descritas en `.cursor/agents/veterinary-langchain-backend.mdc` y en la skill `.cursor/skills/veterinary-langchain-chatbots/SKILL.md`.
  - Usa prompts de sistema, herramientas (RAG, agenda, FAQs) y flujos de conversación con foco en **seguridad clínica y disclaimers médicos**.

- **Fuentes de conocimiento y datos**
  - Documentos internos del repositorio (`DOCs/` y reglas de negocio).
  - Posibles bases de datos de negocio (pacientes, citas, historial, etc.) que se detallarán en tickets de implementación específicos.

- **Infraestructura y despliegue (alto nivel)**
  - Entornos como `dev` y `prod` (nombres propuestos; la configuración concreta se abordará en otros tickets).

### 1.2 Principios de diseño

- **Separación de responsabilidades**: backend HTTP, capa LangChain y reglas de negocio diferenciadas.
- **Seguridad clínica**: el chatbot **no diagnostica ni prescribe**; orienta, educa y deriva al equipo veterinario cuando procede, siguiendo la skill veterinaria.
- **Documentación como fuente única de verdad**: este `README.md` debe apuntar a todos los documentos relevantes en `DOCs/` y `.cursor/` para que cualquier persona pueda entender el sistema sin contexto externo.

---

## 2. Tecnologías utilizadas

Esta sección documenta las tecnologías clave elegidas y/o recomendadas para ENAE VET. La implementación concreta puede dividirse en varios tickets, pero el stack de referencia es:

- **Lenguaje principal**
  - Python **3.11+** recomendado.

- **Framework backend**
  - `FastAPI` (u otro framework HTTP moderno en Python con tipado y OpenAPI).
  - Motivos:
    - Buen rendimiento.
    - Soporte nativo de **type hints** y validación de datos.
    - Generación automática de documentación OpenAPI.

- **Orquestación de IA**
  - `LangChain` como capa de orquestación de LLMs, herramientas y flujos de conversación.
  - Se siguen las guías definidas en `.cursor/skills/veterinary-langchain-chatbots/SKILL.md`.

- **Proveedor(es) de LLM**
  - Se contemplan opciones como **OpenAI**, **Anthropic** u otros proveedores compatibles.
  - La selección concreta debe ser **configurable por entorno** (por ejemplo, mediante variables de entorno o configuración en ficheros).

- **Persistencia y almacenamiento**
  - Base de datos relacional (p. ej. **PostgreSQL**) para entidades de negocio:
    - Clientes, mascotas, citas, historial clínico, etc.
  - Almacenamiento para conocimiento (p. ej. **vector store**) si se requiere RAG sobre documentación interna.

- **Infraestructura**
  - Contenedores Docker para ejecutar los servicios en local y en otros entornos.
  - Posible uso de `docker-compose` para orquestar:
    - Backend.
    - Base de datos.
    - Servicios auxiliares (p. ej. vector store).

- **Herramientas de desarrollo**
  - **Cursor** como IDE principal, con reglas definidas en `.cursor/rules/`.
  - Estándares de Python documentados en `.cursor/rules/Python-Context.mdc` (formato, estilo, testing, etc.).
  - Integración con:
    - **Jira** para gestión de tareas (incluido este ticket `SCRUM-5`).
    - **GitHub** para control de versiones (`https://github.com/LuimiGod/ENAE-VET-ES.git`).

---

## 3. Flujo de trabajo de desarrollo (Scrum + Jira)

El proyecto sigue un flujo de trabajo alineado con **Scrum** y el uso de **Jira** como sistema de seguimiento.

### 3.1 Estados típicos en Jira

- **Tareas por hacer (To Do)**: ticket creado y priorizado en el backlog.
- **En progreso (In Progress / En curso)**: la persona desarrolladora está trabajando en el ticket (documentación o código).
- **En revisión (Code Review / Review)**: existe una rama y un Pull Request abierto con cambios listos para revisión.
- **Listo para merge (Ready to Merge)**: se han resuelto los comentarios críticos y las validaciones básicas.
- **Hecho (Done / Finalizada)**:
  - El PR se ha mergeado en la rama principal (`main`).
  - El ticket de Jira se ha actualizado con la información relevante.

### 3.2 Flujo específico para tickets de documentación (ej. `SCRUM-5`)

1. Revisar el contexto actual:
   - `README.md` existente.
   - Documentos en `DOCs/` y reglas en `.cursor/`.
2. Diseñar y redactar la sección de **arquitectura de alto nivel**.
3. Documentar las **tecnologías utilizadas** y recomendadas.
4. Describir el **workflow de desarrollo** y el uso de Jira.
5. Completar o actualizar el **índice/glosario de documentación**.
6. Crear una rama dedicada (ejemplo sugerido): `docs/SCRUM-5-improve-readme`.
7. Actualizar los archivos de documentación necesarios (principalmente `README.md`; sin tocar business rules).
8. Abrir un Pull Request, solicitar revisión y aplicar feedback.
9. Hacer merge a `main` una vez aprobados los cambios.
10. Actualizar el ticket de Jira con:
    - Enlace al PR mergeado.
    - Breve resumen de los cambios.

> **Nota sobre la definición de Done:** un ticket se considera realmente **Hecho (Done)** cuando el código o la documentación correspondiente está **mergeado en `main`** y el ticket de Jira refleja dicho estado.

---

## 4. Índice de documentación

Esta sección actúa como glosario de los documentos clave del repositorio. Todos los enlaces son relativos al root del proyecto.

- **`README.md` (este archivo)**
  - Descripción general del proyecto ENAE VET.
  - Arquitectura de alto nivel.
  - Tecnologías utilizadas.
  - Flujo de trabajo de desarrollo y uso de Jira.
  - Índice de documentación.

- **Reglas de negocio (carpeta `DOCs/`)**
  - [`DOCs/Business-Rules.mdc`](DOCs/Business-Rules.mdc)
    - Descripción general de las reglas de negocio del dominio.
    - Referencia de alto nivel para el sistema.
  - [`DOCs/Reglas-de-Negocio-Logica-Agenda.mdc`](DOCs/Reglas-de-Negocio-Logica-Agenda.mdc)
    - Lógica de agenda quirúrgica basada en inventario de minutos.
    - Restricciones de capacidad diaria, número de perros por día, ventanas de entrega por especie, etc.

- **Contexto de repositorio y reglas de Python (carpeta `.cursor/rules/`)**
  - [`.cursor/rules/repo-context.mdc`](.cursor/rules/repo-context.mdc)
    - Contexto general del repositorio utilizado por Cursor.
  - [`.cursor/rules/Python-Context.mdc`](.cursor/rules/Python-Context.mdc)
    - Lineamientos y convenciones de Python (estilo, formato, testing, packaging, etc.).

- **Agente backend basado en LangChain**
  - [`.cursor/agents/veterinary-langchain-backend.mdc`](.cursor/agents/veterinary-langchain-backend.mdc)
    - Definición del agente backend de LangChain para atención al cliente veterinaria.
    - Describe el rol del agente, su enfoque de seguridad y la relación con las skills.
  - [`.cursor/skills/veterinary-langchain-chatbots/SKILL.md`](.cursor/skills/veterinary-langchain-chatbots/SKILL.md)
    - Skill con las guías específicas para chatbots de atención veterinaria (disclaimers, triage, tono, herramientas, etc.).

---

## 5. Próximos pasos

Los siguientes pasos se implementarán en tickets adicionales:

- Definir la estructura concreta de módulos Python (`src/` layout, routers de FastAPI, etc.).
- Implementar la API HTTP y los endpoints de conversación / agenda.
- Configurar la capa de LangChain (prompts, herramientas de RAG, integración con business rules).
- Añadir scripts de infraestructura (Docker, `docker-compose`, configuración de entornos).

Este `README.md` debe mantenerse actualizado cada vez que se añadan nuevas piezas relevantes a la arquitectura o a la documentación.

