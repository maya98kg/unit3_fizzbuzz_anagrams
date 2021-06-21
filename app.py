from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
    title="This is a homepage"
    text="Go to fizzbuzz to play :)"
    
    return render_template('main.html',title=title,text=text)

@app.route('/fizzbuzz/<int:n>')
def fizzbuzz(n):
    title="This is page for playing FizzBuzz"
    text="Pick a number and play FizzBuzz challenge"
    l=list(range(1,n+1))
    return render_template('fizz_buzz.html',list=l)


@app.route('/words/<string:word>')
def words(word):
    f=open("words.txt")
    words=f.read().splitlines()
    anagrams=[]
    word=word.upper()
    for w in words:
        if sorted(word)==sorted(w):
            anagrams.append(w)
    return render_template('words.html',word_list=anagrams)

