from dotenv import load_dotenv
import os
import openai
import csv
from io import StringIO

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
total_lines = len(lines)
lines_per_variable = total_lines // 5

# Divide the lines into five variables
variable1 = '\n'.join(lines[:lines_per_variable])
variable2 = '\n'.join(lines[lines_per_variable:2*lines_per_variable])
variable3 = '\n'.join(lines[2*lines_per_variable:3*lines_per_variable])
variable4 = '\n'.join(lines[3*lines_per_variable:4*lines_per_variable])
variable5 = '\n'.join(lines[4*lines_per_variable:])
print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)


openai.api_key = os.getenv("OPENAIAPI")

print("20%...")
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
print("20 Response: " + gpt_response1)

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
      "content": "We're trying to sell our corporate meal boxes, we are an indian cuisine restaurant based in Miami. I will give you the information on the prospects, I want you to use the info to craft engaging custom one liners for each prospect. The one-liners should be concise yet interesting and well-written enough to hook their attention. They should seem highly personalized, and make the prospect feel noticed and special. I would want you to keep in mind all of the given information on a prospect while crafting the one liners. But, a general priority order would look like this: Last Post > Award/Certification > Degree, Education > Job Title. Use all data points if possible. Make sure you mention their name in the most appropriate way in the one liners. Follow the line numbers to create the exact number of one liners. \nGenerate catchy one liners related to the person's gathered information so that we can catch their attention through cold emails.\n\nFirst name,Title,Company,Education,Award/Certification,Degree,Last Post.\n\nThese informations are provided sequencially in the lines below. Just reply and no need to add quotations marks around the sentences. \n\n\n\n\n"+variable2
    }
  ],
  temperature=1,
  max_tokens=2600,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

gpt_response2 = response['choices'][0]['message']['content']
print("40 Response: " + gpt_response2)

print("60%...")
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You are a cold email professional with exceptional writing skills, who is currently working on writing highly personalized custom one-liners on potential prospects for an Indian cuisine restaurant situated in Miami."
    },
    {
      "role": "user",
      "content": "We're trying to sell our corporate meal boxes, we are an indian cuisine restaurant based in Miami. I will give you the information on the prospects, I want you to use the info to craft engaging custom one liners for each prospect. The one-liners should be concise yet interesting and well-written enough to hook their attention. They should seem highly personalized, and make the prospect feel noticed and special. I would want you to keep in mind all of the given information on a prospect while crafting the one liners. But, a general priority order would look like this: Last Post > Award/Certification > Degree, Education > Job Title. Use all data points if possible. Make sure you mention their name in the most appropriate way in the one liners. Follow the line numbers to create the exact number of one liners. \nGenerate catchy one liners related to the person's gathered information so that we can catch their attention through cold emails.\n\nFirst name,Title,Company,Education,Award/Certification,Degree,Last Post.\n\nThese informations are provided sequencially in the lines below. Just reply and no need to add quotations marks around the sentences. \n\n\n\n\n"+variable3
    }
  ],
  temperature=1,
  max_tokens=2600,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

gpt_response3 = response['choices'][0]['message']['content']
print("60 Response: " + gpt_response3)
print("80%...")
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You are a cold email professional with exceptional writing skills, who is currently working on writing highly personalized custom one-liners on potential prospects for an Indian cuisine restaurant situated in Miami."
    },
    {
      "role": "user",
      "content": "We're trying to sell our corporate meal boxes, we are an indian cuisine restaurant based in Miami. I will give you the information on the prospects, I want you to use the info to craft engaging custom one liners for each prospect. The one-liners should be concise yet interesting and well-written enough to hook their attention. They should seem highly personalized, and make the prospect feel noticed and special. I would want you to keep in mind all of the given information on a prospect while crafting the one liners. But, a general priority order would look like this: Last Post > Award/Certification > Degree, Education > Job Title. Use all data points if possible. Make sure you mention their name in the most appropriate way in the one liners. Follow the line numbers to create the exact number of one liners. \nGenerate catchy one liners related to the person's gathered information so that we can catch their attention through cold emails.\n\nFirst name,Title,Company,Education,Award/Certification,Degree,Last Post.\n\nThese informations are provided sequencially in the lines below. Just reply and no need to add quotations marks around the sentences. \n\n\n\n\n"+variable4
    }
  ],
  temperature=1,
  max_tokens=2600,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

