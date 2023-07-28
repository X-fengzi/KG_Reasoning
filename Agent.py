import torch.nn as nn
import torch.nn.functional as F
import torch



class LSTM_network(nn):
    def __init__(self, state_dim, hidden_size, num_layer, action_dim) -> None:
        super(LSTM_network, self).__init__()

        self.lstm = nn.LSTM(state_dim, hidden_size, num_layer, batch_first=True, bidirectional = False)
        self.fc1 = nn.Linear(hidden_size, action_dim)

    def forward(self,x):
        x = self.lstm(x)
        x = self.fc1(x)
        return x

class Agent():
    def __init__(self, policy_network) -> None:
        self.policy = policy_network

    def step(self, state, action_idx, action_space):
        
        action_mask = self.policy(state)
        action_prob = F.softmax(torch.matmul(action_mask,action_space))
        select_action = action_idx[torch.multinomial(input=action_prob,num_samples=1)]
        return select_action




    

