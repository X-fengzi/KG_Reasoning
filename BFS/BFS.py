try:
    from Queue import Queue
except ImportError:
    from queue import Queue
import numpy as np
import os
import sys
module_path = os.path.abspath("./")
sys.path.append(module_path)

from utils import list_data_storage

def BFS(KG, entity1, rel, entity2):

    all_path = []
    res = find_path(KG)
    res.mark_found(entity1,None,None)
    q = Queue()
    q.put(entity1)

    while(not q.empty()):
        cur_node = q.get()
        for relation in KG.h_find_r[cur_node]:
            for tail in KG.find_tail(cur_node,relation):              
                next_entity = tail
                connect_relation = relation     
                if (next_entity == entity2):
                    res.mark_found(next_entity, cur_node, connect_relation)
                    entity_list, relation_list, path = res.reconstruct_path(entity1, entity2)
                    # print(path)
                    all_path.append(path)
                if (not res.is_found(next_entity)):
                    res.mark_found(next_entity, cur_node, connect_relation)
                    q.put(next_entity)
    print(all_path)

    file_path = "./datasets/NELL-995/BFS_result/"+str(rel)+'/'
    file_name = str(entity1)+'_'+str(entity2)+'.txt'
    list_data_storage(all_path,file_path,file_name)

    record_path = "./datasets/NELL-995/BFS_result/"
    record_name = 'record.txt'
    record_item = [entity1,rel,entity2]
    list_data_storage(record_item,record_path,record_name)
    
    return all_path

class find_path(object):
    def __init__(self,KG) -> None:
        self.entities = {}
        self.KG = KG
        for item in self.KG.entity_id:
            self.entities[item] = (False, "", "")

    def is_found(self, entity):
        return self.entities[entity][0]
    
    def mark_found(self, entity, pre_node, relation):
        self.entities[entity] = (True, pre_node, relation)

    def reconstruct_path(self,entity1,entity2):
        entity_list = []
        relation_list = []
        cur_node = entity2

        while(cur_node != entity1):
            entity_list.append(cur_node)
            relation_list.append(self.entities[cur_node][2])
            cur_node = self.entities[cur_node][1]
        entity_list.append(cur_node)

        entity_list.reverse()
        relation_list.reverse()

        path = []

        for i in range(len(entity_list)-1):
            path.append(entity_list[i])
            path.append(relation_list[i])
        path.append(entity_list[len(entity_list)-1])

        return entity_list, relation_list, path
        
