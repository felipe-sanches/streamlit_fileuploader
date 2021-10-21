#!/usr/bin/python3

# importar as bibliotecas necessárias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit import uploaded_file_manager
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

#Analise dos dados
def data_analysis(file):

    #importando dataframe
    df = pd.read_excel(file)
    
    #Igualando os registros sem medição à 0
    df= df.replace('NV', 0)

    #tratando nomes de colunas
    mapping = {df.columns[7]:'Upload', df.columns[8]: 'Download'}
    df = df.rename(columns=mapping)
    
    #atribuindo score aos registros
    df["score"]= df["Upload"] + df["Download"]


    # plotar o scatterplot
    fig1, ax = plt.subplots()

    fig1 = px.scatter(df,
        y="Download",
        x="Upload",
        color="score",
        title="Taxas de Download e Upload",
        labels={
            "Download":"Download (Mbps)",
            "Upload":"Upload (Mbps)",
            "score":"Score"
        } 
            )
    st.write(fig1)


    #plotando boxplot de Download
    df['Download'].plot(kind='box', vert=False, figsize=(10,3));
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())
    
    #plotando boxplot de Upload
    df['Upload'].plot(kind='box', vert=False, figsize=(10,3));
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(plt.show())



def main():

    st.title("Medições Qualidade de Conexão")

    #Widget para upload de arquivo
    uploaded_file = st.sidebar.file_uploader("Faça upload do arquivo em EXCEL:")

    if uploaded_file is not None:
        data_analysis(uploaded_file)



if __name__ == '__main__':
    main()