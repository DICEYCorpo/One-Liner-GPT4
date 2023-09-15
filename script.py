from dotenv import load_dotenv
import os
import openai
import csv
import re

load_dotenv()



csv_file = "One-liner details ( Tech Companies) - Sheet1.csv"  # Replace with the path to your CSV file

# Initialize an empty list to store the rows with line numbers
formatted_rows = []

# Open the CSV file and read its contents
with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    # Skip the header row if it exists
    header = next(reader, None)

    # Initialize a line number counter
    line_number = 1

    # Iterate through the rows in the CSV file
    for row in reader:
        # Format the values as a comma-separated string
        formatted_values = [f"{value.strip()}" for value in row]

        # Create the formatted row with line number
        formatted_row = f"{line_number}. " + ', '.join(formatted_values) + '.'

        # Append the formatted row to the list
        formatted_rows.append(formatted_row)

        # Increment the line number counter
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
      "content": "You are a cold email professional with exceptional writing skills, who is currently working on writing highly personalized custom one-liners on potential prospects for an Indian cuisine restaurant situated in Miami."
    },
    {
      "role": "user",
      "content": "We're trying to sell our corporate meal boxes, we are an indian cuisine restaurant based in Miami. I will give you the information on the prospects, I want you to use the info to craft engaging custom one liners for each prospect. The one-liners should be concise yet interesting and well-written enough to hook their attention. They should seem highly personalized, and make the prospect feel noticed and special. I would want you to keep in mind all of the given information on a prospect while crafting the one liners. But, a general priority order would look like this: Last Post > Award/Certification > Degree, Education > Job Title. Use all data points if possible. Make sure you mention their name in the most appropriate way in the one liners. Follow the line numbers to create the exact number of one liners. \nGenerate catchy one liners related to the person's gathered information so that we can catch their attention through cold emails.\n\nFirst name,Title,Company,Education,Award/Certification,Degree,Last Post.\n\nThese informations are provided sequencially in the lines below. Just reply and no need to add quotations marks around the sentences. \n\n\n\n\n"+variable1
    }
  ],
  temperature=1,
  max_tokens=2600,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

gpt_response1 = response['choices'][0]['message']['content']
gpt_response1_list = re.split(r'\d+\.', gpt_response1)
gpt_response1_list = [gpt_response1_list.strip() for gpt_response1_list in gpt_response1_list if gpt_response1_list.strip()]
print("-------------------------Variables-------------------------")
print(variable1)
print("------------------Response-------------------------")
print(gpt_response1)
print("list length:",len(gpt_response1_list))

print("75%...")
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You are a cold email professional with exceptional writing skills, who is currently working on writing highly personalized custom one-liners on potential prospects for an Indian cuisine restaurant situated in Miami."
    },
    {
      "role": "user",
      "content": "We're trying to sell our corporate meal boxes, we are an indian cuisine restaurant based in Miami. I will give you the information on the prospects, I want you to use the info to craft engaging custom one liners for each prospect. The one-liners should be concise yet interesting and well-written enough to hook their attention. They should seem highly personalized, and make the prospect feel noticed and special. I would want you to keep in mind all of the given information on a prospect while crafting the one liners. But, a general priority order would look like this: Last Post > Award/Certification > Degree, Education > Job Title. Use all data points if possible. Make sure you mention their name in the most appropriate way in the one liners. \nGenerate catchy one liners related to the person's gathered information so that we can catch their attention through cold emails.\n\nFirst name,Title,Company,Education,Award/Certification,Degree,Last Post.\n\nThese informations are provided sequencially in the lines below. Just reply and no need to add quotations marks around the sentences. \n\n\n\n\n"+variable2
    }
  ],
  temperature=1,
  max_tokens=2600,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

gpt_response2 = response['choices'][0]['message']['content']
gpt_response2_list = re.split(r'\d+\.', gpt_response2)
gpt_response2_list = [gpt_response2_list.strip() for gpt_response2_list in gpt_response2_list if gpt_response2_list.strip()]
print("-------------------------Variables-------------------------")
print(variable2)
print("------------------Response-------------------------")
print(gpt_response2)
print("list length:",len(gpt_response2_list))
print("Generating Final Response...")
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You are a cold email professional with exceptional writing skills, who is currently working on writing highly personalized custom one-liners on potential prospects for an Indian cuisine restaurant situated in Miami."
    },
    {
      "role": "user",
      "content": "We're trying to sell our corporate meal boxes, we are an indian cuisine restaurant based in Miami. I will give you the information on the prospects, I want you to use the info to craft engaging custom one liners for each prospect. The one-liners should be concise yet interesting and well-written enough to hook their attention. They should seem highly personalized, and make the prospect feel noticed and special. I would want you to keep in mind all of the given information on a prospect while crafting the one liners. But, a general priority order would look like this: Last Post > Award/Certification > Degree, Education > Job Title. Use all data points if possible. Make sure you mention their name in the most appropriate way in the one liners. \nGenerate catchy one liners related to the person's gathered information so that we can catch their attention through cold emails.\n\nFirst name,Title,Company,Education,Award/Certification,Degree,Last Post.\n\nThese informations are provided sequencially in the lines below. Just reply and no need to add quotations marks around the sentences. \n\n\n\n\n"+variable3
    }
  ],
  temperature=1,
  max_tokens=2600,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

gpt_response3 = response['choices'][0]['message']['content']
gpt_response3_list = re.split(r'\d+\.', gpt_response3)
gpt_response3_list = [gpt_response3_list.strip() for gpt_response3_list in gpt_response3_list if gpt_response3_list.strip()]
print("-------------------------Variables-------------------------")
print(variable3)
print("------------------Response-------------------------")
print(gpt_response3)
print("list length:",len(gpt_response3_list))

combined_lines = gpt_response1_list+gpt_response2_list+gpt_response3_list


input_csv_file = "One-liner details ( Tech Companies) - Sheet1.csv"
output_csv_file = "output.csv"

# Read the existing CSV file and store its content in a list of dictionaries
data = []
with open(input_csv_file, mode="r", newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        data.append(row)

# Make sure the number of rows in the CSV matches the number of lines in combined_lines
if len(data) != len(combined_lines):
    print("Error: The number of rows in the CSV does not match the number of lines in combined_lines.")
else:
    # Add a new "One Liner" column to each row and populate it with the corresponding line from combined_lines
    for i, row in enumerate(data):
        row["One Liner"] = combined_lines[i]

    # Write the updated data to the output CSV file
    with open(output_csv_file, mode="w", newline="", encoding="utf-8") as outfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for row in data:
            writer.writerow(row)

    print("CSV file has been updated with the 'One Liner' column.")
