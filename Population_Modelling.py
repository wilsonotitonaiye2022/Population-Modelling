import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import base64

from PDFCreator import create_pdf_report



st.set_page_config(layout="wide")

colour_list = ['blue', 'orange', 'green', 'red', 'purple']
condition_list = ['Healthy', 'Single', 'Multi', 'Frail', 'Deaths']
condition_list_without_death = condition_list[:-1]

def get_binary_file_downloader_html(bin_file, file_label='File'):
            with open(bin_file, 'rb') as f:
                data = f.read()
            bin_str = base64.b64encode(data).decode()
            href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{bin_file}">Download {file_label}</a>'
            return href

st.markdown("<h1 style='text-align: center; color: blue;'>Population Modelling (Incidence/Prevalence)</h1>", unsafe_allow_html=True)

with st.expander('**Flow Diagram**'):
    st.image('Images/flow_diagram.png',
            caption='Population Modelling Flow Diagram',
            use_column_width=True)

with st.sidebar:
    st.subheader(':scroll: About App')
    st.write("""
             
             The population modelling app allows you to simulate the population dynamics of a given population 
             over a specified period of time. 
             
             The app allows you to specify the initial population size for each age group and health condition, 
             as well as the transition probabilities between health conditions.
             
             The app also allows you to specify the net migration rates between age groups. 
             
             The app will then simulate the population dynamics over the specified period of time and provide 
             you with the results in the form of tables and plots.
             
             """)


