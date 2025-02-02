import re
from token_types import TokenTypes
from file_handler import read_file, write_file

# Especificaciones de tokens (expresiones regulares)
TOKEN_SPECS = [
    (TokenTypes.PALABRA_CLAVE, r"\b(if|else|then)\b"),
    (TokenTypes.IDENTIFICADOR, r"[a-zA-Z_][a-zA-Z0-9_]*"),
    (TokenTypes.NUMERO_ENTERO, r"\b\d+\b"),
    (TokenTypes.NUMERO_REAL, r"\b\d+\.\d+\b"),
    (TokenTypes.CADENA, r"\".*?\""),
    (TokenTypes.OPERADOR_ARITMETICO, r"[+\-*/]"),
    (TokenTypes.OPERADOR_LOGICO, r"==|!=|<|>|<=|>="),
    (TokenTypes.DELIMITADOR, r"[;(){}]"),
    (TokenTypes.ASIGNACION, r"="),
    (TokenTypes.ESPACIO, r"\s+"),
    (TokenTypes.COMENTARIO, r"//.*?$|/\*.*?\*/"),
]

# Función principal del lexer
def lex(code):
    tokens = []
    position = 0

    while position < len(code):
        match = None

        # Buscar coincidencias con los patrones de tokens
        for token_type, pattern in TOKEN_SPECS:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                value = match.group(0)
                if token_type != TokenTypes.ESPACIO and token_type != TokenTypes.COMENTARIO:
                    tokens.append({"type": token_type, "value": value})
                position = match.end()
                break

        if not match:
            raise ValueError(f"Error léxico: carácter inesperado en posición {position} ('{code[position]}')")

    return tokens

# Punto de entrada del programa
if __name__ == "__main__":
    # Rutas de archivos
    input_file_path = "../input/example.txt"
    output_file_path = "../output/tokens.json"

    try:
        # Leer el archivo de entrada
        code = read_file(input_file_path)

        # Ejecutar el lexer
        tokens = lex(code)

        # Guardar los tokens en un archivo de salida
        write_file(output_file_path, tokens)

        print("✅ Análisis léxico completado. Tokens guardados en:", output_file_path)
    except Exception as e:
        print("❌ Error:", e)
