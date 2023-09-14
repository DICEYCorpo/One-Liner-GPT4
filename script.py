from dotenv import load_dotenv
import os
import openai
import csv
import pandas as pd
load_dotenv()



# Initialize an empty list to store the formatted rows
formatted_rows = []

# Open the CSV file for reading
with open('One-liner details ( Tech Companies) - Sheet1.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Initialize a line counter
    line_number = 1

    # Loop through each row in the CSV file
    for row in csv_reader:
        # Extract values from the row and format them
        values = [
            row.get('First', 'not found'),
            row.get('Title', 'not found'),
            row.get('Company', 'not found'),
            row.get('Education', 'not found'),
            row.get('Award/Certification', 'not found'),
            row.get('Degree', 'not found'),
            row.get('Last Post', 'not found')
        ]

        # Replace consecutive commas with ",not found"
        formatted_values = [value if value.strip() else 'not found' for value in values]

        # Combine the values into a single string separated by commas
        formatted_row = f"{line_number}. " + ','.join(formatted_values) + '.'

        # Append the formatted row to the list
        formatted_rows.append(formatted_row)

        # Increment the line counter
        line_number += 1

# Join the formatted rows into a single string with line breaks
result = '\n'.join(formatted_rows)

# Print the result or store it in a variable as needed
lines = result.split('\n')

# Calculate the number of lines per variable
lines_per_variable = len(lines) // 3

# Divide the lines into three variables
variable1 = '\n'.join(lines[:lines_per_variable])
variable2 = '\n'.join(lines[lines_per_variable:2*lines_per_variable])
variable3 = '\n'.join(lines[2*lines_per_variable:])



openai.api_key = os.getenv("OPENAIAPI")

print("40%...")
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You are a professional one liner cold mail writer who is currently working for an Indian cuisine restaurant situated in Miami. "
    },
    {
      "role": "user",
      "content": "We're trying to sell our corporate meal boxes, we are an indian cuisine restaurant based in maimi, I will give you the information on the prospects, I want you to use the info to craft engaging custom one liners for each prospect. The one liners should be concisee and enough to hook their attention, they should seem highly personalized, I would want you to keep in mind all of the given information on a prospect while crafting the one liners. But, a general priority order would look like this: Last Post > Award/Certification > Degree, Education > Job Title. Make sure you mention their name in the most appropriate way in the one liners.\nGenerate catchy one liners related to the person's gathered information so that we can catch their attention through cold emails. \n\nFirst name,Title,Company,Education,Award/Certification,Degree,Last Post.\n\nThese informations are provided sequencially in the lines below. Just reply and no need to add quotations marks around the sentences. \n\n\n\n\n"+variable1
    }
  ],
  temperature=1,
  max_tokens=2600,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

gpt_response1 = response['choices'][0]['message']['content']

print("75%...")
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You are a professional one liner cold mail writer who is currently working for an Indian cuisine restaurant situated in Miami. "
    },
    {
      "role": "user",
      "content": "We're trying to sell our corporate meal boxes, we are an indian cuisine restaurant based in maimi, I will give you the information on the prospects, I want you to use the info to craft engaging custom one liners for each prospect. The one liners should be concisee and enough to hook their attention, they should seem highly personalized, I would want you to keep in mind all of the given information on a prospect while crafting the one liners. But, a general priority order would look like this: Last Post > Award/Certification > Degree, Education > Job Title. Make sure you mention their name in the most appropriate way in the one liners.\nGenerate catchy one liners related to the person's gathered information so that we can catch their attention through cold emails. \n\nFirst name,Title,Company,Education,Award/Certification,Degree,Last Post.\n\nThese informations are provided sequencially in the lines below. Just reply and no need to add quotations marks around the sentences. \n\n\n\n\n"+variable2
    }
  ],
  temperature=1,
  max_tokens=2600,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

gpt_response2 = response['choices'][0]['message']['content']


print("Generating Final Response...")
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You are a professional one liner cold mail writer who is currently working for an Indian cuisine restaurant situated in Miami. "
    },
    {
      "role": "user",
      "content": "We're  an indian cuisine restaurant based in maimi trying to sell our corporate meal boxes. I want you to use the info to craft engaging custom one liners for each prospect. The one liners should be concisee and enough to hook their attention, they should seem highly personalized, But, a general priority order would look like this: Last Post > Award/Certification > Degree, Education > Job Title. Make sure you mention their name in the most appropriate way in the one liners.\nGenerate catchy one liners related to the person's gathered information so that we can catch their attention through cold emails. \n\nFirst name,Title,Company,Education,Award/Certification,Degree,Last Post.\n\nThese informations are provided sequencially in the lines below. Just reply and no need to add quotations marks around the sentences. \n\n\n\n\n"+variable3
    }
  ],
  temperature=1,
  max_tokens=2600,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

gpt_response3 = response['choices'][0]['message']['content']

final = gpt_response1+gpt_response2+gpt_response3


print(final)
# Split the variable into individual lines
# lines = final.strip().split('\n')
#
# # Remove the numbering at the beginning of each sentence
# one_liners = [line.split(". ", 1)[1] for line in lines]
#
# # Load the existing CSV file into a DataFrame
# csv_file_path = 'One-liner details ( Tech Companies) - Sheet1.csv'
# df = pd.read_csv(csv_file_path)
#
# # Add the "One Liners" column to the DataFrame
# df['One Liners'] = one_liners
#
# # Save the DataFrame back to the CSV file with the new column
# df.to_csv(csv_file_path, index=False)
#
# print(f"The 'One Liners' column has been added to the existing CSV file '{csv_file_path}'.")
