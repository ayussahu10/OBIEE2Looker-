import vertexai
from vertexai.language_models import TextGenerationModel
from github import Github
import streamlit as st
import re
from io import BytesIO

#model
vertexai.init(project="us-gcp-ame-con-177cf-sbx-1", location="us-central1")

parameters = {

    "temperature": 0.2,

    "max_output_tokens": 1024,

    "top_p": 0.8,

    "top_k": 40

}

model = TextGenerationModel.from_pretrained("text-bison@001")

def generate_view_file(df):
    
    #Get unique View Files names
    filename = df['View Name'].unique()

    #prompt
    prompt1 = "create a file in the format mentioned below from the the csv data given below, also remove double qoutes in the generated file"+ df.to_string()
    
    #feeding prompt to the model
    response1 = model.predict(prompt1 + 
"""
In the format.
        
view: <<View Name>>  { 
  sql_table_name: `<<Physical Schema>>.<<Physical Table>>` ;;

  dimension: <<Physical Column alias>> { 
    type: <<type>>
    primary_key: <<primary_key>>
    sql: ${TABLE}.<<Physical Column>> ;;
    hidden: hidden
  }

The resultant file should follow this format.
view: OD_GDS  {
  sql_table_name: `MIDT_CONSUMPTION.GDS_DIM` ;;

  dimension: GDS_ID {
    type: string
    primary_key: yes
    sql: ${TABLE}.GDS_ID ;;
    hidden: yes
  }

  dimension: GDS_TYPE_CODE {
    type: string
    primary_key: no
    sql: ${TABLE}.GDS_TYPE_CODE ;;
    hidden: no
  }

  dimension: GDS_Name {
    type: string
    primary_key: no
    sql: ${TABLE}.GDS_NAME ;;
    hidden: no
  }

  dimension: GDS_Code {
    type: string
    primary_key: no
    sql: ${TABLE}.GDS_CODE ;;
    hidden: no
  }
}

view: od_monthly_bookings_agg  {
  sql_table_name: `MIDT_CONSUMPTION.OD_MONTHLY_BOOKINGS_AGG` ;;

  dimension: GDS_ID {
    type: string
    primary_key: yes
    sql: ${TABLE}.GDS_ID ;;
    hidden: no
  }

  dimension: Departure_Date_key {
    type: date
    primary_key: no
    sql: cast(${TABLE}.DEPARTURE_DATE as) ;;
    hidden: no
  }

  dimension: Passenger_Count {
    type: number
    primary_key: no
    sql: ${TABLE}.PASSENGER_COUNT ;;
    hidden: no
  }

  measure: Passenger_Count_M {
    type: sum
    sql: ${Passenger_Count} ;;
  }
  
}

view: OD_Market  {
  sql_table_name: `MIDT_CONSUMPTION.CLIENT_AIRPORT_PAIR_DIM` ;;

  dimension: AIRPP_ID {
    type: string
    primary_key: yes
    sql: ${TABLE}.AIRPP_ID ;;
    hidden: no
  }

  dimension: CLIENT_ID {
    type: string
    primary_key: no
    sql: ${TABLE}.CLIENT_ID ;;
    hidden: no
  }

  dimension: Origin_Airport_Code {
    type: string
    primary_key: no
    sql: ${TABLE}.AIRPP_DEPART_AIRP_CODE ;;
    hidden: no
  }

  dimension: Origin_City_Code {
    type: string
    primary_key: no
    sql: ${TABLE}.CTY_DEP_CITY_CODE ;;
    hidden: no
  }

  dimension: Origin_Country_Code {
    type: string
    primary_key: no
    sql: ${TABLE}.CO_DEP_CNTRY_CODE ;;
    hidden: no
  }

  dimension: Origin_Region_Code {
    type: string
    primary_key: no
    sql: ${TABLE}.WA_DEP_WA_CODE ;;
    hidden: no
  }
}

Also show how the generated file will look.
Show how the result file will look, DO NOT WRITE CODE
""",
        **parameters
    )
    # Storing the model output in a variable
    output = response1.text
    
    #preview of view file
    st.text(output)

    #save the file in the local device
    with st.chat_message("user"):
        st.write("Files saved in local device 💾")

    # #get the occurence of new view 
    # v_ind = [m.start() for m in re.finditer('view:', output)]

    # #save the file in the local device
    # for i in range(0,len(filename)):
    #     def commit_and_push_to_github(repo_path, file_path, commit_message, github_token):
    #         try:
    #             g = Github(github_token)
    #             repo = g.get_repo(repo_path)
                
    #             if i+1 < len(filename):
    #                 with open(file_path, 'a'):
    #                     start = v_ind[i]
    #                     end = v_ind[i+1]
    #                     content = output[start:end]
    #             else:
    #                 with open(file_path, 'a'):
    #                     start = v_ind[i]
    #                     content = output[start:]
                

    #             #Saving the content in file
    #             buffer = BytesIO()

    #             # Save the content to the buffer as bytes
    #             buffer.write(content.encode())

    #             # Seek to the beginning of the buffer
    #             buffer.seek(0)

    #             # Specify the file's name 
    #             filename = filename[i] + ".view.lkml"
    #             mime_type = "text/plain"

    #             # Trigger the file download
    #             st.download_button(
    #                 label="Click here to download", 
    #                 data=buffer, 
    #                 file_name=filename, 
    #                 mime=mime_type) 

    #         except Exception:
    #             st.text("Sorry an error has occurred.Make sure the file is not already present in your repository.")




 # #write in file and upload in github 
    # for i in range(0,len(filename)):
    #     def commit_and_push_to_github(repo_path, file_path, commit_message, github_token):
    #         try:
    #             g = Github(github_token)
    #             repo = g.get_repo(repo_path)
                
    #             if i+1 < len(filename):
    #                 with open(file_path, 'a'):
    #                     start = v_ind[i]
    #                     end = v_ind[i+1]
    #                     content = output[start:end]
    #             else:
    #                 with open(file_path, 'a'):
    #                     start = v_ind[i]
    #                     content = output[start:]

    #             #create and save file in github
    #             repo.create_file(file_path, commit_message, content, branch="main")    
    #             return True
    #         except Exception:
    #             st.text("Sorry an error has occurred.Make sure the file is not already present in your repository.")

    #     # Replace these values with your actual file path, content, and repository path
    #     file_path = filename[i] +'.view.lkml'
    #     commit_message = 'Added a new file to the repository.'
    #     repo_path = 'ayussahu10/OBIEE2Looker-'
    #     github_token = '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'

    #     commit_and_push_to_github(repo_path, file_path, commit_message, github_token) == True