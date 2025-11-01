from dotenv import load_dotenv
load_dotenv()

from crewai import LLM

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.1
)

from crewai import Agent,Task,Crew

research_agent=Agent(
    role="Research Specialist",
    goal="Research interesting facts about the topic: {topic}",
    backstory="You are an expert at finding relevant and factual data.",
    verbose=True,
    llm=llm
)

writer_agent=Agent(
    role="Creative Writer",
    goal="Write a short blog summary usinig the research",
    backstory="You are skilled at writing engaging summaries based on provided content.",
    llm=llm,
    verbose=True
)

seo_agent=Agent(
    name="SEO Strategist",
    role="Analyze blog content and optimize it for SEO without compromising readability",
    goal=
        """Identify primary and secondary keywords related to the topic,
        Generate meta title and meta description,
        Ensure proper heading structure (H1,H2,H3),
        Advise on keyword placement and linking strategy.,
        keep keyword density below 2%,
        Use modern SEO principles.
    """,
    backstory="You are skilled at Search Engine Optimization and knows about the techniques to apply for blogs.",
    llm=llm,
    verbose=True
)


task1=Task(
    description="Find 10-15 interesting and latest facts about {topic}.",
    expected_output="A bullet list of 10-15 facts",
    agent=research_agent
)

task2=Task(
    description="Write a 300 to 500 word blog post summary about {topic} using the facts from the research.",
    expected_output="A blog post summary",
    agent=writer_agent,
    context=[task1]
)

task3=Task(
     description="Analyze the final blog draft and output SEO recommendations including keywords, meta title, and meta description.",
     expected_output="Output in JSON format with keys: keywords, meta_title, meta_description, recommendations.",
     agent=seo_agent,
     inputs={"blog_draft":"{{writer_agent_output}}"}
)

task4=Task(
    description="Revise the blog draft based on SEO recommendations.",
    expected_output="A refined blog based on the SEO recommendations",
    agent=writer_agent,
    inputs={
        "draft":"{{writer_agent_output}}",
        "seo_feedback":"{{seo_agent_output}}"
    }
)

def generate_blog(topic: str):

    crew=Crew(
    agents=[research_agent,writer_agent,seo_agent],
    tasks=[task1,task2,task3,task4],
    verbose=True,
)

    result=crew.kickoff(inputs={"topic":topic})
    return result

if __name__=="__main__":
    print("importing main func")
    result=generate_blog("The future of electrical vehicles")
    print(result)
    