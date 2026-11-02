import sys, os
from pathlib import Path
from unittest.mock import MagicMock

pcb = MagicMock(); pcb.Version = lambda: "10.0.0"
sys.modules["pcbnew"] = pcb
sys.modules["wx"] = MagicMock()

from kbplacer.schematic_project import SchematicRequest, create_schematic_project

root = Path.home() / "keyboard75"
mb = root / "libs/marbastlib/footprints/marbastlib-mx.pretty"
diode = "/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints/Diode_SMD.pretty"

create_schematic_project(
    root / "keyboard75.kicad_pro",
    root / "layout_via.json",
    [SchematicRequest("key_matrix", {
        "switch_footprint": f"{mb}:SW_MX_HS_CPG151101S11_{{:g}}u",
        "stabilizer_footprint": f"{mb}:STAB_MX_{{:g}}u",
        "diode_footprint": f"{diode}:D_SOD-123",
        "add_stabilizers": True,
    })],
    strategy="flat",
)
print("done ->", root)
