from fastapi import APIRouter
from textblob import TextBlob

api = APIRouter()




@api.get("/")
async def home_page():
    return {
        "message": "Home"
    }
    
    
    
@api.get("/sentiment/{text}")
async def get_sentiment(text):
    blob = TextBlob(text).sentiment
    result = {
        "original_text": text,
        "polarity":blob.polarity,
        "subjectivity":blob.subjectivity
    }
    return result