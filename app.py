import streamlit as st
from openai import OpenAI

# Seiteneinstellungen
st.set_page_config(page_title="IP-Impact Engine", page_icon="🔮")

st.title("🔮 IP-Impact Engine")
st.subheader("Patentansprüche in Business-Value übersetzen")

# API Key Eingabe (Sicherer Weg über Sidebar)
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

if api_key:
    client = OpenAI(api_key=api_key)
    
    # Input Feld
    claims_input = st.text_area("Kopiere hier die Patentansprüche (Claims) rein:", height=200)

    if st.button("Strategie-Analyse generieren"):
        if claims_input:
            with st.spinner('Analysiere Patente...'):
                prompt = f"Analysiere diese Patentansprüche und erstelle eine Business-Summary mit: 1. Kern (einfach), 2. Wettbewerbs-Vorteil, 3. Monopoly-Frage, 4. Sales-Pitch, 5. Risiko. Claims: {claims_input}"
                
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}]
                )
                
                # Ergebnis anzeigen
                st.success("Analyse abgeschlossen!")
                st.markdown(response.choices[0].message.content)
        else:
            st.warning("Bitte gib zuerst Patentansprüche ein.")
else:
    st.info("Bitte gib deinen OpenAI API Key in der Sidebar ein, um zu starten.")
