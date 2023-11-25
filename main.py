import streamlit as st
import base64

# Set the page title and icon
st.set_page_config(page_title="HBD NAT!",
                   page_icon=":heart:", layout="centered")


def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


autoplay_audio('birthday_song.mp3')
st.caption('Song: GMS Live - Happy Birthday')

st.title("Haii Nat!")

with st.container():

    st.write("Kamu pasti bingung sama link yang aku bagiin, ya kan? Jadi, ini tu kado ultah buat kamu. Happy birthday yah!")
    st.write(
        "Btw, kalo musiknya blom mulai bisa di play di atas. Gedein volumenya sekalian ya 😉")
    st.write("Selama 6 tahun kita kenalan kayaknya aku ngak pernah ngucapin ultah ke kamu, ya kan? hehe maap yah. Tapi meskipun begitu, aku inget ultahmu kapan kok. Tahun ini aku udah mikirin kado apa yang cocok buat kamu, sesuatu yang bisa kita kenang sama-sama.")
    st.write("Dan, kebetulan aku bisa buat website. Yah ini sih bukan apa-apa, soalnya aku juga masih belajar. Masih banyak orang-orang yang bisa buat website ini lebih menarik. Website ini aku buat untuk kamu sekaligus buat mengenang masa kalo kita pernah sekolah bareng.")
    st.write("Scroll sampe bawah ya, I've got you something little special. hehe")

st.write("Disini Aku punya beberapa foto yang mungkin bisa kita kenang sama-sama.")

col1, col2 = st.columns(2, gap="small")

with col1:
    st.image("./img/NAT_18.jpg",
             caption="Baru nyadar aku punya double chin, tapi gpp soalnya disini kamu cantik soalnya, hehe.")
    st.image("./img/NAT_11.jpg",
             caption="Aku kalo punya kumis kek om-om gitu yah.")
    st.image("./img/NAT_8.jpg",
             caption="Kaku amat om-om satu ni.")
    st.image("./img/NAT_19.jpg",
             caption="Maap yah, ini aku ss dari story kelasmu dulu 😝")
    st.image("./img/NAT_2.jpg",
             caption="Kok kamu ucul sihh, emang bole serandom itu?")

with col2:
    st.image("./img/NAT_16.jpg",
             caption="Keren uga foto kita 😎")
    st.image("./img/NAT_12.jpg", caption="Pose salam 2 jari, check ✅")
    st.image("./img/NAT_6.jpg", caption="Keknya aku sok cuek banget yah.")
    st.image("./img/NAT_15.jpg",
             caption="Apa persamaan kamu sama nata de coco? ya sama-sama manis lah. hehe")
    st.image("./img/NAT_7.jpg", caption="Emang bole secantik itu?")


st.write("Sebenernya sih masih banyak lagi, tapi menurutku itu aja sih yang bagus. Semoga ini memberimu kesan walau hanya hal sederhana.")

with st.container():
    st.title("Birthday Wishes")
    st.write("For your 18th birthday today, I wish you well.")
    st.write("May God always bless you and your future. ")
    st.write("May He also bless your family and your friends all around you.")
    st.write("May you get what you've been wishing for.")
    st.write("May you become a girl who obeys God words.")
    st.write("and May you also become a gorgeous adorable girl.")

st.write("I also want to confess that I :heart: you, since years ago. I like your randomness, it's such a chaotic personality.")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
