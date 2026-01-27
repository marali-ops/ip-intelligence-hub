import streamlit as st
import requests
import time

st.set_page_config(page_title="IP-Impact Engine", page_icon="🔮")

st.title("🔮 IP-Impact Engine")
st.subheader("Strategische Patent-Analyse")

# Neues, stabileres Modell (Google Gemma)
API_URL = "https://api-inference.huggingface.co/models/google/gemma-1.1-7b-it"
headers = {"Authorization": "Bearer hf_VvSNoYmzXpXpXpXpXpXpXpXpXpXpXp"} # Nur ein Platzhalter

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

claims_input = st.text_area("Patentansprüche hier einfügen:", height=200)

if st.button("Analyse starten"):
    if claims_input:
        with st.spinner('KI wird geweckt... bitte ggf. 2x klicken...'):
            # Wir machen den Prompt noch klarer
            prompt = f"User: Analysiere diesen Patentanspruch auf Deutsch. 1. Kern der Idee, 2. Vorteil, 3. Strategie. Anspruch: {claims_input}\nAssistant:"
            
            data = query({"inputs": prompt, "parameters": {"max_new_tokens": 500}})
            
            # Fehlerprüfung
            if isinstance(data, dict) and "error" in data:
                if "estimated_time" in data:
                    st.info(f"Modell lädt noch... Bitte in {int(data['estimated_time'])} Sekunden nochmal klicken.")
                else:
                    st.error("Server antwortet nicht. Ich probiere ein Ersatz-Modell...")
                    # Ersatz-Modell-URL falls Gemma hakt
                    API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
            elif isinstance(data, list) and len(data) > 0:
                result = data[0].get('generated_text', '').split("Assistant:")[-1]
                st.success("Analyse fertig!")
                st.markdown(result)
            else:
                st.warning("Kein Ergebnis. Bitte Button erneut drücken.")
    else:
        st.warning("Bitte Text eingeben.")
