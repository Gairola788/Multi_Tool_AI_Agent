
from weather_tool import weather_Agent
from calculator_tool import calculate_Agent
from search_tool import search_Agent

def user_description(user_input):
    
    user_input.lower()
    
    if "weather" in user_input:
        city = user_input.split("in")[-1].strip()
        return weather_Agent(city)
    
    elif "search" in user_input:
        query = user_input.replace("search","").strip()
        return search_Agent(query)
        
    elif "calculate" in user_input:
         expression = user_input.replace("calculate","").strip()
         return calculate_Agent(expression)
    
    else:
        return "I did not understand your Requirements,pls ask questions as suggested"
        

while True:
    
    user = input("Ask any query regarding calculations ,weather or web search")
    
    if(user.lower() == 'exit'):
        break
    
    print(user_description(user))
    