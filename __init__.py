bl_info = {
    "name": "OrtogCompare",
    "author": "Cicero Moraes",
    "version": (1, 1, 1),
    "blender": (2, 75, 0),
    "location": "View3D",
    "description": "Planejamento de Cirurgia Ortognática no Blender",
    "warning": "",
    "wiki_url": "",
    "category": "Mesh",
    }

import bpy
import bmesh
import fnmatch
import csv
import tempfile
import subprocess
import math
import platform
import os
from math import sqrt
from mathutils import Matrix,Vector
from bpy_extras.object_utils import AddObjectHelper, object_data_add

from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )

def AdicionaEMPTYCompDef(Nome):

    bpy.ops.object.empty_add(type='PLAIN_AXES', radius=6, view_align=False)
    bpy.context.object.name = Nome
    bpy.context.object.show_name = True

# PONTOS REAIS

class AdicionaPnREAL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_pn_real"
    bl_label = "Add Pn REAL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Pn-REAL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Pn-REAL")
        return {'FINISHED'}

class AdicionaSnREAL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_sn_real"
    bl_label = "Add Sn REAL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Sn-REAL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Sn-REAL")
        return {'FINISHED'}

class AdicionaAREAL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_a_real"
    bl_label = "Add A REAL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'A-REAL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("A-REAL")
        return {'FINISHED'}

class AdicionaLsREAL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_ls_real"
    bl_label = "Add Ls REAL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Ls-REAL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Ls-REAL")
        return {'FINISHED'}

class AdicionaStREAL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_st_real"
    bl_label = "Add St REAL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'St-REAL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("St-REAL")
        return {'FINISHED'}

class AdicionaLiREAL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_li_real"
    bl_label = "Add Li REAL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Li-REAL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Li-REAL")
        return {'FINISHED'}

class AdicionaBREAL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_b_real"
    bl_label = "Add B REAL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'B-REAL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("B-REAL")
        return {'FINISHED'}

class AdicionaPogREAL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_pog_real"
    bl_label = "Add Pog REAL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Pog-REAL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Pog-REAL")
        return {'FINISHED'}

class AdicionaGnREAL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_gn_real"
    bl_label = "Add Gn REAL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Gn-REAL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Gn-REAL")
        return {'FINISHED'}

class AdicionaMeREAL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_me_real"
    bl_label = "Add Me REAL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Me-REAL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Me-REAL")
        return {'FINISHED'}

# PONTOS DOLPHIN

class AdicionaPnDIGIDOL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_pn_digidol"
    bl_label = "Add Pn DIGIDOL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Pn-DIGIDOL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Pn-DIGIDOL")
        return {'FINISHED'}

class AdicionaSnDIGIDOL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_sn_digidol"
    bl_label = "Add Sn DIGIDOL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Sn-DIGIDOL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Sn-DIGIDOL")
        return {'FINISHED'}

class AdicionaADIGIDOL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_a_digidol"
    bl_label = "Add A DIGIDOL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'A-DIGIDOL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("A-DIGIDOL")
        return {'FINISHED'}

class AdicionaLsDIGIDOL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_ls_digidol"
    bl_label = "Add Ls DIGIDOL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Ls-DIGIDOL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Ls-DIGIDOL")
        return {'FINISHED'}

class AdicionaStDIGIDOL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_st_digidol"
    bl_label = "Add St DIGIDOL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'St-DIGIDOL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("St-DIGIDOL")
        return {'FINISHED'}

class AdicionaLiDIGIDOL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_li_digidol"
    bl_label = "Add Li DIGIDOL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Li-DIGIDOL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Li-DIGIDOL")
        return {'FINISHED'}

class AdicionaBDIGIDOL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_b_digidol"
    bl_label = "Add B DIGIDOL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'B-DIGIDOL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("B-DIGIDOL")
        return {'FINISHED'}

class AdicionaPogDIGIDOL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_pog_digidol"
    bl_label = "Add Pog DIGIDOL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Pog-DIGIDOL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Pog-DIGIDOL")
        return {'FINISHED'}

class AdicionaGnDIGIDOL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_gn_digidol"
    bl_label = "Add Gn DIGIDOL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Gn-DIGIDOL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Gn-DIGIDOL")
        return {'FINISHED'}

class AdicionaMeDIGIDOL(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_me_digidol"
    bl_label = "Add Me DIGIDOL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Me-DIGIDOL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Me-DIGIDOL")
        return {'FINISHED'}

# PONTOS ORTOG

