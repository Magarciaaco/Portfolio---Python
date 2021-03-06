# Coded by: Miguel Angel Garcia Acosta
# Contact: MAGA.DevCS@Gmail.com
# --------------------------
# MATRIX RECURSIVE REPLACER:
# --------------------------
# ----- ----- ----- ----- --
#
# ----- ----- ----- IMPORTS ----- ----- ----- #
import csv
# ----- ----- ----- IMPORTS ----- ----- ----- #
#
# START
#
# FILE TO READ DATA ==> .CSV
FileReader = "filename.csv"
#
# INITIALIZE ROWS AND COLUMNS
Field = []
Rows = []
#
# =============================
# READ FILENAME.CSV
#
with open(FileReader, 'r') as csvfile:
    # CREATE CSV OBJECT
    CSV_READER = csv.reader(csvfile)
    #
    # GET FIELD NAMES FROM FIRST ROW
    Field = next(CSV_READER)
    #
    # GET DATA FROM ROWS
    for Row in CSV_READER:
        Rows.append(Row)
    #
# GET THE TOTAL NUMBER OF ROWS
print("Total Rows: %d" % (CSV_READER.line_num))
#
# GET THE FIELD NAMES
print("FIELD NAMES: " + ','.join(Field for Field in Field))
#
# PRINT ROWS
print("\nROWS:")
for Row in Rows:
    print(' , '.join(Row for Row in Row))
print("\n")
# END