import streamlit as st

st.set_page_config(page_title = "DailyGlow", page_icon = "✨", layout = "centered" )
st.title("💖 DailyGlow – Your Personalized Makeup & Skincare Recommender ")
st.write("Welcome! Let’s find the perfect beauty match for your skin, mood, and weather.")

skin_type = st.selectbox("🌸 What's your skin type?", ["dry", "oily", "normal", "combination"])
weather = st.selectbox("☀️ What's the weather like today?", ["sunny", "rainy", "cold", "hot"])
mood = st.selectbox("💭 How are you feeling today?", ["tired", "happy", "excited", "calm"])

if st.button("Get My Recommendation"):
    st.subheader("💄 Your Personalized DailyGlow Tip")

    if skin_type == "dry" and weather == "cold":
        st.write("Your skin needs extra care today :\") Use a **hydrating moisturizer** and **creamy foundation**.")
        st.write("💋 Product ideas:")
        st.markdown("- Clinique *Moisture Surge* 100H")
        st.markdown("- L’Oréal *True Match Foundation* (Creamy Formula)")
    elif skin_type == "oily" and weather == "hot":
        st.write("Stay fresh with **oil-free**, **matte** products to control shine.")
        st.write("💋 Product ideas:")
        st.markdown("- Fenty Beauty *Pro Filt’r Matte Foundation*")
        st.markdown("- La Roche-Posay *Effaclar Gel Cleanser*")
    elif mood == "tired":
        st.write("Lift your energy with a **bright blush** and **glowy highlighter.**")
        st.write("💋 Product ideas:")
        st.markdown("- Rare Beauty *Soft Pinch Blush*")
        st.markdown("- Maybelline *Superstay Lipstick*")
    else:
        st.write("Keep it simple and natural with **soft tones** and a **light base.**")
        st.write("💋 Product ideas:")
        st.markdown("- Maybelline *Fit Me Foundation*")
        st.markdown("- The Ordinary *Hyaluronic Acid Serum*")
    st.info("💖 Remember, confidence is your best glow product!")
st.caption("Made with love, by Ulkar Chobanova")


