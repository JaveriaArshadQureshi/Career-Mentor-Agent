import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from roadmap_tool import get_career_roadmap

# Load environment variables from .env file
load_dotenv()
# Initialize the OpenAI model

client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"  # Adjust the base URL as needed
)

model = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)
config = RunConfig(model=model, tracing_disabled=True)

# Create an agent with the career roadmap tool
career_agent = Agent(
    name="CareerRoadmapAgent",
    instructions="You ask about interests and suggest a career field.",
    model=model
)

skills_agent = Agent(
    name="SkillsAgent",
    instructions="Create roadmap using the get_career_roadmap tool.",
    model=model,
    tools=[get_career_roadmap]  # Register the career roadmap tool
)

job_agent = Agent(
    name="JobAgent",
    instructions="Your role is to suggest job title .",
    model=model
)

def main():
    print("Welcome to the Career Roadmap Assistant!")
    interests = input("What are your interests? ")

    result1 = Runner.run_sync(career_agent, interests, run_config=config)
    field = result1.final_output.strip()
    print("\n  Suggested career field: ",field)

    result2 = Runner.run_sync(skills_agent, field, run_config=config)
    print("\n Required Skills:", result2.final_output)

    result3 = Runner.run_sync(job_agent, field, run_config=config)
    print("\n Suggested Job Title: ", result3.final_output)

if __name__ == "__main__":
        main()