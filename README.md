# Chatbot_ieci
Pasos para ejecutar el código en Google Colab
Clonar el repositorio de GitHub:

Abre Google Colab y crea un nuevo notebook. En la primera celda, ejecuta el siguiente comando para clonar el repositorio de GitHub en el entorno de Colab:

!git clone https://github.com/pipe-r-v/Chatbot_ieci

Acceder al directorio del repositorio:

Luego de clonar el repositorio, cambia al directorio donde se encuentra el código ejecutando el siguiente comando:

%cd Chatbot_ieci

Instalar las dependencias:

El código del proyecto puede requerir ciertas librerías y dependencias para funcionar correctamente. En el archivo README.md deberías especificar las librerías necesarias. En el caso del código que proporcionaste, se necesita instalar las siguientes librerías:

!pip install torch transformers sentence_transformers

Ejecuta la celda anterior para instalar las dependencias.

Cargar la base de conocimiento en Colab:

Para cargar la base de conocimiento en Colab, asegúrate de que el archivo base_de_informacion.py se encuentre en el mismo directorio que el notebook de Colab. Esto debería haber sido clonado junto con el resto del repositorio. No necesitas ejecutar este archivo directamente, ya que el código principal lo importará automáticamente. Solo asegúrate de que el archivo esté presente en el directorio.

Ejecutar el código principal (main.py):

Ahora estás listo para ejecutar el código principal. En la siguiente celda, copia y pega todo el contenido del archivo main.py. Luego, ejecuta la celda para iniciar el chatbot.

El chatbot debería imprimir el mensaje de bienvenida y esperar tus preguntas. Puedes escribir tus preguntas en el cuadro de entrada "Tú:" y el chatbot responderá automáticamente basándose en la base de conocimiento que definiste previamente en base_de_informacion.py.

Interactuar con el chatbot:

Ahora, puedes interactuar con el chatbot escribiendo tus preguntas en el cuadro de entrada "Tú:". El chatbot responderá en función de las preguntas y respuestas definidas en la base de conocimiento.

Finalizar la interacción:

Si deseas finalizar la interacción con el chatbot, simplemente escribe 'exit' en el cuadro de entrada "Tú:". Esto hará que el chatbot salga del bucle y termine la ejecución.
