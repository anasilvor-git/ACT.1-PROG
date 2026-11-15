# Fase 5: Resultados Integrados y Análisis Estadístico

**Responsable:** Anthony Mero  
**Objetivo:** Integrar los datos microbiológicos (Fase 3) y fisicoquímicos/moleculares (Fase 4) mediante bioinformática y estadística para evaluar el impacto del vertido de la EDAR sobre el Arroyo EDER.

## Hallazgos Principales (Cruce de Datos)

1. **Trazadores Químicos (HPLC):**
   - Los fármacos y estimulantes actúan como marcadores inequívocos de vertido antropogénico. La Cafeína aumenta de `2.1 µg/L` (Aguas arriba) a `8.7 µg/L` (Aguas abajo), y el antibiótico Sulfametoxazol pasa de `0.5 µg/L` a `2.9 µg/L` tras recibir el efluente de la EDAR (`18.4` y `8.3 µg/L`, respectivamente).

2. **Eficiencia de Depuración vs. Carga Biológica:**
   - La EDAR reduce la carga de indicadores fecales viables en más del 99.9% (*Escherichia coli* cae de `25,000` a `16 UFC/mL`), incrementando las células no viables del `24%` al `38%` (citometría de flujo).
   - Sin embargo, el ADN total (`28.4 ng/µL` en salida EDAR) y la secuenciación 16S rRNA demuestran que el vertido eleva la riqueza taxonómica del arroyo de 65 taxones (Aguas arriba) a 91 en columna de agua y 110 en el sedimento de Aguas abajo.

3. **Diversidad Alfa y Rastreo de Fuentes (Source Tracking):**
   - La comunidad del río control está dominada por *Pseudomonas fluorescens* (50%), mientras que el efluente EDAR aporta principalmente *Bacillus subtilis* (45%) y *Acinetobacter sp.* (35%), alterando la estructura comunitaria aguas abajo.

## Archivos de esta carpeta

- `README.md`: Resumen estadístico e interpretación biológica integrada.
- `analisis_estadistico.py`: Script en Python que procesa los datos reales de las Fases 3 y 4 (cálculo de índice de diversidad de Shannon, tasas de remoción y factores de enriquecimiento químico/biológico).
