import math

import bpy
from mathutils import Vector


def create_view_frustum(
    viewpoint,
    target,
    h_fov_deg=20,
    v_fov_deg=10,
    near=0.5,
    name="ViewFrustum",
    col=bpy.context.scene.collection,
):

    view_pos = viewpoint.matrix_world.translation
    target_pos = target.matrix_world.translation

    direction = target_pos - view_pos
    far = direction.length * 1.2

    if far <= near:
        raise ValueError("Target is too close.")

    forward = direction.normalized()

    world_up = Vector((0, 0, 1))

    # Handle looking straight up/down
    if abs(forward.dot(world_up)) > 0.999:
        world_up = Vector((0, 1, 0))

    right = forward.cross(world_up).normalized()
    up = right.cross(forward).normalized()

    h_fov = math.radians(h_fov_deg)
    v_fov = math.radians(v_fov_deg)

    near_w = 2 * near * math.tan(h_fov / 2)
    near_h = 2 * near * math.tan(v_fov / 2)

    far_w = 2 * far * math.tan(h_fov / 2)
    far_h = 2 * far * math.tan(v_fov / 2)

    nc = view_pos + forward * near
    fc = view_pos + forward * far

    # Near plane
    ntl = nc + up * near_h / 2 - right * near_w / 2
    ntr = nc + up * near_h / 2 + right * near_w / 2
    nbr = nc - up * near_h / 2 + right * near_w / 2
    nbl = nc - up * near_h / 2 - right * near_w / 2

    # Far plane
    ftl = fc + up * far_h / 2 - right * far_w / 2
    ftr = fc + up * far_h / 2 + right * far_w / 2
    fbr = fc - up * far_h / 2 + right * far_w / 2
    fbl = fc - up * far_h / 2 - right * far_w / 2

    verts = [ntl, ntr, nbr, nbl, ftl, ftr, fbr, fbl]

    faces = [
        [0, 1, 2, 3],  # near
        [4, 5, 6, 7],  # far
        [0, 1, 5, 4],  # top
        [1, 2, 6, 5],  # right
        [2, 3, 7, 6],  # bottom
        [3, 0, 4, 7],  # left
    ]

    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, [], faces)
    mesh.update()

    obj = bpy.data.objects.new(name, mesh)
    col.objects.link(obj)

    return obj


col = bpy.data.collections.get("Viewboxes")

if col is None:
    col = bpy.data.collections.new("Viewboxes")
    bpy.context.scene.collection.children.link(col)

for obj in list(col.objects):
    bpy.data.objects.remove(obj, do_unlink=True)

vp = bpy.data.collections["Viewpoints"].objects
tg = bpy.data.collections["Targets"].objects

for v in vp:
    for t in tg:
        create_view_frustum(v, t, 20, 10, 0.5, f"{v.name}_to_{t.name}", col)
