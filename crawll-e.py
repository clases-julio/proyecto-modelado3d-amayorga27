import bpy

separated = True
context = bpy.context
scene = context.scene

def delete_scene():
  # Borra los objetos que haya en la escena y los materiales
  bpy.ops.object.select_all(action='SELECT')
  bpy.ops.object.delete(use_global=False, confirm=False)
  for m in bpy.data.materials:
      bpy.data.materials.remove(m)

def scale(v):
    # Escala el objeto con los datos del vector dado
    context.object.scale[0] = v[0]
    context.object.scale[1] = v[1]
    context.object.scale[2] = v[2]

def locate(v):
    # Mueve el objeto con los datos del vector dado
    context.object.location[0] = v[0]
    context.object.location[1] = v[1]
    context.object.location[2] = v[2]

def rotate(v):
    # Rota el objeto con los datos del vector dado
    context.object.rotation_euler[0] = v[0]
    context.object.rotation_euler[1] = v[1]
    context.object.rotation_euler[2] = v[2]

def smooth(smooth_offset, smooth_segments):
    # Suaviza el objeto con la informacion dada
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.bevel(offset=smooth_offset, offset_pct=0, segments=smooth_segments, vertex_only=False)
    bpy.ops.object.editmode_toggle()


def difference(body_obj_name, body_cut_name):
    # Realiza la operacion diferencia entre dos objetos dados (el primero menos el segundo)
    body_obj = scene.objects.get(body_obj_name)
    body_cut = scene.objects.get(body_cut_name)

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

def deselect():
    # Deseleccionamos todo
    bpy.ops.object.select_all(action='DESELECT') 


def set_scene():
    # Preparamos la escena, luz y camara, con dos opciones de camara
    bpy.ops.object.light_add(type='POINT', location=(1.18, -4.18, 2.92))
    context.object.data.energy = 600
    if not separated:
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(6.5818, -5.7146, 2.54), rotation=(1.33705, 0, 0.83348))
    else:
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(8.7953, -8.6922, 3.3955), rotation=(1.346, 0, 0.861409))







def arm(name):
    #
    # Genera la pieza de la mano
    #
    
    # Punta de la mano
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    arm = context.active_object
    scale((0.2, 0.5, 0.15))
    smooth(0.0970081, 29)

    # Pieza que agarra al antebrazo
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    elbow_base = context.active_object
    scale((0.4, 0.25, 0.15))
    locate((0, 0.42, 0))
    smooth(0.0970081, 29)



    # Cilindro para hacer suave el borde de la pieza
    bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, location=(0, 0, 0))
    elbow_rot = context.active_object
    rotate((0, 1.5708, 0))
    scale((0.15, 0.15, 0.4))
    locate((0, 0.67, 0))
    smooth(0.0970081, 29)

    arm.select_set(True)
    elbow_base.select_set(True)
    # Los juntamos en una unica pieza
    bpy.ops.object.join()

    # Hueco para introducir el antebrazo
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    cut_obj = context.active_object
    locate((0, 0.66, 0))
    scale((0.3, 0.4, 0.2))

    difference("Cylinder", "Cube")

    objectToSelect = bpy.data.objects["Cylinder"]
    objectToSelect.select_set(True)
    context.view_layer.objects.active = objectToSelect



    for obj in context.selected_objects:
        obj.name = name     # Lo llamamos con el nombre que se le pase (Para diferenciar de lados)

    # Por ultimo lo posicionamos en el (0,0,0)
    locate((0, 0, 0))


    return context.active_object



