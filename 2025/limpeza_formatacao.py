import pandas as pd
import numpy as np
import os

script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'concatenado_2025teste.csv')

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Arquivo não encontrado: {input_path}")

# 1. Carregar o arquivo unificado que você gerou
df = pd.read_csv(input_path, sep=';', encoding='latin-1')

print("Iniciando o pipeline de tratamento de dados...")

# ==========================================
# ETAPA 1: TRATAMENTO DAS COLUNAS FINANCEIRAS
# ==========================================
colunas_dinheiro = [
    'REMUN_BASICA', 'VANT_PESSOAIS', 'FUNC_COMISSIONADA', 'GRAT_NATALINA', 
    'HORAS_EXTRAS', 'OUTRAS_EVENTUAIS', 'ABONO_PERMANENCIA', 'REVERSAO_TETO_CONST', 
    'IMPOSTO_RENDA', 'PREVIDÊNCIA', 'FALTAS', 'REM_LIQUIDA', 'DIÁRIAS', 'AUXÍLIOS'
]

for col in colunas_dinheiro:
    if col in df.columns:
        # Remove espaços em branco, substitui a vírgula brasileira pelo ponto decimal
        df[col] = df[col].astype(str).str.strip().str.replace(',', '.')
        # Força a conversão para número (valores inválidos viram NaN temporariamente)
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Preenche valores vazios (NaN) das colunas financeiras com 0
df[colunas_dinheiro] = df[colunas_dinheiro].fillna(0)


# ==========================================
# ETAPA 2: TRATAMENTO DA COLUNA SÍMBOLO FUNÇÃO
# ==========================================
if 'SÍMBOLO FUNÇÃO' in df.columns:
    # 2.1 Preenche os valores nulos com a categoria padrão "SEM FUNÇÃO"
    df['SÍMBOLO FUNÇÃO'] = df['SÍMBOLO FUNÇÃO'].fillna('SEM FUNÇÃO')
    
    # 2.2 Limpa espaços em branco ocultos e padroniza tudo em maiúsculo
    df['SÍMBOLO FUNÇÃO'] = df['SÍMBOLO FUNÇÃO'].astype(str).str.strip().str.upper()
    
    # 2.3 Criação da hierarquia numérica (Ordinal Encoding)
    # Nota: Mapeamos do menor (sem função = 0) para os maiores níveis de gratificação (ex: FC-1 a FC-5)
    mapeamento_funcao = {
        'SEM FUNÇÃO': 0,
        'FC-1': 1,
        'FC-2': 2,
        'FC-3': 3,
        'FC-4': 4,
        'FC-5': 5
    }
    
    # Aplica o mapeamento. Caso apareça alguma sigla inesperada no CSV, o fillna(0) garante que não quebre
    df['FUNCAO_NUMERICA'] = df['SÍMBOLO FUNÇÃO'].map(mapeamento_funcao).fillna(0).astype(int)


# ==========================================
# ETAPA 3: PADRONIZAÇÃO DE OUTROS TEXTOS E NULOS
# ==========================================
if 'LOTAÇÃO EXERCÍCIO' in df.columns:
    df['LOTAÇÃO EXERCÍCIO'] = df['LOTAÇÃO EXERCÍCIO'].astype(str).str.strip().str.upper()

if 'CARGO' in df.columns:
    df['CARGO'] = df['CARGO'].fillna('NÃO APLICÁVEL').astype(str).str.strip().str.upper()

if 'REFERÊNCIA CARGO' in df.columns:
    df['REFERÊNCIA CARGO'] = df['REFERÊNCIA CARGO'].fillna('SEM REF').astype(str).str.strip().str.upper()


# ==========================================
# ETAPA 4: EXPORTAÇÃO DO ARQUIVO FINAL CLEAN
# ==========================================
arquivo_saida = os.path.join(script_dir, 'base_senado_pronta_mineracao.csv')
df.to_csv(arquivo_saida, sep=';', index=False, encoding='utf-8')

print(f"\n[SUCESSO] O arquivo limpo foi salvo como: '{arquivo_saida}'")
print("\n--- Amostra do tratamento da coluna Símbolo Função ---")
print(df[['SÍMBOLO FUNÇÃO', 'FUNCAO_NUMERICA']].drop_duplicates().reset_index(drop=True))