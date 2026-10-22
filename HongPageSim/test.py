import ollama

response = ollama.generate(
    model='llama3.1:8b', 
    prompt='You are an agent trying to find the maximum value in a list of 1000 elements. You can move only forward and the list loops around when you get to the end. I want you to develop a strategy called a heuristic. Your heuristic consists of the steps forward you want to take. It can only be 4 elements long, cannot include duplicates, and can have your elements in any order. The maximum steps forward you can take (the maximum element you can have in your heuristic) is 20. You will begin by checking the value of the location (your starting location plus the first element of your heuristic). If that is better than your current location, you will move there and check (that location plus your second heuristic). If not, check your starting location plus second heuristic. Repeat until you have exhausted your list of heuristics and cannot find a better location to move to. What is your heuristic?'
    ) 

print(response['response'])
