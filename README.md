# Overview

In this project, I updated 3 examples from https://github.com/joaomdmoura/crewAI-examples/ to use the latest version of CrewAI (0.30.11).

To track the performance of each example, I added AgentOps to each project.

Once everything was setup, I ran each example project with ChatGPT4 and ChatGPT4o.

Check the results below!

# Results

## 1. Game Builder

### ChatGPT4o Result

- AgentOps Id: 6763a693-542b-47eb-bd51-40a5c09f86c0
- LLM Cost: $0.18
- Time: 1m 33s
- Prompt Tokens: 14,487
- Completion Tokens: 6,948

### ChatGPT4-Turbo Result

- AgentOps Id: a60b39c0-ae51-48be-b430-08383f95d6fc
- LLM Cost: $0.23
- Time: 1m 33s
- Prompt Tokens: 9,416
- Completion Tokens: 4,557

### Comparison

- Cost: ChatGPT4o is about 21.7% cheaper than ChatGPT4-Turbo.
- Response Time: Both ChatGPT4o and ChatGPT4-Turbo have the same response time.
- Token Usage: ChatGPT4o uses about 41.9% more tokens overall compared to ChatGPT4-Turbo, indicating potentially more detailed responses.

## 2. Trip Planner

### ChatGPT4o Result

- AgentOps Id: c826fdea-8710-4a60-b1a4-5825acb41246
- LLM Cost: $0.36
- Time: 2m 45s
- Prompt Tokens: 44,736
- Completion Tokens: 9,370

### ChatGPT4-Turbo Result

- AgentOps Id: 55da4c75-8c76-4e19-946b-0abc94929c84
- LLM Cost: $0.48
- Time: 4m 40s
- Prompt Tokens: 33,699
- Completion Tokens: 6,277

### Comparison

- Cost: ChatGPT4o is about 25% cheaper than ChatGPT4-Turbo.
- Response Time: ChatGPT4o is about 41% faster than ChatGPT4-Turbo.
- Token Usage: ChatGPT4o uses about 32% more tokens overall compared to ChatGPT4-Turbo.

## 3. Stock analysis

### ChatGPT4o Result

- AgentOps Id: f5d5f942-3b0f-47a2-8cd3-b843eef72116
- LLM Cost: $0.33
- Time: 3m 14s
- Prompt Tokens: 38,838
- Completion Tokens: 9,051

### ChatGPT4-Turbo Result

- AgentOps Id: fbe4b206-12ce-49eb-b86b-53ed56b6ec85
- LLM Cost: $0.52
- Time: 3m 36s
- Prompt Tokens: 40,777
- Completion Tokens: 3,793

### Comparison

- Cost: ChatGPT4o is about 36.5% cheaper than ChatGPT4-Turbo.
- Response Time: ChatGPT4o is about 10.2% faster than ChatGPT4-Turbo.
- Token Usage: ChatGPT4o uses about 11.3% fewer tokens overall compared to ChatGPT4-Turbo.
