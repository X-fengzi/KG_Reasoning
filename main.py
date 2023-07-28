import torch
import numpy as np
import random
import os

from KG import KG
from Env import Env
from Agent import Agent, LSTM_network
from utils import *

args = read_options()

file_path = "./datasets/NELL-995/"

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

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("the train of model is on {}".format(device))

nell = KG()
nell.create_KG(triple_file_path, entity2id_file_path, relation2id_file_path, entity_embedding_file_path, relation_embedding_file_path)

env = Env(nell)

policy_nn = LSTM_network(args.state_dim, args.hidden_size, args.num_layer, args.action_dim).to(device)

agent = Agent(policy_nn)

def train():
    tasks = []
    task = edict(mode = None,
             head = None,
             tail = None,
             query = None,
             cur_entity = None,
             transition = None,
             transitions = None,
             reward = None,
             done = None)
    tasks.append(task)


    for task in tasks:
        for i in range(args.steps):

            state = env.get_state(task)
            state = torch.FloatTensor(state).to(device)
            action_idx, action_space = env.get_actions(task)
            action_idx = torch.LongTensor(action_idx).to(device)
            action_space = torch.FloatTensor(action_space).to(device)

            select_action = agent.step(state,action_idx,action_space)
            task = env.interact(task,select_action)
            if task.cur_entity == task.tail:
                task.done = True
                break
        
        if task.done:
            reward = args.success_reward + 1




