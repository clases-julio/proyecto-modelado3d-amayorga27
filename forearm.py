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

def arm(name):
    # MAIN ARM
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    arm = context.active_object
    context.object.scale[0] = 0.2
    context.object.scale[1] = 0.5
    context.object.scale[2] = 0.15
    bpy.ops.object.editmode_toggle()
#    wideframe()
    bpy.ops.mesh.bevel(offset=0.0970081, offset_pct=0, segments=29, vertex_only=False)
#    solid()
    bpy.ops.object.editmode_toggle()

    # ELBOW_BASE
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    elbow_base = context.active_object
    context.object.scale[0] = 0.4
    context.object.scale[1] = 0.25
    context.object.scale[2] = 0.15
    context.object.location[1] = 0.42
    bpy.ops.object.editmode_toggle()
#    wideframe()
    bpy.ops.mesh.bevel(offset=0.0970081, offset_pct=0, segments=29, vertex_only=False)
#    solid()
    bpy.ops.object.editmode_toggle()



    # ELBOW ROT
    bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, location=(0, 0, 0))
    elbow_rot = context.active_object
    context.object.rotation_euler[1] = 1.5708
    context.object.scale[0] = 0.15
    context.object.scale[1] = 0.15
    context.object.scale[2] = 0.4
    context.object.location[1] = 0.67
    bpy.ops.object.editmode_toggle()
#    wideframe()
    bpy.ops.mesh.bevel(offset=0.0970081, offset_pct=0, segments=29, vertex_only=False)
#    solid()
    bpy.ops.object.editmode_toggle()

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
    context.object.scale[0] = 0.3
    context.object.scale[1] = 0.4
    context.object.scale[2] = 0.2


    fore_arm = scene.objects.get("Cylinder")
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

    objectToSelect = bpy.data.objects["Cylinder"]
    objectToSelect.select_set(True)
    bpy.context.view_layer.objects.active = objectToSelect



    for obj in bpy.context.selected_objects:
        obj.name = name

    return context.active_object


def forearm(name):
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    end = context.active_object
    bpy.context.object.scale[0] = 0.3
    bpy.context.object.scale[1] = 0.46
    bpy.context.object.scale[2] = 0.22
    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0.987126
    bpy.context.object.location[2] = 0

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.bevel(offset=0.172636, offset_pct=0, segments=12, vertex_only=False)
    bpy.ops.object.editmode_toggle()


    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    middle = context.active_object
    bpy.context.object.scale[0] = 0.23
    bpy.context.object.scale[1] = 0.31
    bpy.context.object.scale[2] = 0.11
    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 1.5571
    bpy.context.object.location[2] = -0.11048

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.bevel(offset=0.172636, offset_pct=0, segments=12, vertex_only=False)
    bpy.ops.object.editmode_toggle()


    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    base = context.active_object
    bpy.context.object.scale[0] = 0.43
    bpy.context.object.scale[1] = 0.43
    bpy.context.object.scale[2] = 0.11
    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 2.0171
    bpy.context.object.location[2] = -0.11048

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.bevel(offset=0.172636, offset_pct=0, segments=12, vertex_only=False)
    bpy.ops.object.editmode_toggle()


    end.select_set(True)
    middle.select_set(True)

    bpy.ops.object.join()







#############################
#           MAIN            #
#############################

delete_scene()


arm1 = arm("Left_arm")
forearm1 = forearm("Left_forearm")
#context.object.location[1] = 0.8

#bpy.ops.transform.translate(value=(1.36147, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

#arm = arm("Right")
