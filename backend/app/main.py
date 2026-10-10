from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Pydantic model
class ArticleCreate(BaseModel):
    title: str
    content: str


# Temporary article database
articles = [
    {
        "id": 1,
        "title": "Galatasaray'ın Pres Problemi",
        "content": "Galatasaray'ın önde baskı yapısında bazı problemler var."
    },
    {
        "id": 2,
        "title": "Guardiola ve 3-2 Build-up",
        "content": "Manchester City'nin geriden oyun kurulumuna bakalım."
    },
    {
        "id": 3,
        "title": "Modern Futbolda Half-Space",
        "content": "Half-space kullanımının modern futboldaki önemini inceliyoruz."
    }
]


# Root endpoint
@app.get("/")
def root():
    return {"message": "Football Blog API is running"}


# Health endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}


# Get all articles
@app.get("/articles")
def get_articles():
    return articles


# Get a single article by ID
@app.get("/articles/{article_id}")
def get_article(article_id: int):

    for article in articles:
        if article["id"] == article_id:
            return article

    raise HTTPException(
        status_code=404,
        detail="Article not found"
    )

# Create a new article
@app.post("/articles", status_code=201)
def create_article(article: ArticleCreate):

    new_id = max(
        [item["id"] for item in articles],
        default=0
    ) + 1

    new_article = {
        "id": new_id,
        "title": article.title,
        "content": article.content
    }

    articles.append(new_article)

    return new_article

@app.put("/articles/{article_id}")
def update_article(article_id: int, updated_article: ArticleCreate):

    for article in articles:
        if article["id"] == article_id:

            article["title"] = updated_article.title
            article["content"] = updated_article.content

            return article

    raise HTTPException(
        status_code=404,
        detail="Article not found"
    )

@app.delete("/articles/{article_id}")
def delete_article(article_id: int):

    for article in articles:
        if article["id"] == article_id:

            articles.remove(article)

            return {"message": "Article deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail="Article not found"
    )
