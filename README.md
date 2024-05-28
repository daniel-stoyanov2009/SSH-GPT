python3, linux

# SSH-GPT
Give chatGPT access to your computer

# Description
Source code for GPT in the GPT store. You can give him instructions and he will make them on your computer. 

# Example
### Prompt
``` Install SqlMap on my server! ```
### ChatGPT's request to your server
``` apt install sqlmap -y ```

# Installation
1. Clone the git repository
``` git clone https://github.com/daniel-stoyanov2009/SSH-GPT.git ```

# Configuration
2. Log into repo's directory. 
``` cd SSH-GIT ```
3. Open server.py and set up a user and password. 
``` nano server.py ```
4. Open openai-specification.yaml and set up your ip address. 
``` nano openai-specification.yaml ```
5. Create an GPT with action and dont forget to setup authenication (User &  Pass)
6. Install requirements
``` pip3 install -r requirements.txt ```

# Run the app
``` python3 server.py ```

# ENJOY
This repo is open for contributions. 
