import bpy
src = "/home/seb/Downloads/2_Asset Library/Materials/RobotMaterials.blend"
with bpy.data.libraries.load(src, link=False) as (df, dt):
    mats = list(df.materials)
print("=== MATERIALS IN RobotMaterials.blend ===")
for m in sorted(mats):
    print("   ", m)
print("TOTAL:", len(mats))
