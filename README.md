# Projeto de Mineração de Dados: Análise de Remuneração e Horas Extras (Senado Federal 2025)

Este repositório contém o projeto avaliativo desenvolvido para a disciplina de **Mineração de Dados** do curso de Tecnólogo de Inteligência Artificial da **FATEC RC**.

## 📋 Descrição do Projeto
O trabalho consiste na aplicação de técnicas de extração de conhecimento a partir de bases de dados reais do **Senado Federal Brasileiro** referente ao ano de 2025. A análise busca identificar padrões salariais, correlações entre departamentos e o volume de horas extras pagas aos servidores.

## 🎯 Objetivos
*   Analisar a distribuição salarial entre diferentes categorias e cargos.
*   Agrupar departamentos com perfis remuneratórios semelhantes.
*   Descobrir regras de associação entre cargos, lotações e o recebimento de horas extras.

## 📊 Base de Dados
A base de dados é composta por **12 arquivos CSV** (Janeiro a Dezembro de 2025) extraídos do Portal da Transparência do Senado Federal.
*   **Atributos Principais:** Categoria, Cargo, Lotação Exercício, Tipo de Folha (Normal/Suplementar), Remuneração Básica e Horas Extras.
*   **Quantidade de registros:** Dados consolidados de todos os servidores ativos e parlamentares ao longo do ano de 2025.

## 🛠️ Técnicas de Mineração Aplicadas
Seguindo os requisitos pedagógicos, o projeto utiliza:

1.  **Agrupamento de Dados (Clustering):**
    *   **Algoritmo:** K-Means.
    *   **Objetivo:** Segmentar as lotações de exercício com base na média de `REMUN_BASICA` e no volume de `HORAS_EXTRAS`.
2.  **Regras de Associação:**
    *   **Algoritmo:** Apriori / FP-Growth.
    *   **Objetivo:** Identificar padrões do tipo "Se o servidor pertence ao cargo X e departamento Y, então a chance de horas extras acima do limite Z é de W%".

## 📂 Estrutura do Repositório
Conforme as instruções de entrega:
*   `/2025`: Contém os arquivos CSV originais utilizados na análise.
*   `/projeto`: Códigos desenvolvidos (Notebooks/Scripts Python).
*   `/documentos`: Relatório final escrito em PDF contendo Introdução, Justificativa e Revisão da Literatura.
*   `/apresentacao`: Slides da apresentação do projeto.

## 👥 Equipe
*   **Brendol Alves**
*   **Gabriel Nascimento**
*   **Luiz Henrique**

## 📅 Datas Importantes
*   **Entrega do Repositório:** 28/05.
*   **Apresentações:** Entre 29/05 e 12/06 (Duração: 15 a 20 minutos).

---
*Este projeto foi desenvolvido estritamente para fins acadêmicos utilizando dados públicos sob a Lei de Acesso à Informação.*
