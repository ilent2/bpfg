import bpy

from bpfg.lsystem import LSystem
from bpfg.node import Node
from bpfg.builtin import SB, EB, Left, Right, Forward
import math

class ExampleLSystem(LSystem):
  """ Example LSystem (This is just the fractal fern example). """
  class A(Node):
    def __init__(self, v, bpfg):
      Node.__init__(self, "A({})".format(v))
      self._v = v
      self._bpfg = bpfg

    def produce(self, tree):
      bpfg = self._bpfg

      if self._v < bpfg.d:
        tree += ExampleLSystem.A(self._v + 1, bpfg)
      elif self._v == bpfg.d:
        tree += ExampleLSystem.I(1, bpfg)
        tree += SB() + Right(bpfg.angle)
        tree += ExampleLSystem.A(0, bpfg) + EB()
        tree += SB() + Left(bpfg.angle)
        tree += ExampleLSystem.A(0, bpfg) + EB()
        tree += ExampleLSystem.I(1, bpfg)
        tree += ExampleLSystem.A(self._v, bpfg)

    def interpret(self, tree):
      tree += Forward(0.025*self._v)

  class I(Node):
    def __init__(self, x, bpfg):
      Node.__init__(self, "I({})".format(x))
      self._x = x
      self._bpfg = bpfg

    def produce(self, tree):
      tree += ExampleLSystem.I(self._bpfg.r*self._x, self._bpfg)

    def interpret(self, tree):
      tree += Forward(0.025*self._x)

  def __init__(self, mesh):
    LSystem.__init__(self)

    bpfg = mesh.bpfg_example
    self += ExampleLSystem.A(1.0, bpfg)
    self.evolve(bpfg.depth)
    self.create_object(mesh)

def update_func(self, context):
  """ Update the LSystem

  At the moment this just replaces the old one, this is really
  bad but until we store the LSystem internally or find another
  option, this quick and dirty solution works.
  """
  ExampleLSystem(context.active_object.data)

class Settings(bpy.types.PropertyGroup):
  is_example = bpy.props.BoolProperty(default=False,
      description="True if the mesh is of the Example LSystem type")
  depth = bpy.props.IntProperty(name="Derivation Depth",
      description="How many times to evolve the LSystem",
      subtype='UNSIGNED', update=update_func, default=18)

  angle = bpy.props.FloatProperty(name="Angle",
      description="LSystem example parameter",
      subtype='ANGLE', update=update_func, default=math.radians(45.0))
  d = bpy.props.IntProperty(name="D",
      description="LSystem example parameter",
      subtype='UNSIGNED', update=update_func, default=3)
  r = bpy.props.FloatProperty(name = "R",
      description="LSystem example parameter",
      update=update_func, default=1.28)

class AddObject(bpy.types.Operator):
  """ Defines an operator to add this LSystem to the scene. """
  bl_idname = "bpfg.example_operator"
  bl_label = "Add Example LSystem"

  def execute(self, context):
    bpy.ops.object.add(type='MESH')
    obj = bpy.context.active_object
    obj.data.bpfg_example.is_example = True
    ExampleLSystem(obj.data)
    return {'FINISHED'}

class ControlPanel(bpy.types.Panel):
  """ Defines a panel for controlling LSystem properties. """
  bl_idname = "BPFG_PT_example_panel"
  bl_label = "Example LSystem"
  bl_space_type = 'PROPERTIES'
  bl_region_type = 'WINDOW'
  bl_context = "data"

  @classmethod
  def poll(cls, context):
    return (context.active_object is not None
        and context.active_object.type == 'MESH'
        and context.active_object.data.bpfg_example.is_example)

  def draw(self, context):
    layout = self.layout
    props = context.active_object.data.bpfg_example

    layout.prop(props, "depth")
    layout.prop(props, "angle")
    layout.prop(props, "d")
    layout.prop(props, "r")

def menu_func(self, context):
  self.layout.operator(AddObject.bl_idname, icon='PLUGIN')

def register():
  bpy.utils.register_class(Settings)
  bpy.utils.register_class(AddObject)
  bpy.utils.register_class(ControlPanel)

  bpy.types.INFO_MT_mesh_add.append(menu_func)
  bpy.types.Mesh.bpfg_example = bpy.props.PointerProperty(type=Settings)

def unregister():
  bpy.utils.unregister_class(Settings)
  bpy.utils.unregister_class(AddObject)
  bpy.utils.unregister_class(ControlPanel)

  bpy.types.INFO_MT_mesh_add.remove(menu_func)
  del bpy.types.Mesh.bpfg_example

if __name__ == "__main__":
  register()

