# GUI_for_Internship
Created a GUI using Tkinter to make the process of Data processing easier

Follows the Data Processing Flow of Project

1) ssh into robinson server to run Olivier's timing scripts to generate timing reports
2) Takes these timing scripts and runs a python script that concatenates these scripts into one file and dumps the result where you want
3) Imports silicon data from ISE
4) Parses the silicon data using a PERL script created by Natalie Lun (no longer and employee) and dumps the files into a folder called 'CRUNCHED' where you want
5) Runs another script created by Natalie that compares the CRUNCHED silicon data and the timing data
