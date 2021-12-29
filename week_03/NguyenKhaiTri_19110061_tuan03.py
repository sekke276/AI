import numpy as np;
import matplotlib.pyplot as plt;
from mpl_toolkits.mplot3d import axes3d;
from matplotlib import cm;
import pandas as pd;

def ex1():
    arr = np.array([[1,2,30,4,50],[20,30,1,23,4]]);
    print(arr);
    print(arr.max()); # find the largest number in the matrix
    print(arr.max(0)); # find the largest numbers of each columns if it is the array it find the largest number of array
    print(arr.max(1)); # find the largest number of each rows it not use in array



def ex2():
    X = np.linspace(-10,10,50);
    Y = np.linspace(-10,10,50);
    X, Y = np.meshgrid(X,Y);
    Z= X**3 + Y**2 + 3;
    fig = plt.figure();
    ax = fig.gca(projection = '3d');
    surf = ax.plot_surface(X,Y,Z,cmap = cm.coolwarm)
    plt.show();
    


def ex3():
    result = pd.read_csv("C:/Users/tring/Desktop/V01-2021-6.csv");
    #print(result.head(3));
    #print(result.info());
    #print(result.describe());
    # one row
    #print(result.iloc[6]);
    #one column
   # print(result.iloc[:,2]);
    #one elemnent
    #print(result.iloc[[3],[4]]);

   
class animal:
    def __init__(myOb,kind, name,legs,color):
        myOb.name = name;
        myOb.kind = kind;
        myOb.legs = legs;
        myOb.color = color;
    
    def intro(self):
        print("This is my " + self.kind + " his name is " + self.name);

    def detail(self):
        print(self.name + " has " + str(self.legs) + " and he is " + self.color);
        


class cat(animal):
    def __init__(myOb, kind, name, legs, color):
        super().__init__(kind, name, legs, color)

    def sound(self):
        print("Meo meo meo");

    def intro(self):
        return super().intro();
    
    def detail(self):
        return super().detail();

dogg = animal("dog","phat",4,"black");
dogg.detail();

myHomeCat = cat("cat","kitty",4,"white");
myHomeCat.sound();
myHomeCat.intro();
myHomeCat.detail();

   
        
