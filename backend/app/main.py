from fastapi import FastAPI, HTTPException

app = FastAPI()


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


@app.get("/")
def root():
    return {"message": "Football Blog API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/articles")
def get_articles():
    return articles


@app.get("/articles/{article_id}")
def get_article(article_id: int):

    for article in articles:
        if article["id"] == article_id:
            return article

    raise HTTPException(
        status_code=404,
        detail="Article not found"
    )