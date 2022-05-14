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

    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0


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

    objectToSelect = bpy.data.objects["Cylinder"]
    objectToSelect.select_set(True)
    bpy.context.view_layer.objects.active = objectToSelect



    for obj in bpy.context.selected_objects:
        obj.name = name

    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0

    return context.active_object


def shoulder(name, flip):

    bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    right_shoulder = context.active_object
    bpy.context.object.scale[0] = 0.48
    bpy.context.object.scale[1] = 0.48
    bpy.context.object.scale[2] = 0.13
    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 2.0171
    bpy.context.object.location[2] = 0

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.bevel(offset=0.172636, offset_pct=0, segments=12, vertex_only=False)
    bpy.ops.object.editmode_toggle()



    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    right_cut1 = context.active_object
    bpy.context.object.scale[0] = 0.44
    bpy.context.object.scale[1] = 0.44
    bpy.context.object.scale[2] = 0.11
    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 2.0171
    bpy.context.object.location[2] = 0

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.bevel(offset=0.172636, offset_pct=0, segments=12, vertex_only=False)
    bpy.ops.object.editmode_toggle()


    shoulder = scene.objects.get("Cylinder")
    cut = scene.objects.get("Cylinder.001")


    if cut and shoulder:
        bool = shoulder.modifiers.new(name='booly', type='BOOLEAN')
        bool.object = cut
        bool.operation = 'DIFFERENCE'
        bpy.ops.object.modifier_apply(
                {"object": shoulder},
                apply_as='DATA',
                modifier=bool.name)

    # UNSELECT
    context.active_object.select_set(False)
    for obj in context.selected_objects:
        context.view_layer.objects.active = obj

    cut.select_set(True)
    bpy.ops.object.delete(use_global=False, confirm=False)


    bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    right_cut2 = context.active_object
    bpy.context.object.scale[0] = 0.32
    bpy.context.object.scale[1] = 0.32
    bpy.context.object.scale[2] = 0.3
    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 2.0171
    bpy.context.object.location[2] = 0.21

    shoulder = scene.objects.get("Cylinder")
    cut = scene.objects.get("Cylinder.001")


    if cut and shoulder:
        bool = shoulder.modifiers.new(name='booly', type='BOOLEAN')
        bool.object = cut
        bool.operation = 'DIFFERENCE'
        bpy.ops.object.modifier_apply(
                {"object": shoulder},
                apply_as='DATA',
                modifier=bool.name)

    # UNSELECT
    context.active_object.select_set(False)
    for obj in context.selected_objects:
        context.view_layer.objects.active = obj

    cut.select_set(True)
    bpy.ops.object.delete(use_global=False, confirm=False)


    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    right_cut3 = context.active_object
    bpy.context.object.rotation_euler[2] = 0.959931
    bpy.context.object.location[1] = 1.05713
    bpy.context.object.location[2] = 0.929515

    shoulder = scene.objects.get("Cylinder")
    cut = scene.objects.get("Cube")

    if cut and shoulder:
        bool = shoulder.modifiers.new(name='booly', type='BOOLEAN')
        bool.object = cut
        bool.operation = 'DIFFERENCE'
        bpy.ops.object.modifier_apply(
                {"object": shoulder},
                apply_as='DATA',
                modifier=bool.name)

    # UNSELECT
    context.active_object.select_set(False)
    for obj in context.selected_objects:
        context.view_layer.objects.active = obj

    cut.select_set(True)
    bpy.ops.object.delete(use_global=False, confirm=False)


    objectToSelect = bpy.data.objects["Cylinder"]
    objectToSelect.select_set(True)
    bpy.context.view_layer.objects.active = objectToSelect



    for obj in bpy.context.selected_objects:
        obj.name = name

    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0

    if(flip):
        bpy.ops.transform.resize(value=(-1, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    return context.active_object

def base():
    right_shoulder = shoulder("R_shoulder", False)
    context.object.location[0] = -3
    left_shoulder =  shoulder("L_shoulder", True)

    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(0, 0, 0))
    front_base = context.active_object
    bpy.context.object.scale[0] = 2
    bpy.context.object.scale[1] = 0.84
    bpy.context.object.scale[2] = 0.012
    bpy.context.object.location[0] = -1.5
    bpy.context.object.location[2] = -0.11



    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(0, 0, 0))
    body = context.active_object
    bpy.context.object.scale[0] = 2
    bpy.context.object.scale[1] = 3.52
    bpy.context.object.scale[2] = 0.012
    bpy.context.object.location[0] = 0.08
    bpy.context.object.location[1] = -1


    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    body_cut = context.active_object
    bpy.context.object.scale[0] = 2.54
    bpy.context.object.scale[1] = 2.06
    bpy.context.object.scale[2] = 1.74
    bpy.context.object.location[1] = -3.0811

    body_obj = scene.objects.get("Cylinder.001")
    body_cut = scene.objects.get("Cube")

    if body_cut and body_obj:
        bool = body_obj.modifiers.new(name='booly', type='BOOLEAN')
        bool.object = body_cut
        bool.operation = 'DIFFERENCE'
        bpy.ops.object.modifier_apply(
                {"object": body_obj},
                apply_as='DATA',
                modifier=bool.name)

    # UNSELECT
    context.active_object.select_set(False)
    for obj in context.selected_objects:
        context.view_layer.objects.active = obj

    body_cut.select_set(True)
    bpy.ops.object.delete(use_global=False, confirm=False)


    objectToSelect = bpy.data.objects["Cylinder.001"]
    objectToSelect.select_set(True)
    bpy.context.view_layer.objects.active = objectToSelect
    bpy.context.object.location[0] = -1.5
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = -0.11


    front_base.select_set(True)
    right_shoulder.select_set(True)
    left_shoulder.select_set(True)
    body.select_set(True)

    bpy.ops.object.join()


    for obj in bpy.context.selected_objects:
        obj.name = "base"

    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0





    return context.active_object

