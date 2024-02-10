from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html") 

@app.route('/search_beaches', methods=['POST'])
def search_beaches():
    beach = request.json
    
    print('Response received: ', beach)
  

if __name__ == '__main__':
    app.run(port=333)  
   
   
   
   
   