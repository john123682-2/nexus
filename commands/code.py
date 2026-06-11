def execute(agent, prompt):

    code_prompt = f"""
You are a software engineer.

Generate code only.

Task:
{prompt}
"""

    return agent.chat(code_prompt)