with st.form("my_form"):
    st.header('Enter Input Parameters')   
    with st.expander("**Click to expand**"):
        st.subheader('Select population size for each Age Group:')
        st.write('**0 to 4 years**')
        col0, col1, col2,col3, col4 = st.columns(5)
        with col0:   
            healthy_size_0to4 = st.number_input('Healthy', key = 0, min_value=0, max_value=1000000, value=15024)
        with col1:
            single_condition_size_0to4 = st.number_input('Single Condition', key = 1, min_value=0, max_value=100000, value=0)
        with col2:   
            multiple_condition_size_0to4 = st.number_input('Multiple Condition', key = 2, min_value=0, max_value=100000, value=0)
        with col3:
            frail_condition_size_0to4 = st.number_input('Frail Condition', key = 3, min_value=0, max_value=100000, value=0)
        with col4:
            death_size_0to4 = st.number_input('Death', key = 4, min_value=0, max_value=100000, value=0)

        st.write('**5 to 9 years**')
        col5, col6, col7,col8, col9 = st.columns(5)
        with col5:   
            healthy_size_5to9 = st.number_input('Healthy', key = 5, min_value=0,  max_value=1000000, value=18162)
        with col6:
            single_condition_size_5to9 = st.number_input('Single Condition', key = 6, min_value=0, max_value=100000, value=0)
        with col7:   
            multiple_condition_size_5to9 = st.number_input('Multiple Condition', key = 7, min_value=0, max_value=100000, value=0)
        with col8:
            frail_condition_size_5to9 = st.number_input('Frail Condition', key = 8, min_value=0,  max_value=100000, value=0)
        with col9:
            death_size_5to9 = st.number_input('Death', key = 9, min_value=0, max_value=100000,  value=0)

        st.write('**10 to 14 years**')
        col10, col11, col12,col13, col14 = st.columns(5)
        with col10:   
            healthy_size_10to14 = st.number_input('Healthy', key = 10, min_value=0, max_value=1000000, value=20341)
        with col11:
            single_condition_size_10to14 = st.number_input('Single Condition', key = 11, min_value=0, max_value=100000, value=0)
        with col12:
            multiple_condition_size_10to14 = st.number_input('Multiple Condition', key = 12, min_value=0, max_value=100000, value=0)
        with col13:
            frail_condition_size_10to14 = st.number_input('Frail Condition', key = 13, min_value=0, max_value=100000, value=0)
        with col14:
            death_size_10to14 = st.number_input('Death', key = 14, min_value=0, max_value=100000,  value=0)

        st.write('**15 to 19 years**')
        col15, col16, col17,col18, col19 = st.columns(5)
        with col15:   
            healthy_size_15to19 = st.number_input('Healthy', min_value=0, key = 15, max_value=1000000, value=19141)
        with col16:
            single_condition_size_15to19 = st.number_input('Single Condition', key = 16, min_value=0, max_value=100000, value=0)
        with col17:
            multiple_condition_size_15to19 = st.number_input('Multiple Condition', key = 17, min_value=0, max_value=100000, value=0)
        with col18:
            frail_condition_size_15to19 = st.number_input('Frail Condition', key = 18, min_value=0, max_value=100000, value=0)
        with col19:
            death_size_15to19 = st.number_input('Death', key = 19, min_value=0, max_value=100000,  value=0)

        st.write('**20 to 24 years**')
        col20, col21, col22,col23, col24 = st.columns(5)
        with col20:   
            healthy_size_20to24 = st.number_input('Healthy', key = 20, min_value=0, max_value=1000000, value=15295)
        with col21:
            single_condition_size_20to24 = st.number_input('Single Condition', key = 21, min_value=0, max_value=100000, value=0)
        with col22:
            multiple_condition_size_20to24 = st.number_input('Multiple Condition', key = 22, min_value=0, max_value=100000, value=0)
        with col23:
            frail_condition_size_20to24 = st.number_input('Frail Condition', key = 23, min_value=0, max_value=100000, value=0)
        with col24:
            death_size_20to24 = st.number_input('Death', key = 24, min_value=0, max_value=100000,  value=0)

        st.write('**25 to 29 years**')
        col25, col26, col27,col28, col29 = st.columns(5)
        with col25:   
            healthy_size_25to29 = st.number_input('Healthy', key = 25, min_value=0, max_value=1000000, value=16754)
        with col26:
            single_condition_size_25to29 = st.number_input('Single Condition', key = 26, min_value=0, max_value=100000, value=0)
        with col27:
            multiple_condition_size_25to29 = st.number_input('Multiple Condition', key = 27, min_value=0, max_value=100000, value=0)
        with col28:
            frail_condition_size_25to29 = st.number_input('Frail Condition', key = 28, min_value=0, max_value=100000, value=0)
        with col29:
            death_size_25to29 = st.number_input('Death', key = 29, min_value=0, max_value=100000,  value=0)

        st.write('**30 to 34 years**')
        col30, col31, col32,col33, col34 = st.columns(5)
        with col30:   
            healthy_size_30to34 = st.number_input('Healthy', key = 30, min_value=0, max_value=1000000, value=18330)
        with col31:
            single_condition_size_30to34 = st.number_input('Single Condition', key = 31, min_value=0, max_value=100000, value=0)
        with col32:
            multiple_condition_size_30to34 = st.number_input('Multiple Condition', key = 32, min_value=0, max_value=100000, value=0)
        with col33:
            frail_condition_size_30to34 = st.number_input('Frail Condition', key = 33, min_value=0, max_value=100000, value=0)
        with col34:
            death_size_30to34 = st.number_input('Death', key = 34, min_value=0, max_value=100000,  value=0)

        st.write('**35 to 39 years**')
        col35, col36, col37,col38, col39 = st.columns(5)
        with col35:   
            healthy_size_35to39 = st.number_input('Healthy', key = 35, min_value=0, max_value=1000000, value=18325)
        with col36:
            single_condition_size_35to39 = st.number_input('Single Condition', key = 36, min_value=0, max_value=100000, value=0)
        with col37:
            multiple_condition_size_35to39 = st.number_input('Multiple Condition', key = 37, min_value=0, max_value=100000, value=0)
        with col38:
            frail_condition_size_35to39 = st.number_input('Frail Condition', key = 38, min_value=0, max_value=100000, value=0)
        with col39:
            death_size_35to39 = st.number_input('Death', key = 39, min_value=0, max_value=100000,  value=0)

        st.write('**40 to 44 years**')
        col40, col41, col42,col43, col44 = st.columns(5)
        with col40:   
            healthy_size_40to44 = st.number_input('Healthy', key = 40, min_value=0, max_value=1000000, value=18791)
        with col41:
            single_condition_size_40to44 = st.number_input('Single Condition', key = 41, min_value=0, max_value=100000, value=0)
        with col42:
            multiple_condition_size_40to44 = st.number_input('Multiple Condition', key = 42, min_value=0, max_value=100000, value=0)
        with col43:
            frail_condition_size_40to44 = st.number_input('Frail Condition', key = 43, min_value=0, max_value=100000, value=0)
        with col44:
            death_size_40to44 = st.number_input('Death', key = 44, min_value=0, max_value=100000,  value=0)

        st.write('**45 to 49 years**')
        col45, col46, col47,col48, col49 = st.columns(5)
        with col45:   
            healthy_size_45to49 = st.number_input('Healthy', key = 45, min_value=0, max_value=1000000, value=21659)
        with col46:
            single_condition_size_45to49 = st.number_input('Single Condition', key = 46, min_value=0, max_value=100000, value=0)
        with col47:
            multiple_condition_size_45to49 = st.number_input('Multiple Condition', key = 47, min_value=0, max_value=100000, value=0)
        with col48:
            frail_condition_size_45to49 = st.number_input('Frail Condition', key = 48, min_value=0, max_value=100000, value=0)
        with col49:
            death_size_45to49 = st.number_input('Death', key = 49, min_value=0, max_value=100000,  value=0)

        st.write('**50 to 54 years**')
        col50, col51, col52,col53, col54 = st.columns(5)
        with col50:   
            healthy_size_50to54 = st.number_input('Healthy', key = 50, min_value=0, max_value=1000000, value=26915)
        with col51:
            single_condition_size_50to54 = st.number_input('Single Condition', key = 51, min_value=0, max_value=100000, value=0)
        with col52:
            multiple_condition_size_50to54 = st.number_input('Multiple Condition', key = 52, min_value=0, max_value=100000, value=0)
        with col53:
            frail_condition_size_50to54 = st.number_input('Frail Condition', key = 53, min_value=0, max_value=100000, value=0)
        with col54:
            death_size_50to54 = st.number_input('Death', key = 54, min_value=0, max_value=100000,  value=0)

        st.write('**55 to 59 years**')
        col55, col56, col57,col58, col59 = st.columns(5)
        with col55:   
            healthy_size_55to59 = st.number_input('Healthy', key = 55, min_value=0, max_value=1000000, value=29764)
        with col56:
            single_condition_size_55to59 = st.number_input('Single Condition', key = 56, min_value=0, max_value=100000, value=0)
        with col57:
            multiple_condition_size_55to59 = st.number_input('Multiple Condition', key = 57, min_value=0, max_value=100000, value=0)
        with col58:
            frail_condition_size_55to59 = st.number_input('Frail Condition', key = 58, min_value=0, max_value=100000, value=0)
        with col59:
            death_size_55to59 = st.number_input('Death', key = 59, min_value=0, max_value=100000,  value=0)

        st.write('**60 to 64 years**')
        col60, col61, col62,col63, col64 = st.columns(5)
        with col60:   
            healthy_size_60to64 = st.number_input('Healthy', key = 60, min_value=0, max_value=1000000, value=28803)
        with col61:
            single_condition_size_60to64 = st.number_input('Single Condition', key = 61, min_value=0, max_value=100000, value=0)
        with col62:
            multiple_condition_size_60to64 = st.number_input('Multiple Condition', key = 62, min_value=0, max_value=100000, value=0)
        with col63:
            frail_condition_size_60to64 = st.number_input('Frail Condition', key = 63, min_value=0, max_value=100000, value=0)
        with col64:
            death_size_60to64 = st.number_input('Death', key = 64, min_value=0, max_value=100000,  value=0)

        st.write('**65 to 69 years**')
        col65, col66, col67,col68, col69 = st.columns(5)
        with col65:   
            healthy_size_65to69 = st.number_input('Healthy', key = 65, min_value=0, max_value=1000000, value=27017)
        with col66:
            single_condition_size_65to69 = st.number_input('Single Condition', key = 66, min_value=0, max_value=100000, value=0)
        with col67:
            multiple_condition_size_65to69 = st.number_input('Multiple Condition', key = 67, min_value=0, max_value=100000, value=0)
        with col68:
            frail_condition_size_65to69 = st.number_input('Frail Condition', key = 68, min_value=0, max_value=100000, value=0)
        with col69:
            death_size_65to69 = st.number_input('Death', key = 69, min_value=0, max_value=100000,  value=0)

        st.write('**70 to 74 years**')
        col70, col71, col72,col73, col74 = st.columns(5)
        with col70:   
            healthy_size_70to74 = st.number_input('Healthy', key = 70, min_value=0, max_value=1000000, value=30418)
        with col71:
            single_condition_size_70to74 = st.number_input('Single Condition', key = 71, min_value=0, max_value=100000, value=0)
        with col72:
            multiple_condition_size_70to74 = st.number_input('Multiple Condition', key = 72, min_value=0, max_value=100000, value=0)
        with col73:
            frail_condition_size_70to74 = st.number_input('Frail Condition', key = 73, min_value=0, max_value=100000, value=0)
        with col74:
            death_size_70to74 = st.number_input('Death', key = 74, min_value=0, max_value=100000,  value=0)

        st.write('**75 to 79 years**')
        col75, col76, col77,col78, col79 = st.columns(5)
        with col75:   
            healthy_size_75to79 = st.number_input('Healthy', key = 75, min_value=0, max_value=1000000, value=22892)
        with col76:
            single_condition_size_75to79 = st.number_input('Single Condition', key = 76, min_value=0, max_value=100000, value=0)
        with col77:
            multiple_condition_size_75to79 = st.number_input('Multiple Condition', key = 77, min_value=0, max_value=100000, value=0)
        with col78:
            frail_condition_size_75to79 = st.number_input('Frail Condition', key = 78, min_value=0, max_value=100000, value=0)
        with col79:
            death_size_75to79 = st.number_input('Death', key = 79, min_value=0, max_value=100000,  value=0)

        st.write('**80 to 84 years**')
        col80, col81, col82,col83, col84 = st.columns(5)
        with col80:   
            healthy_size_80to84 = st.number_input('Healthy', key = 80, min_value=0, max_value=1000000, value=15737)
        with col81:
            single_condition_size_80to84 = st.number_input('Single Condition', key = 81, min_value=0, max_value=100000, value=0)
        with col82:
            multiple_condition_size_80to84 = st.number_input('Multiple Condition', key = 82, min_value=0, max_value=100000, value=0)
        with col83:
            frail_condition_size_80to84 = st.number_input('Frail Condition', key = 83, min_value=0, max_value=100000, value=0)
        with col84:
            death_size_80to84 = st.number_input('Death', key = 84, min_value=0, max_value=100000,  value=0)

        st.write('**85+ years**')
        col85, col86, col87,col88, col89 = st.columns(5)
        with col85:   
            healthy_size_85plus = st.number_input('Healthy', key = 85, min_value=0, max_value=1000000, value=16216)
        with col86:
            single_condition_size_85plus = st.number_input('Single Condition', key = 86, min_value=0, max_value=100000, value=0)
        with col87:
            multiple_condition_size_85plus = st.number_input('Multiple Condition', key = 87, min_value=0, max_value=100000, value=0)
        with col88:
            frail_condition_size_85plus = st.number_input('Frail Condition', key = 88, min_value=0, max_value=100000, value=0)
        with col89:
            death_size_85plus = st.number_input('Death', key = 89, min_value=0, max_value=100000,  value=0)

        st.subheader('Select transition probabilities:')

        col90, col91, col92 = st.columns(3)
        with col90:
            st.write('**Health Condition Probabilities**')
            healthy_to_single = st.slider('Healthy to Single Condition', min_value=0.0, max_value=1.0, value=0.1)
            single_to_multiple = st.slider('Single to Multiple Conditions', min_value=0.0, max_value=1.0, value=0.54)
            multiple_to_frail = st.slider('Multiple Condition to Frail', min_value=0.0, max_value=1.0, value=0.33)
            frail_to_death = st.slider('Frail to Death', min_value=0.0, max_value=1.0, value=0.60)
            single_to_death = st.slider('Single Condition to Death', min_value=0.0, max_value=1.0, value=0.01)
            multiple_to_death = st.slider('Multiple Conditions to Death', min_value=0.0, max_value=1.0, value=0.03)

        with col91:
            st.write('**Net Migration**')
            net_migration_rate_0to4 = st.number_input('0-4', key = 100, min_value=-100000, max_value=100000, value=-2166)
            net_migration_rate_5to9 = st.number_input('5-9', key = 101, min_value=-100000, max_value=100000, value=533)
            net_migration_rate_10to14 = st.number_input('10-14', key = 102, min_value=-100000, max_value=100000, value=-120)
            net_migration_rate_15to19 = st.number_input('15-19', key = 103, min_value=-100000, max_value=100000, value=-2469)
            net_migration_rate_20to24 = st.number_input('20-24', key = 104, min_value=-100000, max_value=100000, value=-2092)
            net_migration_rate_25to29 = st.number_input('25-29', key = 105, min_value=-100000, max_value=100000, value=1545)
            net_migration_rate_30to34 = st.number_input('30-34', key = 106, min_value=-100000, max_value=100000, value=2512)
            net_migration_rate_35to39 = st.number_input('35-39', key = 107, min_value=-100000, max_value=100000, value=-932)
            net_migration_rate_40to44 = st.number_input('40-44', key = 108, min_value=-100000, max_value=100000, value=-5584)
            net_migration_rate_45to49 = st.number_input('45-49', key = 109, min_value=-100000, max_value=100000, value=-5319)
            net_migration_rate_50to54 = st.number_input('50-54', key = 110, min_value=-100000, max_value=100000, value=1521)
            net_migration_rate_55to59 = st.number_input('55-59', key = 111, min_value=-100000, max_value=100000, value=5360)
            net_migration_rate_60to64 = st.number_input('60-64', key = 112, min_value=-100000, max_value=100000, value=-680)
            net_migration_rate_65to69 = st.number_input('65-69', key = 113, min_value=-100000, max_value=100000, value=1864)
            net_migration_rate_70to74 = st.number_input('70-74', key = 114, min_value=-100000, max_value=100000, value=10124)
            net_migration_rate_75to79 = st.number_input('75-79', key = 115, min_value=-100000, max_value=100000, value=5580)
            net_migration_rate_80to84 = st.number_input('80-84', key = 116, min_value=-100000, max_value=100000, value=2107)
            net_migration_rate_85plus = st.number_input('85+', key = 117, min_value=-100000, max_value=100000, value=2647)

        with col92:
            st.write('**Age Group Transition Probabilities**')
            ag0to4_to_5to9 = st.slider('0-4 to 5-9', min_value=0.0, max_value=1.0, value=0.15)
            ag5to9_to_10to14 = st.slider('5-9 to 10-14', min_value=0.0, max_value=1.0, value=0.15)
            ag10to14_to_15to19 = st.slider('10-14 to 15-19', min_value=0.0, max_value=1.0, value=0.15)
            ag15to19_to_20to24 = st.slider('15-19 to 20-24', min_value=0.0, max_value=1.0, value=0.15)
            ag20to24_to_25to29 = st.slider('20-24 to 25-29', min_value=0.0, max_value=1.0, value=0.15)
            ag25to29_to_30to34 = st.slider('25-29 to 30-34', min_value=0.0, max_value=1.0, value=0.15)
            ag30to34_to_35to39 = st.slider('30-34 to 35-39', min_value=0.0, max_value=1.0, value=0.15)
            ag35to39_to_40to44 = st.slider('35-39 to 40-44', min_value=0.0, max_value=1.0, value=0.15)
            ag40to44_to_45to49 = st.slider('40-44 to 45-49', min_value=0.0, max_value=1.0, value=0.15)
            ag45to49_to_50to54 = st.slider('45-49 to 50-54', min_value=0.0, max_value=1.0, value=0.15)
            ag50to54_to_55to59 = st.slider('50-54 to 55-59', min_value=0.0, max_value=1.0, value=0.15)
            ag55to59_to_60to64 = st.slider('55-59 to 60-64', min_value=0.0, max_value=1.0, value=0.15)
            ag60to64_to_65to69 = st.slider('60-64 to 65-69', min_value=0.0, max_value=1.0, value=0.15)
            ag65to69_to_70to74 = st.slider('65-69 to 70-74', min_value=0.0, max_value=1.0, value=0.15)
            ag70to74_to_75to79 = st.slider('70-74 to 75-79', min_value=0.0, max_value=1.0, value=0.15)
            ag75to79_to_80to84 = st.slider('75-79 to 80-84', min_value=0.0, max_value=1.0, value=0.15)
            ag80to84_to_85plus = st.slider('80-84 to 85+', min_value=0.0, max_value=1.0, value=0.15)

        col93, col94, col95 = st.columns(3)
        with col93:
            st.write('**Number of years to run simulation**')
            # Define the simulation period
            years = st.number_input('Select the number of years to simulate', key = 200, min_value=1, max_value=100, value=10)

    run_simulation = st.form_submit_button("RUN SIMULATION")

