import pandas as pd
import pickle
import os


# Silence SettingWithCopyWarning on pandas < 3. The option is deprecated (and has
# no effect) since pandas 3.0, where Copy-on-Write removed that warning.
if int(pd.__version__.split('.')[0]) < 3:
    pd.options.mode.chained_assignment = None  # default='warn'


# Helper function

def load_obj(data_folder):
    data_folder=os.path.join(os.path.dirname(__file__), data_folder)
    with open(data_folder + '.pkl', 'rb') as f:
        return pickle.load(f)
   

# Save data as dictionary        
# Databases
database_mapping={}
# Gene-level ID table (Ensembl gene ID, gene name, NCBI gene ID) used for ID conversions
gene_mapping={}
Pathways={}
# Join graph
network={}
# The PPI
PPI={}

elm={}
elm_interactions={}

pdb={}

here=os.path.dirname(__file__)


# Human
# exon -> Pfam domain table from Ensembl 116 (gzip-compressed, see scripts/build_exon_domain_table.py)
database_mapping['Human']= pd.read_pickle(os.path.join(here,"data/database/Human"), compression='gzip')
gene_mapping['Human']= database_mapping['Human'][['Gene stable ID','Gene name','NCBI gene ID']].drop_duplicates()
Pathways['Human']= pd.read_pickle(os.path.join(here,"data/pathways/pathways_human"))
network['Human']=load_obj(os.path.join(here,'data/network/graph_human'))
PPI['Human']=load_obj(os.path.join(here,'data/network/PPI_Human'))
elm['Human']= pd.read_pickle(os.path.join(here,"data/database/elm"))
elm_interactions['Human']= pd.read_pickle(os.path.join(here,"data/database/ELM_interactions"))
pdb['Human']= pd.read_pickle(os.path.join(here,"data/database/pdb"))
non_coding=load_obj(os.path.join(here,'data/database/non_coding'))

# exon -> Pfam domain table from Ensembl 116 (gzip-compressed, see scripts/build_exon_domain_table.py)
database_mapping['Mouse']= pd.read_pickle(os.path.join(here,"data/database/Mouse"), compression='gzip')
gene_mapping['Mouse']= database_mapping['Mouse'][['Gene stable ID','Gene name','NCBI gene ID']].drop_duplicates()
Pathways['Mouse']= pd.read_pickle(os.path.join(here,"data/pathways/pathways_mouse"))
network['Mouse']=load_obj(os.path.join(here,'data/network/graph_mouse'))
PPI['Mouse']=load_obj(os.path.join(here,'data/network/PPI_mouse'))
elm['Mouse']= pd.read_pickle(os.path.join(here,"data/database/elm_mouse"))
elm_interactions['Mouse']= pd.read_pickle(os.path.join(here,"data/database/ELM_interactions_mouse"))
pdb['Mouse']= pd.read_pickle(os.path.join(here,"data/database/pdb_mouse"))

