import os
import plotly
from collections import Counter
from plotly.graph_objs import Scatter, Layout, layout

def reorder_files(files_in_dir):
    '''
        Takes a list of files
        Rearranges the files as per the year in the File_Name
    '''
    reordered_files = files_in_dir
    # Sort as per string
    reordered_files = sorted(reordered_files, key=lambda x:x)
    # Google Priv Reordering
    # reordered_files = sorted(reordered_files, key=lambda x: int(x[:4]))
    # Twitter Reordering
    # reordered_files = sorted(reordered_files, key=lambda x: int(x.split(" ")[1]))
    return reordered_files

def get_dir_files(target_dir=os.getcwd()):
    '''
        Takes a directory and lists all the files/folders in it.
        Default dir as the current directory is nothing is passed.
    '''
    files_in_dir = os.listdir(target_dir)
    #print (files_in_dir)
    files_in_dir = reorder_files(files_in_dir)
    file_word_count=[]
    for curr_file in files_in_dir:
        temp = analyze_file(curr_file)
        file_word_count.append(temp)
    return (files_in_dir,file_word_count)
    

def analyze_file(curr_file):
    '''
        Peforms analysis on the file path passed.
    '''
    with open(curr_file) as curr_policy:
        print("Curr File:",curr_file)
        #create a list of all words fetched from the file using a list comprehension
        words = [word for line in curr_policy for word in line.split()]
        print ("The total word count is:", len(words))
        #now use collections.Counter
        # c = Counter(words)
        # for word, count in c.most_common():
        #     print (word, count)
        print("-------------------------")
        return (len(words))

if __name__ == "__main__":
    files_in_dir, file_word_count = get_dir_files()
    layout_param = Layout(
        title=layout.Title(
            # text='Twitter Privacy Policy Revisions',
            # text='Google Privacy Policy Revisions',
            text='Google Privacy Policies Link Expansion',
            xref='paper',
            x=0
        ),
        xaxis=layout.XAxis(
            title=layout.xaxis.Title(
                # text='Twitter Privacy Policies',
                text='Google Privacy Policies',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        ),
        yaxis=layout.YAxis(
            title=layout.yaxis.Title(
                text='Number of Words in Document',
                font=dict(
                    family='Courier New, monospace',
                    size=16,
                    color='#7f7f7f'
                )
            )
        )
    )
    plotly.offline.plot({
        "data": [Scatter(x=files_in_dir, y=file_word_count)],
        "layout": layout_param
    })