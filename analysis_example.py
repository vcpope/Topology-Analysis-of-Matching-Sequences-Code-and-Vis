# Sample analysis code to test on sample data:
# To run in terminal:
# $ python3 analysis_example
# If matching a large number of shows, it is easiest to run the combo_extractMatches 
# function wth combinations:
# # Transcripts
# from itertools import combinations
# from transcriptseqanalysis import combo_extractMatches
# shownum = 5 # number of shows 
# transcript_files = your_transcript_files # list of .srt filenames
# audio_files = your_audio_files # .wav files the same order as transcript files
# data_type = 'Transcript' # other option is 'TranscriptScript' 
# perfID = which_performer
#for x,y in combinations(range(shownum), 2):  # 2 for pairs, 3 for triplets, etc
#    combo_extractMatches(transcript_files[x], transcript_files[y], 
#                                            audio_files[x], audio_files[y], 'data_type', 'perfID')
# # If matching to transcripts to a script, no need to use combinations:
# shownum = 5 # number of shows
# transcript_files = your_transcript_files 
# audio_files = your_audio_files # in the same order as transcript files
# data_type = 'TranscriptScript' # other option is 'Transcript'
# perfID = which_performer
# x = 0
# for x in range(shownum):  
#    combo_extractMatches(transcript_files[x], "Script.txt",
#                                           audio_files[x], audio_files[x], dataType, perfID)

import transcript_seq_analysis
from transcript_seq_analysis import combo_extractMatches

combo_extractMatches("Data/Transcript_LG_1_cut_Awards1.txt", "Data/Transcript_LG_5_cut_RedCarpet1.txt", 
                                            "Data/LG_Montage_1Award_Mic_Full.wav", "Data/LG_Montage_5RedCarpet_Mic_Full.wav",'Transcript', 'LG')