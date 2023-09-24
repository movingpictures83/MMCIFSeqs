#include "PluginManager.h"
#include <stdio.h>
#include <stdlib.h>
#include "MMCIFSeqsPlugin.h"

void MMCIFSeqsPlugin::input(std::string file) {
 inputfile = file;
 std::ifstream ifile(inputfile.c_str(), std::ios::in);
 while (!ifile.eof()) {
   std::string key, value;
   ifile >> key;
   ifile >> value;
   parameters[key] = value;
 }
}

void MMCIFSeqsPlugin::run() {

}

void MMCIFSeqsPlugin::output(std::string file) {
//SQLITE_DATABASE_DIR = "../../epitopedia.sqlite3"
//PDB_INPUT="6VXX_A"
//PDB_DATABASE_DIR = "../../mmcif"
//outprefix = "query_pdb_seq"

   std::string command = "export OLDPATH=${PYTHONPATH}; ";
   command += "export PYTHONPATH=/usr/local/lib64/python3.9/site-packages/:${PYTHONPATH}; ";
   command += "python3.9 plugins/MMCIFSeqs/runMMCIFSeqs.py ";
   command += PluginManager::addPrefix(parameters["sqldatabase"]) + " ";
   command += parameters["pdbinput"] + " ";
   command += PluginManager::addPrefix(parameters["pdbdatabase"]) + " ";
   command += file + "; ";
   command += "export PYTHONPATH=${OLDPATH}";
 std::cout << command << std::endl;

 system(command.c_str());
}

PluginProxy<MMCIFSeqsPlugin> MMCIFSeqsPluginProxy = PluginProxy<MMCIFSeqsPlugin>("MMCIFSeqs", PluginManager::getInstance());
