# # import numpy as np
# a = [[1,2,3,4,5,5,6,6,6],[1,2,3]]
# # np.savetxt('f.txt',np.array(a))
# print(str.replace(str(a[0])[1:-1],',',' ')+'\n')
# import torch
# import torch.nn.functional as F

# action = [1,5,8,9,14]
# action_space = 20
# action = torch.tensor(action)
# target=-0.5
# action_prob = F.softmax(torch.randn(size=(5,20)),dim=1)
# action_mask = F.one_hot(action, num_classes=action_space) > 0
# picked_action_prob = action_prob[action_mask]
# loss = torch.sum(-torch.log(picked_action_prob)*target)

# print('enhen')0
# from utils import task

# import numpy as np
# act_dim = 100
# act_mask = np.zeros(act_dim, dtype=np.uint8)
# act_idxs = list(range(10))
# keep_size = int(len(act_idxs[1:]) * (1.0 - 0.1))
# tmp = np.random.choice(act_idxs[1:], keep_size, replace=False).tolist()
# act_idxs = [act_idxs[0]] + tmp
# act_mask[act_idxs] = 1

# actor_logits = np.random.randint(1,10,size=(128,100))
# x = 1 - act_mask
# actor_logits[x] = -999999.0
# print(act_mask)

for i in range(10):
    for ii in range(5):
        i = i+1
        print(i)