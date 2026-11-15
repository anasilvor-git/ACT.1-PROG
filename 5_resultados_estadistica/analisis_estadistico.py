import numpy as np
import pandas as pd

# 1. Datos de abundancia microbiológica (Fase 3 - Ana)
abundancias = pd.DataFrame({
    "Microorganismo": [
        "Escherichia coli", "Enterococcus faecalis", "Acinetobacter sp.",
        "Bacillus subtilis", "Pseudomonas fluorescens"
    ],
    "Entrada_EDAR_UFC": [25000, 15000, 5000, 3000, 2000],
    "Salida_EDAR_UFC": [16, 8, 140, 180, 56],
    "Rio_Control_UFC": [8, 2, 30, 60, 100]
}).set_index("Microorganismo")

def shannon(serie):
    p = serie[serie > 0] / serie.sum()
    return -np.sum(p * np.log(p))

print("=== 1. DIVERSIDAD ALFA (ÍNDICE DE SHANNON) ===")
print(abundancias.apply(shannon).round(3))

# Eficiencia de remoción de patógenos fecales en la EDAR
remocion_ecoli = (1 - (16 / 25000)) * 100
print(f"\nEficiencia de remoción de E. coli en EDAR: {remocion_ecoli:.2f}%")

# 2. Análisis de impacto químico HPLC (Fase 4 - Yuly)
hplc = pd.DataFrame({
    "Compuesto": ["Cafeina", "Ibuprofeno", "Sulfametoxazol"],
    "Salida_EDAR_ugL": [18.4, 12.1, 8.3],
    "Aguas_Arriba_ugL": [2.1, 0.8, 0.5],
    "Aguas_Abajo_ugL": [8.7, 4.2, 2.9]
}).set_index("Compuesto")

hplc["Factor_Incremento_Arroyo"] = (hplc["Aguas_Abajo_ugL"] / hplc["Aguas_Arriba_ugL"]).round(2)
print("\n=== 2. IMPACTO QUÍMICO EN ARROYO (HPLC) ===")
print(hplc[["Aguas_Arriba_ugL", "Aguas_Abajo_ugL", "Factor_Incremento_Arroyo"]])

# 3. Impacto en riqueza taxonómica 16S rRNA (Fase 4 - Yuly)
riqueza = pd.Series(
    [85, 72, 65, 91, 110],
    index=["Entrada_EDAR", "Salida_EDAR", "Aguas_arriba", "Aguas_abajo", "Aguas_abajo_sedimento"]
)
incremento_riqueza = ((91 - 65) / 65) * 100
print(f"\n=== 3. IMPACTO BIOLÓGICO (16S rRNA) ===")
print(f"Incremento de riqueza taxonómica en agua (Aguas arriba -> Aguas abajo): +{incremento_riqueza:.1f}%")
