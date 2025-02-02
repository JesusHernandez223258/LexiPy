# **LexiPy - Analizador Léxico en Python**

## **Descripción del Repositorio**

**LexiPy** es un **analizador léxico** desarrollado en **Python**, diseñado para escanear código fuente y convertirlo en una secuencia de **tokens**. Utiliza **expresiones regulares (RegEx)** y un **Autómata Finito Determinista (AFD)** para reconocer identificadores, números, operadores y palabras clave en un lenguaje de programación definido.

## **Características**
- ✅ Reconocimiento de **tokens**: palabras clave, identificadores, números, operadores y delimitadores.
- ✅ Implementado con **expresiones regulares** y técnicas de **teoría de autómatas**.
- ✅ Soporte para **comentarios y espacios en blanco**.
- ✅ Salida en formato **JSON** para facilitar el análisis sintáctico.
- ✅ Código modular con pruebas unitarias en **unittest**.

## **Estructura del Proyecto**
```plaintext
/LexiPy/
│
├── src/                # Código fuente
│   ├── lexer.py        # Implementación del lexer
│   ├── token_types.py  # Definición de tipos de tokens
│   └── file_handler.py # Gestión de archivos
│
├── test/               # Pruebas unitarias
│   └── test_lexer.py
│
├── input/              # Archivos de entrada
│   └── example.txt
│
├── output/             # Tokens generados
│   └── tokens.json
│
├── requirements.txt    # Dependencias
├── README.md           # Documentación
└── .gitignore          # Archivos ignorados por Git
```

## **Ejemplo de Uso**

### 1️⃣ **Clona el repositorio**  
```bash
git clone https://github.com/JesusHernandez223258/LexiPy.git
cd LexiPy
```

### 2️⃣ **Instala dependencias**  
```bash
pip install -r requirements.txt
```

### 3️⃣ **Ejecuta el analizador léxico**  
```bash
python src/lexer.py
```

### 4️⃣ **Verifica los tokens generados en `output/tokens.json`**  

🚀 **LexiPy** es ideal para aprender sobre compiladores y teoría de autómatas. ¡Contribuciones y mejoras son bienvenidas! 😊

