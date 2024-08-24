#!/usr/bin/python3
# setup the script arguments
import argparse
import os
import re
import sys

parser = argparse.ArgumentParser(description='Prepare the latex project for compilation')
parser.add_argument('--main_tex', type=str, help='The main tex file')
parser.add_argument('--project_path', type=str, help='The path to the latex project')
parser.add_argument('--figures_folder', type=str, help='The new figures directory')
parser.add_argument('--bib_folder', type=str, help='The new bib directory')
args = parser.parse_args()


# print(args.project_path)
figures_extensions = [".png", ".jpg", ".jpeg", ".pdf", ".eps"]

def get_directory_paths():

    latex_project_directory = args.project_path

    

    for item in os.listdir(latex_project_directory):
        # find the directories that contain figures and bib files
        if os.path.isdir(os.path.join(latex_project_directory, item)):
            
            # go in the directories and check if image files or bibfiles are there
            for file in os.listdir(os.path.join(latex_project_directory, item)):
                for extension in figures_extensions:
                    if file.endswith(extension):
                        figures_directory = os.path.join(latex_project_directory, item)
                if file.endswith(".bib"):
                    bib_directory = os.path.join(latex_project_directory, item)


    # print(f"figures: {figures_directory}")
    # print(f"bib: {bib_directory}")
    return figures_directory, bib_directory

def find_used_figures():
    # go into the .tex file and find the figures that are used
    main_tex = args.main_tex
    print(main_tex)

    # create path to the main tex file
    main_tex_path = os.path.join(args.project_path, main_tex)
    if not os.path.exists(main_tex_path):
        print("The main tex file does not exist")
        sys.exit(1)

    which_figures = []
    with open(main_tex_path, 'r') as file:
        for line in file:
            # if "includegraphics" in line and any(extension in line for extension in figures_extensions):
                # check if the line contains the figure extension

            pattern = r'\\includegraphics\[[^\]]*\]\{([^}]+)\}'
            match = re.search(pattern, line)
            # TODO exclude commented out lines
            if match:
                # print(match.group(1))
                which_figures.append(match.group(1))

    return which_figures

    
    # print(which_figures)


[figures, bibs] =  get_directory_paths()
figures_list = find_used_figures()
print(figures_list)
# print(figures)
# print(bibs)