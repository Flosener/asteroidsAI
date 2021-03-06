import torch
import torch.nn as nn


class Agent(nn.Module):
    """ Feed-forward neural network for our spaceship agent. """
    
    def __init__(self, n_inputs, n_hidden, n_outputs):
        """ Declare layers and activations of the NN. """
        super(Agent, self).__init__()
        
        self.linear1 = nn.Linear(n_inputs, n_hidden)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(n_hidden, n_outputs)
        self.tanh = nn.Tanh()
        
        
    def forward(self, x):
        """ Computes a forward step through the network. """
        
        y = self.linear1(x)
        y = self.relu(y)
        y = self.linear2(y)
        y = self.tanh(y)
        
        # Return the activation of the output layer (with tanH activation for actions between -1 and 1)
        return y