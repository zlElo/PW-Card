import streamlit as st
from generator import create_password_card
from tools.id import id_gen
from searching import search_file

# Konfiguriere die Seite
st.set_page_config(page_title='PW-Card', page_icon=':credit_card:', layout='centered')
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Überschrift
st.title('PW-Card')
st.header('A way, to know every secure password')

# Fragen und Antworten
with st.expander('QA'):
    # Was ist PW-Card? - Seite
    st.subheader('What is PW-Card?')
    st.markdown('PW-Card is a web tool that is coded in Python and allows you to create password cards. Password maps help you to know every password. You only need to remember the coordinates on the card, e.g. a1-k1.')

    # Ist es sicher? - Seite
    st.subheader('Is it secure?')
    st.markdown('PW-Card is completely open source and anyone can view the code. Nothing is stored except the password card! This tool is designed to help you stay more secure and not be the next website to lose your information due to a security incident.')

    st.subheader('What is stored?')
    st.markdown('Nothing of yours will be saved. Only the generated cards are stored permanently in order to make the re-download feature available. Your own password card with a unique ID is generated on the server. You can then download this as a PDF. If you lose the PDF and want to print out your password card again, you can enter the ID of your card in the search and download the PDF.')

st.write('---')

# example password card
st.image('files/example_pic.png', caption='Example card', width=None, use_column_width=True, output_format='auto')
# Generieren-Schaltfläche
if st.button('Generate'):
    st.write('---')
    st.write('Your own password card has been successfully generated! In the box below you can write down the ID in case you lose your printed card. Click on the "Download" button to download the PDF.')
    id = id_gen()
    create_password_card(f"archive/{id}.pdf", 15, 26, id)

    st.code(f'{id}')

    with open(f'archive/{id}.pdf', "rb") as file:
        st.download_button(
            label="Download",
            data=file,
            file_name=f'{id}.pdf',
            mime='pdf',
        )



st.write('---')
st.write('Already have a card?')
if st.text_input("Enter your existing ID:", key="search").strip():
    search_id = st.session_state.search
    check = search_file(search_id)
    if check == True:
        with open(f'archive/{search_id}.pdf', "rb") as file:
            st.download_button(
                label="Download",
                data=file,
                file_name=f'{search_id}.pdf',
                mime='pdf',
            )
    else:
        st.warning('Unfortunately, this ID could not be found in the database. Maybe you mistyped it?')

    
    
        

st.markdown(
    """
    <style>
    button[kind="primary"] {
        background: none!important;
        border: none;
        padding: 0!important;
        color: white !important;
        text-decoration: none;
        cursor: pointer;
        border: none !important;
    }
    button[kind="primary"]:hover {
        text-decoration: none;
        color: white !important;
    }
    button[kind="primary"]:focus {
        outline: none !important;
        box-shadow: none !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

    