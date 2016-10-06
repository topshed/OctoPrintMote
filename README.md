# OctoPrintMote

This simple OctoPrint plugin controls [Pimoroni Mote LED strips] (https://shop.pimoroni.com/products/mote) which can be used to add some colour and flare to your 3D printer. Designed for a Raspberry Pi running [OctoPi] (https://octopi.octoprint.org/).

Currently the lights change in response to Octoprint events:

####On Octoprint startup - *flash blue four times*

####When Octoprint connects to printer - *lights up green*

####When Octoprint disconnects from printer - *LEDs off*

####On successful file upload - *flash yellow once*

####When print job starts and while printing - *white light*

####When print job has fully finished - *pink light*

####When print job fails or is cancelled - *red light*

##Installation

1) Clone this repo

2) Copy the motePrinterConnect.py file into your .octoprint/plugins directory

3) Restart OctoPrint