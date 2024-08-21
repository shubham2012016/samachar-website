# from flask import Flask
from flask import Flask, render_template
from googlesearch import search
import newspaper

keyword = search("banking sector today")
urls = []
url_length = []
data=[]
for a in keyword:
    urls.append(a)
for a in range(len(urls)):
    url_length.append(a)
def paragraph_extractor(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()
    content = article.text
    return content
for a in urls:
    data.append(paragraph_extractor(a))
generated_data = dict(zip(urls,data))
app = Flask(__name__,template_folder="C:/Users/Dell/Desktop/newsdata/templates",static_folder="C:/Users/Dell/Desktop/newsdata/static")
@app.route("/")
def home():
    return render_template("index.html",data=generated_data)
    # return jsonify(generated_data)
