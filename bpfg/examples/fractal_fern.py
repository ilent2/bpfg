
from bpfg.lsystem import LSystem
from bpfg.node import Node
from bpfg.builtin import SB, EB, Left, Right, Forward
import math

WIDTH = 3

ANGLE = math.radians(45.0)
STEPS = 18
D = 3
R = 1.28

class A(Node):
  def __init__(self, v):
    Node.__init__(self, "A({})".format(v))
    self._v = v

  def produce(self, tree):
    if self._v < D:
      tree += A(self._v + 1)
    elif self._v == D:
      tree += I(1)
      tree += SB() + Right(ANGLE) + A(0) + EB()
      tree += SB() + Left(ANGLE)  + A(0) + EB()
      tree += I(1)
      tree += A(self._v)

  def interpret(self, tree):
    tree += Forward(0.025*self._v)

class I(Node):
  def __init__(self, x):
    Node.__init__(self, "I({})".format(x))
    self._x = x

  def produce(self, tree):
    tree += I(R*self._x)

  def interpret(self, tree):
    tree += Forward(0.025*self._x)

if __name__ == '__main__':

  # Create L-System
  tree = LSystem()

  # Define axiom
  tree += A(1.0)

  # Evolve L-System desired number of steps
  tree.evolve(STEPS)

  # Add L-System as blender object
  tree.create_object()

