BPFG
====

This is a prototype for a LPFG/CPFG inspired Plant Fractal Generator
for use with Blender.
Both the implementation and L-System specification will be implemented
(at this stage) entirely in Python.
For Vectors and Rotations, the Blender mathutils library is used.

For more information about the LPFG plant modelling language, see:

    http://algorithmicbotany.org/lstudio/LPFGman.pdf

BPFG is still in development, this version only provides one working
example which creates a very simple fractal fern mesh.
If you have any useful ideas for the development of this library,
don't hesitate to contribute.

Installation and Usage
----------------------

You must have a modern version of Blender installed.

To install this module in Blender, copy it to the Blender addons path.
For Linux based systems this is something like:

    /home/<username>/.config/blender/<version>/scripts/addons/

Start Blender and go to File -> User Preferences -> Addons -> User
and enable the BPFG addon.

In the Text Editor, there should now be a new submenu under the
Templates menu, select a test script and click Run Script.

