import pandas as pd
import matplotlib.pyplot as plt

# Carregando o conjunto de dados
data_path = "/mnt/data/cases-brazil-cities.csv"
df = pd.read_csv(data_path)

# Limpeza inicial
df = df.dropna(subset=['totalCases', 'deaths'])  # Removendo linhas com valores nulos em totalCases ou deaths
df['totalCases'] = pd.to_numeric(df['totalCases'], errors='coerce')
df['deaths'] = pd.to_numeric(df['deaths'], errors='coerce')
df = df.dropna(subset=['totalCases', 'deaths'])

# Removendo a linha de total por estado/país, se presente
df = df[~df['city'].str.contains("TOTAL", na=False)]

# 1. Cidade com mais casos de covid
city_most_cases = df.loc[df['totalCases'].idxmax()]

# 2. Cidade com menos casos de covid
city_least_cases = df.loc[df['totalCases'].idxmin()]

# Agrupando por estado
states_grouped = df.groupby('state').sum()

# 3. Estado com mais casos de covid
state_most_cases = states_grouped['totalCases'].idxmax()

# 4. Estado com menos casos de covid
state_least_cases = states_grouped['totalCases'].idxmin()

# 5. Cidade com mais mortes por covid
city_most_deaths = df.loc[df['deaths'].idxmax()]

# 6. Cidade com menos mortes por covid
city_least_deaths = df.loc[df['deaths'].idxmin()]

# 7. Estado com mais mortes por covid
state_most_deaths = states_grouped['deaths'].idxmax()

# 8. Estado com menos mortes por covid
state_least_deaths = states_grouped['deaths'].idxmin()

# 9. Total de casos de covid no Brasil
total_cases_brazil = df['totalCases'].sum()

# 10. Total de mortes por covid no Brasil
total_deaths_brazil = df['deaths'].sum()

# Exibindo os resultados
print("Cidade com mais casos de COVID:", city_most_cases['city'], "- Casos:", city_most_cases['totalCases'], "- Mortes:", city_most_cases['deaths'])
print("Cidade com menos casos de COVID:", city_least_cases['city'], "- Casos:", city_least_cases['totalCases'], "- Mortes:", city_least_cases['deaths'])
print("Estado com mais casos de COVID:", state_most_cases)
print("Estado com menos casos de COVID:", state_least_cases)
print("Cidade com mais mortes por COVID:", city_most_deaths['city'], "- Mortes:", city_most_deaths['deaths'], "- Casos:", city_most_deaths['totalCases'])
print("Cidade com menos mortes por COVID:", city_least_deaths['city'], "- Mortes:", city_least_deaths['deaths'], "- Casos:", city_least_deaths['totalCases'])
print("Estado com mais mortes por COVID:", state_most_deaths)
print("Estado com menos mortes por COVID:", state_least_deaths)
print("Total de casos de COVID no Brasil:", total_cases_brazil)
print("Total de mortes por COVID no Brasil:", total_deaths_brazil)

# 11. Gráfico: 5 estados com mais mortes
top5_states_deaths = states_grouped['deaths'].nlargest(5)
plt.figure(figsize=(10, 6))
top5_states_deaths.plot(kind='bar', color='red', alpha=0.7)
plt.title("5 Estados com Mais Mortes por COVID")
plt.ylabel("Número de Mortes")
plt.xlabel("Estado")
plt.show()

# 12. Gráfico: 5 estados com menos mortes
bottom5_states_deaths = states_grouped['deaths'].nsmallest(5)
plt.figure(figsize=(10, 6))
bottom5_states_deaths.plot(kind='bar', color='blue', alpha=0.7)
plt.title("5 Estados com Menos Mortes por COVID")
plt.ylabel("Número de Mortes")
plt.xlabel("Estado")
plt.show()
