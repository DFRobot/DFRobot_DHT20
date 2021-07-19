# DFRobot_DHT20
The DHT20 temperature & humidity sensor is the newly upgraded version of the DHT11. The DHT20 features a brand-new ASIC dedicated chip, an improved MEMS semiconductor capacitive humidity sensor element and a standard on-chip temperature element. All sensors are factory calibrated and characterized by low power, high precision & stability, fast response, and strong anti-interference. Moreover, the DHT20 performance parameters of accuracy, power supply voltage, measurement range and response time have been enhanced greatly over the previous generation,making it more cost-effective. Besides that, the DHT20 temperature & humidity sensor employs I2C digital output protocol, which is very suitable for HVAC,automobiles, data loggers, weather stations, home appliances, and other related temperature and humidity detection and controlled areas. <br>

![正反面svg效果图](https://github.com/cdjq/DFRobot_LIS2DW12/raw/master/resources/images/SEN0245svg4.png)

## 产品链接（链接到英文商城）
    SKU：产品名称
## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)

## Summary

Provide an RaspberryPi library to get Humidity and Temperature by reading data from dht20.
## Installation

Download the DFRobot_DHT20 file to the Raspberry Pi file directory, then run the following command line to use this sensor:

## Methods
```python
  '''
    @brief init function
    @return Return 0 if initialization succeeds, otherwise return non-zero and error code.
   '''
  def begin(self ):

  '''
    @brief Get ambient temperature, unit: °C
    @return ambient temperature, its measurement range is (-40°C ~ 80°C)
  '''
  def get_temperature(self):
     
  '''
    @brief Get relative humidity, unit: %RH. 
    @return relative humidity, its measurement range is (1-100%)
  '''
  def get_humidity(self):
```

## Compatibility

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
Raspberry Pi              |      √         |            |             | 


## History

- Date 2021-7-2
- Version V0.1


## Credits

Written by fengli(li.feng@dfrobot.com), 2021.7.2 (Welcome to our [website](https://www.dfrobot.com/))





