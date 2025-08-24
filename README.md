<div align="center">
		<h1>🤖 OpenAI Agent Boilerplate</h1>
		<p>Quickstart guide to run a basic agent using <b>OpenAI Agents SDK</b> with <b>uv</b> and environment variables!</p>
</div>

---


## 📦 Features

- 🤖 Basic agent boilerplate using <b>OpenAI Agents SDK</b>
- 🐍 Python-based project
- ⚡ Easy virtual environment setup with <b>uv</b>
- 🔒 Supports environment variables via `.env`
- 🏁 Simple run command for quick start

---

## 🛠️ Setup Instructions

### 1️⃣ Add Your Environment Variables

Create a `.env` file in the project directory and add your secrets/configuration:

```env
GEMINI_API_KEY=your_api_key_here
```

---

### 2️⃣ Create a Virtual Environment

Open a terminal **in the project directory** and run:

```powershell
uv venv
```

---


### 3️⃣ Run the Agent

Start your agent with:

```powershell
uv run main.py
```

---


## 📁 Project Structure

```
main.py          # Entry point for the agent
pyproject.toml   # Project configuration
README.md        # Project documentation
uv.lock          # uv dependency lock file
.env             # Environment variables
```

---


## 🙋‍♂️ Need Help?

Feel free to open an issue or reach out for support!

---

<details>
	<summary>ℹ️ About This Project</summary>
	<p>
		This is a boilerplate for running a basic agent using the <b>OpenAI Agents SDK</b>. It is not a simple Python script, but a foundation for building agent-based applications.<br>
		<br>
		<b>Requirements:</b>
		<ul>
			<li>Python</li>
			<li>uv (for environment management)</li>
			<li>OpenAI Agents SDK</li>
		</ul>
	</p>
</details>

---

<div align="center">
	<b>Happy Coding! 🎉</b>
</div>
