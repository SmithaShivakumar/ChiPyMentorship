import os

def figure_out_the_puzzle():
    #1. to get the file names
    file_list = os.listdir(r"C:\Users\Smitha\Desktop\mystuff\prank\prank")
    print(os.getcwd())
    os.chdir(r"C:\Users\Smitha\Desktop\mystuff\prank\prank")
    
    #2. to rename the files
    for file_name in file_list:
        print("\n\n",file_name,file_name.translate(None,"1234567890"))
        os.rename(file_name, file_name.translate(None,"1234567890"))
        
figure_out_the_puzzle()