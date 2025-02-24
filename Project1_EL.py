from ollama import chat
from ollama import ChatResponse
import os
# Required librays for Ollama and file I/O

# Deletes \n at the end of lines
def RMNewLine(arr, index):
    temp = arr[index]
    arr[index] = temp[:-1]
    return

# Reads prompts from txt file and adds them to an array
def FileToArr(fileName, arr):
    file = open(fileName, "r")

    for line in file:
        prompt.append(line)

    file.close()

    RMNewLine(prompt, 0)
    RMNewLine(prompt, 1)
    return

# Creates new file for responses
def CreateFile(fileName):
    file = open(fileName, "w")
    file.close()

# Writes responses to file
def WriteResponses(fileName, responses):
    file = open(fileName , "a")
    file.write(responses)
    file.close()

# Gives AI a prompt and then returns the result
def AIResponse(model, prompt):
    response:ChatResponse = chat(model, messages = [
        {
            'role' : 'user',
            'content': prompt,
        },
    ])

    return response.message.content


readFile = "prompts.txt"
prompt = []

FileToArr(readFile, prompt)

CreateFile("phi3_responses.txt")
WriteResponses("phi3_responses.txt", "Phi3 Mini responses\n")

for query in prompt:
    WriteResponses("phi3_responses.txt", AIResponse('Phi3:mini', query))

CreateFile("llama3_responses.txt")
WriteResponses("llama3_responses.txt", "Llama 3.2 responses\n")

for query in prompt:
    WriteResponses("llama3_responses.txt", AIResponse('llama3.2', query))

print("Finished writing responses.")