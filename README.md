# 🚧 Under Construction 🚧

# docsRetold

Summarize text from documents, websites, images, videos using AI.

Summarize your information using facebook's [Bart(large)](https://huggingface.co/facebook/bart-large-cnn) model fine-tuned on large summarization dataset - [cnn_dailymail](https://huggingface.co/datasets/abisee/cnn_dailymail).

Goal of summarizing is to save user's time and still give him the key information from the information source. It prevents user of spending too much time reading the information he's not gonna remember anyways and give him just the essential one.

Current available information sources: text

# Setup

1. Clone the repository
```bash
git clone https://github.com/Anubisworkingexperience/docsRetold.git
cd docsRetold
```

2. Run frontend
```bash
npm run dev
```

3. Install dependencies in venv
```bash
cd models
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Run FastAPI server
```bash
uvicorn facebook_bart:app --reload --host 0.0.0.0 --port 8000
```
