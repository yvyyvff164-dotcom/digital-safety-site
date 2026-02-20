from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/phishing")
def phishing():
    return """
    <h2>Алаяқтық</h2>
    <p>
    Бейтаныс сілтемелерге өтпе.<br>
    Банк ешқашан SMS арқылы құпия код сұрамайды.<br>
    Күмәнді хабарламаларға сенбе.
    </p>
    """

@app.route("/passwords")
def passwords():
    return """
    <h2>Аккаунтты қорғау</h2>
    <p>
    Күрделі пароль қолдан.<br>
    Бір парольді барлық жерде қолданба.<br>
    Екі факторлы қорғауды (2FA) қос.
    </p>
    """

@app.route("/examples")
def examples():
    return """
    <h2>Фишинг мысалдары</h2>
    <ul>
        <li>Сіздің картаңыз бұғатталды</li>
        <li>Сіз жүлде ұттыңыз</li>
        <li>Аккаунтыңызға кірмек болды</li>
    </ul>
    """

@app.route("/hacked")
def hacked():
    return """
    <h2>Аккаунт бұзылса не істеу керек?</h2>
    <ol>
        <li>Парольді ауыстыр</li>
        <li>Барлық құрылғылардан шығу</li>
        <li>2FA қос</li>
    </ol>
    """

if __name__ == "__main__":
    app.run(debug=True)