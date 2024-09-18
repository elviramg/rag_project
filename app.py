import sys
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def review_code(file_path):
    with open(file_path, 'r') as f:
        code = f.read()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "Eres un experto en programación que evalúa código."},
            {"role": "user", "content": f"Revisa el siguiente código y otórgale una puntuación del 1 al 10, además de sugerencias de mejora:\n\n{code}"}
        ],
        max_tokens=150,
        temperature=0.7
    )

    review = response['choices'][0]['message']['content'].strip()
    return review

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python app.py <ruta_al_archivo_de_codigo>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"El archivo {file_path} no existe.")
        sys.exit(1)

    review = review_code(file_path)
    print(review)
