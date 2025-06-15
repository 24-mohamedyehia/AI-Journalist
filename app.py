from flask import Flask, render_template, request, send_file, redirect, flash
from src.journalist_crew import ArticleMakingCrew
from datetime import datetime
from src.db import Database
import os
import time 
from src.journalist_crew import clean_report

RESEARCH_FOLDER = './src/journalist_crew/research'
RESULT_FOLDER = './src/journalist_crew/results'
os.makedirs(RESEARCH_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def clean_folder(folder_path: str):
    for filename in os.listdir(folder_path):
        path = os.path.join(folder_path, filename)
        try:
            os.remove(path)
        except:
            print("Failed to remove file:", path)

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    db = Database()
    articles = db.get_all_articles()
    file_name = None
    if request.method == 'POST':    
        topic = request.form.get('topic')
        language = request.form.get('language')
        try:
            clean_folder(RESEARCH_FOLDER)
            clean_folder(RESULT_FOLDER)
            inputs = {
                'no_keywords': 3,
                'language': language,
                'topic': topic,
                'current_year': datetime.now().year,
                'search_results': os.path.join(f"./src/journalist_crew/research/step_one_research_topic.json"),
                'collected_articles': os.path.join(f"./src/journalist_crew/research/step_two_extracted_articles.json")
            }
            ArticleMakingCrew().crew().kickoff(inputs=inputs)

            time.sleep(3.0)
            article_path = os.path.join(RESULT_FOLDER, 'final_article.md')
            clean_report(article_path)
            with open(article_path, 'r', encoding='utf-8') as f:
                article = f.read()
            
            db.insert_article(topic=topic, article=article)
            file_name = 'final_article.md'

        except Exception as e:
            flash(f'Error: {str(e)}')
            return redirect(request.url)
    db.close()
    return render_template('index.html', articles=articles, file_name=file_name)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(RESULT_FOLDER, filename)
    return send_file(file_path, as_attachment=True)

@app.route('/view_article/<int:article_id>')
def view_article(article_id):
    db = Database()
    article_data = db.get_article_by_id(article_id)
    db.close()
    if article_data:
        id, topic, article, date = article_data
        return render_template('view_article.html', article=article, topic=topic, date=date)
    else:
        flash('Article not found')
        return redirect('/')

@app.route('/preview/<filename>')
def preview_file(filename):
    file_path = os.path.join(RESULT_FOLDER, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        article = f.read()
    return render_template('view_article.html', article=article)

if __name__ == '__main__':
    app.run(debug=True, port=5000)