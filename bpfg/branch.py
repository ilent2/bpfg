# #### BEGIN LICENSE BLOCK ####
#
# branch.py - Part of Blender Plant Fractal Generator.
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

import mathutils

class Branch:
  def __init__(self, tree, depth):
    self._tree = tree
    self.depth = depth
    self.active_vert = None

    self.position = mathutils.Vector((0.0, 0.0, 0.0))
    self.rotation = mathutils.Quaternion((1.0, 0.0, 0.0, 0.0))

  def copy(self):
    branch = Branch(self._tree, self.depth)
    branch.position += self.position
    branch.rotation *= self.rotation
    branch.active_vert = self.active_vert
    return branch

  def forward(self):
    return self.rotation * mathutils.Vector((1.0, 0.0, 0.0))

  def left(self):
    return self.rotation * mathutils.Vector((0.0, 1.0, 0.0))

  def up(self):
    return self.rotation * mathutils.Vector((0.0, 0.0, 1.0))

