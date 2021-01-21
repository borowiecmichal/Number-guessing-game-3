from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def guess_num():
    minimal = int(request.form.get('min', 0))
    maximal = int(request.form.get('max', 1000))
    ans = request.form.get('ans', 0)
    guess = int(((maximal - minimal) / 2) + minimal)
    if ans == "too little":
        minimal = guess
        guess = int(((maximal - minimal) / 2) + minimal)
    elif ans == "too many":
        maximal = guess
        guess = int(((maximal - minimal) / 2) + minimal)
    elif ans == "correct":
        return 'I WON!!!'

    html = f"""
        <p>I'm guessing {guess}</p>
        <form method='POST'>
            <input type='hidden' name='min' value={minimal}>
            <input type='hidden' name='max' value={maximal}>
            <fieldset>
                <legend>Check an option</legend>
                <label><input type="radio" name="ans" value="too little"> Too little </label><br>  
                <label><input type="radio" name="ans" value="too many"> Too many </label><br>
                <label><input type="radio" name="ans" value="correct"> Correct! </label><br>
            </fieldset>
            <input type='submit' value='SEND'>
        </form>
        """
    return html



if __name__ == '__main__':
    app.run()
