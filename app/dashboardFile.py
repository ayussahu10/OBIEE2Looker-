import vertexai
from vertexai.language_models import TextGenerationModel
from github import Github
import streamlit as st
import re
import bs4
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from lxml import etree

#model
vertexai.init(project="us-gcp-ame-con-177cf-sbx-1", location="us-central1")

parameters = {

    "temperature": 0.1,

    "max_output_tokens": 1024,

    "top_p": 0.9,

    "top_k": 30

}

model = TextGenerationModel.from_pretrained("text-bison@001")

#DASHBOARD FILE
def generate_dashboard_file(Bs_data,r,c,w,h):

    #title
    title = Bs_data.find_all('cvCell')
    title

    #model
    #model
    mod = Bs_data.find_all('criteria')
    modstring = ""
    for x in mod:
        modstring+= str(x)
    type(modstring)
    parser = etree.XMLParser(recover=True)
    modl = etree.fromstring(modstring, parser=parser)
    modl = modl.get('subjectArea')
    modl

    #type
    typxml = Bs_data.find_all('saw:display')
    chartType = []
    for x in typxml:
        chartType.append(x.get('type'))

    #fields
    dim = Bs_data.find_all('columnFormula')
    fields = []
    for i in dim:
        fields.append(i.text.replace('"',''))

    prompt3 = "create a file in the format mentioned below,also remove double qoutes in the generated file"

    dashformat = "- dashboard: test_dashboard" + "\n  title: test_dashboard" + "\n  layout: newspaper" + "\n  preferred_viewer: dashboards-next" + "\n  elements:" + "\n"
    dashboard_output = ""

    chartformat = ""
    for i in chartType:
        if i == 'bar':
            chartformat = "\n- title: " + title[0].text +"\n  name: test_dashboard" +"\n  model: " + modl +"\n  explore: " + "\n  type : looker_bar" + "\n  fields: [" + ', '.join(str(x) for x in fields)+"]"  + "\n  sorts: []" +"\n  limit: 500" +"\n  x_axis_gridlines: false" +"\n  y_axis_gridlines: true" +"\n  show_view_names: false" +"\n  show_y_axis_labels: true" +"\n  show_y_axis_ticks: true" +"\n  y_axis_tick_density: default " +"\n  y_axis_tick_density_custom: 5" +"\n  show_x_axis_label: true" +"\n  show_x_axis_ticks: true" +"\n  y_axis_scale_mode: linear" +"\n  x_axis_reversed: false" +"\n  y_axis_reversed: false" +"\n  plot_size_by_field: false" +"\n  trellis: '' " +"\n  stacking: '' " + "\n  limit_displayed_rows: false"+"\n  legend_position: center" +"\n  point_style: none" +"\n  show_value_labels: false" +"\n  label_density: 25" +"\n  x_axis_scale: auto" +"\n  y_axis_combined: true" +"\n  ordering: none" +"\n  show_null_labels: false" +"\n  show_totals_labels: false" +"\n  show_silhouette: false" +'\n  totals_color: "#808080" ' +"\n  defaults_version: 1" +"\n  series_types: {}" +"\n  listen: {}" +"\n  row: "+ str(r) +"\n  col: "+ str(c) + "\n  width: " + str(w) +"\n  height: " + str(h)
        elif i == 'pie':
            chartformat = "\n- title: " + title[0].text +"\n  name: test_dashboard" +"\n  model: " + modl +"\n  explore: " + "\n  type: looker_pie"  + "\n  fields: [" + ', '.join(str(x) for x in fields)+"]"  + "\n  sorts: []" +"\n  limit: 500"+"\n  value_labels: legend"+"\n  label_type: labPer" +"\n  x_axis_gridlines: false" +"\n  y_axis_gridlines: true" +"\n  show_view_names: false" +"\n  show_y_axis_labels: true" +"\n  show_y_axis_ticks: true" +"\n  y_axis_tick_density: default " +"\n  y_axis_tick_density_custom: 5" +"\n  show_x_axis_label: true" +"\n  show_x_axis_ticks: true" +"\n  y_axis_scale_mode: linear" +"\n  x_axis_reversed: false" +"\n  y_axis_reversed: false" +"\n  plot_size_by_field: false" +"\n  trellis: '' " +"\n  stacking: '' " + "\n  limit_displayed_rows: false"+"\n  legend_position: center" +"\n  point_style: none" +"\n  show_value_labels: false" +"\n  label_density: 25" +"\n  x_axis_scale: auto" +"\n  y_axis_combined: true" +"\n  ordering: none" +"\n  show_null_labels: false" +"\n  show_totals_labels: false" +"\n  show_silhouette: false" +'\n  totals_color: "#808080" ' +"\n  defaults_version: 1" +"\n  series_types: {}" +"\n  listen: {}" +"\n  row: "+ str(r) +"\n  col: "+ str(c) + "\n  width: " + str(w) +"\n  height: " + str(h)
    
    response = model.predict(prompt3 + chartformat +
"""
Do not generate any other content that is not in YAML format.
Please follow the format of the charttype.
- dashboard: ob_to_l_1gai
  title: OB_to_L_1GAI
  layout: newspaper
  preferred_viewer: dashboards-next
  description: ''
  preferred_slug: NhlJkowj9GUObT8Xu3NObh
  elements:
  - title: Bar_Chart
    name: Bar Chart
    model: OB_TO_L_1GAI
    explore: od_monthly_bookings_agg_1GAI
    type : looker_bar
    fields: [OD_GDS_1GAI.GDS_Code, od_monthly_bookings_agg_1GAI.Passenger_Count_M]
    filters: {}
    sorts: [od_monthly_bookings_agg_1GAI.Passenger_Count_M desc 0]
    limit: 500
    column_limit: 50
    x_axis_gridlines: false
    y_axis_gridlines: true
    show_view_names: false
    show_y_axis_labels: true
    show_y_axis_ticks: true
    y_axis_tick_density: default 
    y_axis_tick_density_custom: 5
    show_x_axis_label: true
    show_x_axis_ticks: true
    y_axis_scale_mode: linear
    x_axis_reversed: false
    y_axis_reversed: false
    plot_size_by_field: false
    trellis: '' 
    stacking: '' 
    limit_displayed_rows: false
    legend_position: center
    point_style: none
    show_value_labels: false
    label_density: 25
    x_axis_scale: auto
    y_axis_combined: true
    ordering: none
    show_null_labels: false
    show_totals_labels: false
    show_silhouette: false
    totals_color: "#808080" 
    show_sql_query_menu_options: false
    show_totals: true
    show_row_totals: true
    show_row_numbers: true
    transpose: false
    truncate_text: true
    truncate_header: false
    size_to_fit: true
    minimum_column_width: 75
    series_cell_visualizations:
      od_monthly_bookings_agg_1GAI.Passenger_Count_M:
        is_active: false
    table_theme: white
    enable_conditional_formatting: false
    header_font_size: '12'
    rows_font_size: '12'
    conditional_formatting_include_totals: false
    conditional_formatting_include_nulls: false
    hide_totals: false
    hide_row_totals: false
    defaults_version: 1
    listen: 
      Departure Date key: od_monthly_bookings_agg_1GAI.Departure_Date_key
    row: 0
    col: 0
    width: 8
    height: 6
  - title: Pie chart
    name: Pie chart
    model: OB_TO_L_1GAI
    explore: od_monthly_bookings_agg_1GAI
    type: looker_pie
    fields: [OD_GDS_1GAI.GDS_Code, od_monthly_bookings_agg_1GAI.Passenger_Count_M]
    sorts: [od_monthly_bookings_agg_1GAI.Passenger_Count_M desc 0]
    limit: 500
    column_limit: 50
    value_labels: legend
    label_type: labPer
    defaults_version: 1      
    listen: 
      Departure Date Key: od_monthly_bookings_agg_1GAI.Departure_Date_key
    row: 0
    col: 8
    width: 8
    height: 6
  filters:
  - name: Departure Date key
    title: Departure Date key
    type: field_filter
    default_value: 1 months 
    allow_multiple_values: true
    required: false
    ui_config:
      type: advanced 
      display: popover
    model: OB_TO_L_1GAI
    explore: od_monthly_bookings_agg_1GAI
    listens_to_filters: []
    field: od_monthly_bookings_agg_1GAI.Departure_Date_key
Also show how the generated file will look.
"""
    ,**parameters
    )

    # Storing the model output in a variable
    dashboard_output += dashformat + response.text
    
    #Print result
    st.text(dashboard_output)

    #save the file in the local device
    with st.chat_message("user"):
        st.write("Files saved in local device 💾")
  

