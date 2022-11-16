#              .';:cc;.
#            .,',;lol::c.
#            ;';lddddlclo
#            lcloxxoddodxdool:,.
#            cxdddxdodxdkOkkkkkkkd:.
#          .ldxkkOOOOkkOO000Okkxkkkkx:.
#        .lddxkkOkOOO0OOO0000Okxxxxkkkk:
#       'ooddkkkxxkO0000KK00Okxdoodxkkkko
#      .ooodxkkxxxOO000kkkO0KOxolooxkkxxkl
#      lolodxkkxxkOx,.      .lkdolodkkxxxO.
#      doloodxkkkOk           ....   .,cxO;
#      ddoodddxkkkk:         ,oxxxkOdc'..o'
#      :kdddxxxxd,  ,lolccldxxxkkOOOkkkko,
#       lOkxkkk;  :xkkkkkkkkOOO000OOkkOOk.
#        ;00Ok' 'O000OO0000000000OOOO0Od.
#         .l0l.;OOO000000OOOOOO000000x,
#            .'OKKKK00000000000000kc.
#               .:ox0KKKKKKK0kdc,.
#                      ...
#
# Author: peppe8o
# Date: Dec 11th, 2021
# Version: 1.0
# https://peppe8o.com

from machine import I2C
from hmc5883l import HMC5883L
from time import sleep

# Please check that correct PINs are set on hmc5883l library!
sensor = HMC5883L()

while True:
    sleep(1)
    x, y, z = sensor.read()
    #print(sensor.format_result(x, y, z))
    degrees, minutes = sensor.heading(x, y)
    #print(degrees)
    if degrees < 332.5 and degrees > 287.5:
        print("Norte")        
    elif degrees < 287.5 and degrees > 242.5:
        print("Nordeste")
    elif degrees < 242.5 and degrees > 197.5:
        print("Leste")
    elif degrees < 197.5 and degrees > 152.5:
        print("Sudeste")
    elif degrees < 152.5 and degrees > 107.5:
        print("Sul")
    elif degrees < 107.5 and degrees > 62.5:
        print("Sudoeste")
    elif degrees < 62.5 and degrees > 17.5:
        print("Oeste")
    elif degrees < 17.5 or degrees > 332.5:
        print("Noroeste")
    else: print("Erro")
  
  
  
  