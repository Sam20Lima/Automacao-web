import os
import sys

def find_project_root(start_path):
    # Começa a busca pela raiz do projeto a partir do diretório do script
    current_dir = start_path
    
    while current_dir != os.path.dirname(current_dir):  # Enquanto não chegar na raiz
        if os.path.basename(current_dir) == "Python":  # Verifica se encontrou a pasta raiz do projeto
            return current_dir
        current_dir = os.path.dirname(current_dir)  # Sobe uma pasta

    # Se a raiz não for encontrada, retorna None
    return None

def check_and_create_folders(base_folder_name):
    # Obtém o diretório onde o script está localizado
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Encontra a raiz do projeto automaticamente
    project_root_directory = find_project_root(script_directory)
    
    if project_root_directory is None:
        print("❌ Não foi possível encontrar a raiz do projeto. O script será encerrado.")
        sys.exit(1)  # Sai do programa com código de erro 1
    
    print(f"🌍 Raiz do projeto encontrada: {project_root_directory}")

    # Caminho completo da pasta base na raiz do projeto
    base_directory = os.path.join(project_root_directory, base_folder_name)

    # Se a pasta base não existir, encerra o script
    if not os.path.exists(base_directory):
        print(f"❌ O diretório base '{base_folder_name}' não existe na raiz do projeto. O script será encerrado.")
        sys.exit(1)

    print(f"✅ Diretório base encontrado: {base_directory}")

    # Lista das subpastas esperadas dentro da pasta base
    expected_folders = ["drivers", "errors", "logs", "resources", "results", "screenshots"]

    # Verifica se todas as subpastas existem e cria se necessário
    for folder in expected_folders:
        folder_path = os.path.join(base_directory, folder)  # Caminho completo da subpasta

        if not os.path.exists(folder_path):  # Se não existir, cria
            os.makedirs(folder_path)
            print(f"📁 Pasta criada: {folder_path}")
        else:
            print(f"✅ Pasta já existe: {folder_path}")

# Nome da pasta desejada (diretório base)
folder_name = "cancel_contracts"  # Altere conforme necessário
check_and_create_folders(folder_name)
