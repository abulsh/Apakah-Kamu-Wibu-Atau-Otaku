import streamlit as st
import pandas as pd

def reset_scores():
    st.session_state.scores = {
        "Wibu": 0,
        "Otaku": 0,
        "Campuran": 0
    }

def show_results():
    max_score = max(st.session_state.scores.values())
    top_categories = [k for k, v in st.session_state.scores.items() if v == max_score]
    
    category_info = {
        "Wibu": {
            "desc": "Kamu cenderung sangat antusias dengan budaya Jepang, terutama anime dan cosplay. Kamu suka hal-hal kawaii dan menikmati anime populer yang sedang tren.",
            "image": "https://cdn-icons-png.flaticon.com/512/869/869636.png",
            "tips": [
                "Ikuti event cosplay untuk memperluas komunitasmu.",
                "Pelajari bahasa Jepang dasar untuk pengalaman lebih dalam."
            ]
        },
        "Otaku": {
            "desc": "Kamu menyukai anime dan manga dengan cerita yang dalam dan karakter yang kompleks. Kamu suka mendalami sejarah dan perkembangan industri anime.",
            "image": "https://cdn-icons-png.flaticon.com/512/2847/2847903.png",
            "tips": [
                "Coba eksplor genre anime yang jarang diketahui.",
                "Ikuti diskusi dan panel tentang sejarah anime."
            ]
        },
        "Campuran": {
            "desc": "Kamu memiliki ketertarikan seimbang antara menonton anime dan membaca manga, serta menikmati berbagai genre sesuai suasana hati.",
            "image": "https://cdn-icons-png.flaticon.com/512/565/565547.png",
            "tips": [
                "Coba kombinasikan marathon anime dengan baca manga favorit.",
                "Bergabung dengan komunitas yang beragam minat."
            ]
        }
    }

    st.markdown("---")
    st.subheader("🔍 Hasil Analisis Kepribadian Anime Kamu")
    
    if len(top_categories) > 1:
        st.warning(f"⚠️ Kamu memiliki kecocokan yang sama tinggi pada: {', '.join(top_categories)}")
    
    for cat in top_categories:
        info = category_info[cat]
        st.markdown(f"""
        <div style="border:1px solid #ddd; border-radius:10px; padding:1rem; margin-bottom:1.5rem; background:#f9f9f9;">
            <h2 style="color:#4e73df;">{cat}</h2>
            <img src="{info['image']}" width="80" style="float:right; margin-left:1rem;">
            <p>{info['desc']}</p>
            <p><strong>💡 Tips untukmu:</strong></p>
            <ul>
                {''.join([f'<li>{tip}</li>' for tip in info['tips']])}
            </ul>
            <div style="clear:both;"></div>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("📊 Detail Skoring"):
        df = pd.DataFrame.from_dict(st.session_state.scores, orient='index', columns=['Skor'])
        st.bar_chart(df)

def main():
    st.set_page_config(page_title="Apakah Kamu Wibu atau Otaku?", page_icon="🎌", layout="centered")

    st.markdown("""
    <style>
    .question {
        font-size: 1.1rem;
        font-weight: 600;
        color: #2c3e50;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .stButton>button {
        background-color: #4e73df;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    questions = [
        {
            "question": "1. Apa yang paling sering kamu lakukan saat waktu luang?",
            "options": [
                "Menonton anime terbaru dan viral secara marathon",
                "Kadang nonton anime, kadang baca manga secara bergantian",
                "Membaca manga lawas dan mendalami teori anime lama"
            ],
            "weights": {"Wibu":3, "Campuran":2, "Otaku":1}
        },
        {
            "question": "2. Saat ada event cosplay atau budaya Jepang, kamu biasanya...?",
            "options": [
                "Langsung pakai cosplay dan datang ikut event dengan semangat",
                "Datang untuk lihat-lihat cosplay dan acara saja tanpa ikut",
                "Cari sesi diskusi panel, beli koleksi langka, atau berburu merchandise eksklusif"
            ],
            "weights": {"Wibu":3, "Campuran":2, "Otaku":1}
        },
        {
            "question": "3. Apa yang lebih kamu pilih saat mengisi waktu senggang?",
            "options": [
                "Marathon nonton anime dari awal sampai tamat",
                "Kombinasi antara nonton anime dan baca manga",
                "Fokus baca manga atau novel ringan, sambil mendalami cerita dan ilustrasi"
            ],
            "weights": {"Wibu":3, "Campuran":2, "Otaku":1}
        },
        {
            "question": "4. Bagaimana sikap kamu terhadap karakter waifu/husbando favorit?",
            "options": [
                "Sangat obses, bahkan punya koleksi dan shrine pribadi",
                "Suka, tapi tidak sampai fanatik berlebihan",
                "Fokus pada pengembangan karakter dan peran dalam cerita, bukan hanya fisik"
            ],
            "weights": {"Wibu":3, "Campuran":2, "Otaku":1}
        },
        {
            "question": "5. Jenis anime apa yang paling sering kamu tonton?",
            "options": [
                "Isekai, romance, slice of life yang ringan dan menghibur",
                "Campuran sesuai mood, kadang action, kadang comedy",
                "Psychological, sejarah, drama kompleks yang butuh perhatian lebih"
            ],
            "weights": {"Wibu":3, "Campuran":2, "Otaku":1}
        },
        {
            "question": "6. Seberapa dalam pengetahuanmu soal sejarah anime dan manga?",
            "options": [
                "Hanya tahu anime populer yang sedang tren saat ini",
                "Tahu beberapa nama besar, sutradara, dan genre ikonik",
                "Mengikuti perkembangan studio, sejarah industri, serta genre secara mendalam"
            ],
            "weights": {"Wibu":1, "Campuran":2, "Otaku":3}
        },
        {
            "question": "7. Genre manga atau anime apa yang paling kamu sukai?",
            "options": [
                "Romance, Isekai, Harem yang penuh drama dan romantisme",
                "Action, Fantasy, Comedy yang penuh energi dan keseruan",
                "Shonen klasik dengan cerita mendalam dan karakter kuat"
            ],
            "weights": {"Wibu":3, "Campuran":2, "Otaku":1}
        }
    ]

    if 'scores' not in st.session_state:
        reset_scores()

    st.title("🎌 Apakah Kamu Wibu atau Otaku?")
    st.markdown("Temukan tipe kamu berdasarkan preferensi anime dan budaya Jepang!")

    with st.form(key="quiz_form"):
        for i, q in enumerate(questions):
            st.markdown(f'<div class="question">{q["question"]}</div>', unsafe_allow_html=True)
            answer = st.radio(label="", options=q["options"], key=f"q_{i}")

        submitted = st.form_submit_button("📊 Lihat Hasil")

        if submitted:
            # Reset scores before calculating
            reset_scores()

            for i, q in enumerate(questions):
                answer = st.session_state.get(f"q_{i}")
                if not answer:
                    st.warning("Silakan jawab semua pertanyaan terlebih dahulu!")
                    return
                else:
                    # Tambahkan skor sesuai jawaban
                    idx = q["options"].index(answer)
                    # Map index 0,1,2 ke kategori skor sesuai bobot
                    # Pilihan index 0 => Wibu, index 1 => Campuran, index 2 => Otaku
                    if idx == 0:
                        st.session_state.scores["Wibu"] += q["weights"]["Wibu"]
                    elif idx == 1:
                        st.session_state.scores["Campuran"] += q["weights"]["Campuran"]
                    elif idx == 2:
                        st.session_state.scores["Otaku"] += q["weights"]["Otaku"]

            show_results()

if __name__ == "__main__":
    main()
