from src.journalist_crew import ArticleMakingCrew
from datetime import datetime
from src.db import Database
import os
from src.journalist_crew import clean_report
def run():
    """
    Run the article making crew.
    """
    inputs = {
        'no_keywords': 3,
        'language': "English",
        'topic': 'Artificial Intelligence in Healthcare',
        'current_year': datetime.now().year,
        'search_results': os.path.join(f"./src/journalist_crew/research/step_one_research_topic.json"),
        'collected_articles': os.path.join(f"./src/journalist_crew/research/step_two_extracted_articles.json")
    }

    # Create and run the crew
    ArticleMakingCrew().crew().kickoff(inputs=inputs)

    article_path = os.path.join('./src/journalist_crew/results/final_article.md')
    clean_report(article_path)

    with open(article_path, 'r', encoding='utf-8') as f:
        article = f.read()  

    data_base = Database()

    data_base.insert_article(topic=inputs['topic'], article=article)

    data_base.close()

    print("\n\n=== Article generation is complete ===\n\n")

if __name__ == "__main__":
    run()


