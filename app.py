import streamlit as st
import requests

st.set_page_config(page_title="IP-Impact Engine", page_icon="🔮")

st.title("🔮 IP-Impact Engine")
st.subheader("Free Open-Source Edition")

# Wir nutzen ein robustes Modell von Hugging Face
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

claims_input = st.text_area("Patentansprüche hier einfügen:", height=200, placeholder="z.B. 1. Vorrichtung umfassend...")

if st.button("Strategie-Analyse generieren"):
    if claims_input:
        with st.spinner('KI analysiert... bitte Geduld...'):
            # Wir bauen einen klaren Prompt
            prompt = f"<s>[INST] Analysiere diesen Patentanspruch auf Deutsch. Gib 3 Punkte aus: 1. Kern der Erfindung, 2. Wirtschaftlicher Vorteil, 3. Strategische Empfehlung. Patent: {claims_input} [/INST]"
            
            output = query({
                "inputs": prompt,
                "parameters": {"max_new_tokens": 500, "return_full_text": False}
            })
            
            if isinstance(output, list) and len(output) > 0:
                result = output[0].get('generated_text', 'Keine Antwort erhalten.')
                st.success("Analyse abgeschlossen!")
                st.markdown(result)
            else:
                st.error("Der KI-Server startet gerade neu. Bitte klicke in 30 Sekunden noch einmal auf den Button.")
    else:
        st.warning("Bitte gib einen Text ein.")

st.divider()
st.info("Hinweis: Diese Version nutzt kostenlose Ressourcen. Bei Überlastung kann es zu Verzögerungen kommen.")
