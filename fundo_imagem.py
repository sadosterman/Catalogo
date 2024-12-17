from PIL import Image
from rembg import remove
import os

# Diretório com as imagens
input_dir = r"C:\Users\João\Desktop\Nova pasta\Web program catalog\Catalogo"
output_dir = r"C:\Users\João\Downloads\Catalogo_Padronizado"

# Configurações de tamanho
output_size = (500, 500)  # Ajuste para o tamanho desejado (largura, altura)

# Certifique-se de que o diretório de saída existe
os.makedirs(output_dir, exist_ok=True)

# Processar as imagens
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):  # Verificar extensões de imagem
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Abrir a imagem
        with open(input_path, 'rb') as img_file:
            img = Image.open(img_file)
            
            # Remover fundo
            try:
                img_no_bg = remove(img)  # Remover fundo
            except Exception as e:
                print(f"Erro ao remover fundo da imagem {filename}: {e}")
                continue

            # Redimensionar usando o método correto
            img_resized = img_no_bg.resize(output_size, Image.Resampling.LANCZOS)
            
            # Salvar no formato PNG para manter a transparência
            img_resized.save(output_path, format='PNG')
            print(f"Imagem processada e salva: {output_path}")
