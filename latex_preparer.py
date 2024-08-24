#!/usr/bin/python3
# setup the script arguments
import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Prepare the latex project for compilation')
parser.add_argument('--project_path', type=str, help='The path to the latex project')
args = parser.parse_args()


print(args.project_path)

latex_project_directory = args.project_path

figures_extensions = [".png", ".jpg", ".jpeg", ".pdf"]

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


print(f"figures: {figures_directory}")
print(f"bib: {bib_directory}")
