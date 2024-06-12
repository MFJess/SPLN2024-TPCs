import jinja2
from glob import glob
import ast

# para todas os Import que serao as dependencias
def extract_dependencies(filename):
    with open(filename, 'r') as file:
        texto = ast.parse(file.read(), filename=filename)
    
    dependencies = set()
    for nodo in ast.walk(texto): # para todos os nodos do texto
        if isinstance(nodo, ast.Import): # se nodo é um import
            for alias in nodo.names: 
                dependencies.add(alias.name) # adicionar package como dependencia
        elif isinstance(nodo, ast.ImportFrom): # se nodo é um ImportFrom
            dependencies.add(nodo.module) # adicionar modulo como dependencia
    
    return list(dependencies)


# todos os ficheiros python
py = glob("*.py")


# extrair todas as dependencias sem repetidos, dos ficheiros de python
all_dependencies = set()
for mode in py: 
    dependencies = extract_dependencies(mode) 
    all_dependencies.update(dependencies)


# se houver ficheiros python escolher o principal
if py:
   ans = 0
   while not (ans.isdigit() and int(ans) <= len(py)): # enquanto a resposta nao for um digito correspondente ao numero de um ficheiro py
    print("Select the main file:")
    for file, mode in enumerate(py, start=1): # mostrar todas as opções
        print(f"{file}. {mode}")

    ans = input("Enter the respective number: ") # pedir a resposta
    if ans.isdigit() and int(ans) <= len(py): # verifica se cumpre as condicoes e se sim, escolhe
        primary_index = int(ans) - 1
        name = py[primary_index].replace(".py", "")
else:
    name = "Module?"

# Create Jinja2 template
pp = jinja2.Template("""[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "{{name}}"
authors = [
    {name = "{{autor}}", email = "{{email}}"},
]
classifiers = [
    "License :: OSI Approved :: MIT License",
]
requires-python = ">=3.8"
dynamic = ["version", "description"]
dependencies = [
    {% for dependency in dependencies %}
    "{{ dependency }}",
    {% endfor %}
]

[project.scripts]
{{name}} = "{{name}}:main"
""")

# Render the template with dependencies
rendered_content = pp.render(name=name, autor="MFJess", email="a93318@alunos.uminho.pt", dependencies=all_dependencies)

print(rendered_content)