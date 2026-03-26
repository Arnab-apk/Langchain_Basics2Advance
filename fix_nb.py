import json

nb_path = r'C:/Users/arnab/Desktop/Folders/Langchain/Langchain_Nayak/GenerativeAI/agent_intro.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        for i, line in enumerate(source):
            if "from langchain.agents import create_agent" in line:
                source[i] = line.replace("from langchain.agents import create_agent", "from langgraph.prebuilt import create_react_agent")
            
            if "agent = create_agent(" in line:
                source[i] = line.replace("agent = create_agent(", "agent = create_react_agent(")
                
            if "system_prompt=" in line:
                source[i] = line.replace("system_prompt=", "state_modifier=")

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=4)
print("Notebook modified successfully.")
