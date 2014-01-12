# #### BEGIN LICENSE BLOCK ####
#
# node.py - Part of Blender Plant Fractal Generator.
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

class Node:
  def __init__(self, name):
    self._name = name

  def __str__(self):
    return self._name

  def __radd__(self, other):
    if type(other) == list:
      return other + [self]
    else:
      return [other, self]

  def produce(self, tree):
    tree += self

  def interpret(self, tree):
    pass

