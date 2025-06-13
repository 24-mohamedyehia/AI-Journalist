from pydantic import BaseModel, Field
from typing import List

class SingleSearchResult(BaseModel):
    title: str
    url: str = Field(..., title="The URL of the web page")
    score: float
    search_query: str = Field(..., title="The search query used to get this result")

class AllSearchResults(BaseModel):
    results: List[SingleSearchResult]


class SingleExtractedArticle(BaseModel):
    title: str
    content: str = Field(..., title="The content of the article")

class AllExtractedArticles(BaseModel):
    articles: List[SingleExtractedArticle]
