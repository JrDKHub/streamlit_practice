import streamlit as st
from textblob import TextBlob
from deep_translator import GoogleTranslator

# function to calculate subjectivity
def getSubjectivity(review):
    return TextBlob(review).sentiment.subjectivity

# function to calculate polarity
def getPolarity(review):
    return TextBlob(review).sentiment.polarity

# function to analyze the reviews
def analysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

# function to analyze the reviews #Fine-grain
def analysis2(score):
    if score < -0.7:
        return 'Very Negative'
    elif score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    elif score > 0.7:
        return 'Very Positive'
    elif score > 0:
        return 'Positive'



st.title("Un peu de NLP")

t = st.text_input('phrase')


if st.button('Analyser'):
    translated = GoogleTranslator(source='auto', target='en').translate(t)
    translated
    subj = getSubjectivity(translated)
    pol = getPolarity(translated)
    sentiment = analysis(pol)
    st.write(pol)
    st.write(subj)
    st.write(sentiment)