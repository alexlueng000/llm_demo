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

import inspect

def get_source_code(function_name):
    return inspect.getsource(function_name)



class CodeReviewerPromptTemplate(StringPromptTemplate, BaseModel):
    """
        A custom prompt template that takes in the function name as input, 
        and formats the prompt template to provide the source code of the function.
    """

    @validator("input_variables")
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
        Now you are a code review bot. I will give you a piece of code and you will tell me if it is good or bad.
        And then you need to review the code base on the following criteria:
        1. Readability: Code should be easily readable and understandable. 
        2. Consistency: The code should follow a consistent style throughout, usually dictated by a specific style guide. 
        3. Commenting: Comments should be used to explain the purpose and functionality of complex or non-obvious parts of the code.
        4. Error Handling: The code should robustly handle potential errors or exceptions, and it should fail gracefully in unexpected circumstances.
        5. Security: The code should be reviewed for potential security vulnerabilities.
        6. Scalability: If the software is intended to scale, the code should be written in a way that it can handle increased load.
        Source Code:
        {source_code}
        Code Review:
        """
        return prompt

    def _prompt_type(self):
        return "code-reviewer"



prompt_val = ""

QA_PROMPT_TMPL = (
    prompt_val + "\\\\n"
    "We have provided context information below. \\\\n"
    "Good layout of output text. \\\\n"
    "---------------------\\\\n"
    "{context_str}"
    "\\\\n---------------------\\\\n"
    "Given this information, please answer the question: {query_str}\\\\n"
)
\

# An example prompt with no input variables
no_input_prompt = PromptTemplate(input_variables=[], template="Tell me a joke.")
no_input_prompt.format()
# -> "Tell me a joke."

# An example prompt with one input variable
one_input_prompt = PromptTemplate(input_variables=["adjective"], template="Tell me a {adjective} joke.")
one_input_prompt.format(adjective="funny")
# -> "Tell me a funny joke."

# An example prompt with multiple input variables
multiple_input_prompt = PromptTemplate(
    input_variables=["adjective", "content"], 
    template="Tell me a {adjective} joke about {content}."
)
multiple_input_prompt.format(adjective="funny", content="chickens")
# -> "Tell me a funny joke about chickens."