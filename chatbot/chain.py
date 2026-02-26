from langchain_core.runnables import RunnablePassthrough

def format_history(memory):
    history = memory.load_memory_variables({})["history"]
    return "\n".join([f"{m.type}: {m.content}" for m in history])

def build_chain(prompt, llm, memory):
    chain = (
        {
            "input": RunnablePassthrough(),
            "history": lambda x: format_history(memory)
        }
        | prompt
        | llm
    )
    return chain