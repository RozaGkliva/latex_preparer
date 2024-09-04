#!/usr/bin/python3

# Copyright 2024 Roza Gkliva
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Module Name: latex_preparer.py
Author: Roza Gkliva
Date: 2024-08-24

Description:
    This script is used to prepare a latex project for compilation. It copies the figures and bib files to new directories specified by the user

Usage:
    ./latex_preparer.py [options]

Options:
    -h, --help: Show this help message and exit
    --main_tex: The main tex file
    --project_path: The path to the latex project
    --figures_folder: The new figures directory
    --bib_folder: The new bib directory

Example:
    ./latex_preparer.py --main_tex main.tex --project_path /path/to/latex_project --figures_folder figures --bib_folder bib

"""

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
    # print(main_tex)

    # create path to the main tex file
    main_tex_path = os.path.join(args.project_path, main_tex)
    if not os.path.exists(main_tex_path):
        print("The main tex file does not exist")
        sys.exit(1)

    which_figures = []
    with open(main_tex_path, 'r') as file:
        for line in file:
            # print(line)

            pattern = r'\\includegraphics\[[^\]]*\]\{([^}]+)\}'
            match = re.search(pattern, line)
            
            if match:
                # if match is found, check if the figure is in a directory and remove the directory
                figure_path = match.group(1)
                figure_name = figure_path.split("/")[-1]
                # print(figure_name)

                # print(match.group(1))
                which_figures.append(figure_name)

    return which_figures

    
def copy_figures_to_new_folder(figures_list, figures_dir):

    target_directory = os.path.join(args.project_path, args.figures_folder)
    source_directory = os.path.join(args.project_path, figures_dir)
    # print(f"target directory: {target_directory}")
    # print(f"source directory: {source_directory}")

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    for figure in figures_list:
        target_path = os.path.join(target_directory, figure)
        source_path = os.path.join(source_directory, figure)
        
        # print(f"source: {source_path}")
        if os.path.exists(target_path):
            print(f"The figure {figure} already exists in the figures directory: {target_path}")
        else:
            print(f"The figure {figure} does not exist in the figures directory: {target_path}")

            print(f"copying: {source_path} to {target_path}")
            os.system(f"cp {source_path} {target_path}")


[figures_dir, bibs_dir] =  get_directory_paths()
figures_list = find_used_figures()
# print(figures_list)

copy_figures_to_new_folder(figures_list, figures_dir)
# print(figures)
# print(bibs)