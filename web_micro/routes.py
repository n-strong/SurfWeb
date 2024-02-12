from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html") 


@app.route('/search_beaches', methods=['POST'])
def search_beaches():

    beach = request.json
    print('Response received: ', beach)

    return redirect('search_results')

@app.route('/search_results')
def search_results():
    return render_template('search_results.html') 


if __name__ == '__main__':
    app.run(port=333)  
   
   
   
   
