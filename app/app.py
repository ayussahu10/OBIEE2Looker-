# app.py
import streamlit as st
import pandas as pd
import pandas as pd
import viewFile, modelFile, dashboardFile
import bs4
from bs4 import BeautifulSoup


# Custom CSS styling for the app
with open('style.css') as f:
    st.markdown(f.read(), unsafe_allow_html=True)

def read_csv(uploaded_file):
    # Read the file based on its type
    if uploaded_file is not None:
        if uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
    else:
        st.error("No file detected.Please upload a CSV files")
        df = None
    return df

def process_xml(file):
    # Read the content of the file and convert it into a file-like object
    if file is not None:
        soup = BeautifulSoup(file, "xml")
    else:
        st.error("No files detected. Please upload XML files")
        soup = None
    return soup

def main():
    #Add icon to the page
    icon_image = "deloitte_logo.png"  
    
    # Display the icon image
    st.image(icon_image, use_column_width=False,width=80)
    st.title("BI Modernisation")
    st.write("Choose from the dropdown menu below.")
    
    option1 = st.selectbox("Select option 1:", ["OBIEE", "Option B", "Option C"])
    option2 = st.selectbox("Select option 2:", ["LookerML", "Option Y", "Option Z"])
    
    if option1 == "OBIEE" and option2 == "LookerML":
        # File upload button
        but1 ,but2 = st.columns(2)
        csv_file = but1.file_uploader("Choose a CSV file",type="csv",accept_multiple_files=False)
        xml_files = but2.file_uploader("Choose all the XML Files", type="xml",accept_multiple_files=True)

        if csv_file is not None:
            st.subheader("Uploaded File Details")
            st.write(f"File Name: {csv_file.name}")
            df = read_csv(csv_file)
            
        # Generate output button (same as before)
        col1, col2 ,col3 = st.columns(3)
        #VIEW FILE
        if col1.button("Generate View File"):
            if csv_file.type == "text/csv":
                viewFile.generate_view_file(df)
            else:
                st.text("Make sure you have uploaded the right file.")
            
                
        #MODEL FILE
        if col2.button("Generate Model File"):
            if csv_file.type == "text/csv":
                modelFile.generate_model_file(df)
            else:
                st.text("Make sure you have uploaded the right file.")

            model_filename = st.input("Enter filename")
            st.download_button(
            label="Download RCA Analysis",
            data=st.session_state["download_status"],
            file_name= model_filename + '.csv',
            mime='text/csv',
            )
                
        #DASHBOARD FILE        
        if col3.button("Generate Dashboard File"):
            if xml_files is not None:
                st.write(f"Uploaded {len(xml_files)} XML file(s):")
                index = 0
                total_files = len(xml_files)
                r = 0
                c = 0
                w = 8
                h = 6

                while index < total_files:
                    file_content = xml_files[index].read()
                    data = process_xml(file_content)
                    
                    # Generate the dashboard file
                    dashboardFile.generate_dashboard_file(data, r, c, w, h)
                    c += w
                    if c >= 24:
                        r += h
                        c = 0

                    index += 1
            else:
                st.text("Make sure you have uploaded the right files.")   
    
   
if __name__ == "__main__":
    main()