if run_simulation:
    with st.spinner('Running Simulation...'):
        # Define the initial population sizes for each age cohort and health state
        initial_population = {
            '0-4': {'Healthy': healthy_size_0to4, 'Single': single_condition_size_0to4, 'Multi': multiple_condition_size_0to4, 'Frail': frail_condition_size_0to4, 'Deaths': death_size_5to9},
            '5-9': {'Healthy': healthy_size_5to9, 'Single': single_condition_size_5to9, 'Multi': multiple_condition_size_5to9, 'Frail': frail_condition_size_5to9, 'Deaths': death_size_5to9},
            '10-14': {'Healthy': healthy_size_10to14, 'Single': single_condition_size_10to14, 'Multi': multiple_condition_size_10to14, 'Frail': frail_condition_size_10to14, 'Deaths': death_size_10to14},
            '15-19': {'Healthy': healthy_size_15to19, 'Single': single_condition_size_15to19, 'Multi': multiple_condition_size_15to19, 'Frail': frail_condition_size_15to19, 'Deaths': death_size_15to19},
            '20-24': {'Healthy': healthy_size_20to24, 'Single': single_condition_size_20to24, 'Multi': multiple_condition_size_20to24, 'Frail': frail_condition_size_20to24, 'Deaths': death_size_20to24},
            '25-29': {'Healthy': healthy_size_25to29, 'Single': single_condition_size_25to29, 'Multi': multiple_condition_size_25to29, 'Frail': frail_condition_size_25to29, 'Deaths': death_size_25to29},
            '30-34': {'Healthy': healthy_size_30to34, 'Single': single_condition_size_30to34, 'Multi': multiple_condition_size_30to34, 'Frail': frail_condition_size_30to34, 'Deaths': death_size_30to34},
            '35-39': {'Healthy': healthy_size_35to39, 'Single': single_condition_size_35to39, 'Multi': multiple_condition_size_35to39, 'Frail': frail_condition_size_35to39, 'Deaths': death_size_35to39},
            '40-44': {'Healthy': healthy_size_40to44, 'Single': single_condition_size_40to44, 'Multi': multiple_condition_size_40to44, 'Frail': frail_condition_size_40to44, 'Deaths': death_size_40to44},
            '45-49': {'Healthy': healthy_size_45to49, 'Single': single_condition_size_45to49, 'Multi': multiple_condition_size_45to49, 'Frail': frail_condition_size_45to49, 'Deaths': death_size_45to49},
            '50-54': {'Healthy': healthy_size_50to54, 'Single': single_condition_size_50to54, 'Multi': multiple_condition_size_50to54, 'Frail': frail_condition_size_50to54, 'Deaths': death_size_50to54},
            '55-59': {'Healthy': healthy_size_55to59, 'Single': single_condition_size_55to59, 'Multi': multiple_condition_size_55to59, 'Frail': frail_condition_size_55to59, 'Deaths': death_size_55to59},
            '60-64': {'Healthy': healthy_size_60to64, 'Single': single_condition_size_60to64, 'Multi': multiple_condition_size_60to64, 'Frail': frail_condition_size_60to64, 'Deaths': death_size_60to64},
            '65-69': {'Healthy': healthy_size_65to69, 'Single': single_condition_size_65to69, 'Multi': multiple_condition_size_65to69, 'Frail': frail_condition_size_65to69, 'Deaths': death_size_65to69},
            '70-74': {'Healthy': healthy_size_70to74, 'Single': single_condition_size_70to74, 'Multi': multiple_condition_size_70to74, 'Frail': frail_condition_size_70to74, 'Deaths': death_size_70to74},
            '75-79': {'Healthy': healthy_size_75to79, 'Single': single_condition_size_75to79, 'Multi': multiple_condition_size_75to79, 'Frail': frail_condition_size_75to79, 'Deaths': death_size_75to79},
            '80-84': {'Healthy': healthy_size_80to84, 'Single': single_condition_size_80to84, 'Multi': multiple_condition_size_80to84, 'Frail': frail_condition_size_80to84, 'Deaths': death_size_80to84},
            '85+': {'Healthy': healthy_size_85plus, 'Single': single_condition_size_85plus, 'Multi': multiple_condition_size_85plus, 'Frail': frail_condition_size_85plus, 'Deaths': death_size_85plus}
            }
        #convert the initial population dictionary to a dataframe
        initial_population_df = pd.DataFrame(initial_population)
        #st.dataframe(initial_population_df)
        # Define transition probabilities between health states
        transition_probs_health = {
            'Healthy_to_Single':  healthy_to_single,
            'Single_to_Multi': single_to_multiple,
            'Multi_to_Frail': multiple_to_frail,
            'Frail_to_Death': frail_to_death,
            'Single_to_Death': single_to_death,
            'Multi_to_Death': multiple_to_death
        }
        #convert the transition probabilities dictionary to a dataframe 
        transition_probs_health_df = pd.DataFrame(transition_probs_health, index=[0])
        #st.dataframe(transition_probs_health_df)

        # Define transition probabilities between age groups
        transition_probs_age = {'0-4_to_5-9': ag0to4_to_5to9, 
                                '5-9_to_10-14': ag5to9_to_10to14,
                                '10-14_to_15-19': ag10to14_to_15to19,
                                '15-19_to_20-24': ag15to19_to_20to24,
                                '20-24_to_25-29': ag20to24_to_25to29,
                                '25-29_to_30-34': ag25to29_to_30to34,
                                '30-34_to_35-39': ag30to34_to_35to39,
                                '35-39_to_40-44': ag35to39_to_40to44,
                                '40-44_to_45-49': ag40to44_to_45to49,
                                '45-49_to_50-54': ag45to49_to_50to54,
                                '50-54_to_55-59': ag50to54_to_55to59,
                                '55-59_to_60-64': ag55to59_to_60to64,
                                '60-64_to_65-69': ag60to64_to_65to69,
                                '65-69_to_70-74': ag65to69_to_70to74,
                                '70-74_to_75-79': ag70to74_to_75to79,
                                '75-79_to_80-84': ag75to79_to_80to84,
                                '80-84_to_85+': ag80to84_to_85plus
                                }
        #convert the transition probabilities dictionary to a dataframe
        transition_probs_age_df = pd.DataFrame(transition_probs_age, index=[0])
        #st.dataframe(transition_probs_age_df)

        # Define net migration rates for each age group cohort
        net_migration =     {'0-4': net_migration_rate_0to4,
                            '5-9': net_migration_rate_5to9,
                            '10-14': net_migration_rate_10to14,
                            '15-19': net_migration_rate_15to19,
                            '20-24': net_migration_rate_20to24,
                            '25-29': net_migration_rate_25to29,
                            '30-34': net_migration_rate_30to34,
                            '35-39': net_migration_rate_35to39,
                            '40-44': net_migration_rate_40to44,
                            '45-49': net_migration_rate_45to49,
                            '50-54': net_migration_rate_50to54,
                            '55-59': net_migration_rate_55to59,
                            '60-64': net_migration_rate_60to64,
                            '65-69': net_migration_rate_65to69,
                            '70-74': net_migration_rate_70to74,
                            '75-79': net_migration_rate_75to79,
                            '80-84': net_migration_rate_80to84,
                            '85+': net_migration_rate_85plus
                            }
        #convert the net migration dictionary to a dataframe 
        net_migration_df = pd.DataFrame(net_migration, index=[0])
        #st.dataframe(net_migration_df)

        # Initialize the results dictionary
        results = {age_group: {state: [] for state in initial_population['0-4'].keys()} for age_group in initial_population.keys()}
        total_population = {age_group: [] for age_group in initial_population.keys()}

        # Run the simulation over the defined period
        for year in range(years):
            new_population = {age_group: population.copy() for age_group, population in initial_population.items()}
            
            for age_group, population in initial_population.items():
                # Apply net migration
                new_population[age_group]['Healthy'] += net_migration[age_group]
                
                # Health state transitions within the same age group
                for state in condition_list_without_death:
                    if state == 'Healthy':
                        new_population[age_group]['Single'] += population[state] * transition_probs_health['Healthy_to_Single']
                        new_population[age_group][state] -= population[state] * transition_probs_health['Healthy_to_Single']
                    elif state == 'Single':
                        new_population[age_group]['Multi'] += population[state] * transition_probs_health['Single_to_Multi']
                        new_population[age_group][state] -= population[state] * transition_probs_health['Single_to_Multi']
                        new_population[age_group]['Deaths'] += population[state] * transition_probs_health['Single_to_Death']
                        new_population[age_group][state] -= population[state] * transition_probs_health['Single_to_Death']
                    elif state == 'Multi':
                        new_population[age_group]['Frail'] += population[state] * transition_probs_health['Multi_to_Frail']
                        new_population[age_group][state] -= population[state] * transition_probs_health['Multi_to_Frail']
                        new_population[age_group]['Deaths'] += population[state] * transition_probs_health['Multi_to_Death']
                        new_population[age_group][state] -= population[state] * transition_probs_health['Multi_to_Death']
                    elif state == 'Frail':
                        new_population[age_group]['Deaths'] += population[state] * transition_probs_health['Frail_to_Death']
                        new_population[age_group][state] -= population[state] * transition_probs_health['Frail_to_Death']

            # Age group transitions
            age_groups = list(initial_population.keys())
            for i in range(len(age_groups) - 1):
                current_age_group = age_groups[i]
                next_age_group = age_groups[i + 1]
                for state in ['Healthy', 'Single', 'Multi', 'Frail']:
                    new_population[next_age_group][state] += new_population[current_age_group][state] * transition_probs_age[f'{current_age_group}_to_{next_age_group}']
                    new_population[current_age_group][state] -= new_population[current_age_group][state] * transition_probs_age[f'{current_age_group}_to_{next_age_group}']

            # Update the population for the next year
            initial_population = new_population
            
            # Store the results
            for age_group, population in new_population.items():
                for state in population.keys():
                    results[age_group][state].append(population[state])
                total_population[age_group].append(sum(population[state] for state in population.keys() if state != 'Deaths'))

        st.subheader('**Age Group Population Broken Down by Health State Over the Years**')
        # Plot the results
        with st.expander('**Bar Plots**'):
            # Create stacked bar charts for each age cohort
            for age_group in initial_population.keys():
                fig_bar = go.Figure()

                for state, color in zip(condition_list, colour_list):
                    fig_bar.add_trace(go.Bar(
                        x=list(range(1, years + 1)),
                        y=results[age_group][state],
                        name=state,
                        marker_color=color
                    ))

                fig_bar.update_layout(
                    title=f"Population in Each Health State Over {years} Years for Age Group {age_group}",
                    xaxis_title="Years",
                    yaxis_title="Population",
                    barmode='stack'
                )
                st.plotly_chart(fig_bar)

        with st.expander('**Line Plots**'):
            # Create line chart for total population in each age group
            for age_group in initial_population.keys():
                fig_line = go.Figure()

                for state, color in zip(condition_list, colour_list):
                    fig_line.add_trace(go.Scatter(
                        x=list(range(1, years + 1)),
                        y=results[age_group][state],
                        mode='lines',
                        name=state,
                        line=dict(color=color)
                    ))

                fig_line.update_layout(
                    title=f"Population Distribution Over {years} Years for Age Group {age_group}",
                    xaxis_title="Years",
                    yaxis_title="Population"
                )

                st.plotly_chart(fig_line)
        
        # Create stacked bar chart for aggregated total population broken down by different health states over the years
        st.subheader('Aggregated Total Population Broken Down by Health State Over the Years')
        fig_total_bar = go.Figure()

        for state, color in zip(condition_list, colour_list):
            state_population = np.zeros(years)
            for age_group in initial_population.keys():
                state_population += np.array(results[age_group][state])

            fig_total_bar.add_trace(go.Bar(
                x=list(range(1, years + 1)),
                y=state_population,
                name=state,
                marker_color=color
            ))

        fig_total_bar.update_layout(
            title=f"Aggregated Total Population Broken Down by Health State Over {years} Years",
            xaxis_title="Years",
            yaxis_title="Population",
            barmode='stack'
        )

        st.plotly_chart(fig_total_bar)

        # Create line chart for aggregated total population broken down by different health states over the years
        fig_total_line = go.Figure()

        for state, color in zip(condition_list, colour_list):
            state_population = np.zeros(years)
            for age_group in initial_population.keys():
                state_population += np.array(results[age_group][state])

            fig_total_line.add_trace(go.Scatter(
                x=list(range(1, years + 1)),
                y=state_population,
                mode='lines',
                name=state,
                line=dict(color=color)
            ))

        fig_total_line.update_layout(
            title=f"Aggregated Total Population Broken Down by Health State Over {years} Years",
            xaxis_title="Years",
            yaxis_title="Population"
        )

        st.plotly_chart(fig_total_line)

        #convert the results dictionary to a separate dataframe for each age group
        results_0to4_df = pd.DataFrame(results['0-4'])
        results_5to9_df = pd.DataFrame(results['5-9'])
        results_10to14_df = pd.DataFrame(results['10-14'])
        results_15to19_df = pd.DataFrame(results['15-19'])
        results_20to24_df = pd.DataFrame(results['20-24'])
        results_25to29_df = pd.DataFrame(results['25-29'])
        results_30to34_df = pd.DataFrame(results['30-34'])
        results_35to39_df = pd.DataFrame(results['35-39'])
        results_40to44_df = pd.DataFrame(results['40-44'])
        results_45to49_df = pd.DataFrame(results['45-49'])
        results_50to54_df = pd.DataFrame(results['50-54'])
        results_55to59_df = pd.DataFrame(results['55-59'])
        results_60to64_df = pd.DataFrame(results['60-64'])
        results_65to69_df = pd.DataFrame(results['65-69'])
        results_70to74_df = pd.DataFrame(results['70-74'])
        results_75to79_df = pd.DataFrame(results['75-79'])
        results_80to84_df = pd.DataFrame(results['80-84'])
        results_85plus_df = pd.DataFrame(results['85+'])
        #convert the total population dictionary to a dataframe
        total_population_df = pd.DataFrame(total_population)

        #Generate an excel file with the results
        writer = pd.ExcelWriter('result.xlsx', engine='xlsxwriter')
        dataframes = {"results_0to4_df": results_0to4_df, 
                      "results_5to9_df": results_5to9_df,
                      "results_10to14_df": results_10to14_df,
                      "results_15to19_df": results_15to19_df,
                      "results_20to24_df": results_20to24_df,
                      "results_25to29_df": results_25to29_df,
                      "results_30to34_df": results_30to34_df,
                      "results_35to39_df": results_35to39_df,
                      "results_40to44_df": results_40to44_df,
                      "results_45to49_df": results_45to49_df,
                      "results_50to54_df": results_50to54_df,
                      "results_55to59_df": results_55to59_df,
                      "results_60to64_df": results_60to64_df,
                      "results_65to69_df": results_65to69_df,
                      "results_70to74_df": results_70to74_df,
                      "results_75to79_df": results_75to79_df,
                      "results_80to84_df": results_80to84_df,
                      "results_85plus_df": results_85plus_df,
                      "total_population_df": total_population_df
                      }
        for name, frame in dataframes.items():
            frame.to_excel(writer, sheet_name = name, index=False)
        writer.close()

        # Generate PDF report
        dataframes = [initial_population_df, 
                      transition_probs_health_df, 
                      transition_probs_age_df, 
                      net_migration_df]
        plotly_figures = [fig_total_bar, fig_total_line]
        

        dataframes_dict = {name: frame for name, frame in zip(['Initial Population', 
                                                               'Health Transition Probabilities', 
                                                               'Age Transition Probabilities', 
                                                               'Net Migration'], 
                                                               dataframes)}
        create_pdf_report(dataframes_dict, plotly_figures, 'report.pdf')        
        
        
        #Add download button for the excel file and pdf report
        st.markdown(get_binary_file_downloader_html('result.xlsx', 'Output dataframes in Excel'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('report.pdf', 'PDF report with Parameters and Aggregated Total Population Charts'), unsafe_allow_html=True)

        st.success('Simulation completed successfully!')
        
        #Add Reset button
        st.warning('Click the button below to reset the application and start a new simulation.')
        reset = st.button('Reset App')




