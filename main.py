from KG import KG
from BFS import find_path, BFS
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import os
import numpy as np

def main():

    file_path = "./KG_scripts/datasets/NELL-995/"

    triple_file = "kb_env_rl.txt"
    entity2id_file = "entity2id.txt"
    relation2id_file = "relation2id.txt"
    entity_embedding_file = "entity2vec.bern"
    relation_embedding_file = "relation2vec.bern"

    triple_file_path = file_path + triple_file
    entity2id_file_path = file_path + entity2id_file
    relation2id_file_path = file_path + relation2id_file
    entity_embedding_file_path = file_path + entity_embedding_file
    relation_embedding_file_path = file_path + relation_embedding_file

    nell = KG()
    nell.create_KG(triple_file_path, entity2id_file_path, relation2id_file_path, entity_embedding_file_path, relation_embedding_file_path)
    pool = ProcessPoolExecutor(18)
    # print('{} {} {}'.format(nell.entity2id['concept_politicsblog_perspective'],nell.relation2id['concept:proxyfor'],nell.entity2id['concept_book_new']))
    # BFS(nell,2,3)
    i = 0
    record_path = "./KG_scripts/datasets/NELL-995/BFS_result/" 
    if os.path.exists(record_path):
        pass
    else:
        os.makedirs(record_path)
    record_file = record_path + 'record.txt'
    for item in nell.triple_id:
        h = item[0]
        r = item[1]
        t = item[2]
        record = np.loadtxt(record_file,dtype=int).tolist()
        if item in record:
            continue
        pool.submit(BFS,nell,h,r,t)
        i = i+1
        if i == 50:
            break
    pool.shutdown()
if __name__ == '__main__':
    main()