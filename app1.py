# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:26:28 2025

@author: jperezr
"""


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Título de la aplicación
st.title("Análisis de Sentimientos - AFORE PENSIONISSSTE")

# Sidebar con resumen e información sobre la IA utilizada
with st.sidebar:
    st.header("Resumen")
    st.write("""
    Este código implementa una aplicación en Streamlit que:
    
    - Carga un archivo **Excel** con comentarios.
    - Usa **VADER** para analizar el sentimiento de cada comentario.
    - Clasifica los comentarios como **Positivos, Negativos o Neutrales**.
    - Muestra los resultados en un **DataFrame**.
    - Genera un **gráfico** con la distribución de los sentimientos.
    - Muestra **métricas clave** sobre los comentarios analizados.
    
    ✨ Perfecto para evaluar opiniones sobre **AFORE PENSIONISSSTE** de manera rápida e interactiva. 🎯
    """)

    st.header("🔍 ¿Qué tipo de IA usa este código?")
    st.write("""
    **Procesamiento de Lenguaje Natural (NLP)** 🧠  
    - Se usa para analizar texto y determinar su polaridad emocional (**positivo, negativo o neutral**).

    **IA Basada en Reglas y Lexicón** 📖  
    - **VADER** utiliza un diccionario de palabras con valores predefinidos de sentimiento.  
    - No es un modelo de **Machine Learning**, sino un método basado en **reglas heurísticas**.

    **Análisis de Sentimiento Léxico** 📊  
    - Evalúa cada palabra en un comentario y le asigna un **puntaje de sentimiento**.  
    - Calcula un **"compound score"**, que determina la **emoción general** del texto.
    
    - Desrrollado por: 
    - Javier Horacio Pérez Ricárdez    
    
    """)

# Cargar el archivo de Excel
archivo = st.file_uploader("Sube el archivo de comentarios (Excel)", type=["xlsx"])

if archivo is not None:
    # Leer el archivo
    df = pd.read_excel(archivo)

    # Mostrar los primeros 5 comentarios
    st.subheader("Primeros 5 Comentarios")
    st.write(df.head())

    # Inicializar el analizador de sentimientos
    analyzer = SentimentIntensityAnalyzer()

    # Función para analizar el sentimiento de un texto
    def analizar_sentimiento(texto):
        score = analyzer.polarity_scores(texto)
        if score['compound'] >= 0.05:
            return "Positivo"
        elif score['compound'] <= -0.05:
            return "Negativo"
        else:
            return "Neutral"

    # Aplicar el análisis de sentimientos a cada comentario
    df["Sentimiento Analizado"] = df["Comentario"].apply(analizar_sentimiento)

    # Mostrar los resultados del análisis
    st.subheader("Resultados del Análisis de Sentimientos")
    st.write(df)

    # Gráfico de distribución de sentimientos
    st.subheader("Distribución de Sentimientos")
    conteo_sentimientos = df["Sentimiento Analizado"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(conteo_sentimientos.index, conteo_sentimientos.values, color=["green", "blue", "red"])
    ax.set_xlabel("Sentimiento")
    ax.set_ylabel("Número de Comentarios")
    st.pyplot(fig)

    # Métricas clave
    st.subheader("Métricas Clave")
    st.write(f"Comentarios Positivos: {conteo_sentimientos.get('Positivo', 0)}")
    st.write(f"Comentarios Neutrales: {conteo_sentimientos.get('Neutral', 0)}")
    st.write(f"Comentarios Negativos: {conteo_sentimientos.get('Negativo', 0)}")
else:
    st.write("Por favor, sube un archivo de Excel para comenzar el análisis.")
