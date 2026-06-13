import ollama


def ask_llm(prompt, model="llama3.2:1b"):
    """
    Centralized AI service layer.
    All agents communicate with LLM through this service.
    """

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an enterprise procurement intelligence AI. "
                        "You analyze purchase orders, vendor risks, financial exposure, "
                        "SLA violations, operational failures, and business impact."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"AI Error: {str(e)}"