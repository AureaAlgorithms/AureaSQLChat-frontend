import requests
import streamlit as st

"# (nazwa apki)"
with st.chat_message("ai"):
    st.write("witamy\n\n(może tutorial?)")

ddl_file = st.file_uploader('definicja DDL',
                            accept_multiple_files=False,
                            )
if ddl_file is None:
    st.error('nie mamy pliku... :(')
    st.info('wczytaj plik DDL')
    st.stop()
# ddl_file.file_id
ddl_data = ddl_file.read()

with st.chat_message("ai"):
    st.write(f"wczytano plik {ddl_file.name}")


with st.chat_message('user'):
    st.write('pytanie')

question = st.text_input("Your question")
if not question:
    st.error("please ask a question")
    st.stop()  # stop execution here


@st.cache_data(ttl=3600, show_spinner=True)
def api_request(ddl_data: bytes, user_question: str):
    # TODO: API
    return requests.get('http://localhost:8501').text[:50]


btn_next = st.button('next', type='primary')
if btn_next:
    # TODO: parameters to this cached function
    resp = api_request(ddl_data, question)
    t = "```html\n"+resp+"\n```"
    st.write(t)
    st.session_state['shown_text'] = t
elif st.session_state.get('shown_text'):
    st.write(st.session_state.get('shown_text'))

# with st.chat_message('user'):
#     st.write(inp)
