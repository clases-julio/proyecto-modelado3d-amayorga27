import bpy

context = bpy.context
scene = context.scene


# DELETE ALL PREVIOUS OBJECTS
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)


bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
tip = context.active_object
context.object.scale[1] = 0.5
context.object.scale[0] = 0.2
context.object.scale[2] = 0.15

bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
elbow_base = context.active_object
context.object.scale[0] = 0.5
context.object.scale[2] = 0.15
context.object.scale[1] = 0.34
context.object.location[1] = 0.42




bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, location=(0, 0, 0))
elbow_rot = context.active_object
context.object.rotation_euler[1] = 1.5708
context.object.scale[0] = 0.15
context.object.scale[1] = 0.15
context.object.scale[2] = 0.5
context.object.location[1] = 0.76

tip.select_set(True)
elbow_base.select_set(True)

bpy.ops.object.join()

# UNSELECT
#context.active_object.select_set(False)
#for obj in context.selected_objects:
#    context.view_layer.objects.active = obj

bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
cut_obj = context.active_object
context.object.location[1] = 0.66
context.object.scale[0] = 0.4
context.object.scale[1] = 0.45
context.object.scale[2] = 0.2


fore_arm = scene.objects.get("Cylinder.001")
cut = scene.objects.get("Cube")


if cut and fore_arm:
    bool = fore_arm.modifiers.new(name='booly', type='BOOLEAN')
    bool.object = cut
    bool.operation = 'DIFFERENCE'
    bpy.ops.object.modifier_apply(
            {"object": fore_arm},
            apply_as='DATA',
            modifier=bool.name)

# UNSELECT
context.active_object.select_set(False)
for obj in context.selected_objects:
    context.view_layer.objects.active = obj

cut_obj.select_set(True)
bpy.ops.object.delete(use_global=False, confirm=False)
