import os

# Caminho para a pasta das imagens
caminho_pasta = r"C:\Users\João\Downloads\Catalogo"

# Obtém a lista de arquivos na pasta
arquivos = os.listdir(caminho_pasta)

# Filtro para pegar apenas arquivos de imagem (jpg, png, etc.)
extensoes_permitidas = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
imagens = [arquivo for arquivo in arquivos if arquivo.lower().endswith(extensoes_permitidas)]

# Ordena a lista de arquivos (opcional, para manter ordem)
imagens.sort()

# Renomeia as imagens para o padrão "produto1.jpg", "produto2.jpg", ...
for indice, imagem in enumerate(imagens, start=1):
    extensao = os.path.splitext(imagem)[1]  # Obtém a extensão do arquivo (ex: .jpg)
    novo_nome = f"produto{indice}{extensao}"  # Novo nome do arquivo
    caminho_atual = os.path.join(caminho_pasta, imagem)
    caminho_novo = os.path.join(caminho_pasta, novo_nome)
    
    # Renomeia o arquivo
    os.rename(caminho_atual, caminho_novo)
    print(f"Renomeado: {imagem} -> {novo_nome}")

print("Renomeação concluída!")
