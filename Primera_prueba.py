import bpy

bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
tip = bpy.context.active_object
bpy.context.object.scale[1] = 0.5
bpy.context.object.scale[0] = 0.2
bpy.context.object.scale[2] = 0.15

bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
elbow_base = bpy.context.active_object
bpy.context.object.scale[0] = 0.5
bpy.context.object.scale[2] = 0.15
bpy.context.object.scale[1] = 0.34
bpy.context.object.location[1] = 0.42




bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, location=(0, 0, 0))
elbow_rot = bpy.context.active_object
bpy.context.object.rotation_euler[1] = 1.5708
bpy.context.object.scale[0] = 0.15
bpy.context.object.scale[1] = 0.15
bpy.context.object.scale[2] = 0.5
bpy.context.object.location[1] = 0.76

tip.select_set(True)
elbow_base.select_set(True)

bpy.ops.object.join()

# UNSELECT
#bpy.context.active_object.select_set(False)
#for obj in bpy.context.selected_objects:
#    bpy.context.view_layer.objects.active = obj

bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
bpy.context.object.location[1] = 0.66
bpy.context.object.scale[0] = 0.4
bpy.context.object.scale[1] = 0.45
bpy.context.object.scale[2] = 0.2
