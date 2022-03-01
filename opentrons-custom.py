from typing import List
from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Flag Printer',
    'author': 'Eugen Ursu',
    'description': 'A simple protocol printing a flag',
    'apiLevel': '2.11'
}

def paint_wells(
    color_well: str, 
    wells: List[str], 
    pipette: protocol_api.InstrumentContext,
    canvas: protocol_api.labware.Labware):
    """
    Paints a group of `wells` from same `color_well`.
    """
    pipette.pick_up_tip()

    for well in wells:
        pipette.aspirate(100, color_well)
        pipette.dispense(100, canvas[well])

    pipette.drop_tip()


# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # NOTE: Do not change anything in this section — we will assume the OpenTrons
    # is set up according to this configuration
    # ---------------------------------------------------------------------------
    # labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    palette = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    canvas = protocol.load_labware('nest_96_wellplate_200ul_flat', '5')

    color = {
        'green': 'A1',
        'blue': 'A2',
        'red': 'A3',
        'yellow': 'A4'
    }

    # pipettes
    left_pipette = protocol.load_instrument(
         'p300_single', 'left', tip_racks=[tiprack])

    # NOTE: Describe your commands below this line
    # ---------------------------------------------------------------------------
    # make sure you are pipetting FROM the palette TO the canvas
    # use the color mpa for easy well reference:
    # palette[color['green']] == palette['A1']
    
    number_range = range(1, 13)
    upper_half_letters = "ABCD"
    upper_half_wells = [
        f"{letter}{number}" 
        for letter in upper_half_letters 
        for number in number_range
    ]

    lower_half_letters = "EFGH"
    lower_half_wells = [
        f"{letter}{number}" 
        for letter in lower_half_letters 
        for number in number_range
    ]

    paint_wells(
        color_well = palette[color['blue']],
        wells = upper_half_wells,
        pipette = left_pipette,
        canvas = canvas
    )

    paint_wells(
        color_well = palette[color['yellow']],
        wells = lower_half_wells,
        pipette = left_pipette,
        canvas = canvas
    )