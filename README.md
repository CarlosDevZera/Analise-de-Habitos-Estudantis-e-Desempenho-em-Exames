# 📊 Análise de Hábitos Estudantis e Desempenho em Provas

Este projeto realiza uma análise exploratória de dados para identificar **quais hábitos influenciam positiva ou negativamente a nota de estudantes em provas**.

## 🧠 Objetivo

Avaliar a correlação entre diferentes hábitos (como horas de estudo, sono, uso de redes sociais, etc.) e o desempenho dos estudantes em exames, utilizando um **heatmap de correlação** e gráficos descritivos.

## 🗂️ Dataset

O conjunto de dados utilizado está disponível em:  
🔗 [Student Habits vs Academic Performance – Kaggle](https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance)

## 📌 Funcionalidades

- Limpeza dos dados (remoção de valores nulos em colunas críticas).
- Tradução dos nomes das colunas para o português.
- Cálculo da matriz de correlação entre os hábitos e a nota do exame.
- Visualização da matriz de correlação com `seaborn`.
- Gráfico de barras com os fatores que mais **ajudam** e **atrapalham** a nota.

## 📷 Exemplos de Visualizações

- **Heatmap de Correlação**  
  Mostra visualmente a força da relação entre diferentes hábitos e o desempenho.
  
- **Gráfico de Barras Horizontal**  
  Destaca os hábitos que mais impactam positivamente e negativamente a nota no exame.

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Instale as dependências:
   ```bash
   pip install pandas seaborn matplotlib
   ```
3. Baixe o dataset do link do Kaggle e coloque o arquivo CSV no diretório do projeto.
   🔗 [Student Habits vs Academic Performance – Kaggle](https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance)

4. Execute o script:
   ```bash
   python analise_habitos_estudantis.py
   ```
✍️ Autor
Feito com carinho por Carlos Alberto



