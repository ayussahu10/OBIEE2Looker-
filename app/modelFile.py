import vertexai
from vertexai.language_models import TextGenerationModel
from github import Github
import streamlit as st
import re

#model
vertexai.init(project="us-gcp-ame-con-177cf-sbx-1", location="us-central1")

parameters = {

    "temperature": 0.2,

    "max_output_tokens": 1024,

    "top_p": 0.8,

    "top_k": 40

}

model = TextGenerationModel.from_pretrained("text-bison@001")

#FOR MODEL FILE
def generate_model_file(df):

    #prompt
    prompt2 = "create a file in the format mentioned below from the the csv data given below, also remove double qoutes in the generated file"+ df.to_string()
    
    #feeding prompt to the model
    response2 = model.predict(prompt2 +
"""
In the format.Include the first four lines only once in the file.

connection: "<<connection>>"
include: "/Views/**/*.view"

explore: OD_Monthly_Bookings {
from: <<table1>>
                    
  join: <<table2>> {
   type: <<type>>
   sql_on: ${ <<sql_on>> }  ;;
   sql_where: ${ <<sql_where>> }  ;;
   relationship: <<relationship>>
  }
}
The file should follow this format.
connection:"midt_prod_connect"
include: "/Views/**/*.view"

explore: od_monthly_bookings_agg{
from: od_monthly_bookings_agg

  join: OD_GDS{
   type: left_outer
   sql_on: ${OD_Monthly_Bookings.GDS_ID}=${OD_GDS.GDS_ID} ;;
   sql_where: ${OD_GDS.GDS_TYPE_CODE}='00' ;;
   relationship: many_to_one
 }

  join: OD_Market{
   type: left_outer
   sql_on: ${OD_Monthly_Bookings.Airport_Pair_Dir}=${OD_Market.AIRPP_ID} ;;
   sql_where: ${OD_Market.CLIENT_ID}=2 ;;
   relationship: many_to_one
 }
}
Also show how the generated file will look.
""",
    **parameters
)
    # Storing the model output in a variable
    model_output = response2.text

    #Preview of model file
    st.text(model_output) 

    #save the file in the local device
    with st.chat_message("user"):
        st.write("Files saved in local device 💾")
















    # #write in file and upload in github 
    # def commit_and_push_to_github(repo_path, file_path, commit_message, github_token):
    #     try:
    #         g = Github(github_token)
    #         repo = g.get_repo(repo_path)
                
    #         with open(file_path, 'a'):
    #             content = model_output

    #             repo.create_file(file_path, commit_message, content, branch="main")
    #             print("File uploaded to GitHub successfully!")

    #             repo.create_file(file_path, commit_message, content, branch="main")
                
    #             st.text("File uploaded to GitHub successfully!")
    #     except Exception:
    #         st.text("Sorry an error has occurred")

    # #Get filename from user   
    # filename = st.text_input(label= "Enter filename", value="")

    # # Replace these values with your actual file path, content, and repository path
    # file_path = filename +'.dashboard.lkml'
    # commit_message = 'Added a new file to the repository.'
    # repo_path = 'ayussahu10/OBIEE2Looker-' 
    # github_token = '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'

    # #Button to upload file in github
    # if st.button("Upload in Github"):
    #     commit_and_push_to_github(repo_path, file_path, commit_message, github_token)
    # else:
    #     st.text("Please check if the file is not already uploaded")
    