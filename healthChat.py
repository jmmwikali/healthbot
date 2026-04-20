import pandas as pd

# Load your data into a dataframe
df = pd.read_csv("health_data.csv")
# print(df)
print("\n HealthBot: Hello there, i am your help assistant bot. Ask me about any symptoms.")
while True:
    # Get the user input and store the same into a variable
    user_text = input("\n You: ").lower()
    
    # Check if the user want to exit
    if user_text == "quit":
        print("\n HealthBot: Goodbye! Nice to have been of service to you. Stay Healthy.")
        break

    # Create a variable that will store the details structured in the csv file
    found_answer =  False

    # Come up with a loop that loops through the entire data frame created before
    for index, row in df.iterrows():
        # Clean up the key words from the csv row
        keywords_list = str(row['Keywords']).split(",")

        # Below we heck every key wordin that given row (Keywords)
        for  word in keywords_list:
            clean_word = word.strip().lower()

            # If the keyword in inside of the user sentence
            if clean_word in user_text:
                print("\n HealthBot:", row["Response"])
                found_answer = True
                break # Stop looking at the other keywords
        
        if found_answer:
            break # Stop looking at other answers since we already found a match

    # If we went throught thr entire/wholecsv file and never found any match for the keyword, we need to display a message to the use
    if not found_answer:
        print("\n HealthBot: Sorry, i do not know that one. Try asking for something else.")
