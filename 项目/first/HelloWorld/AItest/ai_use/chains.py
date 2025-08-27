from langchain_core.prompts import ChatPromptTemplate
from models import get_tongyi_llm
from langchain_core.messages import AIMessage
import json
from langchain_core.output_parsers import StrOutputParser

# 连接模型
model = get_tongyi_llm()
output_parser = StrOutputParser()

def sentiment_output_parser(response: AIMessage) -> dict:
    """
    输出解析器
    ResultEntity: {
        "response": {"sentiment": "情感色彩"},
        "msg": "错误信息"
    }
    错误信息：
        - 没有内容
        - 格式错误
    """
    # 取出生成的内容
    content = response.content.strip()

    # 如果没有内容，则返回错误信息
    if not content:
        return {"response": {"sentiment": ""}, "msg": "没有内容"}
    # 删除 ```json 和 ```
    content = content.strip("```json").strip("```")

    # 转dict
    try:
        response = json.loads(s=content)
        return {"response": response, "msg": None}
    except Exception as e:
        return {"response": {"sentiment": content}, "msg": "格式错误"}


def get_sentiment_chain():
    """获取情感识别链"""
    sentiment_prompt = ChatPromptTemplate.from_messages(
        messages=[
            (
                "system",
                """
            你是一个情感识别专家！请识别用户输入的酒店评论的情感色彩！
            输出格式参考：
            {{
                "sentiment": "情感色彩"
            }}
            
            请注意：
                1, 如果是积极正面的评论，请输出：
                {{
                "sentiment": "正面"
                }};
                
                2, 如果是消息负面的评论，请输出：
                {{
                "sentiment": "负面"
                }};
                3, 结果只有正面和负面两种情况;
                4，只需要输出最终的结果，不要做任何解释或说明！
                5，结果不要使用 ```json 和 ```包裹！
                
            
            """,
            ),
            ("user", "{comment}"),
        ]
    )
    #  情感识别 chain 接口
    sentiment = sentiment_prompt | model | sentiment_output_parser
    return sentiment


def get_translation_chain():
    """
    获取万能翻译链
    """
    translation_prompt = ChatPromptTemplate.from_messages(
        messages=[
            (
                "system",
                """
            你是一个语言翻译专家！请把用户的输入翻译为{language}！
            输出格式参考：
            
            {{
                "translation": "翻译后的文本"
            }}
            
            请注意：
                1, 只需要输出最终的结果，不要做任何解释或说明！
                2, 结果不要使用 ```json 和 ```包裹！
            """,
            ),
            ("user", "{text}"),
        ]
    )
    #  情感识别 chain 接口
    translation = translation_prompt | model | output_parser
    return translation
