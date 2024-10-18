import streamlit as st
from datetime import datetime
import pandas as pd
from predictions import *

dateMin = datetime.strptime('01-01-2018', '%d-%m-%Y')
df = pd.read_csv(r'dataset/Preproccessed.csv')

selected_colomn = ['Region', 'Location', 'Department', 'quarters', 'years', 'shift_type', 'shiftHrs', 'Skill']


org_unique = ['Select'] + df['Organization'].unique().tolist()
# Create columns to reduce dropdown width
col1, _ = st.columns([1, 3])  # Adjust the proportion to control width

with col1:
    org = st.selectbox('Select a Organization', org_unique)

if org != "Select":
    temp_df = df[df['Organization'] == org]
    location_unique = ['Select'] + temp_df['Location'].unique().tolist()


    with col1:
        Location = st.selectbox('Select a Location', location_unique)

    if Location != 'Select':
        temp_df = temp_df[temp_df['Location'] == Location]
        Department_unique = ['Select'] + temp_df['Department'].unique().tolist()

        with col1:
            Department = st.selectbox('Select a Department', Department_unique)

        if Department != 'Select':
            temp_df = temp_df[temp_df['Department'] == Department]
            Skill_unique = ['Select'] + temp_df['Skill'].unique().tolist()

            with col1:
                Skill = st.selectbox('Select a Skill', Skill_unique)

                start_date = st.date_input('Enter the start date', min_value=dateMin)

                fromTime = st.time_input('Enter the Shift Start time', value=datetime.strptime('09:00', '%H:%M'))

                toTime = st.time_input('Enter the Shift End time', value=datetime.strptime('17:00', '%H:%M'))

            # Collecting user data
            user_data = {
                'Organization': org,
                'Location': Location,
                'Department': Department,
                'Skill': Skill,
                'date': start_date,
                'fromTime': fromTime,
                'toTime': toTime
            }
            with col1:
                submit = st.button('Submit')
                if submit:
                    try:
                        model_prediction = model_prediction_all(user_data,5)
                        with col1:
                            st.success(f'The Predicted BillRate for given input is $ {round(model_prediction[1], 2)}')
                            st.warning(f'The result model was trained on a dataset with {model_prediction[2]} entries. '
                                    f'Tested with {model_prediction[3]} entries, got error around {round(model_prediction[0], 2)} ')
                            st.warning(f'So the prediction may vary by $ {round(model_prediction[0], 2)}')
                    except Exception as e:
                        err = str(e)
                        if 'Select' in err:
                            st.warning('Please fill in all the values and try again', icon="⚠️")
                        else:
                            st.error(f"An error occurred: {e}")
