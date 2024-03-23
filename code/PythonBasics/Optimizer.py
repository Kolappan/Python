import numpy as np
from fastai.vision.all import *
from fastbook import *
import fastbook

fastbook.setup_book() 

linear_model = nn.Linear(28*28,1)
print(linear_model.weight.shape, linear_model.bias.shape)

def get_data():
    path = Path("/Users/kolappanpillai/SampleData/fastai/mnist_sample")
    print(path)
   
    threes = (path/'train'/'3').ls().sorted()
    sevens = (path/'train'/'3').ls().sorted()
    
    stacked_threes = torch.stack([tensor(Image.open(o)) for o in threes]).float()/255
    stacked_sevens = torch.stack([tensor(Image.open(o)) for o in sevens]).float()/255
    train_x = torch.cat([stacked_threes, stacked_sevens]).view(-1, 28*28)
    train_y = tensor([1]*len(threes) + [0]*len(sevens)).unsqueeze(1)
    dset = list(zip(train_x, train_y))
    valid_3_tens = torch.stack([tensor(Image.open(o)) for o in (path/'valid'/'3').ls()])
    valid_3_tens = valid_3_tens.float()/255
    valid_7_tens = torch.stack([tensor(Image.open(o)) for o in (path/'valid'/'7').ls()])
    valid_7_tens = valid_7_tens.float()/255
    valid_x = torch.cat([valid_3_tens, valid_7_tens]).view(-1, 28*28)
    valid_y = tensor([1]*len(valid_3_tens) + [0]*len(valid_7_tens)).unsqueeze(1)
    return train_x, train_y, valid_x, valid_y

class BasicOptim:
    def __init__(self,params,lr): self.params,self.lr = list(params),lr

    def step(self, *args, **kwargs):
        for p in self.params: p.data -= p.grad.data * self.lr

    def zero_grad(self, *args, **kwargs):
        for p in self.params: p.grad = None

def mnist_loss(predictions, targets):
    return torch.where(targets==1, 1-predictions, predictions).mean()


def calc_grad(xb, yb, model):
    preds = model(xb)
    loss = mnist_loss(preds, yb)
    loss.backward()

x_train, y_train, x_valid, y_valid = get_data() 
print("shapes: ", x_train.shape, y_train.shape)

dset = list(zip(x_train, y_train))
dl = DataLoader(dset, batch_size=256)

lr = 1e-5

opt = BasicOptim(linear_model.parameters(), lr)

def train_epoch(model):
    for xb,yb in dl:
        calc_grad(xb, yb, model)
        opt.step()
        opt.zero_grad()