def shell():
    bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, location=(0, 0, 0))
    front = context.active_object
    bpy.context.object.scale[0] = 2.
    bpy.context.object.scale[1] = 1.12
    bpy.context.object.scale[2] = 1.2
    bpy.context.object.location[0] = 0.08
    bpy.context.object.location[1] = -1


    bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, location=(0, 0, 0))
    body = context.active_object
    bpy.context.object.scale[0] = 1
    bpy.context.object.scale[1] = 3.25
    bpy.context.object.scale[2] = 1.2
    bpy.context.object.location[0] = 0.08
    bpy.context.object.location[1] = -1


    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    body_cut = context.active_object
    bpy.context.object.scale[0] = 2.54
    bpy.context.object.scale[1] = 2.06
    bpy.context.object.scale[2] = 1.74
    bpy.context.object.location[1] = -3.0811

    body_obj = scene.objects.get("Sphere.001")
    body_cut = scene.objects.get("Cube")

    if body_cut and body_obj:
        bool = body_obj.modifiers.new(name='booly', type='BOOLEAN')
        bool.object = body_cut
        bool.operation = 'DIFFERENCE'
        bpy.ops.object.modifier_apply(
                {"object": body_obj},
                apply_as='DATA',
                modifier=bool.name)

    # UNSELECT
    context.active_object.select_set(False)
    for obj in context.selected_objects:
        context.view_layer.objects.active = obj

    body_cut.select_set(True)
    bpy.ops.object.delete(use_global=False, confirm=False)

    objectToSelect = bpy.data.objects["Sphere.001"]
    objectToSelect.select_set(True)
    bpy.context.view_layer.objects.active = objectToSelect

    bpy.context.object.scale[0] = 2.

    front.select_set(True)
    bpy.ops.object.join()


    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    bottom_cut = context.active_object
    bpy.context.object.scale[0] = 2.21
    bpy.context.object.location[2] = -1.0125
    bpy.context.object.scale[1] = 2.53


    body_obj = scene.objects.get("Sphere.001")
    body_cut = scene.objects.get("Cube")

    if body_cut and body_obj:
        bool = body_obj.modifiers.new(name='booly', type='BOOLEAN')
        bool.object = body_cut
        bool.operation = 'DIFFERENCE'
        bpy.ops.object.modifier_apply(
                {"object": body_obj},
                apply_as='DATA',
                modifier=bool.name)

    # UNSELECT
    context.active_object.select_set(False)
    for obj in context.selected_objects:
        context.view_layer.objects.active = obj

    body_cut.select_set(True)
    bpy.ops.object.delete(use_global=False, confirm=False)





    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    right_leg_cut = context.active_object
    bpy.context.object.scale[0] = 0.5
    bpy.context.object.scale[1] = 0.5
    bpy.context.object.scale[2] = 0.62
    bpy.context.object.location[0] = -1.6729
    bpy.context.object.location[1] = -1.5

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.bevel(offset=0.305771, offset_pct=0, segments=11, vertex_only=False)
    bpy.ops.object.editmode_toggle()


    body_obj = scene.objects.get("Sphere.001")
    body_cut = scene.objects.get("Cube")

    if body_cut and body_obj:
        bool = body_obj.modifiers.new(name='booly', type='BOOLEAN')
        bool.object = body_cut
        bool.operation = 'DIFFERENCE'
        bpy.ops.object.modifier_apply(
                {"object": body_obj},
                apply_as='DATA',
                modifier=bool.name)

    # UNSELECT
    context.active_object.select_set(False)
    for obj in context.selected_objects:
        context.view_layer.objects.active = obj

    body_cut.select_set(True)
    bpy.ops.object.delete(use_global=False, confirm=False)





    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    left_leg_cut = context.active_object
    bpy.context.object.scale[0] = 0.5
    bpy.context.object.scale[1] = 0.5
    bpy.context.object.scale[2] = 0.62
    bpy.context.object.location[0] = 1.7729
    bpy.context.object.location[1] = -1.5

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.bevel(offset=0.305771, offset_pct=0, segments=11, vertex_only=False)
    bpy.ops.object.editmode_toggle()


    body_obj = scene.objects.get("Sphere.001")
    body_cut = scene.objects.get("Cube")

    if body_cut and body_obj:
        bool = body_obj.modifiers.new(name='booly', type='BOOLEAN')
        bool.object = body_cut
        bool.operation = 'DIFFERENCE'
        bpy.ops.object.modifier_apply(
                {"object": body_obj},
                apply_as='DATA',
                modifier=bool.name)

    # UNSELECT
    context.active_object.select_set(False)
    for obj in context.selected_objects:
        context.view_layer.objects.active = obj

    body_cut.select_set(True)
    bpy.ops.object.delete(use_global=False, confirm=False)

    # EYES
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(0, 0, 0))
    right_leg_cut = context.active_object
    bpy.context.object.scale[0] = 0.17
    bpy.context.object.scale[1] = 0.17
    bpy.context.object.scale[2] = 0.23
    bpy.context.object.location[0] = -0.21075
    bpy.context.object.location[1] = -2.0
    bpy.context.object.location[2] = 0.63
    bpy.context.object.rotation_euler[0] = 1.5708



    body_obj = scene.objects.get("Sphere.001")
    body_cut = scene.objects.get("Cylinder")

    if body_cut and body_obj:
        bool = body_obj.modifiers.new(name='booly', type='BOOLEAN')
        bool.object = body_cut
        bool.operation = 'DIFFERENCE'
        bpy.ops.object.modifier_apply(
                {"object": body_obj},
                apply_as='DATA',
                modifier=bool.name)

    # UNSELECT
    context.active_object.select_set(False)
    for obj in context.selected_objects:
        context.view_layer.objects.active = obj

    body_cut.select_set(True)
    bpy.ops.object.delete(use_global=False, confirm=False)



    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(0, 0, 0))
    left_leg_cut = context.active_object
    bpy.context.object.scale[0] = 0.17
    bpy.context.object.scale[1] = 0.17
    bpy.context.object.scale[2] = 0.23
    bpy.context.object.location[0] = 0.360
    bpy.context.object.location[1] = -2.0
    bpy.context.object.location[2] = 0.63
    bpy.context.object.rotation_euler[0] = 1.5708



    body_obj = scene.objects.get("Sphere.001")
    body_cut = scene.objects.get("Cylinder")

    if body_cut and body_obj:
        bool = body_obj.modifiers.new(name='booly', type='BOOLEAN')
        bool.object = body_cut
        bool.operation = 'DIFFERENCE'
        bpy.ops.object.modifier_apply(
                {"object": body_obj},
                apply_as='DATA',
                modifier=bool.name)

    # UNSELECT
    context.active_object.select_set(False)
    for obj in context.selected_objects:
        context.view_layer.objects.active = obj

    body_cut.select_set(True)
    bpy.ops.object.delete(use_global=False, confirm=False)


    objectToSelect = bpy.data.objects["Sphere.001"]
    objectToSelect.select_set(True)
    bpy.context.view_layer.objects.active = objectToSelect

    for obj in bpy.context.selected_objects:
        obj.name = "shell"

    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0.27787
    bpy.context.object.location[2] = 0

    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, location=(0, 0, 0))
    bpy.context.object.location[1] = 0.25
    bpy.context.object.scale[0] = 1.99
    bpy.context.object.scale[1] = 0.58
    bpy.context.object.scale[2] = 1.18

    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(0, 0, 0))
    bpy.context.object.location[2] = -1
    bpy.context.object.scale[0] = 2.02

    body_obj = scene.objects.get("Sphere")
    body_cut = scene.objects.get("Cube")

    if body_cut and body_obj:
        bool = body_obj.modifiers.new(name='booly', type='BOOLEAN')
        bool.object = body_cut
        bool.operation = 'DIFFERENCE'
        bpy.ops.object.modifier_apply(
                {"object": body_obj},
                apply_as='DATA',
                modifier=bool.name)

    # UNSELECT
    context.active_object.select_set(False)
    for obj in context.selected_objects:
        context.view_layer.objects.active = obj

    body_cut.select_set(True)
    bpy.ops.object.delete(use_global=False, confirm=False)




    body_obj = scene.objects.get("shell")
    body_cut = scene.objects.get("Sphere")

    if body_cut and body_obj:
        bool = body_obj.modifiers.new(name='booly', type='BOOLEAN')
        bool.object = body_cut
        bool.operation = 'DIFFERENCE'
        bpy.ops.object.modifier_apply(
                {"object": body_obj},
                apply_as='DATA',
                modifier=bool.name)

    body_cut.select_set(True)
    bpy.ops.object.delete(use_global=False, confirm=False)

#############################
#           MAIN            #
#############################

delete_scene()


#arm1 = arm("Left_arm")
#bpy.context.object.location[0] = 0
#bpy.context.object.location[1] = -0.1
#bpy.context.object.location[2] = 0
#bpy.context.object.rotation_euler[1] = 1.5708

#forearm1 = forearm("Left_forearm")
#bpy.context.object.location[0] = 0
#bpy.context.object.location[1] = 1.23
#bpy.context.object.location[2] = -0.1
#context.object.location[1] = 0.8
base()
shell()
#bpy.ops.transform.translate(value=(1.36147, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

#arm = arm("Right")
