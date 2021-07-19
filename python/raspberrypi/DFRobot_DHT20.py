# -*- coding: utf-8 -*
"""
  *@file DFRobot_DHT20.py
  *@brief Define the basic structure of class DFRobot_DHT20
  *@copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  *@licence     The MIT License (MIT)
  *@author [fengli](li.feng@dfrobot.com)
  *@version  V1.0
  *@date  2021-6-25
  *@get from https://www.dfrobot.com
  *@https://github.com/DFRobot/DFRobot_DHT20
"""
import serial
import time
import smbus
                
class DFRobot_DHT20(object):
  ''' Conversion data '''

  _addr      =  0x50

  def __init__(self ,bus,address):
    self.i2cbus = smbus.SMBus(bus)
    self._addr = address
    self.idle =    0

  '''
    @brief init function
    @return Return 0 if initialization succeeds, otherwise return non-zero and error code.
   '''
  def begin(self ):

    #self.i2cbus.write_byte(self._addr,0xaa)
    time.sleep(0.5)
    data = self.read_reg(0x71,1)
    
    if (data[0] | 0x08) == 0:
      return False
    else:
      return True

  '''
    @brief Get ambient temperature, unit: °C
    @return ambient temperature,the measurement range is -40°C ~ 80°C
  '''
  def get_temperature(self):
     self.write_reg(0xac,[0x33,0x00])
     time.sleep(0.1)
     data = self.read_reg(0x71,7)
     rawData = ((data[3]&0xf) <<16) + (data[4]<<8)+data[5]
     #print(rawData)
     temperature = float(rawData)/5242 -50
     return temperature
     
  '''
    @brief Get relative humidity, unit: %RH. 
    @return relative humidity, the measurement range is (1-100%)
  '''
  def get_humidity(self):
     self.write_reg(0xac,[0x33,0x00])
     time.sleep(0.1)
     data = self.read_reg(0x71,7)
     rawData = ((data[3]&0xf0) >>4) + (data[1]<<12)+(data[2]<<4)
     humidity = float(rawData)/0x100000
     return humidity*100
     
  
  def write_reg(self, reg,data):
    time.sleep(0.01)
    self.i2cbus.write_i2c_block_data(self._addr,reg,data)
  
  
  def read_reg(self,reg,len):
    time.sleep(0.01)
    rslt = self.i2cbus.read_i2c_block_data(self._addr,reg,len)
    #print(rslt)
    return rslt
