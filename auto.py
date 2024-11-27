import streamlit as st
import schedule
import time

def task():
    st.write("Tarefa automatizada executada!")

# Configuração do agendamento
schedule.every(10).seconds.do(task)

# Loop para verificar agendamento
while True:
    schedule.run_pending()
    time.sleep(1)