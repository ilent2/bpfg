# #### BEGIN LICENSE BLOCK ####
#
# builtin.py - Part of Blender Plant Fractal Generator.
# Copyright (C) 2013 Isaac Lenton (aka ilent2)
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# #### END LICENSE BLOCK ####

from . import node
import mathutils

class SB(node.Node):
  def __init__(self):
    node.Node.__init__(self, "SB()")

  def interpret(self, tree):
    tree._branch_depth += 1
    tree._branch_index += 1
    if (len(tree._branches) <= tree._branch_index
        or tree.branch().depth != tree._branch_depth):
      new = tree._branches_depth[-1].copy()
      new.depth = tree._branch_depth
      tree._branches.insert(tree._branch_index, new)
    else:
      tree._branches[tree._branch_index] = tree._branches_depth[-1].copy()
      tree._branches[tree._branch_index].depth = tree._branch_depth

    tree._branches_depth.append(tree.branch())

class EB(node.Node):
  def __init__(self):
    node.Node.__init__(self, "EB()")

  def interpret(self, tree):
    tree._branch_depth -= 1
    tree._branches_depth.pop(-1)

class Left(node.Node):
  def __init__(self, angle):
    node.Node.__init__(self, "Left({})".format(angle))
    self._angle = angle

  def interpret(self, tree):
    branch = tree.branch()
    branch.rotate(mathutils.Quaternion((0.0, 0.0, 1.0), self._angle))

class Right(node.Node):
  def __init__(self, angle):
    node.Node.__init__(self, "Right({})".format(angle))
    self._angle = angle

  def interpret(self, tree):
    branch = tree.branch()
    branch.rotate(mathutils.Quaternion((0.0, 0.0, 1.0), -self._angle))

class Up(node.Node):
  def __init__(self, angle):
    node.Node.__init__(self, "Up({})".format(angle))
    self._angle = angle

  def interpret(self, tree):
    branch = tree.branch()
    branch.rotate(mathutils.Quaternion((0.0, 1.0, 0.0), -self._angle))

class Down(node.Node):
  def __init__(self, angle):
    node.Node.__init__(self, "Down({})".format(angle))
    self._angle = angle

  def interpret(self, tree):
    branch = tree.branch()
    branch.rotate(mathutils.Quaternion((0.0, 1.0, 0.0), self._angle))

class RollLeft(node.Node):
  def __init__(self, angle):
    node.Node.__init__(self, "RollLeft({})".format(angle))
    self._angle = angle

  def interpret(self, tree):
    branch = tree.branch()
    branch.rotate(mathutils.Quaternion((1.0, 0.0, 0.0), -self._angle))

class RollRight(node.Node):
  def __init__(self, angle):
    node.Node.__init__(self, "RollRight({})".format(angle))
    self._angle = angle

  def interpret(self, tree):
    branch = tree.branch()
    branch.rotate(mathutils.Quaternion((1.0, 0.0, 0.0), self._angle))

class SetWidth(node.Node):
  def __init__(self, width):
    node.Node.__init__(self, "SetWidth({})".format(width))
    self._width = width

class IncColor(node.Node):
  def __init__(self):
    node.Node.__init__(self, "IncColor()")

class Forward(node.Node):
  def __init__(self, dst):
    node.Node.__init__(self, "Forward({})".format(dst))
    self._dst = dst

  def interpret(self, tree):
    branch = tree.branch()

    if branch.active_vert == None:
      branch.active_vert = tree.add_vert(branch.position)
    branch.position += branch.forward() * self._dst

    new_vert = tree.add_vert(branch.position)
    tree.add_edge(branch.active_vert, new_vert)
    branch.active_vert = new_vert

class MoveForward(node.Node):
  def __init__(self, dst):
    node.Node.__init__(self, "MoveForward({})".format(dst))
    self._dst = dst

  def interpret(self, tree):
    branch = tree.branch()
    branch.position += branch.forward() * self._dst
    branch.active_vert = None

