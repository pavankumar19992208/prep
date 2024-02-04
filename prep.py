import streamlit as st
from pymongo import MongoClient
import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB Atlas
# client = MongoClient("mongodb+srv://pavan_tech:U0q0E6cdGK2CCNtY@cluster0.3zqhlo9.mongodb.net/?retryWrites=true&w=majority")
# db = client.get_database('pavan')
# records = db.test
# Replace <YOUR_MONGODB_URI> with your actual MongoDB URI
mongo_uri = "mongodb+srv://pavan_tech1:Amma9502@cluster0.3zqhlo9.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)

# Access your database and collection
db = client.get_database('pavan')
collection = db.get_collection('users')
records = db.test
# Streamlit UI
st.title("HELLO SAKEE MADAME")
st.caption("A GOOD TEACHER IS LIKE A CANDLE. IT CONSUMES ITSELF TO LIGHT THE WAY FOR OTHERS")

st.markdown("### EVERY ONE STARTS AT ZERO. BUT IT MATTERS WHO TURNS INTO HERO")

subject = st.selectbox('SELECT SUBJECT', ['MATHEMATICS', 'SCIENCE', 'SOCIAL', 'PSYCHOLOGY', 'TELUGU', 'ENGLISH'])
topic = st.text_input('ENTER TOPIC')
marks = st.text_input('Marks (optional)')
strength = st.selectbox('STRENGTH', ['WEAK', 'MEDIUM', 'STRONG'])

if st.button('Submit'):
    new_record = {
        'subject': subject,
        'topic': topic,
        'marks': marks,
        'strength': strength
    }
    records.insert_one(new_record)

# Fetch records and display
all_records = records.find()

# Create a dictionary to store records by subject
subject_records = {}

for record in all_records:
    subject = record['subject']
    topic = record['topic']
    marks = record['marks']
    strength = record['strength']

    # Create a new record dictionary
    new_record = {
        'topic': topic,
        'marks': marks,
        'strength': strength
    }

    # Add the record to the subject_records dictionary
    if subject in subject_records:
        subject_records[subject].append(new_record)
    else:
        subject_records[subject] = [new_record]

# Display records in a grid format
for subject, records in subject_records.items():
    st.markdown("### Subject: " + subject)
    df = pd.DataFrame(records)
    
    # Set background color based on strength value
    def highlight_strength(row):
        if row['strength'] == 'STRONG':
            return ['background-color: rgba(0,255,0, 0.1)'] * len(row)
        elif row['strength'] == 'WEAK':
            return ['background-color: rgba(255, 0, 0, 0.1)'] * len(row)
        else:
            return [''] * len(row)
    
    st.dataframe(df.style.apply(highlight_strength, axis=1))

