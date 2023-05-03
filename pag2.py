import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_house = pd.read_csv('https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/formart_house.csv')
df_house.rename(columns={"medv":"price"}, inplace=True)
df_house.drop(df_house.tail(1).index,inplace=True)
s = df_house.select_dtypes(include='object').columns
df_house[s] = df_house[s].astype("float")


def show_footer():
    st.markdown("")




def main():
    st.title ("GRAFICHIAMO")

    # df_house = pd.read_csv('https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/formart_house.csv')
    # df_house.rename(columns={"medv":"price"}, inplace=True)
    # df_house.drop(df_house.tail(1).index,inplace=True)
    # s = df_house.select_dtypes(include='object').columns
    # df_house[s] = df_house[s].astype("float")

    option = st.radio (
    'che grafico vuoi visualizzare?',
    ('Correlation Matrix', 'Pair Plot',), horizontal=True)

    if option == 'Correlation Matrix':
        df_house = pd.read_csv('https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/formart_house.csv')
        df_house.rename(columns={"medv":"price"}, inplace=True)
        df_house.drop(df_house.tail(1).index,inplace=True)
        s = df_house.select_dtypes(include='object').columns
        df_house[s] = df_house[s].astype("float")
        fig,ax=plt.subplots()
        sns.heatmap(df_house.corr(),annot=True)
        st.write(fig)

    elif option == 'Pair Plot':
        df_house = pd.read_csv('https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/formart_house.csv')
        df_house.rename(columns={"medv":"price"}, inplace=True)
        df_house.drop(df_house.tail(1).index,inplace=True)
        s = df_house.select_dtypes(include='object').columns
        df_house[s] = df_house[s].astype("float")
        pairplot=sns.pairplot(df_house,hue='price',height=3, aspect=1)
        st.pyplot(pairplot)



    # graph_name = ["CorrelationMatrix","PairPlot"]
    # OPTIONS = graph_name

    # graph_selection = st.selectbox('Che grafico vuoi visualizzare?', OPTIONS)


    # if graph_selection ==  graph_selection[0]:
    #     correlation_matrix()
    # elif graph_selection ==  graph_selection[1]:
    #     pair_plot()
    # else:
    #     st.markdown("Something went wrong. We are looking into it.")





    #     # fig,ax=plt.subplots()
    #     # sns.heatmap(df_house.corr(),annot=True)
    #     # st.write(fig)


    #     # sns.pairplot(df_house,hue='price',height=3, aspect=1)


    show_footer()

if __name__ == "__main__":
    main()
