import streamlit as st
import requests

# Seiteneinstellungen
st.set_page_config(page_title="IP-Impact Engine", page_icon="🔮")

st.title("🔮 IP-Impact Engine (Free Edition)")
st.subheader("Patentansprüche in Business-Value übersetzen")

# Wir nutzen eine kostenlose API von Hugging Face (keine Kreditkarte nötig)
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

def query(payload):
    # Hier ist ein öffentlicher Token für die Demo. 
    # Für Profis: Später eigenen Account bei Hugging Face machen (auch kostenlos).
    response = requests.post(API_URL, json=payload)
    return response.json()

claims_input = st.text_area("Kopiere hier die Patentansprüche (Claims) rein:", height=200)

if st.button("Strategie-Analyse generieren"):
    if claims_input:
        with st.spinner('KI analysiert... (kann beim ersten Mal 10 Sek. dauern)'):
            prompt = f"Analysiere dieses Patent und antworte auf Deutsch: 1. Kern-Idee, 2. Business-Vorteil, 3. Sales-Pitch. Patent: {claims_input}"
            
            output = query({
                "inputs": prompt,
                "parameters": {"max_new_tokens": 500}
            })
            
            # Ergebnis anzeigen
            try:
                result = output[0]['generated_text'].split(prompt)[-1]
                st.success("Analyse fertig!")
                st.markdown(result)
            except:
                st.error("Der Server ist gerade beschäftigt. Bitte kurz warten und nochmal klicken!")
    else:
        st.warning("Bitte Text eingeben.")

st.divider()
st.caption("Läuft über Open-Source Modelle (Mistral/HuggingFace). Ohne OpenAI-Kosten.")
