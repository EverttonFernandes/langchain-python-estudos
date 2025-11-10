from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"],
    template="Hello, {name}! Welcome to LangChain.",
)

text = template.format(name="Everton")
print(text)
