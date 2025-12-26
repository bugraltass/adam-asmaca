from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)

# ===== FRONTEND YOLU =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")

# ===== OYUN VERİLERİ =====
words = ["python", "bilgisayar", "yazilim", "programlama", "flask"]
selected_word = random.choice(words)
guessed_letters = []
lives = 6


# ===== FRONTEND =====
@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)


# ===== BACKEND API =====
@app.route("/status", methods=["GET"])
def status():
    display_word = "".join(
        [letter if letter in guessed_letters else "_" for letter in selected_word]
    )
    return jsonify({
        "word": display_word,
        "lives": lives
    })


@app.route("/guess", methods=["POST"])
def guess():
    global lives

    data = request.get_json()
    letter = data.get("letter")

    if not letter or len(letter) != 1:
        return jsonify({"error": "Geçersiz harf"}), 400

    if letter not in guessed_letters:
        guessed_letters.append(letter)
        if letter not in selected_word:
            lives -= 1

    display_word = "".join(
        [l if l in guessed_letters else "_" for l in selected_word]
    )

    return jsonify({
        "word": display_word,
        "lives": lives
    })


if __name__ == "__main__":
    app.run(debug=True)

