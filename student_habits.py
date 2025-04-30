import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o dataset
df = pd.read_csv('D:/PyProjetos/pjt002/Analise-de-Habitos-Estudantis-e-Desempenho-em-Exames/student_habits_performance.csv')

# Limpeza: removendo valores ausentes em colunas críticas
df.dropna(subset=['parental_education_level'], inplace=True)

# Mapeando nomes para o português
mapeamento_colunas = {
    'study_hours_per_day': 'horas_de_estudo_por_dia',
    'social_media_hours': 'horas_de_redes_sociais',
    'attendance_percentage': 'percentual_de_frequencia',
    'exercise_frequency': 'frequencia_de_exercicio',
    'exam_score': 'nota_do_exame',
    'netflix_hours': 'horas_de_netflix',
    'sleep_hours': 'horas_de_sono',
    'mental_health_rating': 'avaliacao_saude_mental'
}
df.rename(columns=mapeamento_colunas, inplace=True)

# Selecionando colunas para análise
colunas = [
    'horas_de_estudo_por_dia',
    'horas_de_redes_sociais',
    'horas_de_netflix',
    'horas_de_sono',
    'avaliacao_saude_mental',
    'percentual_de_frequencia',
    'frequencia_de_exercicio',
    'nota_do_exame'
]

# Calculando correlação
matriz_de_correlacao = df[colunas].corr()

# Exibindo heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(matriz_de_correlacao, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.title('Correlação entre Hábitos e Nota no Exame')
plt.tight_layout()
plt.show()

# Correlação com a nota
correlacoes = matriz_de_correlacao['nota_do_exame'].sort_values()

print("\nFatores que mais ATRAPALHAM a nota:")
print(correlacoes.head(5))

print("\nFatores que mais AJUDAM a nota:")
print(correlacoes.tail(5))

# Gráfico de correlação com nota
plt.figure(figsize=(10, 5))
correlacoes.drop('nota_do_exame').sort_values().plot(kind='barh', color='skyblue')
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Correlação dos Hábitos com a Nota no Exame')
plt.xlabel('Correlação')
plt.tight_layout()
plt.show()
