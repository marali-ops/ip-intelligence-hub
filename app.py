import streamlit as st
from openai import OpenAI

# 1. Verbindung zu OpenAI (nutzt deinen Key aus den Secrets)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 2. Layout der App
st.set_page_config(page_title="IP-Intelligence Hub", page_icon="🔮")

st.title("🔮 IP-Intelligence Hub")
st.markdown("### Strategische Patent-Analyse via GPT-4o")

# 3. Eingabefeld (Ganz links am Rand!)
claims_input = st.text_area(
    "Patentansprüche hier einfügen:", 
    height=250, 
    placeholder="1. Vorrichtung zur Datenverarbeitung, umfassend..."
)

# 4. Analyse-Logik
if st.button("Strategie-Analyse generieren"):
    if claims_input:
        with st.spinner('KI analysiert die Ansprüche... bitte warten.'):
            try:
                # Der "Prompt" – hier sagen wir der KI, wie sie arbeiten soll
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "Du bist ein erfahrener Patentanwalt und Strategieberater. Analysiere die Ansprüche präzise, strukturiert und professionell auf Deutsch."},
                        {"role": "user", "content": f"Analysiere folgenden Patentanspruch:\n\n{claims_input}\n\nGib mir:\n1. Eine Zusammenfassung des Kerns der Erfindung.\n2. Die größten wirtschaftlichen Vorteile.\n3. Eine Einschätzung zur Durchsetzbarkeit (Infringement-Check Potential)."}
                    ]
                )
                
                # Ergebnis ausgeben
                st.success("Analyse abgeschlossen")
                st.markdown("---")
                st.markdown(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"Fehler: {e}")
    else:
        st.warning("Bitte füge zuerst Patentansprüche ein.")

# 5. Disclaimer (Wichtig für die Außenwirkung)
st.divider()
st.caption("Hinweis: Dies ist ein KI-gestütztes Tool. Die Ergebnisse dienen der strategischen Orientierung und ersetzen keine Rechtsberatung durch einen zugelassenen Patentanwalt.")
