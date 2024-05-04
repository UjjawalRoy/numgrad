import numpy as np

np.random.seed(0)

# ============================================ INPUT ==========================================================================
# creating an input layer with batch_size=5, and each input containing 4 features
# shape of which will be (5, 4)
# input_shape = (5, 4)
X = np.array([[1.3, 2.5, 3.6, 1],
          [2.3, 5.6, 1.2, 6],
          [3.2, 5, 4.9, 1.5],
          [1.5, 5, 3.2, 4.5],
          [3.6, 1.9, 2, 5]], dtype='uint8')

class Layer_Dense:
    """
    A class to represent a dense (fully connected) neural network layer.

    This class initializes a dense layer with a given number of input features and neurons.
    It also handles the forward propagation step, where it computes the output for the given inputs.
    
    Attributes:
        weights (numpy.ndarray): The weights matrix of the layer with shape (n_inputs, n_neurons). 
                                 Initialized with random values scaled by 0.10 to keep them small.
        biases (numpy.ndarray): The biases for the layer with shape (1, n_neurons). 
                                Initialized to zeros.
    
    Methods:
        forward(inputs):
            Computes the dot product between the input data and the weights, then adds the biases.
            The result is stored in the 'output' attribute.
    """
    
    def __init__(self, n_inputs, n_neurons):
        """
        Initializes a dense layer with given input size and number of neurons.

        Args:
            n_inputs (int): The number of input features.
            n_neurons (int): The number of neurons in the layer.
        
        This initializes the weights with random values scaled by 0.10 and the biases as zeros.
        """
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        """
        Perform the forward propagation through this dense layer.

        Args:
            inputs (numpy.ndarray): The input data with shape (batch_size, n_inputs).

        This method calculates the dot product of the inputs and the layer's weights, then adds the biases.
        The computed result is stored in the 'output' attribute.
        """
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation:
    """
    A class containing common activation functions used in neural networks.

    This class provides two nested classes representing specific activation functions: 
    ReLU (Rectified Linear Unit) and Sigmoid. Each nested class has a 'forward' method 
    for applying the activation function to the inputs.

    Nested Classes:
        ReLU:
            Implements the ReLU activation function, which outputs the maximum of 0 and the input value.
        
        Sigmoid:
            Implements the Sigmoid activation function, which outputs a value between 0 and 1, calculated
            as 1/(1 + exp(-input)).
    """
    
    class ReLU:
        """
        ReLU (Rectified Linear Unit) activation function.

        This activation function outputs the maximum of 0 and the input value, effectively "rectifying" 
        the input. It is commonly used in deep learning models due to its simplicity and effectiveness.
        
        Method:
            forward(inputs):
                Applies the ReLU function to the given inputs and stores the result in 'output'.
        """
        def forward(self, inputs):
            self.output = np.maximum(0, inputs)

    class Sigmoid:
        """
        Sigmoid activation function.

        This activation function transforms the input into a value between 0 and 1, using the formula 
        1/(1 + exp(-input)). It is often used in logistic regression and binary classification tasks.
        
        Method:
            forward(inputs):
                Applies the Sigmoid function to the given inputs and stores the result in 'output'.
        """
        def forward(self, inputs):
            self.output = 1 / (1 + np.exp(-inputs))


layer1 = Layer_Dense(4, 5)      # number of feature inputs = 4 and number of neurons in current layer = 5
layer2 = Layer_Dense(5, 3)      # number of feature inputs = number of neurons of prev layer = 5 and number of neurons in current layer = 3
activation_sigmoid = Activation.Sigmoid()
activation_relu = Activation.ReLU()

layer1.forward(X)
print("Layer 1 output =======> ", layer1.output)
activation_sigmoid.forward(layer1.output)
print("Sigmoid activated output =======> ", activation_sigmoid.output)
layer2.forward(activation_sigmoid.output)
print("Layer 2 output =======> ", layer2.output)
activation_relu.forward(layer2.output)
print("ReLU activated output =======> ", activation_relu.output)