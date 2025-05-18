import streamlit as st

# Data soal
quiz_data = [
    {
        "question": "Ibukota negara Jepang adalah…",
        "choices": ["Beijing", "Bangkok", "Tokyo", "Seoul"],
        "answer": "Tokyo"
    },
    {
        "question": "Siapa penemu bola lampu pijar?",
        "choices": ["Alexander Graham Bell", "Nikola Tesla", "Thomas Alva Edison", "Albert Einstein"],
        "answer": "Thomas Alva Edison"
    },
    {
        "question": "Planet terbesar dalam tata surya adalah…",
        "choices": ["Bumi", "Jupiter", "Saturnus", "Uranus"],
        "answer": "Jupiter"
    },
    {
        "question": "Negara dengan jumlah penduduk terbanyak di dunia adalah…",
        "choices": ["India", "China", "Rusia", "Amerika Serikat"],
        "answer": "India"
    },
    {
        "question": "Presiden ketiga Indonesia adalah…",
        "choices": ["B.J. Habibie", "Ir. Soekarno", "Megawati Soekarnoputri", "Soeharto"],
        "answer": "B.J. Habibie"
    },
    {
        "question": "Unsur kimia dengan simbol ‘O’ adalah…",
        "choices": ["Karbon Dioksida", "Metana", "Emas", "Oksigen"],
        "answer": "Oksigen"
    },
    {
        "question": "Hewan tercepat di darat adalah…",
        "choices": ["Kuda", "Singa", "Cheetah", "Harimau"],
        "answer": "Cheetah"
    },
    {
        "question": "What is the synonym of the word 'Fast'?",
        "choices": ["Slow", "Quick", "Lightning", "Speed"],
        "answer": "Quick"
    },
    {
        "question": "10 - (9 + 26) 4 =",
        "choices": ["90", "-130", "-550", "140"],
        "answer": "-130"
    },
    {
        "question": "Bangsa Indonesia merdeka pada tanggal...",
        "choices": ["18 Agutus 1945", "17 Agustus 1946", "1 Juni 1945", "17 Agustus 1945"],
        "answer": "17 Agustus 1945"
    },
    # Add more questions here
]

# Simpan skor
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_num = 0

st.title("Aplikasi Kuis Web")

if st.session_state.q_num < len(quiz_data):
    q = quiz_data[st.session_state.q_num]
    st.subheader(q["question"])
    choice = st.radio("Pilih jawaban:", q["choices"])

    if st.button("Jawab"):
        if choice == q["answer"]:
            st.success("Benar!")
            st.session_state.score += 1
        else:
            st.error("Salah!")

        st.session_state.q_num += 1
        st.rerun()
else:
    st.success(f"Kuis selesai! Skor akhir kamu: {st.session_state.score}/{len(quiz_data)}")
    if st.button("Ulangi kuis"):
        st.session_state.q_num = 0
        st.session_state.score = 0
        st.experimental_rerun()