class AdicionaPnDIGIORT(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_pn_digiort"
    bl_label = "Add Pn DIGIORT"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Pn-DIGIORT' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Pn-DIGIORT")
        return {'FINISHED'}

class AdicionaSnDIGIORT(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_sn_digiort"
    bl_label = "Add Sn DIGIORT"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Sn-DIGIORT' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Sn-DIGIORT")
        return {'FINISHED'}

class AdicionaADIGIORT(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_a_digiort"
    bl_label = "Add A DIGIORT"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'A-DIGIORT' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("A-DIGIORT")
        return {'FINISHED'}

class AdicionaLsDIGIORT(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_ls_digiort"
    bl_label = "Add Ls DIGIORT"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Ls-DIGIORT' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Ls-DIGIORT")
        return {'FINISHED'}

class AdicionaStDIGIORT(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_st_digiort"
    bl_label = "Add St DIGIORT"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'St-DIGIORT' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("St-DIGIORT")
        return {'FINISHED'}

class AdicionaLiDIGIORT(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_li_digiort"
    bl_label = "Add Li DIGIORT"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Li-DIGIORT' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Li-DIGIORT")
        return {'FINISHED'}

class AdicionaBDIGIORT(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_b_digiort"
    bl_label = "Add B DIGIORT"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'B-DIGIORT' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("B-DIGIORT")
        return {'FINISHED'}

class AdicionaPogDIGIORT(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_pog_digiort"
    bl_label = "Add Pog DIGIORT"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Pog-DIGIORT' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Pog-DIGIORT")
        return {'FINISHED'}

class AdicionaGnDIGIORT(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_gn_digiort"
    bl_label = "Add Gn DIGIORT"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Gn-DIGIORT' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Gn-DIGIORT")
        return {'FINISHED'}

class AdicionaMeDIGIORT(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_me_digiort"
    bl_label = "Add Me DIGIORT"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Me-DIGIORT' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        AdicionaEMPTYCompDef("Me-DIGIORT")
        return {'FINISHED'}


class BotoesPontosReal(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "FACE REAL"
    bl_idname = "face.real"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Compare"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("mesh.add_pn_real", text="Pn-REAL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_sn_real", text="Sn-REAL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_a_real", text="A'-REAL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_ls_real", text="Ls-REAL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_st_real", text="St-REAL", icon="OUTLINER_DATA_EMPTY")     

        row = layout.row()
        row.operator("mesh.add_li_real", text="Li-REAL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_b_real", text="B'-REAL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_pog_real", text="Pog'-REAL", icon="OUTLINER_DATA_EMPTY") 

        row = layout.row()
        row.operator("mesh.add_gn_real", text="Gn'-REAL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_me_real", text="Me'-REAL", icon="OUTLINER_DATA_EMPTY")  

class BotoesPontosDigidol(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "FACE DOLPHIN"
    bl_idname = "face.dolphin"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Compare"

    def draw(self, context):
        layout = self.layout

        obj = context.object       
    
        row = layout.row()
        row.operator("mesh.add_pn_digidol", text="Pn-DIGIDOL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_sn_digidol", text="Sn-DIGIDOL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_a_digidol", text="A'-DIGIDOL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_ls_digidol", text="Ls-DIGIDOL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_st_digidol", text="St-DIGIDOL", icon="OUTLINER_DATA_EMPTY")     

        row = layout.row()
        row.operator("mesh.add_li_digidol", text="Li-DIGIDOL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_b_digidol", text="B'-DIGIDOL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_pog_digidol", text="Pog'-DIGIDOL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_gn_digidol", text="Gn'-DIGIDOL", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_me_digidol", text="Me'-DIGIDOL", icon="OUTLINER_DATA_EMPTY") 

class BotoesPontosDigiort(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "FACE ORTOGONBLENDER"
    bl_idname = "face.ortogonblender"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Compare"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("mesh.add_pn_digiort", text="Pn-DIGIORT", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_sn_digiort", text="Sn-DIGIORT", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_a_digiort", text="A'-DIGIORT", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_ls_digiort", text="Ls-DIGIORT", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_st_digiort", text="St-DIGIORT", icon="OUTLINER_DATA_EMPTY")     

        row = layout.row()
        row.operator("mesh.add_li_digiort", text="Li-DIGIORT", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_b_digiort", text="B'-DIGIORT", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_pog_digiort", text="Pog'-DIGIORT", icon="OUTLINER_DATA_EMPTY") 

        row = layout.row()
        row.operator("mesh.add_gn_digiort", text="Gn'-DIGIORT", icon="OUTLINER_DATA_EMPTY")

        row = layout.row()
        row.operator("mesh.add_me_digiort", text="Me'-DIGIORT", icon="OUTLINER_DATA_EMPTY")

def register():
    bpy.utils.register_class(BotoesPontosReal)
    bpy.utils.register_class(AdicionaPnREAL)
    bpy.utils.register_class(AdicionaSnREAL)
    bpy.utils.register_class(AdicionaAREAL)
    bpy.utils.register_class(AdicionaLsREAL)
    bpy.utils.register_class(AdicionaStREAL)
    bpy.utils.register_class(AdicionaLiREAL)
    bpy.utils.register_class(AdicionaBREAL)
    bpy.utils.register_class(AdicionaPogREAL)
    bpy.utils.register_class(AdicionaGnREAL)
    bpy.utils.register_class(AdicionaMeREAL)
    bpy.utils.register_class(BotoesPontosDigidol)
    bpy.utils.register_class(AdicionaPnDIGIDOL)
    bpy.utils.register_class(AdicionaSnDIGIDOL)
    bpy.utils.register_class(AdicionaADIGIDOL)
    bpy.utils.register_class(AdicionaLsDIGIDOL)
    bpy.utils.register_class(AdicionaStDIGIDOL)
    bpy.utils.register_class(AdicionaLiDIGIDOL)
    bpy.utils.register_class(AdicionaBDIGIDOL)
    bpy.utils.register_class(AdicionaPogDIGIDOL)
    bpy.utils.register_class(AdicionaGnDIGIDOL)
    bpy.utils.register_class(AdicionaMeDIGIDOL)
    bpy.utils.register_class(BotoesPontosDigiort)
    bpy.utils.register_class(AdicionaPnDIGIORT)
    bpy.utils.register_class(AdicionaSnDIGIORT)
    bpy.utils.register_class(AdicionaADIGIORT)
    bpy.utils.register_class(AdicionaLsDIGIORT)
    bpy.utils.register_class(AdicionaStDIGIORT)
    bpy.utils.register_class(AdicionaLiDIGIORT)
    bpy.utils.register_class(AdicionaBDIGIORT)
    bpy.utils.register_class(AdicionaPogDIGIORT)
    bpy.utils.register_class(AdicionaGnDIGIORT)
    bpy.utils.register_class(AdicionaMeDIGIORT)

    
def unregister():
    bpy.utils.unregister_class(BotoesPontosReal)
    bpy.utils.unregister_class(AdicionaPnREAL)
    bpy.utils.unregister_class(AdicionaSnREAL)
    bpy.utils.unregister_class(AdicionaAREAL)
    bpy.utils.unregister_class(AdicionaLsREAL)
    bpy.utils.unregister_class(AdicionaStREAL)
    bpy.utils.unregister_class(AdicionaLiREAL)
    bpy.utils.unregister_class(AdicionaBREAL)
    bpy.utils.unregister_class(AdicionaPogREAL)
    bpy.utils.unregister_class(AdicionaGnREAL)
    bpy.utils.unregister_class(AdicionaMeREAL)
    bpy.utils.unregister_class(BotoesPontosDigidol)
    bpy.utils.unregister_class(AdicionaPnDIGIDOL)
    bpy.utils.unregister_class(AdicionaSnDIGIDOL)
    bpy.utils.unregister_class(AdicionaADIGIDOL)
    bpy.utils.unregister_class(AdicionaLsDIGIDOL)
    bpy.utils.unregister_class(AdicionaStDIGIDOL)
    bpy.utils.unregister_class(AdicionaLiDIGIDOL)
    bpy.utils.unregister_class(AdicionaBDIGIDOL)
    bpy.utils.unregister_class(AdicionaPogDIGIDOL)
    bpy.utils.unregister_class(AdicionaGnDIGIDOL)
    bpy.utils.unregister_class(AdicionaMeDIGIDOL)
    bpy.utils.unregister_class(BotoesPontosDigiort)
    bpy.utils.unregister_class(AdicionaPnDIGIORT)
    bpy.utils.unregister_class(AdicionaSnDIGIORT)
    bpy.utils.unregister_class(AdicionaADIGIORT)
    bpy.utils.unregister_class(AdicionaLsDIGIORT)
    bpy.utils.unregister_class(AdicionaStDIGIORT)
    bpy.utils.unregister_class(AdicionaLiDIGIORT)
    bpy.utils.unregister_class(AdicionaBDIGIORT)
    bpy.utils.unregister_class(AdicionaPogDIGIORT)
    bpy.utils.unregister_class(AdicionaGnDIGIORT)
    bpy.utils.unregister_class(AdicionaMeDIGIORT)

if __name__ == "__main__":
    register()
