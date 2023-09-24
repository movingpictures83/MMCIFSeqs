#!/usr/bin/python3.10

# Copyright (c) 2021 Christian Balbin
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

#import os
#import json
import sqlite3
import tempfile
import sys
#from functools import partial
#import subprocess
#from multiprocessing import Pool

#from rich.progress import track

#from epitopedia.app import config
#from epitopedia.app.blastparser import BLASTParser
#from epitopedia.app.config import console
#from epitopedia.app.hitparser import parseHit
from MMCIFSeqs import MMCIFSeqs
#from epitopedia.app.MMCIFSeqs import MMCIFSeqs
#from epitopedia.app.reduce import reduce_results
#from epitopedia.utils.utils import remove_previous_files

# from epitopedia.viz.serve import write_html, serve_html
#from epitopedia.app.args import args

#SQLITE_DATABASE_DIR = "../../epitopedia.sqlite3"
#PDB_INPUT="6VXX_A"
#PDB_DATABASE_DIR = "../../mmcif"
#outprefix = "query_pdb_seq"
SQLITE_DATABASE_DIR = sys.argv[1]
PDB_INPUT=sys.argv[2]
PDB_DATABASE_DIR = sys.argv[3]
outprefix = sys.argv[4]

con = sqlite3.connect(SQLITE_DATABASE_DIR)

query_pdb_base = PDB_INPUT.split("_")[0].lower()
query_pdb_chain = PDB_INPUT.split("_")[1]
pdb_path = f"{PDB_DATABASE_DIR}/{query_pdb_base[1:3]}/{query_pdb_base}.cif"

#################################################################################################
print("Extracting query protein...")
query_pdb_seq = MMCIFSeqs(query_pdb_base, query_pdb_chain, SQLITE_DATABASE_DIR,compute_acc=True)
outfile = open(outprefix+".seqres.txt", 'w')
#fp = tempfile.NamedTemporaryFile(mode="w", delete=False)
#file_path = fp.name
#print(file_path)
outfile.write(query_pdb_seq.seqres)
outfile.close()
outfile2 = open(outprefix+".rasa.txt", 'w')
outfile3 = open(outprefix+".seqnums.txt", 'w')
outfile5 = open(outprefix+".binaryrasa.txt", 'w')
for i in range(len(query_pdb_seq.rasa)):
    outfile2.write(str(query_pdb_seq.rasa[i]))
    outfile3.write(str(query_pdb_seq.seqnums[i]))
    outfile5.write(str(query_pdb_seq.binaryrasa[i]))
    outfile2.write("\n")
    outfile3.write("\n")
    outfile5.write("\n")
outfile2.close()
outfile3.close()
outfile5.close()
outfile4 = open(outprefix+".seqsolv.txt", 'w')
outfile4.write(query_pdb_seq.seqsolv)
outfile4.close()
#print(query_pdb_seq.seqnums)
#print(query_pdb_seq.seqsolv)
print("Query protein extracted")
#################################################################################################

