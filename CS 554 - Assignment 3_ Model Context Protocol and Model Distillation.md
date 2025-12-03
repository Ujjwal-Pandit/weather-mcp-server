### **Task 1: Setting up an MCP Server** (24 PTS)

For this task, follow the official [Build an MCP server guide](https://modelcontextprotocol.io/docs/develop/build-server?utm_source=chatgpt.com). In this exercise, you will connect an MCP server to an external API provided by the [National Weather Service](https://www.weather.gov/) to fetch information:

- Set up a new Python project using uv and create a virtual environment.  
- Install the required dependencies (mcp\[cli\], httpx).  
- Test a **weather MCP server** with two tools:  
  * get\_alerts(state) → fetch active weather alerts for a U.S. state.  
  * get\_forecast(latitude, longitude) → fetch forecasts for a location.  
- Configure your MCP host (Claude for Desktop) to connect to your server.  
- Run the server (uv run weather.py) and test tool calls from Claude.

**Deliverables:** 

1. Include a screenshot of a working call of the weather server on Claude Code, asking for weather alerts and forecasts of your home town. If you’re international and don’t consider any US city to be your home town, use the first city that you landed in, and include that in the documentation. (12 pts)

2. In get\_alerts and get\_forecast, the functions wrap external API calls and return human-readable text. If you were to create your own tool (e.g. for stock prices, translations, or movie info), what steps would you need to follow to design the function? Outline the inputs it will take, how you would fetch/process data, and the output format. (4 pts)

3. Notice how both tools check whether the API returned valid data and fall back to safe messages like *“Unable to fetch…”*. Why is this kind of error handling important for tools connected to an AI client? If you were building your own tool, what kinds of errors would you expect and how would you handle them? (4 pts)

4. The weather tools format raw JSON data into strings that are easier for a human to read. If your tool instead had to return results that another program (not a human) would consume, how would you change the output design? Give an example of what your function’s output might look like. (4 pts)

### **Task 2: Building Your First MCP Server** (31 PTS)

Now, in this task, you will design tools following the given starter code that perform mathematical reasoning locally using [SymPy](https://docs.sympy.org/latest/index.html), a Python library for symbolic math. 

In the starter code calc.py, the helper functions including \_safe\_expr, \_fmt, and the evaluate function for basic arithmetic, substitution, and closed-form simplification, have been implemented. You will complete the more advanced logic with differentiation and integration, as well as basic algebraic and transcendental equations over ℝ or ℂ. 

**Deliverables:**

1. Attach your completed calc.py on Canvas, and paste a screenshot of a successful call that demonstrates natural language input into calculator input into results. (20 pts)

2. The evaluate tool tries to compute a numeric result when no variables are present, but leaves expressions symbolic otherwise. Why is it important to distinguish between symbolic (e.g. x\*\*2 \+ 2\*x \+ 1) and numeric (e.g. 1) outputs? (4 pts)

3. Error handling is a crucial component of an MCP. What are some possible edge cases or errors users can run into when using these tools? (2 pts) 

4. Implement a new MCP tool that handles statistical  expectation and variance for simple distributions (Uniform, Normal, Bernoulli) using SymPy’s stats module. (5 pts)

### **Task 3: Exploring Existing Ecosystem** (15 PTS)

So far, you’ve built a simple MCP server, but MCP is designed to unify many different sources of data and tools. In this task, to see the bigger picture, you will be exploring what’s already out there — both community **example servers** and Claude’s built-in **connectors** — and reflecting on how they might combine with your own server in real workflows.

1. Browse the [MCP example servers](https://modelcontextprotocol.io/examples) page and pick one of the current reference servers that demonstrate core MCP features and SDK usage. Write a description of what it does, and how it differs from the calculator/weather servers from previous tasks. (6 pts)

2. In Claude Code, click on the Search and tools button, similar to where you toggled the weather and calculator servers, then click on “Add connectors”. Explore the available connectors out there, and discuss how some of these might be combined with your own MCP server or the reference server you chose from earlier. (6 pts)

3. In practice, many workflows don’t formally adopt complete MCP and simply focus on the agent orchestration aspects when it comes to tool and context integration. Discuss the trade-offs between whether or not to formally implement MCP. (3 pts)

### **Task 4: Model Distillation** (30 PTS \+ 5 EC)

1. In this task, you will explore **knowledge distillation** ([instruction](https://medium.com/@ghatifernado.inc/model-distillation-secrets-shrinking-your-nlp-model-without-sacrificing-performance-98cfde831862)) as an alternative to direct fine-tuning. You will use a larger, high-performing model (teacher) to generate soft probability distributions on the SQuAD dataset, and then train a smaller model to learn from these soft targets. This process allows the student to capture richer information about the teacher’s confidence and decision boundaries.   
   Different from Assignment 1, which treated question answering as a generative task, here we consider extractive QA, where the answer is a span directly selected from the original context. We will use BERT-large fine-tuned on SQuAD as the teacher model, and BERT-base as the student model.  
   You will then compare the performance of the distilled model against a normally fine-tuned model, and reflect on the trade-offs related to efficiency, accuracy, and generalization.  
   Your tasks:  
1. Complete the function train\_kd in bert\_dist.py. (12 points)  
2. Run the script and report the evaluation results (training loss and metric results)of both the normal fine-tuned model and the distilled model (screenshot). (4 points)  
3. Explain the loss function used in train\_kd (i.e., how hard labels and soft teacher logits are combined). (2 points)  
4. Describe the benefits of model distillation. (3 points)

   

2. In this task, you will explore **Agent Distillation**, which compresses a multi-step, tool-using reasoning pipeline into a **single LLM policy**, following the [Agent Distillation (Nardien et al., 2025\)](https://arxiv.org/pdf/2505.17612) and its accompanying [GitHub repo](https://github.com/Nardien/agent-distillation) implementation. The goal is to understand how a student model can internalize the reasoning behaviors of a teacher agent that relies on multiple external tools.  
1. Briefly explain the workflow of the teacher agent, including how it performs reasoning, selects tools (e.g., retrieval or code execution), and uses their outputs. (3pt)  
2. Describe how the distilled student learns to imitate this *reason–act–observe* behavior pattern, even without explicitly calling external tools. (3pts)  
3. The paper introduces two techniques to help the student imitate the teacher agent: **first-thought prefix** and **self-consistent action generation**. Choose **one** and briefly explain what it is, why it matters, and how it helps the student generalize or use tools better. (3 pts)  
4. (EXTRA CREDIT) Check [this part](https://github.com/Nardien/agent-distillation?tab=readme-ov-file#-quickstart-run-the-distilled-agent) in github implementation. Run your own example experiments. Attach the running screenshot and write down your observation in terms of answer quality, speed/latency, and consistency of reasoning behavior (5 pts)

