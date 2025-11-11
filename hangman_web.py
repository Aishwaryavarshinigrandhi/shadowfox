from flask import Flask, request
import random, re

app = Flask(__name__)

# Word list
WORDS = [
     "developer", "shadowfox", "internship",
    "function", "variable", "algorithm", "dictionary", "aishwarya","college", "environment",
    "success",  "love", "fastfood", "pizza", "cake", "movies", "game", "immunity",
    "earth", "sun", "corporate",  "satellite", "traffic",
    "software", "vehicle", "system", "youth", "save", "seminar", "beautiful","decision","actress","table","goodday","children",
    "laptop","coconut","morning","magic","dinner","grammar","mother","doraemon",
    "shinchan","umbrella","bus","car","moon","snacks","snake","subject","steps","jewellery","joker",
    "lightening","juice","month","candle","sticker","fruits","automobiles"
]

# HTML Template (embedded)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hangman - Python Web Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f7fa;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            text-align: center;
            width: 400px;
        }
        h1 {
            color: #4b6584;
            margin-bottom: 20px;
        }
        .word {
            font-size: 2em;
            letter-spacing: 10px;
            margin: 20px 0;
        }
        .message {
            color: #3867d6;
            font-weight: bold;
            margin: 15px 0;
        }
        button, .newgame {
            background-color: #3867d6;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
        }
        button:hover, .newgame:hover {
            background-color: #2d98da;
        }
        .footer {
            font-size: 12px;
            color: gray;
            margin-top: 15px;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>🐍 Hangman - Python Internship Project</h1>

    <p class="word">{{display_word}}</p>
    <p>Wrong guesses: {{wrong}} / 6</p>

    {% if not game_over %}
    <form method="post">
        <input type="hidden" name="word" value="{{word}}">
        <input type="hidden" name="guessed" value="{{guessed}}">
        <input type="hidden" name="wrong" value="{{wrong}}">
        <input type="text" name="letter" maxlength="1" required autofocus>
        <button type="submit">Guess</button>
    </form>
    {% endif %}

    <p class="message">{{message}}</p>
    <p>Guessed letters: {{guessed}}</p>

    {% if game_over %}
        <a class="newgame" href="/">🔁 Play Again</a>
    {% endif %}

    <p class="footer">Developed using Python Flask | ShadowFox Internship</p>
</div>
</body>
</html>
"""

# Simple HTML render substitute
def render_template(text, **kwargs):
    for key, value in kwargs.items():
        text = text.replace("{{" + key + "}}", str(value))
    # handle {% if ... %} conditions manually
    if kwargs.get("game_over"):
        text = re.sub(r"\{% if not game_over %\}.*?\{% endif %\}", "", text, flags=re.S)
        text = text.replace("{% if game_over %}", "").replace("{% endif %}", "")
    else:
        text = re.sub(r"\{% if game_over %\}.*?\{% endif %\}", "", text, flags=re.S)
        text = text.replace("{% if not game_over %}", "").replace("{% endif %}", "")
    return text


@app.route("/", methods=["GET", "POST"])
def hangman():
    if request.method == "GET":
        # Start new game
        word = random.choice(WORDS)
        wrong = 0

        # Choose 1 or 2 random hint letters
        hint_count = random.choice([1, 2])
        hints = random.sample(word, hint_count)
        guessed = "".join(set(hints))  # pre-fill with hint letters

        display_word = " ".join([c if c in guessed else "_" for c in word])
        message = f"💡 Hint: The word contains the letter(s): {', '.join(hints)}"

        return render_template(
            HTML_TEMPLATE,
            word=word,
            guessed=guessed,
            wrong=wrong,
            message=message,
            display_word=display_word,
            game_over=False
        )

    # POST: process user guess
    word = request.form["word"]
    guessed = request.form["guessed"]
    wrong = int(request.form["wrong"])
    letter = request.form["letter"].lower()

    message = ""
    if letter in guessed:
        message = f"You already guessed '{letter}'."
    elif letter in word:
        guessed += letter
        message = f"✅ Correct! '{letter}' is in the word."
    else:
        guessed += letter
        wrong += 1
        message = f"❌ '{letter}' is not in the word."

    display_word = " ".join([c if c in guessed else "_" for c in word])

    # Check for win/loss
    if all(c in guessed for c in word):
        message = f"🎉 You won! The word was '{word}'."
        return render_template(
            HTML_TEMPLATE,
            word=word,
            guessed=guessed,
            wrong=wrong,
            message=message,
            display_word=word,
            game_over=True
        )

    if wrong >= 6:
        message = f"💀 You lost! The word was '{word}'."
        return render_template(
            HTML_TEMPLATE,
            word=word,
            guessed=guessed,
            wrong=wrong,
            message=message,
            display_word=display_word,
            game_over=True
        )

    return render_template(
        HTML_TEMPLATE,
        word=word,
        guessed=guessed,
        wrong=wrong,
        message=message,
        display_word=display_word,
        game_over=False
    )


if __name__ == "__main__":
    app.run(debug=True)
