import streamlit as st
import google.generativeai as genai

# Configurar Gemini AI
genai.configure(api_key=st.secrets["GEMINI_API_KEY"].value)
print(st.secrets["GEMINI_API_KEY"].value)
model = genai.GenerativeModel('gemini-pro')

# Función para generar recomendación
def generate_recommendation(prompt):
    response = model.generate_content(prompt)
    return response.text

# Validar que la entrada del usuario está relacionada con laptops
def is_laptop_related(input_text):
    ignored_keywords = ['phone', 'tablet', 'smartwatch']  # Palabras clave a ignorar
    laptop_keywords = ['laptop', 'computadora portátil', 'notebook', 'portátil']
    # Verificar si la entrada contiene palabras clave de laptops o características específicas y no contiene palabras a ignorar
    return (any(keyword in input_text.lower() for keyword in laptop_keywords) or
            any(characteristic in input_text.lower() for characteristic in ['ram', 'ssd', 'procesador', 'videojuegos','gamer'])) and not any(ignore_keyword in input_text.lower() for ignore_keyword in ignored_keywords)
# Streamlit App
def main():
    st.title("Recomendación de Laptops")

    # Entrada del usuario
    user_input = st.text_input("Ingresa las características o el propósito específico para el cual necesitas una laptop, así podré brindarte una recomendación más precisa")

    if st.button("Generar Recomendación"):
        if user_input:
            print(user_input)
            # Validar que la entrada esté relacionada con laptops
            if is_laptop_related(user_input):
                # Generar recomendación
                recommendation = generate_recommendation('ayúdame a encontrar la laptop o cpu perfecta para mis necesidades, solo dame 5 opciones y con la liga de la laptoo sugerida:'+ user_input)

                # Mostrar la recomendación
                st.subheader("Recomendación:")
                st.write(recommendation)
            else:
                st.warning("Por favor, ingrese una pregunta relacionada con laptops.")
        else:
            st.warning("Por favor, ingrese una pregunta antes de generar la recomendación.")

if __name__ == "__main__":
    main()