gpt_response4 = response['choices'][0]['message']['content']
print("80 Response: " + gpt_response4)

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You are a cold email professional with exceptional writing skills, who is currently working on writing highly personalized custom one-liners on potential prospects for an Indian cuisine restaurant situated in Miami."
    },
    {
      "role": "user",
      "content": "We're trying to sell our corporate meal boxes, we are an indian cuisine restaurant based in Miami. I will give you the information on the prospects, I want you to use the info to craft engaging custom one liners for each prospect. The one-liners should be concise yet interesting and well-written enough to hook their attention. They should seem highly personalized, and make the prospect feel noticed and special. I would want you to keep in mind all of the given information on a prospect while crafting the one liners. But, a general priority order would look like this: Last Post > Award/Certification > Degree, Education > Job Title. Use all data points if possible. Make sure you mention their name in the most appropriate way in the one liners. Follow the line numbers to create the exact number of one liners. \nGenerate catchy one liners related to the person's gathered information so that we can catch their attention through cold emails.\n\nFirst name,Title,Company,Education,Award/Certification,Degree,Last Post.\n\nThese informations are provided sequencially in the lines below. Just reply and no need to add quotations marks around the sentences. \n\n\n\n\n"+variable5
    }
  ],
  temperature=1,
  max_tokens=2600,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

gpt_response5 = response['choices'][0]['message']['content']
print("Final Response: " + gpt_response5)

combined_lines = gpt_response1+"\n"+gpt_response2+"\n"+gpt_response3+"\n"+gpt_response4+"\n"+gpt_response5


# Split the response into individual lines
lines = combined_lines.split("\n")

# Remove empty lines and leading/trailing spaces
lines = [line.strip() for line in lines if line.strip()]

# Create a CSV buffer
csv_buffer = StringIO()

# Define the CSV writer
csv_writer = csv.writer(csv_buffer)

# Write the header
csv_writer.writerow(["one liners"])

# Write each line as a row in the CSV
for line in lines:
    csv_writer.writerow([line])

# Reset the buffer position to the beginning
csv_buffer.seek(0)

# Save the CSV data to a file
with open("output.csv", "w", newline="") as csv_file:
    csv_file.write(csv_buffer.getvalue())

# Close the CSV buffer
csv_buffer.close()


# Open and read the first CSV file (csv1)
csv1_data = []
with open('output.csv', 'r', newline='', encoding='utf-8', errors='ignore') as csv1_file:
    csv_reader = csv.reader(csv1_file)
    headers = next(csv_reader)  # Read and store the header row
    for row in csv_reader:
        csv1_data.append(row[0])  # Assuming "one liners" is the first column in csv1

# Open and update the second CSV file (csv2)
with open('One-liner details ( Tech Companies) - Sheet1.csv', 'r', newline='', encoding='utf-8', errors='ignore') as csv2_file:
    csv2_data = list(csv.reader(csv2_file))

# Add the "one liners" column from csv1 to csv2
csv2_data[0].append("one liners")  # Add the column header
for i, row in enumerate(csv2_data[1:], start=1):
    row.append(csv1_data[i-1])  # Append the corresponding value from csv1_data

# Save the updated csv2 with the added column
with open('updated_csv2.csv', 'w', newline='', encoding='utf-8', errors='ignore') as updated_csv2_file:
    csv_writer = csv.writer(updated_csv2_file)
    csv_writer.writerows(csv2_data)