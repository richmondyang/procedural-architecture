import bpy


class Test(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "TESTUI"
    bl_label = "MONKEYS 2025"

    def draw(self, context: bpy.types.Context) -> None:
        layout = self.layout
        layout.use_property_split = True

        layout.operator("object.monkey_grid")

        object = context.object
        if not object:
            return
        layout.prop(object, "name")
        layout.prop(object, "parent")
        layout.prop(object, "color", text="Viewport Color")
