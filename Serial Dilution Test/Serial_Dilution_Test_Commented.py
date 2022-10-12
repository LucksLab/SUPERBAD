from opentrons import protocol_api

metadata = {'Protocol Name': 'Serial_Dilution_Test',
           'apiLevel': '2.11',
           'Author': 'Jacob Mangini',
           'Description': 'Serial Dilution Plate'}

def run (protocol: protocol_api.ProtocolContext):
    
    #Loads the Opentrons 96 Filter Tip Rack 1000uL to the robot's spot 1
    tips1000ul = protocol.load_labware('opentrons_96_filtertiprack_1000ul', 1)
    #Loads the Opentrons 96 Filter Tip Rack 200uL to the robot's spot 2
    tips200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', 2)
    #Loads the Opentrons 24 Tube Rack with NEST 1.5mL Snapcap to the robot's spot 4
    tubeRack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 4)
    #Loads the Corning 96 Well Plate 360uL Flat to the robot's spot 5
    wellPlate = protocol.load_labware('corning_96_wellplate_360ul_flat', 5)
    
    #Loads the left mount with a p1000 single-channel gen2 pipette and uses the Opentrons 96 Filter Tip Rack 1000uL
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tips1000ul])
    #loads the right mount with a p300 single-channel gen2 pipette and uses the Opentrons 96 Filter Tip Rack 200uL
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips200ul])
    
    #Transfers 200ul of red colored water to the well plate spot A1
    p1000.transfer(200, tubeRack['A2'], wellPlate.wells_by_name()['A1'])
    #Transfers 200ul of green colored water to the well plate spot B1
    p1000.transfer(200, tubeRack['A3'], wellPlate.wells_by_name()['B1'])
    #Transfers 200ul of blue colored water to the well plate spot C1
    p1000.transfer(200, tubeRack['A4'], wellPlate.wells_by_name()['C1'])
    #Transfers 200 ul of yellow colored water to the well plate spot D1
    p1000.transfer(200, tubeRack['A5'], wellPlate.wells_by_name()['D1'])
    
    #Transfers 20ul of red colored water from well plate spot A1 to well plate spot A2
    p300.transfer(20, wellPlate.wells_by_name()['A1'], wellPlate.wells_by_name()['A2'])
    #Transfers 20ul of green colored water from well plate spot B1 to well plate spot B2
    p300.transfer(20, wellPlate.wells_by_name()['B1'], wellPlate.wells_by_name()['B2'])
    #Transfers 20ul of blue colored water from well plate spot C1 to well plate spot C2
    p300.transfer(20, wellPlate.wells_by_name()['C1'], wellPlate.wells_by_name()['C2'])
    #Transfers 20ul of yellow colored water from well plate spot D1 to well plate spot D2
    p300.transfer(20, wellPlate.wells_by_name()['D1'], wellPlate.wells_by_name()['D2'])
    
    #Dilutes each of the 20ul of undiluted colored water with 80ul of water and mixes 50ul twice
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['A2'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['B2'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['C2'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['D2'], mix_after=(2, 50))
    
    #Transfers 20ul of diluted red colored water from well plate spot A2 to well plate spot A3
    p300.transfer(20, wellPlate.wells_by_name()['A2'], wellPlate.wells_by_name()['A3'])
    #Transfers 20ul of diluted green colored water from well plate spot B2 to well plate spot B3
    p300.transfer(20, wellPlate.wells_by_name()['B2'], wellPlate.wells_by_name()['B3'])
    #Transfers 20ul of diluted blue colored water from well plate spot C2 to well plate spot C3
    p300.transfer(20, wellPlate.wells_by_name()['C2'], wellPlate.wells_by_name()['C3'])
    #Transfers 20ul of diluted yellow colored water from well plate spot D2 to well plate spot D3
    p300.transfer(20, wellPlate.wells_by_name()['D2'], wellPlate.wells_by_name()['D3'])
    
    #Dilutes each of the 20ul of diluted colored water with 80ul of water and mixes 50ul twice
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['A3'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['B3'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['C3'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['D3'], mix_after=(2, 50))
    
    #Transfers 20ul of diluted red colored water from well plate spot A3 to well plate spot A4
    p300.transfer(20, wellPlate.wells_by_name()['A3'], wellPlate.wells_by_name()['A4'])
    #Transfers 20ul of diluted green colored water from well plate spot B3 to well plate spot B4
    p300.transfer(20, wellPlate.wells_by_name()['B3'], wellPlate.wells_by_name()['B4'])
    #Transfers 20ul of diluted blue colored water from well plate spot C3 to well plate spot C4
    p300.transfer(20, wellPlate.wells_by_name()['C3'], wellPlate.wells_by_name()['C4'])
    #Transfers 20ul of diluted yellow colored water from well plate spot D3 to well plate spot D4
    p300.transfer(20, wellPlate.wells_by_name()['D3'], wellPlate.wells_by_name()['D4'])
    
    #Dilutes each of the 20ul of diluted colored water with 80ul of water and mixes 50ul twice
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['A4'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['B4'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['C4'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['D4'], mix_after=(2, 50))
    
    #Transfers 20ul of diluted red colored water from well plate spot A4 to well plate spot A5
    p300.transfer(20, wellPlate.wells_by_name()['A4'], wellPlate.wells_by_name()['A5'])
    #Transfers 20ul of diluted green colored water from well plate spot B4 to well plate spot B5
    p300.transfer(20, wellPlate.wells_by_name()['B4'], wellPlate.wells_by_name()['B5'])
    #Transfers 20ul of diluted blue colored water from well plate spot C4 to well plate spot C5
    p300.transfer(20, wellPlate.wells_by_name()['C4'], wellPlate.wells_by_name()['C5'])
    #Transfers 20ul of diluted yellow colored water from well plate spot D4 to well plate spot D5
    p300.transfer(20, wellPlate.wells_by_name()['D4'], wellPlate.wells_by_name()['D5'])
    
    #Dilutes each of the 20ul of diluted colored water with 80ul of water and mixes 50ul twice
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['A5'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['B5'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['C5'], mix_after=(2, 50))
    p300.transfer(80, tubeRack['A1'], wellPlate.wells_by_name()['D5'], mix_after=(2, 50))