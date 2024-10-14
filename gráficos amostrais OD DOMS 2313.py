import pandas as pd
import matplotlib.pyplot as plt
import os

planilha = r'C:\Users\moesios\Desktop\DOMICILIAR GRÁFICOS\BANCO DE DADOS_ATUALIZADO REV01.xlsx'
df_morador = pd.read_excel(planilha, sheet_name='MORADOR')

modalidade_counts = df_morador['MODALIDADE TRABALHO'].value_counts()
modalidade_percentages = df_morador['MODALIDADE TRABALHO'].value_counts(normalize=True) * 100

plt.figure(figsize=(10, 6))
bars = modalidade_percentages.plot(kind='bar', color='skyblue')
plt.title('Modalidade de Trabalho')
plt.xticks(rotation=45)
plt.tight_layout()

for bar in bars.patches:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{bar.get_height():.2f}%',
        ha='center',
        va='bottom'
    )

plt.show()

dir_path = os.path.dirname(planilha)

txt_file_path = os.path.join(dir_path, 'modalidade_trabalho.txt')

with open(txt_file_path, 'w', encoding='utf-8') as f:
    for modalidade, count in modalidade_counts.items():
        percentage = modalidade_percentages[modalidade]
        f.write(f'{modalidade}: {count} ({percentage:.2f}%)\n')