import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
from transformers import pipeline

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')

st.title('Aplikacja Streamlit do przetwarzania języka naturnalnego')
st.header('Wydźwięk oraz tłumaczenie tekstu')

st.subheader('O Streamlit')
st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')

#st.image('slownik.jpg', caption='Słownik', use_column_width=True)

st.subheader('Instrukcja użytkowania')
st.write('Aplikacja umożliwia analizę wydźwięku tekstu oraz tłumaczenie z języka angielskiego na język niemiecki.')
st.write('Wybierz odpowiednią opcję z listy poniżej, a następnie wprowadź tekst do analizy lub tłumaczenia oraz wciśnij ctrl + enter.')

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumaczenie tekstu z angielskiego na niemiecki",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner('Analiza wydźwięku...'):
            time.sleep(5)
            classifier = pipeline("sentiment-analysis")
            answer = classifier(text)
            st.success('Zakończono!')
            st.balloons()
            st.write(answer)

            if answer[0]['label'] == 'POSITIVE':
                st.image('happy_image.jpg', caption='Pozytywny Wydźwięk', use_column_width=True)
            else:
                st.image('sad_image.jpg', caption='Negatywny Wydźwięk', use_column_width=True)

if option == "Tłumaczenie tekstu z angielskiego na niemiecki":
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner('Tłumaczenie tekstu...'):
            time.sleep(5)
            translator = pipeline("translation_en_to_de")
            answer = translator(text, max_length=512)
            st.success('Zakończono!')
            st.balloons() 
            st.write(answer[0]['translation_text'])

            st.image('deutch_image.jpg', caption='Deutch', use_column_width=True)

st.write('Numer indeksu: s22275')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
