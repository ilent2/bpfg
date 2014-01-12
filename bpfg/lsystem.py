# #### BEGIN LICENSE BLOCK ####
#
# lsystem.py - Part of Blender Plant Fractal Generator.
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

from . import branch

import bpy
import bmesh


class LSystem:
  def __init__(self):
    self._buffer = []
    self._lsystem = []

    self._interpret_string = []

    self._branch_index = 0
    self._branch_depth = 0
    self._branches = [branch.Branch(self, self._branch_depth)]
    self._branches_depth = [self._branches[0]]

    self._bm = None

  def __iadd__(self, other):
    if type(other) == list:
      self._buffer.extend(other)
      return self
    else:
      self._buffer.append(other)
      return self

  def evolve(self, steps=1):
    # Add any nodes currently in the buffer
    if len(self._buffer) != 0:
      self._lsystem.extend(self._buffer)
      self._buffer = []

    for i in range(steps):
      self._branch_index = 0
      self._branch_depth = 0
      self._branches_depth = [self._branches[0]]

      j = 0
      while j < len(self._lsystem):
        # Evaluate object and pop
        self._lsystem[j].produce(self)
        self._lsystem.pop(j)

        # Insert buffered objects into L-System
        for k in self._buffer:
          self._lsystem.insert(j, k)
          j += 1
        self._buffer = []

  def interpret(self, max_depth=100, buff=None, record=False):
    if buff == None:
      self._buffer = []
      self._branch_index = 0
      self._branch_depth = 0
      self._branches_depth = [self._branches[0]]
      buff = self._lsystem

    if max_depth < 0:
      raise RuntimeError("Max interpretation depth exceeded!")

    for l in buff:
      l.interpret(self)
      if record: self._interpret_string += str(l)

      # Evaluate new buffered commands
      if len(self._buffer) != 0:
        temp_buff = self._buffer
        self._buffer = []
        self.interpret(max_depth-1, temp_buff, record)

  # TODO: Implement interpret without a bmesh
  def to_string(self, interpret=True):
    if interpret:
      return "Not Yet Implemented!!!"
      #interpret(record=True)
      #return self._interpret_string

    return ''.join(str(l) for l in self._lsystem)

  def create_object(self, mesh=None):
    # Create a new mesh object
    if mesh == None:
      bpy.ops.object.add(type='MESH')
      mesh = bpy.context.object.data

    # Create a BMesh representation
    self._bm = bmesh.new()
    self._bm.from_mesh(mesh)

    # Interpret the L-System
    self.interpret()

    # Clean up
    self._bm.to_mesh(mesh)
    self._bm.free()
    self._bm = None

  def branch(self):
    branch = self._branches[self._branch_index]
    if branch.depth != self._branch_depth:
      return self._branches_depth[-1]
    return branch

  def add_vert(self, vert):
    if self._bm != None: return self._bm.verts.new(vert)

  def add_edge(self, vert1, vert2):
    if self._bm != None: self._bm.edges.new((vert1, vert2))

