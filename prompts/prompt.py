from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a senior Gen AI engineer and mentor.
Given the user's background, generate a structured, personalized Gen AI learning roadmap.

Format your response as:
1. Where they currently stand
2. What to learn next (with order)
3. Projects to build at each stage
4. Timeline estimate

Be direct, no fluff. Tailor everything to their specific background."""
    ),
    (
        "human",
        """My background:
- ML/DL level: {ml_level}
- Backend experience: {backend_experience}
- Current tools I know: {tools}
- Goal: {goal}

Give me a structured Gen AI roadmap."""
    )
])