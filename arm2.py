import bpy

context = bpy.context
scene = context.scene
my_shading = 'WIREFRAME'  # 'WIREFRAME' 'SOLID' 'MATERIAL' 'RENDERED'
my_solid = 'SOLID'  # 'WIREFRAME' 'SOLID' 'MATERIAL' 'RENDERED'

def wideframe():
    my_areas = bpy.context.workspace.screens[0].areas
    for area in my_areas:
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.shading.type = my_shading
def solid():
    my_areas = bpy.context.workspace.screens[0].areas
    for area in my_areas:
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.shading.type = my_solid

def delete_scene():
    # DELETE ALL PREVIOUS OBJECTS
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)

def fore_arm(name):
    # MAIN ARM
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    arm = context.active_object
    context.object.scale[1] = 0.5
    context.object.scale[0] = 0.2
    context.object.scale[2] = 0.15

    # ELBOW_BASE
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    elbow_base = context.active_object
    context.object.scale[0] = 0.5
    context.object.scale[2] = 0.15
    context.object.scale[1] = 0.34
    context.object.location[1] = 0.42



    # ELBOW ROT
    bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, location=(0, 0, 0))
    elbow_rot = context.active_object
    context.object.rotation_euler[1] = 1.5708
    context.object.scale[0] = 0.15
    context.object.scale[1] = 0.15
    context.object.scale[2] = 0.5
    context.object.location[1] = 0.76

    arm.select_set(True)
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

    objectToSelect = bpy.data.objects["Cylinder.001"]
    objectToSelect.select_set(True)
    bpy.context.view_layer.objects.active = objectToSelect

    bpy.ops.object.editmode_toggle()
#    wideframe()
    bpy.ops.mesh.bevel(offset=0.0970081, offset_pct=0, segments=29, vertex_only=False)
#    solid()
    bpy.ops.object.editmode_toggle()


    for obj in bpy.context.selected_objects:
        obj.name = name

    return context.active_object






#############################
#           MAIN            #
#############################

delete_scene()


fore_arm1 = fore_arm("Left")
#context.object.location[1] = 0.8

bpy.ops.transform.translate(value=(1.36147, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

fore_arm2 = fore_arm("Right")
