import streamlit as st 
import pandas as pd
import plotly.express as px
def main():
    st.set_page_config(
        page_title="graficos interativos",
        page_icon="📈",
        layout="wide"
    )
    # Código do anúncio do Google AdSense
    adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-XXXXXX" 
     data-ad-slot="XXXXXX"
     data-ad-format="auto"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

    # Exibir o anúncio
    st.markdown(adsense_code, unsafe_allow_html=True)
   
    st.title("Gráficos interativos")
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")
    st.write("dados utilizados")
    st.dataframe(df)

    st.subheader("gráfico de dispessão")
    fig = px.scatter(df,x="gdpPercap",y="lifeExp",size="pop",color="continent",hover_name="country",log_x=True,size_max=60)
    st.plotly_chart(fig)

    st.subheader("gráfico de linhas")
    df_continente=df.groupby(['continent','year'])['lifeExp'].mean().reset_index()
    fig=px.line(df_continente,x="year",y="lifeExp",color="continent",line_group="continent",title="Expectativa de vida por ano e continente")
    st.plotly_chart(fig)

    st.subheader("gráfico de barras")
    fig = px.bar(df,x="continent",y="pop",color="continent",barmode="relative",title="População por continente")
    st.plotly_chart(fig)
main()