def forearm(name):
    #
    # Genera la pieza del antebrazo
    #

    # Pieza del codo
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    end = context.active_object
    scale((0.3, 0.46, 0.22))
    locate((0, 0.987126, 0))
    smooth(0.172636, 12)


    # Pieza que une el codo y el hombro
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    middle = context.active_object
    scale((0.23, 0.31, 0.11))
    locate((0, 1.5571, -0.11048))
    smooth(0.172636, 12)

    # Pieza del hombro
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    base = context.active_object
    scale((0.43, 0.43, 0.11))
    locate((0, 2.0171, -0.11048))
    smooth(0.172636, 12)


    end.select_set(True)
    middle.select_set(True)
    # Las juntamos
    bpy.ops.object.join()

    objectToSelect = bpy.data.objects["Cylinder"]
    objectToSelect.select_set(True)
    context.view_layer.objects.active = objectToSelect



    for obj in context.selected_objects:
        obj.name = name     # Lo llamamos con el nombre que se le pase

    # Y lo colocamos en el (0,0,0)
    locate((0, 0, 0))

    return context.active_object


def shoulder(name, flip):
    #
    # Devuelve una subpieza que agarra el hombro a la base
    #

    # Esta pieza sera la principal, que sera algo mayor que el hombro, para que al cortarle las dimensiones del hombro, encajen
    bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    shoulder = context.active_object
    scale((0.48, 0.48, 0.13))
    locate((0, 2.0171, 0))
    smooth(0.172636, 12)

    # Primer corte que compone el hueco interior
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    cut1 = context.active_object
    scale((0.44, 0.44, 0.11))
    locate((0, 2.0171, 0))
    smooth(0.172636, 12)

    difference("Cylinder", "Cylinder.001")


    # Segundo corte que deja el borde circular superior
    bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    cut2 = context.active_object
    scale((0.32, 0.32, 0.3))
    locate((0, 2.0171, 0))


    difference("Cylinder", "Cylinder.001")


    # Con el tercer corte se secciona solo un arco del borde superior
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(-0.475012, -0.832874, 0.269516))
    cut3 = context.active_object
    rotate((0, 0, 0.959931))
    locate((0, 1.05713, 0.929515))

    difference("Cylinder", "Cube")


    objectToSelect = bpy.data.objects["Cylinder"]
    objectToSelect.select_set(True)
    context.view_layer.objects.active = objectToSelect



    for obj in context.selected_objects:
        obj.name = name     # Se le asigna el nombre dado

    locate((0, 0, 0))

    if(flip):       # Si se le dio la condicion de voltear se voltea (para obtener los lados izq y der)
        bpy.ops.transform.resize(value=(-1, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    return context.active_object



def base():
    #
    # Devolvera la pieza de la base compuesta por la base, dos hombros y el soporte trasero
    #

    # Creamos y colocamos los hombros
    right_shoulder = shoulder("R_shoulder", False)
    locate((-3, 0, 0))
    left_shoulder =  shoulder("L_shoulder", True)

    # Creamos la primera parte de la base, la frontal
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(0, 0, 0))
    front_base = context.active_object
    scale((2, 0.84, 0.03))
    locate((-1.5, 0, -0.11))

    # Creamos el resto de la base
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(0, 0, 0))
    body = context.active_object
    scale((2, 3.52, 0.03))
    locate((0.08, -1, 0))

    # Este sera el cilindro que sostiene a la rueda loca trasera
    bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, location=(0, 0, 0))
    back_support = context.active_object
    scale((0.15, 0.15, 0.15))
    locate((-1.5, 2.65, -0.05))

    # Y esta seria la bola de la rueda loca
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, location=(0, 0, 0))
    back_ball = context.active_object
    scale((0.13, 0.13, 0.13))
    locate((-1.5, 2.65, -0.2))


    # Esto cortara en la mitad el cilindro usado para componer el cuerpo trasero
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    body_cut = context.active_object
    scale((2.54, 2.06, 1.74))
    locate((0, -3.0811, 0))

    difference("Cylinder.001", "Cube")


    # Lo recolocamos
    objectToSelect = bpy.data.objects["Cylinder.001"]
    objectToSelect.select_set(True)
    context.view_layer.objects.active = objectToSelect
    locate((-1.5, 0, -0.11))


    front_base.select_set(True)
    right_shoulder.select_set(True)
    left_shoulder.select_set(True)
    back_support.select_set(True)
    back_ball.select_set(True)
    body.select_set(True)

    bpy.ops.object.join()   # Y lo juntamos todo


    for obj in context.selected_objects:
        obj.name = "Base"

    # Devolviendolo al (0,0,0)
    locate((0, 0, 0))

    return context.active_object



