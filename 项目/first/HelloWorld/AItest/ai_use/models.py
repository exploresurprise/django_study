from dotenv import load_dotenv
load_dotenv()


from langchain_community.chat_models import ChatTongyi
# 1. 连接大模型
def get_tongyi_llm():
    """
    连接通义大语言模型
    """
    model = ChatTongyi(temperature=0.7, top_p=0.9, model="qwen-turbo")
    return model


# 2. 连接向量化模型

from langchain_community.embeddings import DashScopeEmbeddings
def get_dashscope_embed():
    """
        连接dashscope的向量模型
    """
    embed = DashScopeEmbeddings(model="text-embedding-v3")
    return embed


# 3. 连接重排序
from langchain_community.document_compressors import DashScopeRerank
def get_dashscope_rerank():
    """
        连接 dashscope 的重排序
    """
    rerank = DashScopeRerank()
    return rerank


if __name__ == "__main__":
    model = get_tongyi_llm()
    print(model.invoke("你好"))
    embed = get_dashscope_embed()
    print(embed.embed_query("你好"))
    rerank = get_dashscope_rerank()
    print(rerank.rerank(query="你好", documents=["你好", "几点了"]))
