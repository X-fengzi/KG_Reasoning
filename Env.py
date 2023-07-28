import numpy as np
import random
from utils import Reward

class Env():
    def __init__(self, KG) -> None:
        self.KG = KG

    def get_state(self, task):
        return np.concatenate((self.KG.id_entity_embedding[task.head]),self.KG.id_relation_embedding[task.query],self.KG.id_entity_embedding[task.cur_entity])

    def get_actions(self, task):
        return self.KG.h_find_r(task.cur_entity), self.KG.id_relation_embedding[self.KG.h_find_r(task.cur_entity)]

    def interact(self, task, select_action):
        new_entity = random.choice(self.KG.find_tail(task.cur_entity,select_action))
        task.transition.action = select_action
        task.transition.next_state = new_entity
        task.cur_entity = new_entity
        task.transitions.append(task.transition)
        task.transition.reward.append(Reward(task))

        return task



        