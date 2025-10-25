import streamlit as st
import json
import random

st.set_page_config(page_title = "DailyGlow", page_icon = "✨", layout = "centered" )
st.title("💖 DailyGlow – Your Personalized Makeup & Skincare Recommender ")
st.write("Welcome! Let’s find the perfect beauty match for your skin, mood, and weather.")

skin_type = st.selectbox("🌸 What's your skin type?", ["dry", "oily", "normal", "combination"])
weather = st.selectbox("☀️ What's the weather like today?", ["sunny", "rainy", "cold", "hot"])
mood = st.selectbox("💭 How are you feeling today?", ["tired", "happy", "excited", "calm"])

with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

if st.button("✨ Get My Recommendation"):
    st.subheader("💄 Your Personalized DailyGlow Tip")
    try:
        product_list = products[skin_type][weather]
        suggestions = random.sample(product_list, k = min(2, len(product_list)))
        st.write(f"Since you have **{skin_type}** skin and it's **{weather}** today:")
        st.write("💋 Try these products:")
        for item in suggestions:
            st.markdown(f"- {item}")
        if mood == "tired":
            st.info("🌷 Add a touch of bright blush or gloss to boost your energy!")
        elif mood == "happy":
            st.info("☀️ Keep it natural – your smile is already glowing!")
        elif mood == "excited":
            st.info("💫 Try a bold lipstick to match your energy!")
        else:
            st.info("💖 Calm tones and light coverage will keep your glow serene.")
    except KeyError:
        st.warning("Sorry, no products found for that combination! Try another option :)")


st.caption("Made with love, by Ulkar Chobanova")


