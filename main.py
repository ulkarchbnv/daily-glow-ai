def dailyglow():
    print("Welcome to DailyGlow 💅")
    print("Let's find out the perfect skincare and makeup match for you together.")
    skin_type = input("Can you please tell us about your skin type? (dry/oily/combination/normal): ").lower()
    weather = input("Now let's see what is the weather like today? (sunny/rainy/windy/cold/hot): ").lower()
    mood = input("And how are you feeling right now? (happy/tired/sad/excited/calm/in love): ").lower()

    print("\n✨ Your personalized DailyGlow tip: ")

    if skin_type == "dry" and weather == "cold":
        print("Use a hydrating moisturizer and creamy foundation to protect your skin")
        print("Some product ideas: Clinique Moisture Surge, L’Oréal True Match Foundation")
    elif skin_type == "oily" and weather == "hot":
        print("Go for oil-free, matte products to control shine.")
        print("Some product ideas: Fenty Pro Filt'r Matte Foundation, La Roche-Posay Effaclar Gel")
    else:
        print("Choose a light base and soft tones to enhance your natural beauty and glow")
        print("Some product ideas: Maybelline Fit Me Foundation, The Ordinary Serum")
    print("\n💋 Stay confident and remember: every girl is beautiful in her own way")

dailyglow()


