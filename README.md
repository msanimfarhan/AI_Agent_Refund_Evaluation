# AI Refund Helper and Report Card

A practice project that asks two questions: **Can an AI help a customer ask for a refund? And how can we check its work?**

Imagine a shop with a robot helper. A customer asks for their money back. The robot looks up what they bought, checks the shop's rules, and gives an answer.

This project builds that helper. It also gives the helper a report card to see how well it did.

> This is a learning demo. It uses sample purchase records and does not send real money or create real support tickets. Running the AI and its report cards uses the OpenAI API and can cost money.

## What can it do?

- Ask which customer needs help.
- Look up the customer's purchases.
- Work out how much the requested items cost.
- Use today's date to help check the refund rules.
- Say whether a refund should be allowed.
- Run example questions and check the AI's answers.

The helper is called an **agent**: an AI that can use small Python functions, called **tools**, to do parts of a job.

## A small example

The sample customer `user123` bought a book for $23 and a pen for $7.

```text
Customer: I am user123. I would like a refund for the book.

The helper should:
1. Find user123's purchases.
2. Check the book's purchase date against today's date.
3. Check whether the book follows the refund rules.
4. Allow $23 if it is eligible, or explain why it is not.
```

It should not include the pen, because the customer only asked to return the book.

## The shop's rules

The AI is told to follow these rules:

1. Find the customer before making a refund decision.
2. Only refund items the customer really bought.
3. Only refund the items the customer asks to return.
4. A purchase must be no more than 30 days old and cannot be in the future.
5. Explain the decision to the customer.

These instructions live in [`agent/prompts.py`](agent/prompts.py). They tell the AI what to do, but do not guarantee it will always do the right thing. Checking its work is the main point of this project.

## How the pieces fit together

```text
Customer's message
        |
        v
AI helper <----> Python tools <----> Sample purchases
        |
        v
Answer to the customer
        |
        v
Checks and scores from DeepEval
```

**LangChain** connects the AI to its tools. **LangGraph** keeps conversation history in memory. **DeepEval** checks the AI's work. **OpenAI** provides the models used by the helper and the checks.

## The AI's report card

An **evaluation** is a check of how well the AI did. The project has seven kinds of checks:

| Check | What it asks |
| --- | --- |
| Task completion | Did the helper finish the customer's task? |
| Tool correctness | Did it choose the expected tools? |
| Argument correctness | Did it give those tools the right information? |
| Answer correctness | Did its answer agree with the expected result? |
| Plan quality | Did it choose a sensible way to solve the problem? |
| Plan adherence | Did it follow its plan? |
| Step efficiency | Did it avoid unnecessary steps? |

Some checks use another AI as a grader. Think of it as a second robot checking the first robot's homework. That grader can also make mistakes, so a good score is useful evidence, not proof that everything is correct.

## Try it on your computer

You need **Python 3.11 or newer**, **uv** (a tool that installs Python packages), and an **OpenAI API key** with access to the configured model.

### 1. Download the project

Clone this repository, or download and unzip it. Open a terminal in the project folder.

### 2. Install the packages

```sh
uv sync
```

### 3. Add your secret key

Create a file named `.env` in the project folder. Put this inside it, replacing the placeholder with your own key:

```dotenv
OPENAI_API_KEY=your_api_key_here
```

Treat this key like a password. Do not put it in your README, screenshots, or public GitHub files. The project's `.gitignore` already excludes `.env`.

The helper's model is set in [`agent/models.py`](agent/models.py). The grading model is set in [`evaluations/model.py`](evaluations/model.py). Both currently use `gpt-6-luna`. If your API account cannot use that model, update both files to a compatible model available to you.

### 4. Talk to the helper

```sh
uv run --directory agent python -c "from agent import run_conversation; run_conversation()"
```

The helper starts with a refund request. Type your replies when it asks for them. You can try the sample username `user123`. Press `Ctrl+C` to stop.

### 5. Run the report cards

From the project folder, run:

```sh
uv run python evaluations/eval_all.py
```

This runs the seven checks against the example requests in [`evaluations/datasets.py`](evaluations/datasets.py) and prints results in the terminal. It calls the helper and AI graders, so it can cost more than a single conversation. Repeating the command makes fresh calls because this runner disables evaluation caching.

You can also run a single check, for example:

```sh
uv run python evaluations/tool_correctness.py
```

## Where to find things

| File or folder | What is inside |
| --- | --- |
| `agent/agent.py` | The helper and its terminal conversation loop |
| `agent/prompts.py` | Instructions and refund rules for the AI |
| `agent/tools.py` | Functions for purchases, refund amounts, mock tickets, and today's date |
| `agent/data.py` | Sample customers and purchases |
| `agent/objects.py` | The shapes of answers and requested items |
| `agent/models.py` | The helper's model setting |
| `evaluations/datasets.py` | Example questions and expected results |
| `evaluations/model.py` | The grading model setting |
| `evaluations/eval_all.py` | The runner for all seven checks |
| `pyproject.toml` and `uv.lock` | Package requirements and locked versions |

`main.py` is currently a starter file that only prints a greeting. Use the commands above to run the actual helper and evaluations.

## Limits and safe sharing

- **This is a terminal demo.** There is no website or public chat interface yet.
- **Refunds are pretend.** The ticket tool only returns a success message; it does not contact a team or a bank.
- **Rules need stronger protection for real use.** The tools do not independently enforce the 30-day rule, verify the customer's identity, or validate the refund amount before announcing a ticket. Do not connect them to real payments as they are.
- **Dates change the answers.** Sample purchases have fixed dates, but the helper checks today's date. A purchase that qualifies now may be too old later. Review the expected results when rerunning the checks.
- **Conversation history is temporary.** It is kept in memory and disappears when the process stops.
- **API costs need limits.** There are no explicit application-level spending quotas or request limits. Do not expose this directly as an unrestricted public chat service.
- **Keep private files private.** Review evaluation logs before sharing them; they can contain messages and model outputs. Exclude `.deepeval/` caches and any hosting secrets from Git.

For a public portfolio, saved example conversations and evaluation results let people explore the work without making paid API calls. A live version needs server-side secret storage, access controls, usage limits, and enforced spending controls first.
