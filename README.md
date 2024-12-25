# Using graph structure to contain player relationships in Hoodwinked

[Presentation (in russian)](https://docs.google.com/presentation/d/1sCFkz34Qzv9lIhDiMWedF-vXo9Ch_3wh8cOGBJJqPq8/edit?usp=sharing)

This repo is based on "[Hoodwinked: Cooperation and Deception in a Text-Based Game for Language Models](https://arxiv.org/abs/2308.01404)." Hoodwinked is a text-based murder mystery game modeled after Mafia and Among Us. By forcing humans and language models to communicate in a strategic environment, this game evaluates the skills of deception, lie detection, and goal-directed communication. 

## What is this project about?
In games like Hoodwinked, LLM agents can usually lose some important information about other players and their actions. In some studies, it is common to use context summarization to extract important things. <br />
Our approach is to create a knowledge graph for each agent about other players and fill it with ratings based on people's actions and statements. This graph then helps the LLM focus on what's important, remembering who their friend is and who their enemy is. <br />
## Report
We are using LLama 3.1 8b-Instruct as primary agent model. The results can be significantly improved by using larger model (e.g. GPT-4, which was used in original paper). <br />
Current game stages:
1. Daytime players activities (searching the key)
2. Someone's got murdered
3. Players are discussing the event
4. Updating each agent's graph:
   1. Asking agent what does he think about each other player (we get detailed response containing score from 1 to 10)
   2. Extracting the score from response, updating the graph
5. Voting to banish 1 player
6. Repeat the process until there are no players/killer was banished
### Issues
- we noticed a bad LLama 3.1 8b ability to remember all complex instructions about the game. We had to make complex system prompt and lots of modifications of other prompts to avoid confusions and inadequate behaviour
- we noticed model's unability to rate other players in zero-shot (without detailed thinking in natural language). We assume it will also improve by using larger model
### Experiments
All experiments were performed on a100 40g gpu. <br />
Each experiment has at least 50 games and their results (calculated statistics) can be reproduced.
### Results
You can find all metrics calculations in <code>results/analysis.ipynb</code> <br />
You can also see metrics table in the [presentation](https://docs.google.com/presentation/d/1sCFkz34Qzv9lIhDiMWedF-vXo9Ch_3wh8cOGBJJqPq8/edit?usp=sharing)
## How to reproduce
First, clone the repo. 

Then install the required libraries in a virtual environment (e.g. conda)
```
conda create -n hoodwinked_sna
conda activate hoodwinked_sna
pip install -r requirements.txt
```

Now you can play the game! Just run `python demo.py`. You can edit player names and roles in `demo.py`. 

You can also run a batch of games. Specify the games you'd like to run in jobs/{integer}.csv, then run eval.py. Batch results will be saved in /results. 
