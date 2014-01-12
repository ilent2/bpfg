# #### BEGIN LICENSE BLOCK ####
#
# __init__.py - Part of Blender Plant Fractal Generator.
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

bl_info = {
  "name": "Blender Plant Fractal Generator",
  "description": "Python implementation of CPFG/LPFG for Blender",
  "author": "Isaac Lenton (aka ilent2)",
  "version": (0, 1),
  "blender": (2, 69, 0),
  "location": "Text Editor > Templates > BPFG Examples",
  "warning": "",
  "wiki_url": "",
  "tracker_url": "",
  "category": "Object"
}

__all__ = ["lsystem", "node", "builtin"]

import bpy
import os

class TEXT_MT_template_bpfg(bpy.types.Menu):
  bl_label = "BPFG Examples"

  def draw(self, context):
    self.path_menu([os.path.join(__path__[0], "examples")],
                   "text.open", {"internal": True})

def menu_func(self, context):
  self.layout.menu("TEXT_MT_template_bpfg")

def register():
  bpy.utils.register_module(__name__)
  bpy.types.TEXT_MT_templates.append(menu_func)

def unregister():
  bpy.utils.unregister_module(__name__)
  bpy.types.TEXT_MT_templates.remove(menu_func)

if __name__ == "__main__":
  register()

