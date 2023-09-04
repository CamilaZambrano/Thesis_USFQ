from PIL import Image

def crop_and_save_image(input_path, output_path, top_left, bottom_right):
    # Abre la imagen
    image = Image.open(input_path)

    # Define las coordenadas de las esquinas superiores izquierda y inferior derecha
    left, top = top_left
    right, bottom = bottom_right

    # Recorta la imagen utilizando las coordenadas proporcionadas
    cropped_image = image.crop((left, top, right, bottom))

    # Guarda la imagen recortada
    cropped_image.save(output_path)

    print("Imagen recortada y guardada exitosamente.")

# Coordenadas de las esquinas superiores izquierda y inferior derecha
top_left = (129,1008)
bottom_right = (432,1340)

# Llama a la función para recortar y guardar la imagen
crop_and_save_image('DatabaseImages/InBreast/Original/20587758.jpg', '20587758_1_crop.jpg', top_left, bottom_right)
