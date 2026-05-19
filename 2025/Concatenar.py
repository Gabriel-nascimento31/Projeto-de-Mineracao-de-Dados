import pandas as pd
import glob
import os

# 1. Definir o padrão do nome dos ficheiros (relativo ao próprio script)
script_dir = os.path.dirname(__file__)
caminho_dos_ficheiros = os.path.join(script_dir, 'SF_ConsultaRemuneracaoServidoresParlamentares_2025*.csv')
ficheiros_encontrados = glob.glob(caminho_dos_ficheiros)

# Ordenar os ficheiros para garantir que a sequência mensal esteja correta
ficheiros_encontrados.sort()

lista_dataframes = []

for ficheiro in ficheiros_encontrados:
    # 2. Ler o ficheiro 
    # Skiprows=1 ignora a linha "ÚLTIMA ATUALIZAÇÃO" que está no topo dos seus arquivos
    df_mes = pd.read_csv(ficheiro, sep=';', encoding='latin-1', skiprows=1)
    
    # 3. Extrair o número do mês do nome do ficheiro para manter o histórico
    # Exemplo: do nome '...202501.csv' ele extrai '01'
    nome_base = os.path.basename(ficheiro)
    mes_str = nome_base.split('_')[-1].replace('.csv', '')[-2:]
    df_mes['MES_REFERENCIA'] = int(mes_str)
    
    lista_dataframes.append(df_mes)

# 4. Concatenar todos os DataFrames da lista num único objeto
if not lista_dataframes:
    raise SystemExit("Nenhum arquivo encontrado para concatenar. Verifique o diretório '2025' e o padrão dos arquivos.")

df_final = pd.concat(lista_dataframes, ignore_index=True)

# Salvar no mesmo diretório do script
output_path = os.path.join(script_dir, 'concatenado_2025teste.csv')
df_final.to_csv(output_path, index=False, sep=';', encoding='latin-1')
print(f"Arquivo salvo em: {output_path}")

# Verificar o resultado
print(f"Total de linhas após concatenação: {len(df_final)}")
print(df_final.head())

