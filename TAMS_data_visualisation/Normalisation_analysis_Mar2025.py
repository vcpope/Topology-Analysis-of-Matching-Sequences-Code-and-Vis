import numpy as np
import pandas as pd
import numpy as np
import struct
import os
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
#import seaborn as sns
#sns.set(color_codes=True)

#Data variables to change to point to own data as required:
subdirs = ['PN_Scooby3MIN_SummaryTables', 'PNEd_SummaryTables', 'SP_SummaryTables_Mar2020/']
datatypes = ['Transcript_', 'Transcript_', 'Transcript_']
perfIDs = ['PN', 'PNEd', 'SP']
df_names = ['PN_norm_df', 'PNEd_norm_df', 'SP_norm_df']
table_dir = 'Analysis_Tables/'
normalised_csv_list = []

#Graph variables to change:
graph_alpha = 0.8
graph_marker = 'x'
fntsize = 25
lowy = -0.2
highy = 0.2

def calculate_norm_data(test_data):
    
    col = ["Show_A", "Show_B", 
           "Norm_A_Start", "Norm_B_Start", 
           "Norm_A_End", "Norm_B_End",
       "Norm_A_Dur", "Norm_B_Dur", 
       "Norm_Diff_Start","Norm_Diff_End", "Norm_Diff_Dur"]
    #new_data = pd.DataFrame(columns = col)
    new_data = {}
    show_A_array = []
    show_B_array = []
    norm_A_start_array = []
    norm_B_start_array = []
    norm_A_end_array = []
    norm_B_end_array = []
    norm_A_dur_array = []
    norm_B_dur_array = []
    norm_diff_start_array = []
    norm_diff_end_array = []
    norm_diff_dur_array = []

    for row in test_data.itertuples():

        if row.Index%2 == 0:
            show_A = row.Recording_ID.split('/')[-1]
            norm_A_start = row.Norm_start
            norm_A_end = row.Norm_end
            norm_A_dur = row.Norm_end-row.Norm_start
            
            show_A_array.append(show_A)
            norm_A_start_array.append(norm_A_start)
            norm_A_end_array.append(norm_A_end)
            norm_A_dur_array.append(norm_A_dur)

        elif row.Index%2 != 0:
            show_B = row.Recording_ID.split('/')[-1]
            norm_B_start = row.Norm_start
            norm_B_end = row.Norm_end
            norm_B_dur = row.Norm_end-row.Norm_start

            norm_diff_start = norm_A_start-norm_B_start
            norm_diff_end = norm_A_end-norm_B_end
            norm_diff_dur = norm_A_dur-norm_B_dur
        
            show_B_array.append(show_B)
            norm_B_start_array.append(norm_B_start)
            norm_B_end_array.append(norm_B_end)
            norm_B_dur_array.append(norm_B_dur)
            norm_diff_start_array.append(norm_diff_start)
            norm_diff_end_array.append(norm_diff_end)
            norm_diff_dur_array.append(norm_diff_dur)
            
    new_data = list(zip(show_A_array, show_B_array,
                        norm_A_start_array, norm_B_start_array,
                        norm_A_end_array, norm_B_end_array,
                        norm_A_dur_array, norm_B_dur_array,
                        norm_diff_start_array, norm_diff_end_array,
                        norm_diff_dur_array))
                    
    new_data_df = pd.DataFrame(new_data, columns= col)
    
    return new_data_df
    
subdirs = ['PN_Scooby3MIN_SummaryTables', 'PNEd_SummaryTables', 'SP_SummaryTables_Mar2020/']
datatypes = ['Transcript_', 'Transcript_', 'Transcript_']
perfIDs = ['PN', 'PNEd', 'SP']
df_names = ['PN_norm_df', 'PNEd_norm_df', 'SP_norm_df']


for i in range(0, len(subdirs)):
    directory = table_dir + subdirs[i]
    dataType = datatypes[i]
    perfID = perfIDs[i]
    
    for root,dirs,files in os.walk(directory):
        
        temp_df = pd.DataFrame()
        end_norm = pd.DataFrame()
        
        for file in files:
            if file.endswith(".csv") and file.startswith(dataType):
                print(file)
                
                df = pd.read_csv(os.path.join(root,file))
                norm_df = calculate_norm_data(df)

                temp_df = pd.concat([temp_df, norm_df], ignore_index= True)
                print("Appended")
        
        norm_csv_file = table_dir + '/Norm' + dataType + perfID +'_' + 'ALL' + ".csv"
        normalised_csv_list.append(norm_csv_file)
        temp_df.to_csv(norm_csv_file)
    
    print("File created")

for i in range(0, len(normalised_csv_list)):
    print(i)

    fig, ax = plt.subplots(sharex=True, sharey=True, figsize=(12,10))
    plt.rcParams.update({'font.size': fntsize})
    
    all_norm_data = pd.read_csv(normalised_csv_list[i])

    ax.set_ylim([lowy, highy])
    
    ax.set_xlabel(f'Normalised Show Time \n Across All Shows ({perfIDs[i]})', fontsize = fntsize)
    ax.set_ylabel('Difference between Starts \n in Normalised Show Time', fontsize = fntsize)
    plt.scatter(all_norm_data['Norm_A_Start'], all_norm_data['Norm_Diff_Start'], 
                c="r", alpha= graph_alpha, marker= graph_marker, label="Show 1")
    
    fig_name = 'Norm_graph_'+perfIDs[i]+'.png'
    
    plt.savefig(fig_name,bbox_inches='tight', dpi = 300)
