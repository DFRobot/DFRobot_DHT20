# DFRobot_DHT20

DHT20 配有一个全新设计的 ASIC专用芯片、一个经过改进的MEMS半导体电容式湿度传感元件 <br>
和一个标准的片上温度传感元件，其性能已经大大提升甚至超出了前一代传感器的可靠性水平 <br>
新一代温湿度传感器，经过改进使其在恶劣环境下的性能更稳定。每一个传感器都经过严格的 <br>
校准和测试。由于对传感器做了改良和微型化改进，因此它的性价比更高。<br>

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


Provide an Arduino library to get Humidity and Temperature by reading data from dht20.

## Installation

To use this library, first download the library file, paste it into the \Arduino\libraries directory, then open the examples folder and run the demo in the folder.

## Methods
```C++

  /*!
   * @brief Construct the function
   * @param pWire IC bus pointer object and construction device, can both pass or not pass parameters, Wire in default.
   * @param address Chip IIC address, 0x38 in default.
   */
  DFRobot_DHT20(TwoWire *pWire = &Wire, uint8_t address = 0x38);

  /**
   * @brief init function
   * @return Return 0 if initialization succeeds, otherwise return non-zero and error code.
   */
  int begin(void);
    
  /**
   * @brief 获取环境温度,单位为摄氏度(°C)
   * @return 环境温度,量程为(-40°C ~ 80°C)
   */
  float getTemperature();
    
  /**
   * @brief 获取相对湿度,单位为%RH. 
   * @return 相对湿度, 量程为(1-100%)
   */
  float getHumidity();
```

## Compatibility

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
Arduino Uno        |      √       |              |             | 
Mega2560        |      √       |              |             | 
Leonardo        |      √       |              |             | 
ESP32        |      √       |              |             | 
ESP8266        |      √       |              |             | 
M0        |      √       |              |             | 


## History

- Date 2021-6-25
- Version V0.1


## Credits

Written by fengli(li.feng@dfrobot.com), 2021.7.31 (Welcome to our [website](https://www.dfrobot.com/))





