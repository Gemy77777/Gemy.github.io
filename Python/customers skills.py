users = {
    'Gemy':{
        'Html': '80%',
        'Css': '70%',
        'JavaScript': '60%'
    },
    'Alice':{
        'Html': '90%',
        'Css': '80%',
        'JavaScript': '70%'
    },
    'Ahmed':{
        'Html': '75%',
        'Css': '65%',
        'JavaScript': '55%'
    }
}
for user, skills in users.items():
    print(f"{user}:")
    for skill, level in skills.items():
        print(f"- {skill}: {level}")