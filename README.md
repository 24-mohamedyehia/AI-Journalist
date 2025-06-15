# AI-Journalist
AI Journalist is a Python application that uses AI to generate articles based on a given topic. It uses a crew of AI agents to generate articles, and then uses a database to store the articles.

## Screenshots
![image](./public/image.png)

## Features
- Generate articles based on a given topic
- Use a crew of AI agents to generate articles
- Use a database to store the articles
- support English and Arabic languages

## Requirements
- Python 3.11

### Install Python Using Miniconda
1- Download and install MiniConda from [here](https://www.anaconda.com/docs/getting-started/miniconda/main#quick-command-line-install)

2- Create a new environment using the following command:
```bash
$ conda create --name AI-Journalist python=3.11 -y
```

3- Activate the environment:
```bash
$ conda activate AI-Journalist
```

### Installation

#### Install the required packages
```bash
$ pip install -r requirements.txt
```

### Setup the environment variables
```bash
$ cp .env.example .env
```
#### Set your environment variables in the .env file. Like:
- OPEN_ROUTER_API_KEY value to use LLM
    - You can get your Open Router API key from [here](https://openrouter.ai/settings/keys).
- AGENTOPS_API_KEY value to monitor the agents
    - You can get your AgentOps API key from [here](https://agentops.com/).
- TVLY_SEARCH_API_KEY value to search the web
    - You can get your TVLY_SEARCH_API_KEY from [here](https://tavily.ai/).

## Run the application:
```bash
$ python app.py
```

## Access the application
Open your browser and navigate to `http://127.0.0.1:5000`.

To stop the application, press `Ctrl+C` in your terminal.

## Technologies
- Python 3.11
- Flask
- CrewAI
- AgentOps
- Tavily    

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.