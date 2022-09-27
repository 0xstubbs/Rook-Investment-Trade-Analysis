import os
import functions.data_extraction as de



###*****************************************************************************************************************
"""
 Get transfers, swaps, etc for investments and divestments during the quarter
 * renBTC -This is related to the divestment of renBTC. Sold into Rook and wBTC
 * CVX Divestment
 * Maple Divestment

------------------------------Contract Addresses------------------------------
Rook Treasury: 0x9a67f1940164d0318612b497e8e6038f902a00a4
Rook Stablecoin Test Wallet:
Rook Labs:

CVX: 0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b
CRV: 0xd533a949740bb3306d119cc777fa900ba034cd52
renBTC: 0xeb4c2781e4eba804ce9a9803c67d0893436bb27d
MPL: 0x33349b282065b0284d756f0577fb39c158f935e6
    
    
    
"""
###*****************************************************************************************************************


###*****************************************************************************************************************
'''
--------------------------------------------------------------renBTC--------------------------------------------------------------
KIP was in progress to exit position to wBTC.
There were concerns due to low liquidity and fallout from the Tornado Cash sanctions.

Hazard used his powers from KIP-23(?) to accelerate the movement.                               ||     Trade Path
---------------------------------------------------------------------------------------------------------------------
    - Sold most of the position of renBTC to a large holder than needed to exit their position  ||  renBTC --> ROOK
    - Converted the remaining renBTC to wBTC                                                    ||  renBTC --> wBTC
    
Look at all transfers / swaps of renBTC and get USD Equivalent Values
'''

###*****************************************************************************************************************

renBTC_transfers = de.get_tokenTransfersByTokenContract("0xeb4c2781e4eba804ce9a9803c67d0893436bb27d", "0x9a67f1940164d0318612b497e8e6038f902a00a4")

print(renBTC_transfers)