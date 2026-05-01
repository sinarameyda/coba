import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EcoScan Dashboard", page_icon="♻️", layout="wide")


st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f4fbf6, #eaf7ee);
}

.hero {
    background: linear-gradient(90deg, #1b5e20, #43a047);
    padding: 25px;
    border-radius: 15px;
    color: white;
    margin-bottom: 25px;
}

.metric-card {
    background: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    text-align: center;
}

.insight-box {
    background-color: #e8f5e9;
    border-left: 5px solid #2e7d32;
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)


class_data = pd.DataFrame({
    "Kategori": ["Organik", "Plastik", "Kertas", "Kaca", "Logam", "Others", "Residu"],
    "Jumlah": [2056, 1892, 1430, 1110, 950, 980, 624],
})

three_r_data = pd.DataFrame({
    "3R": ["Recycle", "Reuse", "Reduce"],
    "Jumlah": [6952, 1110, 980],
})

status_data = pd.DataFrame({
    "Status": ["Dapat Dimanfaatkan", "Residu"],
    "Jumlah": [7438, 1604],
})


color_map_kategori = {
    "Organik": "#2E7D32",
    "Plastik": "#0288D1",
    "Kertas": "#F9A825",
    "Kaca": "#7E57C2",
    "Logam": "#78909C",
    "Others": "#A1887F",
    "Residu": "#9E9E9E"
}

color_map_3r = {
    "Recycle": "#2E7D32",
    "Reuse": "#0288D1",
    "Reduce": "#F9A825",
    "Dapat Dimanfaatkan": "#2E7D32",
    "Residu": "#9E9E9E"
}


def metric(title, value, sub):
    st.markdown(f"""
    <div class="metric-card">
        <h4>{title}</h4>
        <h2>{value}</h2>
        <p>{sub}</p>
    </div>
    """, unsafe_allow_html=True)

def bar_chart(data):
    colors = [color_map_kategori[k] for k in data["Kategori"]]

    fig, ax = plt.subplots(figsize=(6,3.2))
    ax.bar(data["Kategori"], data["Jumlah"], color=colors)

    ax.set_title("Distribusi Kategori Sampah")
    ax.set_xticklabels(data["Kategori"], rotation=25)
    ax.spines[['top','right']].set_visible(False)

    st.pyplot(fig)

def pie_chart(data, label_col):
    colors = [color_map_3r[l] for l in data[label_col]]

    fig, ax = plt.subplots(figsize=(4,4))
    ax.pie(data["Jumlah"], labels=data[label_col],
           autopct="%1.1f%%", colors=colors, startangle=90)

    st.pyplot(fig)

def insight(text):
    st.markdown(f"<div class='insight-box'>{text}</div>", unsafe_allow_html=True)


menu = st.sidebar.radio(
    "Pilih Analisis",
    ["Overview", "Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3"]
)


st.markdown("""
<div class="hero">
<h1>♻️ EcoScan Dashboard</h1>
<p>Analisis Sampah dan Potensi Sustainability</p>
</div>
""", unsafe_allow_html=True)


if menu == "Overview":

    c1,c2,c3,c4 = st.columns(4)

    with c1: metric("Total Data", "9.042", "Gambar")
    with c2: metric("Dominan", "Organik", "22.74%")
    with c3: metric("Reuse/Recycle", "82.26%", "Dapat Dimanfaatkan")
    with c4: metric("Residu", "17.74%", "Sulit Diolah")

    col1, col2 = st.columns([1.2,0.8])

    with col1:
        bar_chart(class_data)

    with col2:
        st.dataframe(class_data)

   st.markdown(
        """
        <div class="insight-box">
        Mayoritas sampah dalam dataset EcoScan masih memiliki potensi untuk dimanfaatkan kembali.
        Hal ini menunjukkan bahwa EcoScan dapat membantu proses identifikasi sampah dan mendukung
        pengelolaan sampah berbasis data.
        </div>
        """,
        unsafe_allow_html=True
    )
   

elif menu == "Pertanyaan 1":

    c1,c2,c3 = st.columns(3)
    with c1: metric("Recycle", "76.89%", "6952 Data")
    with c2: metric("Reuse", "12.28%", "1110 Data")
    with c3: metric("Reduce", "10.83%", "980 Data")

    col1,col2 = st.columns(2)

    with col1:
        bar_chart(class_data)

    with col2:
        pie_chart(three_r_data, "3R")

    st.markdown(
        """
        <div class="insight-box">
        Recycle mendominasi sebesar <b>76.89%</b>, diikuti Reuse sebesar <b>12.28%</b>
        dan Reduce sebesar <b>10.83%</b>. Artinya, sekitar <b>89.17%</b> sampah dalam dataset
        EcoScan memiliki potensi untuk dimanfaatkan kembali melalui reuse dan recycle.
        </div>
        """,
        unsafe_allow_html=True
    )


elif menu == "Pertanyaan 2":

    c1,c2 = st.columns(2)
    with c1: metric("Dominan", "Organik", "2056 Data")
    with c2: metric("Proporsi", "22.74%", "Tertinggi")

    bar_chart(class_data)

    st.markdown(
        """
        <div class="insight-box">
        Kategori <b>Organik</b> menjadi kategori paling dominan dengan <b>2.056 data</b>
        atau <b>22.74%</b> dari total dataset. Sampah organik memiliki potensi tinggi untuk
        dimanfaatkan kembali melalui komposting, sehingga dapat menjadi prioritas utama
        dalam strategi pengurangan volume sampah.
        </div>
        """,
        unsafe_allow_html=True
    )


elif menu == "Pertanyaan 3":

    c1,c2 = st.columns(2)
    with c1: metric("Dapat Dimanfaatkan", "82.26%", "7438 Data")
    with c2: metric("Residu", "17.74%", "1604 Data")

    pie_chart(status_data, "Status")

     st.markdown(
        """
        <div class="insight-box">
        Sebanyak <b>82.26%</b> sampah dalam dataset EcoScan dapat dimanfaatkan kembali,
        sedangkan <b>17.74%</b> termasuk residu. Hal ini menunjukkan bahwa mayoritas sampah
        masih memiliki nilai guna, sehingga EcoScan memiliki potensi kuat dalam mendukung
        pengelolaan sampah berkelanjutan.
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("EcoScan Dashboard | Waste Classification & Sustainability Insight")