def shell():
    #
    # Devuelve la pieza superior del robot
    #

    # Al igual que en la anterior se compone de una pieza frontal
    bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, location=(0, 0, 0))
    front = context.active_object
    scale((2, 1.12, 1.2))
    locate((0.08, -1, 0))

    # Y otra que compone el resto del cuerpo
    bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, location=(0, 0, 0))
    body = context.active_object
    scale((1, 3.25, 1.2))
    locate((0.08, -1, 0))

    # Que necesitara ser cortada a la mitad con este cubo
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    body_cut = context.active_object
    scale((2.54, 2.06, 1.74))
    locate((0, -3.0811, 0))

    difference("Sphere.001", "Cube")

    objectToSelect = bpy.data.objects["Sphere.001"]
    objectToSelect.select_set(True)
    context.view_layer.objects.active = objectToSelect

    context.object.scale[0] = 2.

    front.select_set(True)
    bpy.ops.object.join()

    # Con este smooth hariamos la pieza mas suave, pero da problemas con los ojos
#    bpy.ops.object.shade_smooth()

    # Pieza que cortara la parte inferior de la carcasa
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    bottom_cut = context.active_object
    
    context.object.scale[0] = 2.21
    context.object.location[2] = -1.0125
    context.object.scale[1] = 2.53

    difference("Sphere.001", "Cube")




    # Esta pieza cortara la carcasa para hacer hueco para la pata derecha
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    right_leg_cut = context.active_object
    scale((0.5, 0.5, 0.65))

    context.object.location[0] = -1.6729
    context.object.location[1] = -1.5

    smooth(0.305771, 11)

    difference("Sphere.001", "Cube")



    # E igual con la izquierda
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    left_leg_cut = context.active_object
    scale((0.5, 0.5, 0.62))
    locate((1.7729, -1.5, 0))

    smooth(0.305771, 11)

    difference("Sphere.001", "Cube")


    # OJOS

    # Este cilindro compone el ojo derecho
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(0, 0, 0))
    right_eye_cut = context.active_object
    scale((0.17, 0.17, 0.23))
    locate((-0.21075, -2.0, 0.63))
    rotate((1.5708, 0, 0))

    difference("Sphere.001", "Cylinder")


    # Y este el derecho
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(0, 0, 0))
    left_eye_cut = context.active_object
    scale((0.17, 0.17, 0.23))
    locate((0.36, -2, 0.63))
    rotate((1.5708, 0, 0))

    difference("Sphere.001", "Cylinder")


    objectToSelect = bpy.data.objects["Sphere.001"]
    objectToSelect.select_set(True)
    context.view_layer.objects.active = objectToSelect

    for obj in context.selected_objects:
        obj.name = "Shell"      # Seleccionamos la pieza principal y la llamamos "Shell"

    locate((0, 0.27787, 0))     # La recolocamos


    # Este ultimo corte es para hacer hueco en el interior del caparazon
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, location=(0, 0, 0))
    scale((1.99, 0.58, 1.18))
    locate((0, 0.25, 0))

    difference("Shell", "Sphere")

    objectToSelect = bpy.data.objects["Shell"]
    objectToSelect.select_set(True)
    context.view_layer.objects.active = objectToSelect

    locate((0, 0.28, 0))    # Finalmente recolocamos


def pupil():
    #
    # Esta pieza es simplemente para darle color a los ojos similar al ultrasonidos que tiene en la realidad
    #

    # Se compone de un cubo, redimensionado y coloreado
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(0, 0, 0))
    pupils = context.active_object
    scale((0.92, 0.001, 0.28))
    locate((-0.01, -0.495, 0.62))
    activeObject = context.active_object
    Pupilmat = bpy.data.materials.new("Pupil")
    activeObject.data.materials.append(Pupilmat)
    context.object.active_material.diffuse_color = (0.1, 0.1, 0.1, 1)
    for obj in context.selected_objects:
        obj.name = "Pupil"
    objectToSelect = bpy.data.objects["Pupil"]
    objectToSelect.select_set(True)
    context.view_layer.objects.active = objectToSelect


