from opentrons import protocol_api
metadata = {'Protocol Name': 'Serial_Dilution_Test',
	'apiLevel': '2.11',
           'Author': 'Jacob Mangini',
           'Description': 'Serial Dilution Plate'}
def run(protocol: protocol_api.ProtocolContext):
    tips1000ul = protocol.load_labware('opentrons_96_filtertiprack_1000ul', 1)
    tips200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', 2)
    tubeRack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 4)
    wellPlate = protocol.load_labware('corning_96_wellplate_360ul_flat', 5)
    
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tips1000ul])
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips200ul])
    
    p1000.transfer(200, tubeRack['A2'], wellPlate.wells_by_name()['A1'])
    p1000.transfer(200, tubeRack['A3'], wellPlate.wells_by_name()['B1'])
    p1000.transfer(200, tubeRack['A4'], wellPlate.wells_by_name()['C1'])
    p1000.transfer(200, tubeRack['A5'], wellPlate.wells_by_name()['D1'])
    
    p300.transfer(20, wellPlate.wells_by_name()['A1'], wellPlate.wells_by_name()['A2'])
    p300.transfer(20, wellPlate.wells_by_name()['B1'], wellPlate.wells_by_name()['B2'])
    p300.transfer(20, wellPlate.wells_by_name()['C1'], wellPlate.wells_by_name()['C2'])
    p300.transfer(20, wellPlate.wells_by_name()['D1'], wellPlate.wells_by_name()['D2'])
    
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['A2'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['B2'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['C2'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['D2'], mix_after=(2, 50))
    
    p300.transfer(20, wellPlate.wells_by_name()['A2'], wellPlate.wells_by_name()['A3'])
    p300.transfer(20, wellPlate.wells_by_name()['B2'], wellPlate.wells_by_name()['B3'])
    p300.transfer(20, wellPlate.wells_by_name()['C2'], wellPlate.wells_by_name()['C3'])
    p300.transfer(20, wellPlate.wells_by_name()['D2'], wellPlate.wells_by_name()['D3'])
    
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['A3'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['B3'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['C3'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['D3'], mix_after=(2, 50))
    
    p300.transfer(20, wellPlate.wells_by_name()['A3'], wellPlate.wells_by_name()['A4'])
    p300.transfer(20, wellPlate.wells_by_name()['B3'], wellPlate.wells_by_name()['B4'])
    p300.transfer(20, wellPlate.wells_by_name()['C3'], wellPlate.wells_by_name()['C4'])
    p300.transfer(20, wellPlate.wells_by_name()['D3'], wellPlate.wells_by_name()['D4'])
    
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['A4'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['B4'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['C4'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['D4'], mix_after=(2, 50))
    
    p300.transfer(20, wellPlate.wells_by_name()['A4'], wellPlate.wells_by_name()['A5'])
    p300.transfer(20, wellPlate.wells_by_name()['B4'], wellPlate.wells_by_name()['B5'])
    p300.transfer(20, wellPlate.wells_by_name()['C4'], wellPlate.wells_by_name()['C5'])
    p300.transfer(20, wellPlate.wells_by_name()['D4'], wellPlate.wells_by_name()['D5'])
    
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['A5'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['B5'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['C5'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['D5'], mix_after=(2, 50))