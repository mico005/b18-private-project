import streamlit as st
import base64

# Set the page title and icon
st.set_page_config(page_title="HBD NAT!",
                   page_icon="🎉", layout="centered")


def get_file_as_base64(file: str):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def autoplay_audio(file_path: str):
    b64 = get_file_as_base64(file_path)
    md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
    st.markdown(
        md,
        unsafe_allow_html=True,
    )


with st.container():
    autoplay_audio('birthday_song.mp3')
    st.caption('Song: GMS Live - Happy Birthday')

    st.title("Haii Nat!")
    st.write("Kamu pasti bingung sama link yang aku bagiin, ya kan? Mungkin kamu udah baca dari nama linknya juga. Ya jadi, ini tu kado ultah buat kamu. Happy birthday yah!")
    st.write(
        "Btw, kalo musiknya blom mulai bisa di play di atas. Gedein volumenya sekalian ya 😉")
    st.write("Selama 6 tahun kita kenalan kayaknya aku ngak pernah ngucapin ultah ke kamu, ya kan? hehe maap yah. Tapi meskipun begitu, aku inget ultahmu kapan kok. Tahun ini aku udah mikirin kado apa yang cocok buat kamu, sesuatu yang bisa kita kenang sama-sama.")
    st.write("Dan, kebetulan aku bisa buat website. Yah ini sih bukan apa-apa, soalnya aku juga masih belajar. Masih banyak orang-orang yang bisa buat website ini lebih menarik. Website ini aku buat untuk kamu sekaligus buat mengenang masa kalo kita pernah sekolah bareng.")
    st.write("Scroll sampe bawah ya, I've got you something little special.")

image_n_caption = [
    {"path": "./img/NAT_18.jpg",
        "caption": "Baru nyadar aku punya double chin, tapi gpp soalnya disini kamu cantik soalnya, hehe."},
    {"path": "./img/NAT_11.jpg",
        "caption": "Baru nyadar aku punya double chin, tapi gpp soalnya disini kamu cantik soalnya, hehe."},
    {"path": "./img/NAT_8.jpg", "caption": "Aku kalo punya kumis kek om-om gitu yah."},
    {"path": "./img/NAT_19.jpg", "caption": "Kaku amat om-om satu ni."},
    {"path": "./img/NAT_2.jpg", "caption": "Kok kamu ucul sihh, emang bole serandom itu?"},
    {"path": "./img/NAT_13.jpg", "caption": "Gendut? enggak kok, aku bilang ini gemoyy 🥰"},
    {"path": "./img/NAT_16.jpg", "caption": "Keren uga foto kita 😎"},
    {"path": "./img/NAT_12.jpg", "caption": "Pose salam 2 jari, check ✅"},
    {"path": "./img/NAT_6.jpg", "caption": "Keknya aku sok cuek banget yah."},
    {"path": "./img/NAT_15.jpg",
        "caption": "Apa persamaan kamu sama nata de coco? ya sama-sama manis lah. hehe"},
    {"path": "./img/NAT_21.jpg", "caption": "Kece abiezz ketua satu ini"},
    {"path": "./img/NAT_7.jpg", "caption": "Emang bole secantik itu?"},
]

col1, col2 = st.columns(2, gap="small")

with st.container():
    with col1:
        st.header("Our Photos")
        st.write(
            "Disini Aku punya beberapa foto yang mungkin bisa kita kenang sama-sama, baca juga captionnya yaww.")
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
        st.image("./img/NAT_13.jpg",
                 caption="Gendut? enggak kok, aku bilang ini gemoyy 🥰")

    with col2:
        st.image("./img/NAT_16.jpg",
                 caption="Keren uga foto kita 😎")
        st.image("./img/NAT_12.jpg", caption="Pose salam 2 jari, check ✅")
        st.image("./img/NAT_6.jpg", caption="Keknya aku sok cuek banget yah.")
        st.image("./img/NAT_15.jpg",
                 caption="Apa persamaan kamu sama nata de coco? ya sama-sama manis lah. hehe")
        st.image("./img/NAT_21.jpg", caption="Kece abiezz ketua satu ini")
        st.image("./img/NAT_7.jpg", caption="Emang bole secantik itu?")

with st.container():
    st.header("Birthday Wishes")
    st.write("For your 18th birthday today, I wish you well.")
    st.write("May God always bless you now and your future. ")
    st.write("May He also bless your family and your friends all around you.")
    st.write("May you get what you've been wishing for.")
    st.write("May you become a girl who obeys God words.")
    st.write("and May you also become a gorgeous adorable girl.")
    st.write("I also want to confess that I :heart: You, iya, aku suka kamu. Sebenernya sihh udah dari lama, mungkin smp? entah lah. Kenapa baru sekarang aku ungkapin? Karena Tuhan baru ngasih kesempatan sekarang, kalau bukan karena Dia juga aku ngak bakal ungkapin. Kamu itu orangnya random sekalii, ini lah yang membuat kamu jadi unyuu, karena ini juga aku suka kamu. Sebagai penutup, aku cuman mau bilang terimakasih udah jadi temenku selama 6 tahun ini, semoga kita bisa semakin deket dan ngak akan hilang kontak kedepannya.")
    st.write("Oh ya, Selamat Natal dan Tahun baru juga ya.")

    st.write("Sincerely,")
    st.write("From your number one fans")


with open('style1.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown("<script>console.log('hello')</script>", unsafe_allow_html=True)


st.balloons()
