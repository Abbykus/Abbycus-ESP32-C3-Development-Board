# QDEV-ESP32-C3
Abbykus ESP32-C3 development board based on the [Espressif ESP32-C3-WROOM-02 module](https://www.espressif.com/en/news/ESP32_C3).



## DESCRIPTION
The QDEV-ESP32-C3 board is a multipurpose Internet Of Things (IOT) module based on the Espressif ESP32-C3-WROOM-02 MCU. 
The QDEV-ESP32-C3 is a powerful and cost effective development/product ready platform with a *'dongle'* style form factor which incorporates a male USB-A connector allowing direct plugin to a PC / laptop / Raspberry Pi / phone charger / power bank, etc.

The board also has full support for a 3.7V Lithium Ion battery using a high efficiency buck/boost regulator and charging circuitry. See below for more battery information.

## FEATURES
- Espressif ESP32-C3 32 bit RISC-V single core low power MCU.
- 80 / 160 Mhz CPU clock speed.
- 384 KBytes of SRAM.
- 4 MBytes of flash memory.
- WiFi module supports IEEE802.11 b/g/n protocol w/embedded TCPIP stack. 
- WiFi supports adhoc and MESH networks based on ESP-NOW protocol.
- Bluetooth LE: Bluetooth 5.0, Bluetooth MESH, Bluetooth long range.
- Integrated Inverted F PCB antenna.
- 6 channels of 12-bit Analog to Digital converter (ADC).
- 13 GPIO's available with PWM and low power wakeup capability.
- UART supporting baud rates up to 5 Mbaud.
- Auto-programming circuit (eliminates the need for a 'boot' button).
- On-board user LED (IO9).
- High efficiency buck/boost switching regulator yields >90% efficiency for maximum battery life.
- Battery reverse polarity protection.
- Auto-Resettable polyfuse.
- Integrated battery charge circuit with charge state LED.
- Default charge current of 250 milliamps can be modified via an onboard resistor.
- Power on/off switch.
- Reset button.

## SPECIFICATIONS
### MECHANICAL
![PCB_QDEV-ESP32-C3_DIM](https://user-images.githubusercontent.com/99380815/156489479-e63da90b-ce5c-4248-97cb-f0c032cb4949.png)

### ELECTRICAL
#### *POWER*
The board is normally powered by 5 volts via the USB-A connector. The 5 volt input is regulated down to 3.3 volts using a high efficency buck/boost switching regulator. 

The 3.3 volt breakout pin can power external circuits with a maximum current of 600 milliamps. 

**WARNING:** The ESP32-C3 is not 5V tolerant. Voltage applied to any I/O pin should not exceed 3.3V.

#### *BATTERY*
The board can be powered by an external 3.7V Lithium Ion battery connected to the **BAT** terminals. The embedded buck/boost switching regulator maintains a stable 3.3V system voltage from a battery voltage of 4.2V (full charge) down to approximately 2.5V (discharged). 
The battery is charged when 5 volts is applied via the USB-A connector. The on-board RED LED will light while charging and turn off when charging is complete.

Default charge current is set at 250 milliamps. This can be changed by replacing resistor R11 on the PCB. See the AAP2154 datasheet in the **DOCS** folder for information regarding setting the charge current.

Operating current can range from microamps in deep sleep mode to approximately 160 milliamps when transmitting WiFi data. Typical idle current is approximately 50 milliamps.

#### *BREAKOUT PIN DESCRIPTION*
- **3.3V** Output of the 3.3V switching regulator.
- **NRST** MCU reset - active low.
- **IO4** GPIO4 / ADC1_CH4 / FSPIHD / MTMS.
- **IO5** GPIO5 / ADC2_CH0 / FSPIWP / MTDI.
- **IO6** GPIO6 / FSPICLK / MTCK.
- **IO7** GPIO7 / FSPID / MTDO.
- **IO8** GPIO8. **STRAPPING PIN**
- **IO9** GPIO9. **STRAPPING PIN**
- **GND** Board ground connect.

- **IO10** GPIO / FSPICS0.
- **RXD0** UART0_RXD / GPIO20.
- **TXD0** UART0_TXD / GPIO21. 
- **IO18** GPIO18 / USB_D-.
- **IO19** GPIO19 / USB_D+.
- **IO3** GPIO3 / ADC1_CH3.
- **IO2** GPIO2 / ADC1_CH2 / FSPIQ. **STRAPPING PIN**
- **IO1** GPIO1 / ADC1_CH1 / XTAL_32K_N.
- **IO0** GPIO0 / ADC1_CH0 / XTAL_32K_P.


#### *STRAPPING PINS*
Three GPIO pins are used by the ESP32-C3 to control boot mode. The pin level during boot is as follows:
- **IO2** UART download mode: pulldown. Normal boot from flash: floating or pullup.
- **IO8** UART download mode: floating or pullup. Normal boot from flash: don't care.
- **IO9** UART download mode: pulldown. Normal boot from flash: floating or pullup.

## PROGRAMMING
The QDEV-ESP32-C3 is programmed through the USB-A connector. 

## APPLICATION EXAMPLES
### Wireless UART Bridge
The QDEV-ESP32-C3 can function as a UART bridge between two or more computers. 

## FIRMWARE DEVELOPMENT
Firmware can be developed on several platforms such as the Arduino IDE, PlatformIO on VSCode, or the Espressif ESP-IDF development environment. 
The code examples included here were written using the Arduino framework on [PlatformIO IDE](https://platformio.org/install/ide?install=vscode).

While the Arduino IDE is relatively simple, the advanced features of PlatformIO make it much more compelling and useful to developers. 

The Espressif ESP-IDF offers more detailed control of certain features but lacks the rich library support of either the Arduino IDE or PlatformIO and is specific to Espressif devices.


