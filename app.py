import streamlit as st
from openai import OpenAI

# 1. Verbindung zu OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="IP-Intelligence Hub", page_icon="🔮")

# 2. Passwort-Abfrage in der Sidebar
st.sidebar.title("🔐 Zugriffskontrolle")
user_password = st.sidebar.text_input("Bitte Passwort eingeben:", type="password")

st.title("🔮 IP-Intelligence Hub")
st.markdown("### Strategische Patent-Analyse (Premium Edition)")

# 3. Prüfung des Passworts
if user_password == st.secrets["APP_PASSWORD"]:
    st.sidebar.success("Zugriff gewährt!")
    
    claims_input = st.text_area(
        "Patentansprüche hier einfügen:", 
        height=250, 
        placeholder="1. Vorrichtung zur..."
    )

    if st.button("Strategie-Analyse generieren"):
        if claims_input:
            with st.spinner('KI führt Tiefenanalyse durch...'):
                try:
                    # Der optimierte "Profi-Prompt"
                    response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "Du bist ein erfahrener Patentanwalt und Strategieberater. Analysiere präzise auf Deutsch."},
                        {"role": "user", "content": f"""Analysiere diesen Patentanspruch extrem detailliert nach folgendem Schema:

1. **Der Kern der Erfindung**: Was ist der technische 'Clou' in einfachen Worten?
2. **Gibt es das schon? (Einschätzung der Neuheit)**: Basierend auf deinem Wissen, ist dies ein bekannter Standard oder eine echte Innovation? Welche ähnlichen Konzepte gibt es bereits?
3. **Wettbewerbsvorteil & Monopol-Potenzial**: Wie schwer ist es für die Konkurrenz, das zu umgehen? Erzeugt das ein echtes Markt-Monopol?
4. **Der Sales Pitch**: Wie würde man diese Erfindung einem Investor oder Kunden in 2 Sätzen schmackhaft machen?
5. **Risiko-Check**: Wo sind die Schwachstellen im Anspruch? Was könnte ein Wettbewerber nutzen, um das Patent anzugreifen?

Anspruch:\n\n{claims_input}"""}
                    ]
                )
                    
                    # Ergebnis-Anzeige
                    st.success("Analyse abgeschlossen")
                    st.markdown("---")
                    st.markdown(response.choices[0].message.content)
                    
                except Exception as e:
                    st.error(f"Fehler: {e}")
        else:
            st.warning("Bitte Text eingeben.")
else:
    if user_password != "":
        st.sidebar.error("Falsches Passwort!")
    st.info("Bitte gib das Passwort in der Sidebar links ein.")

st.divider()
st.caption("Vertraulichkeits-Hinweis: Daten werden via OpenAI API verarbeitet (kein Training laut OpenAI Enterprise Standard).")
