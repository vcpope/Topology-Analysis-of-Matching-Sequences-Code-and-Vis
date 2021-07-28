# Sequence Matching and Audio Clip Creation from Timestamped Transcripts (.srt)

This script compares timestamped transcripts to one another or a script, creates a folder for analysis results, cleans transcripts, outputs the cleaned files as .txt, locates longest contiguous sequences that match, creates a clip from the audio of each transcript’s .wav file for each match, and creates a .csv file that reports sequences and their location (in time and in number of tokens). The core algorithm compares two shows at a time, but the analysis example code shows how you can feed in a bigger collection of shows easily by using combinations from itertools (I've used 20 transcripts at a time, resulting in 20 choose 2 = 190 output files).

## Motivation
Hi! I'm Vanessa. :wave:

This sequence matching code was written as part of my PhD thesis to help me find patterns in the transcripts of stand-up comedy shows. You can read more about my work here: 
Transferring my code onto GitHub is part of a project to make my research replicable and open source, so this is a learning curve! Any help and feedback would be much appreciated.

## Input
The code takes in .srt files, which are subtitle files that include timestamp information, and .wav files for audio. Because my PhD looks at structure in performance time I wanted to make sure I could capture timing information along with the content itself.

## Output
A folder for each comparison that contains: an audio clip for each show for each subsequence, copies of the cleaned transcripts as .txt files and a .csv file that provides information on each matched subsequence in each row, with match IDs, time data and buffer analysis (the buffer analysis is a little idiosyncratic to my research, looking at whether hesitations were more likely immediately before or after a matching sequence).

## Script Contents
The majority of the functions in the code relate to re-formatting it and outputting it in a human-readable .csv to help with further processing.

This code locates matching subsequences between either two timestamped Subtitle Rip (.srt) or a series of .srt files a .txt text file on sample data provided.  

The files are first processed to remove punctuation and code certain words. Clips for each match are created from the audio (.wav) files for the transcript.

Two summary .csv files accompany the clips as well as cleaned .txt files. One .csv provides information on the contents and location of matching subsequences, the other on the tokens that didn't match.

Implementation:
- Code is run in python3 and is a library of helper functions
- To run an analysis, run the analysis_example.py script also provided
- If using new performances for analysis, create new perfID and show data in combo_extractMatches() and get_showID() in this file (NB: I aim to change these to input parameters but haven't got around to it yet!)
- Files and information needed to run code are: transcript/script/vowel list filenames, show audio filenames, data matchtype (Transcript / TranscriptScript) and performance ID
- File names are used to create folders and identify shows, so the naming convention is important: 

For transcripts: "DataType_PerfID_Location_Note_DDMMMYYYY.txt"
e.g. "Transcript_PN_Edinburgh_Extract_26Aug2018.txt"
For audio: "PerfID_Location_DDMMMYYYY_Source_Note.wav"
 e.g. "PN_Edinburgh_26Aug2018_Mic_Full.wav"


# Example analysis

To run in terminal:
$ python3 analysis_example
If matching a large number of shows, it is easiest to run the combo_extractMatches 
function wth combinations:

### Transcripts
from itertools import combinations
from transcriptseqanalysis import combo_extractMatches
shownum = 5 # number of shows 
transcript_files = your_transcript_files # list of .srt filenames
audio_files = your_audio_files # .wav files the same order as transcript files
data_type = 'Transcript' # other option is 'TranscriptScript' 
perfID = which_performer
for x,y in combinations(range(shownum), 2):  
 2 for pairs, 3 for triplets, etc
    combo_extractMatches(transcript_files[x], transcript_files[y], 
                                            audio_files[x], audio_files[y], 'data_type', 'perfID')
### Scripts

If matching to transcripts to a script, no need to use combinations:
 shownum = 5 # number of shows
 transcript_files = your_transcript_files 
 audio_files = your_audio_files # in the same order as transcript files
 data_type = 'TranscriptScript' # other option is 'Transcript'
 perfID = which_performer
 x = 0
for x in range(shownum):  
    combo_extractMatches(transcript_files[x], "Script.txt",
                                           audio_files[x], audio_files[x], dataType, perfID)
