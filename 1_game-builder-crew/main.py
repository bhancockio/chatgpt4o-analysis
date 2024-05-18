import agentops
from agents import GameAgents
from tasks import GameTasks
from crewai import Crew
from dotenv import load_dotenv
load_dotenv()

agentops.init(tags=["game_builder"])

tasks = GameTasks()
agents = GameAgents()

print("## Welcome to the Game Crew")
print('-------------------------------')
game = """Snake is a classic arcade game where the player controls a snake that continuously moves around the screen. 
The objective is to navigate the snake to eat randomly placed food items, causing the snake to grow in length with each item consumed. 
The game ends if the snake runs into the screen boundaries or collides with its own body, requiring careful maneuvering to achieve a high score."""

# Create Agents
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# Create Tasks
code_game = tasks.code_task(senior_engineer_agent, game)
review_game = tasks.review_task(qa_engineer_agent, game)
approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)

# Create Crew responsible for Copy
crew = Crew(
    agents=[
        senior_engineer_agent,
        qa_engineer_agent,
        chief_qa_engineer_agent
    ],
    tasks=[
        code_game,
        review_game,
        approve_game
    ],
    verbose=True
)

game = crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code for the game:")
print(game)
