import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="EcoScan Dashboard",
    page_icon="♻️",
    layout="wide"
)

# =======================
# CUSTOM STYLE
# =======================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f1f8f4 0%, #e8f5ec 100%);
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #1b5e20;
    margin-bottom: 0px;
}

.subtitle {
    font-size: 18px;
    color: #4f6f52;
    margin-bottom: 25px;
}

.card {
    background-color: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}

.insight-box {
    background-color: #e8f5e9;
    border-left: 6px solid #2e7d32;
    padding: 18px;
    border-radius: 12px;
    color: #1b5e20;
    font-size: 16px;
}

.metric-card {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.07);
    text-align: center;
}

.metric-title {
    color: #607d61;
    font-size: 15px;
}

.metric-value {
    color: #1b5e20;
    font-size: 30px;
    font-weight: 800;
}
</style>
""", unsafe_allow_html=True)

# =======================
# DATA
# =======================

class_data = pd.DataFrame({
    "Kategori": ["Organik", "Plastik", "Kertas", "Kaca", "Logam", "Others", "Residu"],
    "Jumlah": [2056, 1892, 1430, 1110, 950, 980, 624],
})

class_data["Persentase"] = class_data["Jumlah"] / class_data["Jumlah"].sum() * 100

three_r_data = pd.DataFrame({
    "3R": ["Recycle", "Reuse", "Reduce"],
    "Jumlah": [6952, 1110, 980],
    "Persentase": [76.89, 12.28, 10.83]
})

status_data = pd.DataFrame({
    "Status": ["Dapat Dimanfaatkan", "Residu"],
    "Jumlah": [7438, 1604],
    "Persentase": [82.26, 17.74]
})

# =======================
# SIDEBAR
# =======================

st.sidebar.title("♻️ EcoScan")
st.sidebar.caption("Waste Insight Dashboard")

menu = st.sidebar.radio(
    "Pilih Analisis",
    [
        "Overview",
        "Pertanyaan 1: Distribusi & 3R",
        "Pertanyaan 2: Kategori Dominan",
        "Pertanyaan 3: Sustainability"
    ]
)

# =======================
# HEADER
# =======================

st.markdown('<div class="main-title">♻️ EcoScan Dashboard</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Analisis kategori sampah, potensi 3R, dan dampak sustainability berdasarkan dataset EcoScan.</div>',
    unsafe_allow_html=True
)

# =======================
# HELPERS
# =======================

def metric_card(title, value, note=""):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div style="color:#78909c;font-size:13px;">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def bar_chart(data, x, y, title):
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(data[x], data[y])
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    plt.xticks(rotation=30)
    st.pyplot(fig)

def pie_chart(data, labels, values, title):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(
        data[values],
        labels=data[labels],
        autopct="%1.1f%%",
        startangle=90
    )
    ax.set_title(title, fontsize=14, fontweight="bold")
    st.pyplot(fig)

# =======================
# OVERVIEW
# =======================

if menu == "Overview":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Ringkasan Utama")
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Total Data", "9.042", "gambar sampah")
    with c2:
        metric_card("Kategori Dominan", "Organik", "22.74%")
    with c3:
        metric_card("Dapat Dimanfaatkan", "82.26%", "reuse/recycle")
    with c4:
        metric_card("Residu", "17.74%", "sulit diolah")

    st.markdown("### Distribusi Kategori Sampah")
    bar_chart(class_data, "Kategori", "Jumlah", "Jumlah Data per Kategori Sampah")

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

# =======================
# PERTANYAAN 1
# =======================

elif menu == "Pertanyaan 1: Distribusi & 3R":
    st.header("Pertanyaan 1")
    st.write("Berapa persentase tiap kategori sampah serta proporsi reuse, reduce, dan recycle berdasarkan hasil klasifikasi EcoScan?")

    c1, c2, c3 = st.columns(3)
    with c1:
        metric_card("Recycle", "76.89%", "6.952 data")
    with c2:
        metric_card("Reuse", "12.28%", "1.110 data")
    with c3:
        metric_card("Reduce", "10.83%", "980 data")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Distribusi Kategori")
        bar_chart(class_data, "Kategori", "Jumlah", "Distribusi Kategori Sampah")
    with col2:
        st.markdown("### Proporsi 3R")
        pie_chart(three_r_data, "3R", "Jumlah", "Reuse, Reduce, dan Recycle")

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

# =======================
# PERTANYAAN 2
# =======================

elif menu == "Pertanyaan 2: Kategori Dominan":
    st.header("Pertanyaan 2")
    st.write("Kategori sampah apa yang paling dominan dan berapa proporsinya, serta bagaimana potensi pemanfaatannya untuk mengurangi volume sampah secara signifikan?")

    c1, c2 = st.columns(2)
    with c1:
        metric_card("Kategori Dominan", "Organik", "kategori tertinggi")
    with c2:
        metric_card("Proporsi", "22.74%", "2.056 data")

    st.markdown("### Distribusi Kategori Sampah")
    bar_chart(class_data, "Kategori", "Jumlah", "Kategori Sampah Berdasarkan Jumlah Data")

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

# =======================
# PERTANYAAN 3
# =======================

elif menu == "Pertanyaan 3: Sustainability":
    st.header("Pertanyaan 3")
    st.write("Seberapa besar persentase sampah yang dapat dimanfaatkan kembali dibandingkan dengan sampah residu, dan bagaimana hal ini menunjukkan potensi EcoScan dalam mendukung pengelolaan sampah berkelanjutan?")

    c1, c2 = st.columns(2)
    with c1:
        metric_card("Dapat Dimanfaatkan", "82.26%", "7.438 data")
    with c2:
        metric_card("Residu", "17.74%", "1.604 data")

    st.markdown("### Sampah Dapat Dimanfaatkan vs Residu")
    pie_chart(status_data, "Status", "Jumlah", "Pemanfaatan Sampah vs Residu")

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
