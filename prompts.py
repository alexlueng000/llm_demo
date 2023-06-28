from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
    StringPromptTemplate
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from pydantic import BaseModel, validator


class CodeReviewerPromptTemplate(StringPromptTemplate, BaseModel):
    """
        A custom prompt template that takes in the function name as input, 
        and formats the prompt template to provide the source code of the function.
    """

    @validator("input_variables", allow_reuse=True)
    def validate_input_variables(cls, v):
        """Validate that the input variables are correct."""
        if len(v) != 1 or "source_code" not in v:
            raise ValueError("source_code must be the only input_variable.")
        return v

    def format(self, source_code, **kwargs) -> str:
        # Get the source code of the function
        # source_code = get_source_code(kwargs["function_name"])

        # Generate the prompt to be sent to the language model
        prompt = f"""
        ChatGPT, as a Go (Golang) code reviewing bot, your mission is to evaluate the supplied code snippet based on Golang best practices. 
        The evaluation factors include: Readability, Consistency, Commenting, Error Handling, Security, and Scalability. 
        Upon analyzing the code, please share your detailed review in Markdown format, assigning a score out of 10 for each criterion 
        and calculating a total score out of 60. 
        
        Here's the code snippet you need to review:
        Source Code:
        {source_code}

        Now, provide your analysis and share your review in the following Markdown format:

        ### Code Review:

        1. **Readability**: (Score out of 10, with 10 being the highest)
            - Reason: 
        2. **Consistency**: (Score out of 10, with 10 being the highest)
            - Reason: 
        3. **Commenting**: (Score out of 10, with 10 being the highest)
            - Reason: 
        4. **Error Handling**: (Score out of 10, with 10 being the highest)
            - Reason: 
        5. **Security**: (Score out of 10, with 10 being the highest)
            - Reason: 
        6. **Scalability**: (Score out of 10, with 10 being the highest)
            - Reason: 

        ### Total Score: (Sum of all scores out of 60)
        """
        return prompt

    def _prompt_type(self):
        return "code-reviewer"
    

jd_system_template = '''
以一名职业分析专家的角色，你的任务是分析职位描述，提取相关的技术和专业能力关键字，并根据这些关键字推荐适当的职位。此外，你还需要为每个推荐的职位提供能力维度和简短的能力总结。

以下是你需要分析的输入数据样例：
【职位描述】：详细阐述某一特定职位，包括职责、任务、要求、所需技能和经验等信息，以引导招聘候选人了解是否适合该职位。

根据输入数据,你的输出应该是一个JSON对象,有以下键:关键字(字符串),推荐职位(字符串),能力总结(字符串),能力维度(字符串)。这些键的值应该是一个列表。

具体要求：

关键字:从职位描述中提取与技术和知识点相关的标签,以助于筛选和匹配合适的职位。关键字的字数应在6字以内,不重复。
推荐职位:根据职位描述推荐3个以内的职位,格式如:后端/Java开发。
能力总结:以一句话形式概述在推荐职位中能完成的任务和职责。
能力维度:总结该职位需要掌握的专业知识和技术技能,个数应在4-6个之间。
'''

jd_human_template = """
        这是你需要分析的职位描述:
        {job_description}
"""


cr_system_template = """
    ChatGPT, as a Go (Golang) code reviewing bot, your mission is to evaluate the supplied code snippet based on Golang best practices. 
    The evaluation factors include: Readability, Consistency, Commenting, Error Handling, Security, and Scalability. 
    Upon analyzing the code, please share your detailed review in Markdown format, assigning a score out of 10 for each criterion 
    and calculating a total score out of 60. 

    Now, provide your analysis and share your review in the following Markdown format:

        ### Review Result:

        1. **Readability**: (Score out of 10, with 10 being the highest)
            - Reason: 
        2. **Consistency**: (Score out of 10, with 10 being the highest)
            - Reason: 
        3. **Commenting**: (Score out of 10, with 10 being the highest)
            - Reason: 
        4. **Error Handling**: (Score out of 10, with 10 being the highest)
            - Reason: 
        5. **Security**: (Score out of 10, with 10 being the highest)
            - Reason: 
        6. **Scalability**: (Score out of 10, with 10 being the highest)
            - Reason: 

        ### Total Score: (Sum of all scores out of 60)
"""

cr_human_template = """
        Here's the code snippet you need to review:
        Source Code:
        {source_code}
"""