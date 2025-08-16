MySkills = {
    "Python": "90%",
    "JavaScript": "60%",
    "HTML": "80%",
    "CSS": "70%"
}
MyTuple = ('go', 'c++', 'figma')

def display_tools(tools):
    for tool in tools:
        print(f"lang: {tool}")
def display_skills(skills):
    for skill, level in skills.items():
        print(f"{skill}: {level}")
display_skills(MySkills)
print(50 * "=")
display_tools(MyTuple)