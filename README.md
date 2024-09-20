# vectara UAgents RAG
This RAG is created using vectara API and wrapped using fetchs' uAgents. It is deployed Agentverse. This answers all your queries related to fetch uagents.

# Creating Account on Vectara and creating corpus
  - Create an account on (Vectara)[https://vectara.com/].
  - Goto the (Console)[https://console.vectara.com/console/corpora] and create new corpus for yourself using (https://github.com/user-attachments/assets/4c4317c6-e324-4389-8b96-8dc984dc2f86) button.
  - Decide the type of application later and give `name` and `key` for your corupus here. In our case it is `fetchai-docs-explorer`. The corpus key will be used to make API calls to the corpus.
  - Get the `API_KEY` from [Authorisation](https://console.vectara.com/console/apiAccess/personalApiKey) in menu.

# Adding docs to corpus which will be used as RAG knowledge.
  - Goto your corpus and click `data` tab.
  - Click on ![Screenshot 2024-09-20 at 16 44 20](https://github.com/user-attachments/assets/2b91d888-048d-45af-83a8-c8127af861e4) and add data by clicking on ![Screenshot 2024-09-20 at 16 44 53](https://github.com/user-attachments/assets/4c3a8330-698a-4122-9eb0-77a5f26592a7) button.
  - You can upload text, HTML, PDF, Word and other files here.

# Creating Agentverse Agent
  - Goto [Agentverse](https://agentverse.ai/) and login using google.
  - Create a news blank agent from here.![Screenshot 2024-09-20 at 16 46 57](https://github.com/user-attachments/assets/ced62510-2abf-46ce-acad-25e82a7523bb)
  - copy the code in [agent.py](https://github.com/abhifetch/vectaraUAgentsRAG/blob/main/agents.py) and save in `agent.py` file.
  - Add a new python script and name it as `helper_functions.py`. Copy the script from [here](https://github.com/abhifetch/vectaraUAgentsRAG/blob/main/helper_functions.py) and save into that script.
  - Add secrets to your agent by hitting ![Screenshot 2024-09-20 at 16 49 19](https://github.com/user-attachments/assets/aff27e9c-d2a6-4554-a8ab-975e35932058) button and save the `API_KEY` and `CORPUS_KEY` obtained from your vectara console.

# creating Agentverse Function
  - Go to Deploy tab of your agent and click on ![Screenshot 2024-09-20 at 16 51 14](https://github.com/user-attachments/assets/a2757803-5e56-4d0d-afa3-24154695cd73) button.
  - Enter the details on functions as shown in below image.
![Screenshot 2024-09-20 at 16 52 15](https://github.com/user-attachments/assets/41ab5dfe-99a4-415f-bc73-2b38304c63b4)
  - Rest details are self populated and click ![Screenshot 2024-09-20 at 16 52 47](https://github.com/user-attachments/assets/6e2e6153-217e-4105-a1a4-7f551d974315) button.
  - Once your agent is create click on ![Screenshot 2024-09-20 at 16 53 23](https://github.com/user-attachments/assets/5fda6cb1-c7e9-47ae-89a2-07bd3d7bdf4d).

# Using agent on deltaV
  [Watch the video on YouTube](https://youtu.be/5IliBuMlhc8)
  - Use the below video for reference on how to use this on [deltaV](https://deltav.agentverse.ai/).

If you want to access this agent go to [DeltaV](https://deltav.agentverse.ai/home) and select Public Function Group.

# NOTE :

IF YOU MAKE ANY CHANGES TO THE DATA MODELS PLEASE DO REMEMBER TO GO BACK TO FUNCTIONS AND UPDATE THE FUNCTION EVEN IF THERE ARE NO CHANGES.






