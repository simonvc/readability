import streamlit as st
import plotly.graph_objects as go
import textstat

if __name__ == "__main__":

    st.title("TextStat Online")

    '''## Readability Text Stats for Writers, Journalists and Teachers'''
    '''This tool will help you asses the readability of a paragraph of text according to various measures.'''

    sankey="""The quick brown fox jumped over lazy dog"""

    test_data = st.text_area(value=sankey, label="Paste the text you want assessed here:") 




    if sankey != test_data:
        cscore = textstat.text_standard(test_data, float_output=True)
        if cscore > 15:
            st.warning("## Consensus Score is %s, This requires advanced comprehension" % cscore)
        elif cscore > 10:
            st.info("## Consensus score is %s, This requires educated adult comprehension" % cscore)
        elif cscore > 7:
            st.info("## Consensus score is %s, This requires high school level comprehension" % cscore)
        else:
            st.info("## Consensus score is %s, This could be read by a primary school student" % cscore)
    else:
        st.info("## Your result will appear here when you have pasted and submitted your text above.")


    "## The Flesch Reading Ease formula"
    """Returns the Flesch Reading Ease Score.

While the maximum score is 121.22, there is no limit on how low the score can be. A negative score is valid.

https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch_reading_ease
"""
    fre=textstat.flesch_reading_ease(test_data)
    if fre > 90:
        st.info("Very Easy: %f" % fre)
    elif fre > 80:
        st.info("Easy: %f" % fre)
    elif fre > 70:
        st.info("Fairly Easy: %f" % fre)
    elif fre > 60:
        st.info("Standard: %f" % fre)
    elif fre > 50:
        st.info("Fairly Difficult: %f" % fre)
    elif fre > 30:
        st.info("Difficult: %f" % fre)
    else:
        st.warning("Very Confusing: %f" % fre)
    
    
    """## SMOG index """
    """Returns the SMOG index of the given text. This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document.

Texts of fewer than 30 sentences are statistically invalid, because the SMOG formula was normed on 30-sentence samples. textstat requires at least 3 sentences for a result.
https://en.wikipedia.org/wiki/SMOG
"""
    st.info(textstat.smog_index(test_data))

    """## Flesch Kincaid Grade"""
    """Returns the Flesch-Kincaid Grade of the given text. This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document.
    https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch%E2%80%93Kincaid_grade_level"""
    st.info(textstat.flesch_kincaid_grade(test_data))

    """## Coleman Liau Index"""
    """Returns the grade level of the text using the Coleman-Liau Formula. This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document.
    https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index"""
    st.info(textstat.coleman_liau_index(test_data))


    """## Automated Readability Index"""
    """Returns the ARI (Automated Readability Index) which outputs a number that approximates the grade level needed to comprehend the text.

For example if the ARI is 6.5, then the grade level to comprehend the text is 6th to 7th grade.
https://en.wikipedia.org/wiki/Automated_readability_index"""
    st.info(textstat.automated_readability_index(test_data))


"""## Dale Chall Readability Score
Different from other tests, since it uses a lookup table of the most commonly used 3000 English words. Thus it returns the grade level using the New Dale-Chall Formula.
https://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formula"""


dcr = textstat.dale_chall_readability_score(test_data)
if dcr > 9:
    st.info("Readability is at a colleague level: %f" % dcr)
elif dcr > 8:
    st.info("Readability is at a senior 11th or 12th grade level: %f" % dcr)
elif dcr > 7:
    st.info("Readability is at a 9th or 10th grade level: %f" % dcr)
elif dcr > 6:
    st.info("Readability is at a 7th or 8th grade level: %f" % dcr)
elif dcr > 5:
    st.info("Readability is at a 5th or 6th grade level: %f" % dcr)
else:
    st.info("Readability is at a 4th or lower level: %f" % dcr)


"""## Difficult Word Score"""
st.info(textstat.difficult_words(test_data))

"""## Linsear Write Formula"""
st.info(textstat.linsear_write_formula(test_data))

"""Gunning Fog Score"""
st.info(textstat.gunning_fog(test_data))



st.info("This tool based on https://github.com/shivam5992/textstat and available to fork and improve at https://github.com/simonvc/readability")