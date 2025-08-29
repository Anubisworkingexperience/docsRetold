from transformers import pipeline
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

class SummaryRequest(BaseModel):
    article: str
    max_length: int = 300
    min_length: int = 30
    do_sample: bool = False

@app.post("/summarize")
async def summarize(req: SummaryRequest):
    print(req)
    # if len(req.article) < 30:
    #     return {"summary": 'Article is too short to summarize'}
    summary = summarizer(
        req.article,
        max_length=req.max_length,
        min_length=req.min_length,
        do_sample=req.do_sample
    )
    return {"summary": summary[0]['summary_text']}

# ARTICLE = """ some article text
# """
# print(summarizer(ARTICLE, max_length=300, min_length=30, do_sample=False))
# >>> [{'summary_text': 'Liana Barrientos, 39, is charged with two counts of "offering a false instrument for filing in the first degree" In total, she has been married 10 times, with nine of her marriages occurring between 1999 and 2002. She is believed to still be married to four men.'}]
