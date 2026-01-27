import streamlit as st
from openai import OpenAI

# 1. Verbindung zu OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="IP-Intelligence Hub", page_icon="🔮")

# 2. Passwort-Abfrage in der Sidebar
st.sidebar.title("🔐 Zugriffskontrolle")
user_password = st.sidebar.text_input("Bitte Passwort eingeben:", type="password")

st.title("🔮 IP-Intelligence Hub")
st.markdown("### Strategische Patent-Analyse via GPT-4o")

# 3. Prüfung des Passworts
if user_password == st.secrets["APP_PASSWORD"]:
    st.sidebar.success("Zugriff gewährt!")
    
    claims_input = st.text_area(
        "Patentansprüche hier einfügen:", 
        height=250, 
        placeholder="1. Vorrichtung zur Datenverarbeitung..."
    )

    if st.button("Strategie-Analyse generieren"):
        if claims_input:
            with st.spinner('KI analysiert...'):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "Du bist ein erfahrener Patentanwalt. Analysiere präzise auf Deutsch."},
                            {"role": "user", "content": f"Analysiere diesen Anspruch:\n\n{claims_input}"}
                        ]
                    )
                    st.success("Analyse abgeschlossen")
                    st.markdown("---")
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Fehler: {e}")
        else:
            st.warning("Bitte Text eingeben.")
else:
    # Wenn das Passwort falsch oder leer ist
    if user_password != "":
        st.sidebar.error("Falsches Passwort!")
    st.info("Bitte gib das Passwort in der Sidebar links ein, um das Tool freizuschalten.")

st.divider()
st.caption("Hinweis: KI-gestütztes Tool. Keine Rechtsberatung.")
