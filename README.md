# Proyecto de Comparación de Chatbots: LangChain vs LlamaIndex

## Introducción 

### RAG (Retrieval-Augmented Generation)

RAG, o Generación Aumentada por Recuperación, es un enfoque innovador en el campo de la Inteligencia Artificial que combina la potencia de los modelos de lenguaje grandes (LLMs) con la capacidad de recuperar información específica de una base de conocimientos externa. Este método permite a los sistemas de IA generar respuestas más precisas, actualizadas y contextualizadas.

En un sistema RAG:
1. Se recupera información relevante de una base de datos o fuente externa.
2. Esta información se combina con la consulta del usuario.
3. El LLM utiliza ambos inputs para generar una respuesta informada y precisa.

Los sistemas RAG son especialmente útiles para chatbots y asistentes virtuales, ya que pueden proporcionar respuestas basadas en información actualizada y específica, superando las limitaciones de los modelos pre-entrenados.

![Diagrama RAG](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*DZwcPDr0z3QghwxG_H7qnQ.png)

*Figura 1: Diagrama conceptual de un sistema RAG*

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar y comparar chatbots utilizando dos frameworks populares para la creación de aplicaciones de IA: LangChain y LlamaIndex. El propósito es explorar las diferencias, ventajas y desventajas de cada framework en el contexto de la creación de chatbots basados en RAG.

## Objetivos

1. Desarrollar un chatbot utilizando LangChain
2. Desarrollar un chatbot similar utilizando LlamaIndex
3. Comparar el rendimiento, facilidad de uso y características de ambos frameworks
4. Documentar las diferencias clave y los casos de uso ideales para cada framework

## Estructura del Proyecto
rag_project/
├── langchain_bot/
│ ├── src/
│ └── requirements.txt
├── llamaindex_bot/
│ ├── src/
│ └── requirements.txt
├── data/
├── tests/
├── README.md
└── requirements.txt

## Instalación

1. Asegúrate de tener pyenv instalado en tu sistema.

2. Clona este repositorio:
   ```
   git clone https://github.com/elviramg/rag_project.git
   cd rag_project
   ```

3. Activa el entorno virtual existente:
   ```
   pyenv activate langchain_rag
   ```

4. Instala las dependencias del proyecto:
   ```
   pip install -r requirements.txt
   ```

5. Configura las variables de entorno necesarias:
   - Crea un archivo `.env` en la raíz del proyecto.
   - Añade las variables necesarias, como la clave API de OpenAI:
     ```
     OPENAI_API_KEY=tu_clave_api_aqui
     ```

6. Ahora estás listo para ejecutar los notebooks y scripts del proyecto.
