<img width="303" alt="image" src="https://github.com/TomWhitwell/FourLetters/assets/1890544/13c26762-adcf-4bd9-9000-ed20abce8028">

# Four Letters 

Four letters is a tiny ambient display that shows four letter words 

You can see it somewhere here https://www.instagram.com/stories/highlights/17903219396647827/

## Hardware 
* You can solder a [Pimoroni Tiny2040 2mb](https://shop.pimoroni.com/products/tiny-2040?variant=39560012300371) onto the back of a [DL2116T display](https://www.silicon-ark.co.uk/dl2416t-red-intelligent-4-digit-display-by-siemens) - (the [Litronix](https://www.silicon-ark.co.uk/optoelectronics/discounted-led-displays-from-silicon-ark-co-uk/dl2416t-red-intelligent-4-digit-display-by-litronix) version also works just as well). 
* NB: Bend out the bottom layer of pins on the display, so you have space for all the jumper wires
* These are the connections to make (sorry about the image!) 
<img width="608" alt="image" src="https://github.com/TomWhitwell/FourLetters/assets/1890544/d3e54c86-bd57-4fdd-be10-6c47883e9da0">

* In other words:  
  * CE1, CE2 hardwired LOW  
  * CLR Hardwired HIGH  
  * CUE Hardwired Low  
  * CU Hardwired HIgh  
  * WR - Write - connected to GP29  
  * Digit Select 0 - Connected to GP28 
  * Digit Select 1- Connected to GP27 
  * BL Display Blank - Connected to GP7 
  * D0 connected to GP0 
  * D1 connected to GP1
  * D2 connected to GP2 
  * D3 connected to GP3 
  * D4 connected to GP6 
  * D5 connected to GP5 
  * D6 connected to GP4
 
  ## Firmware

  * Just copy the Firmware folder onto the CIRCUITPY folder

  ## Extras

  * There's a desktop version in the extras folder that should run in terminal on a mac 