#############################
#           MAIN            #
#############################

# Borramos lo que habia anteriormente
delete_scene()


# Seleccionamos el modo que queremos
looking_up = True
separated = False


# Y vamos creando cada pieza, añadiendole la textura y posicionandola segun el modo

# Comenzamos por la base
base()
activeObject = context.active_object
Blackmat = bpy.data.materials.new("Black")
activeObject.data.materials.append(Blackmat)
context.object.active_material.diffuse_color = (0, 0, 0, 1)
if looking_up and not separated:
  rotate((-0.174533, 0, 0))
  locate((0, 0, 0.31183))
if separated and not looking_up:
  rotate((0, 0, 0))
  locate((0, 0, 0))

# La carcasa superior
shell()
activeObject = context.active_object
Whitemat = bpy.data.materials.new("White")
activeObject.data.materials.append(Whitemat)
context.object.active_material.diffuse_color = (0.9, 0.9, 0.9, 1)
if looking_up and not separated:
  rotate((-0.174533, 0, 0))
  locate((0, 0.28, 0.30209))
if separated and not looking_up:
  rotate((0, 0, 0))
  locate((-4.3457, 0.27919, 0))


# El antebrazo izquierdo
forearm1 = forearm("Left_forearm")
locate((1.5, 0, 0.11464))
rotate((0, 0, 0.293216))
activeObject = context.active_object
MidBmat = bpy.data.materials.new("MidBlack")
activeObject.data.materials.append(MidBmat)
context.object.active_material.diffuse_color = (0.03, 0.03, 0.03, 1)
context.object.active_material.metallic = 0
context.object.active_material.roughness = 1

if looking_up and not separated:
  rotate((-0.174533, 0, 0))
  locate((1.5, 0, 0.43182))
if separated and not looking_up:
  rotate((0, 0, 0))
  locate((1.5, -1.5, 0))


# El antebrazo derecho
forearm2 = forearm("Right_forearm")
locate((-1.5, 0, 0.11464))
rotate((0, 0, -0.293216))
activeObject = context.active_object
activeObject.data.materials.append(MidBmat)
context.object.active_material.metallic = 0
context.object.active_material.roughness = 1

if looking_up and not separated:
  rotate((-0.174533, 0, 0))
  locate((-1.5, 0, 0.43182))
if separated and not looking_up:
  rotate((0, 0, 0))
  locate((-1.5, -1.5, 0))


# La mano izquierda
arm1 = arm("Left_arm")
locate((1.878, -1.22, 0.18569))
rotate((1.54804, 0.439806, 1.84478))
activeObject = context.active_object
activeObject.data.materials.append(Blackmat)

if looking_up and not separated:
  rotate((1.57722, 0.404274, 1.60493))
  locate((1.5, -1.22, 0.81846))
if separated and not looking_up:
  rotate((0, 1.5708, 0))
  locate((1.5, -3.35, 0))


# La mano derecha
arm2 = arm("Right_arm")
locate((-1.878, -1.22, 0.18569))
rotate((1.65258, 0.410781, 1.35467))
activeObject = context.active_object
activeObject.data.materials.append(Blackmat)
if looking_up:
  rotate((1.58506, 0.41266, 1.59847))
  locate((-1.5, -1.22, 0.81846))
if separated and not looking_up:
  rotate((0, 1.5708, 0))
  locate((-1.5, -3.35, 0))

# Y por ultimo la pupila
pupil()
if looking_up and not separated:
  rotate((-0.174533, 0, 0))
  locate((0, -0.38, 1.07))
if separated and not looking_up:
  rotate((0, 0, 0))
  locate((-4.3457, -0.52081, 0.65))

# Luces, camara y accion!
set_scene()
