import numpy as np

class KG():
    def __init__(self) -> None:
        self.entity = []
        self.relation = []
        self.triple = []

        self.triple_id = []
        self.entity_id =[]
        self.relation_id =[]

        self.h_find_r = {}

        self.entity2id = {}
        self.id2enetity = {}

        self.relation2id = {}
        self.id2relation = {}

        self.id_entity_embedding = None
        self.id_relation_embedding = None

    def create_KG(self, triple_file_path: str, entity2id_file_path: str, relation2id_file_path: str, entity_embedding_file_path: str, relation_embedding_file_path: str):

        # triple_file : (h,r,t)
        # entity2id_file : (entity,id)
        # relation2id_file:(relation,id)
        # entity_embedding_file : ((id),embedding)
        # relation_embedding : ((id),embedding)

        with open(entity2id_file_path,'r') as f1:
            for line in f1:
                entity, id = line.strip().split('\t')
                # print("entity:{}".format(entity))
                # print("id:{}".format(id))
                # exit()
                id = int(id)
                self.entity.append(entity)
                self.entity_id.append(id)
                self.entity2id[entity] = id
                self.id2enetity[id] = entity
                self.h_find_r[id] = []
        f1.close()

        with open(relation2id_file_path,'r') as f2:
            for line in f2:
                relation, id = line.strip().split('\t')
                id = int(id)
                self.relation.append(relation)
                self.relation_id.append(id)
                self.relation2id[relation] = id
                self.id2relation[id] = relation
        f2.close()

        with open(triple_file_path,'r') as f3:
            for line in f3:

                h, t, r = line.strip().split('\t')
                
                try:
                    h_id = self.entity2id[h]
                    r_id = self.relation2id[r]
                    t_id = self.entity2id[t]
                    self.triple.append([h,r,t])
                    self.triple_id.append([h_id,r_id,t_id])
                    if r_id not in self.h_find_r[h_id]:
                        self.h_find_r[h_id].append(r_id)
                except:
                    print('{} {} {} can not find id'.format(h,r,t))

        f3.close()

        self.id_entity_embedding = np.loadtxt(entity_embedding_file_path)
        self.id_relation_embedding = np.loadtxt(relation_embedding_file_path)

    def find_tail(self, id_head, id_relation):
        candidate_tail = []
        for item in self.triple_id:
            if item[0] == id_head and item[1] == id_relation:
                candidate_tail.append(item[2])
            else:
                pass
        return candidate_tail
    



        

