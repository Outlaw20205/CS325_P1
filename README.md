#Project 1 - Ethan Lawrence - CS325

##Step 1: Create and activate the envirnoment
conda create -n P1_EL_CS325 python
conda activate P1_EL_CS325

##Step 2: Install Ollama on your system
Download installer from https://ollama.com/download and install for your system

##Step 3: Install Ollama python library
pip install ollama

##Step 4: Pull LLMs Llama 3.2 and Phi3 Mini
ollama pull llama3.2
ollama pull phi3:mini

##Step 5: Run the Project1_EL.py file
C:\<your_directory>\python.exe Project1_EL.py
Response file will be saved as <model_name>_responses.py