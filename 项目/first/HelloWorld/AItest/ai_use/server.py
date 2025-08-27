from fastapi import FastAPI
from chains import get_sentiment_chain
from chains import get_translation_chain
from langserve import add_routes

# 实例化一个 web app
app = FastAPI(
    title="大模型能力接口",
    version="1.0",
    description="大模型能力开放平台"
)

# 添加一个 情感识别 接口
add_routes(
    app=app,
    runnable = get_sentiment_chain(),
    path="/sentiment"
)

# 添加一个 万能翻译 接口
add_routes(
    app=app,
    runnable = get_translation_chain(),
    path="/translation"
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)