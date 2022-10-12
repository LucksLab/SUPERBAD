from opentrons import protocol_api

metadata = {'Protocol Name': 'Serial_Dilution_Test',
           'apiLevel': '2.11',
           'Author': 'Jacob Mangini',
           'Description': 'Serial Dilution Plate'}

def run (protocol: protocol_api.ProtocolContext):
    
    #Loads the Opentrons 96 Filter Tip Rack 1000uL to the robot's 10th slot
    tips1000ul = protocol.load_labware('opentrons_96_filtertiprack_1000ul', 10)
    #Loads the Opentrons 96 Filter Tip Rack 200uL to the robot's 11th slot
    tips200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul', 11)
    #Loads the Opentrons 24 Tube Rack with NEST 1.5mL Snapcap to the robot's 9th slot
    tubeRack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 9)
    #Loads the Corning 96 Well Plate 360uL Flat to the robot's 8th slot
    wellPlate = protocol.load_labware('corning_96_wellplate_360ul_flat', 8)
    
    #Loads the left pipette mount with the p1000 single gen 2 pipette and to use tips from the 1000uL tip rack on slot 10
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tips1000ul])
    #Loads the right pipette mount with the p300 single gen 2 pipette and to use tips from the 200uL tip rack on slot 11
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips200ul])
    
    #Transfers 200uL from well A2 of the tube rack to well E1 of the corning 96 well plate
    p1000.transfer(200, tubeRack['A2'], wellPlate.wells_by_name()['E1'])
    #Transfers 200uL from well A3 of the tube rack to well F1 of the corning 96 well plate
    p1000.transfer(200, tubeRack['A3'], wellPlate.wells_by_name()['F1'])
    #Transfers 200uL from well A4 of the tube rack to well G1 of the corning 96 well plate
    p1000.transfer(200, tubeRack['A4'], wellPlate.wells_by_name()['G1'])
    #Transfers 200uL from well A5 of the tube rack to well H1 of the corning 96 well plate
    p1000.transfer(200, tubeRack['A5'], wellPlate.wells_by_name()['H1'])
    
    #For loop iterates through the first 4 rows (A-D) of the corning 96 well plate
    for i in range(4):
        #Sets the current row index of the corning 96 well plate
        row = wellPlate.rows()[i+4]
        #Aspirates 60uL from well A1 of the tube rack, dispenses 20uL into
        #columns 2-6 of the current row of the corning 96 well plate
        #and finally drops it's tip into the robot's default trash bin in slot 12
        p300.transfer(60, tubeRack['A1'], row[1:5])
        
    #For loop iterates through the last 4 rows (E-H) of the corning 96 well plate
    for i in range(4):
        #Sets the current row index of the corning 96 well plate
        row = wellPlate.rows()[i+4]
        #Aspirates 20uL from columns 1-4 of the current row of the corning 96 well plate, dispenses 20uL into
        #columns 2-6 of the current row of the corning 96 well plate, mixes 50uL twice after dispensing into the well
        #and finally drops it's tip into the robot's default trash bin in slot 12
        p300.transfer(20, row[:4], row[1:5], mix_after=(2, 50))