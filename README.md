python script that prepares a latex project for submission by collecting the used figures and references

This assumes that the figures and bibfiles are in their own directory

run with:
```
./latex_preparer.py --project_path=/PATH_TO_LATEX_PROJECT/ --figures_folder=new_figures --main_tex=main.tex
```

# Roadmap
- [x] when searching for the list of figures exclude the ones in commented out lines
- [ ] remember! same as above for the bib files
- [ ] check if multiple bib files
- [x] check if figures are under directories
- [ ] tex file does not need to be the main tex file. It can be any tex file that is in the project. Maybe the script should scan all tex files that are used