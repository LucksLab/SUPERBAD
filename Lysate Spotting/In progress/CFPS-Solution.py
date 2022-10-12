from opentrons import protocol_api

metadata = {'Protocol Name': 'CFPS-Solution',
           'apiLevel': '2.11',
           'Author': 'U.S. Army DEVCOM CBC - Jacob Mangini',
           'Description': 'Mixes all the components of a CFPS Solution together'}

def run(protocol: protocol_api.ProtocolContext):
    #Tells the robot that the opentrons 96 filter tip rack 20ul is in slot 6
    tips20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', 6)
    #Tells the robot that the opentrons 96 filter tip rack 200ul is in slot 8
    tips200ul = protocol.load_labware('opentrons_96_filtertiprack_200ul',8)
    #Tells the robot that the opentrons 24 aluminum block with nest 1.5ml snapcap tube rack is in slot 5
    reservoir = protocol.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', 5)
    
    #Tells the robot to use the left mount to load the p20 single channel gen2 pipette with tips from the 96 filter tip rack 20ul
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips20ul])
    #Tells the robot to use the left mount to load the p300 single channel gen2 pipette with tips from the 96 filter tip rack 200ul
    p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips200ul])
    
    #Tells the robot to have the p300 pipette pick up a tip from the 200ul filter tip rack
    p300.pick_up_tip()
    
    #Adds 218.5ul of Reaction Buffer to the solution
    
    #p300 pipette aspirates 200ul of Reaction Buffer from well B1 of the tube rack
    p300.aspirate(200, reservoir['B1'])
    #p300 pipette dispenses 200ul of Reaction Buffer into the solution in well A1 of the tube rack
    p300.dispense(200, reservoir['A1'])
    #p300 pipette aspirates 18.5ul of Reaction Buffer from well B1 of the tube rack
    p300.aspirate(18.5, reservoir['B1'])
    #p300 pipette dispenses 18.5ul of Reaction Buffer into the solution in well A1 of the tube rack
    p300.dispense(18.5, reservoir['A1'])
    
    #Tells the robot to drop the tip on the p300 pipette in the default trash location in slot 12
    p300.drop_tip()
    
    #Tells the robot to have the p300 pipette pick up a tip from the 200ul filter tip rack
    p300.pick_up_tip()
    
    #Adds 4.5ul of T7 Polymerase to the solution
    
    #p300 pipette aspirates 4.5ul of T7 Polymerase from well B2 of the tube rack
    p300.aspirate(4.5, reservoir['B2'])
    #p300 pipette dispenses 4.5ul of T7 Polymerase into the solution in well A1 of the tube rack
    p300.dispense(4.5, reservoir['A1'])
    
    #Tells the robot to drop the tip on the p300 pipette in the default trash location in slot 12
    p300.drop_tip()
    
    #Tells the robot to have the p300 pipette pick up a tip from the 200ul filter tip rack
    p300.pick_up_tip()
    
    #Adds 12.5ul of RNase Inhibitor to the solution
    
    #p300 pipette aspirates 12.5ul of RNase Inhibitor from well B3 of the tube rack
    p300.aspirate(12.5, reservoir['B3'])
    #p300 pipette dispenses 12.5ul of RNase Inhibitor into the solution in well A1 of the tube rack
    p300.dispense(12.5, reservoir['A1'])
    
    #Tells the robot to drop the tip on the p300 pipette in the default trash location in slot 12
    p300.drop_tip()
    
    #Tells the robot to have the p300 pipette pick up a tip from the 200ul filter tip rack
    p300.pick_up_tip()
    
    #Adds 174.5ul of Nuclease-free H2O to the solution
    
    #p300 pipette aspirates 174.5ul of Nuclease-free H2O from well B4 of the tube rack
    p300.aspirate(174.5, reservoir['B4'])
    #p300 pipette dispenses 174.5ul of Nuclease-free H2O into the solution in well A1 of the tube rack
    p300.dispense(174.5, reservoir['A1'])
    
    #Tells the robot to drop the tip on the p300 pipette in the default trash location in slot 12
    p300.drop_tip()
    
    #Tells the robot to have the p300 pipette pick up a tip from the 200ul filter tip rack
    p300.pick_up_tip()
    
    #Adds 50ul of CPRG to the solution
    
    #p300 pipette aspirates 50ul of CPRG from well B5 of the tube rack
    p300.aspirate(50, reservoir['B5'])
    #p300 pipette dispenses 50ul of CPRG into the solution in well A1 of the tube rack
    p300.dispense(50, reservoir['A1'])
    
    #Tells the robot to drop the tip on the p300 pipette in the default trash location in slot 12
    p300.drop_tip()
    
    #Tells the robot to have the p300 pipette pick up a tip from the 200ul filter tip rack
    p300.pick_up_tip()
    
    #Adds 165ul of lacZ Extract to the solution
    
    #p300 pipette aspirates 165ul of lacZ Extract from well B6 of the tube rack
    p300.aspirate(165, reservoir['B6'])
    #p300 pipette dispenses 165ul of lacZ Extract into the solution in well A1 of the tube rack
    p300.dispense(165, reservoir['A1'])
    
    #Changes the p300 aspiration flow rate to 150ul/s
    p300.flow_rate.aspirate = 150
    #Changes the p300 dispense flow rate to 150ul/s
    p300.flow_rate.dispense = 150
    
    #Mixes the the solution 5 times using 150ul of the solution each time
    p300.mix(5, 150, reservoir['A1'])
    
    #Tells the robot to drop the tip on the p300 pipette in the default trash location in slot 12
    p300.drop_tip()