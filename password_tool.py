from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)
    score = result['score']
    print("\nPassword Strength Score:", score, "/ 4")

    if score == 4:
        print("✅ Very strong password!")
    elif score == 3:
        print("🟡 Strong enough, but can improve.")
    elif score == 2:
        print("⚠️ Okay-ish, try making it better.")
    else:
        print("❌ Weak password. Try making it longer and harder.")

def generate_wordlist(inputs):
    wordlist = []

    for word in inputs:
        wordlist.append(word)
        wordlist.append(word + "123")
        wordlist.append(word + "2025")
        wordlist.append(word.capitalize())
        wordlist.append(word[::-1])

    with open("wordlist.txt", "w") as f:
        for item in wordlist:
            f.write(item + "\n")

    print("\n✅ Wordlist saved to wordlist.txt with", len(wordlist), "passwords.")

# ---- Main program starts here ----
print("🔐 PASSWORD STRENGTH ANALYZER")
password = input("Enter a password to test: ")
analyze_password(password)

print("\n🛠 WORDLIST GENERATOR")
name = input("Your Name: ")
pet = input("Pet Name: ")
birth_year = input("Your Birth Year: ")
hobby = input("Hobby: ")

generate_wordlist([name, pet, birth_year, hobby])