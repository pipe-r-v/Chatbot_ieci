# Importar las librerías necesarias
import torch
from transformers import BertTokenizer, BertForMaskedLM
from sentence_transformers import SentenceTransformer, util
from base_de_informacion import base_de_informacion


def obtener_respuesta(input_text, base_de_informacion, tokenizer, model, encoder_model, max_length=100):
    # Calcular el embedding de la consulta del usuario
    # Usamos el encoder_model para obtener el embedding de la consulta
    query_embedding = encoder_model.encode(input_text, convert_to_tensor=True)

    # Convertir los embeddings en tensores
    # Extraemos los embeddings de las preguntas de la base de información y los convertimos en un tensor
    question_embeddings = torch.stack([data['question_embeddings'] for data in base_de_informacion])

    # Calcular la similitud entre la consulta y las preguntas en la base de conocimiento
    # Utilizamos la función de similitud pytorch_cos_sim de SentenceTransformer
    similarities = util.pytorch_cos_sim(query_embedding, question_embeddings)

    # Encontrar el índice de la pregunta más similar
    # Encontramos el índice del valor máximo en las similitudes
    max_sim_index = torch.argmax(similarities)

    # Obtener la respuesta correspondiente a la pregunta más similar
    # Usamos el índice para obtener la respuesta correspondiente
    response = base_de_informacion[max_sim_index]['answer']

    return response


def main():
    # Cargar el modelo preentrenado de BERT para tokenización
    tokenizer = BertTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-uncased")

    # Cargar el modelo preentrenado de BERT para masked language modeling
    model = BertForMaskedLM.from_pretrained("dccuchile/bert-base-spanish-wwm-uncased")

    # Cargar el modelo preentrenado de SentenceTransformer para calcular embeddings
    encoder_model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')

    # Calcular los embeddings para las preguntas en la base de conocimiento
    question_texts = [data['question'] for data in base_de_informacion]
    question_embeddings = encoder_model.encode(question_texts, convert_to_tensor=True)

    # Actualizar la base de información con los embeddings
    # Asignamos los embeddings a cada pregunta en la base de información
    for i in range(len(base_de_informacion)):
        base_de_informacion[i]['question_embeddings'] = question_embeddings[i]

    # Iniciar el chatbot
    print("¡Hola! Soy un chatbot de ieci basado en BERT en español entrenado por la universidad de chile. Escribe 'exit' para salir.")
    while True:
        user_input = input("Tú: ")

        # Salir del loop si el usuario escribe 'exit'
        if user_input.lower() == "exit":
            break

        # Obtener la respuesta del chatbot
        response = obtener_respuesta(user_input, base_de_informacion, tokenizer, model, encoder_model, max_length=100)

        # Imprimir la respuesta del chatbot
        print("Chatbot:", response)


if __name__ == "__main__":
    main()
