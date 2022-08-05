import os
import shutil
import random

merge_list = ["Token_Argument_2", "Token_Member_2", "Token_Command_1", "Token_Argument_3", "Token_String_1", "Token_Member_3", "Token_Command_2"]

merge_list = ["Token_Member_4", "Token_String_2", "Token_Argument_4", "Token_Command_3"]

directory = '/home/kali/Master_Thesis/Obfuscated_out/'

for root in os.listdir(directory):
    if root in merge_list:
        print(root)
        dir = os.path.join(directory, root)
        print(dir)
        sampled_files = random.sample(os.listdir(dir), 2500)
        dest = '/home/kali/Master_Thesis/Obfuscated_out/mix_Format/' + root + '_'
        for file in sampled_files:
            source = os.path.join(dir, file)
            destination = dest + file
            shutil.copyfile(source, destination)
