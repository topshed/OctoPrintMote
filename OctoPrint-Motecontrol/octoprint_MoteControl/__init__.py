# coding=utf-8
# Plugin for motephat
from __future__ import absolute_import

import octoprint.plugin
from colorsys import hsv_to_rgb
#from mote import Mote # uncomment for USB mote hub
try:
    from mote import Mote
    moteType = 'USB'

except ImportError:
    try:
        import motephat as mote #uncomment for motephat
        moteType = 'PHAT'
    except ImportError:
        import sys
        sys.exit(-1)


import time

class MoteControlPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.EventHandlerPlugin):
    def on_after_startup(self):
        global activeClient
        activeClient = False
        self._logger.info("Mote Control Plugin")
        if moteType == 'PHAT':
            #for c in range(1,5):
            #    mote.configure_channel(c, 16, False)
            self._logger.info("Mote Control using motephat")

    def get_settings_defaults(self):
        return dict(motetype=moteType,
                    print_col_r="255",
                    print_col_g="255",
                    print_col_b ="255",
                    start_col_r="0",
                    start_col_g="0",
                    start_col_b ="255",
                    error_col_r="255",
                    error_col_g="0",
                    error_col_b ="0",
                    conn_col_r="0",
                    conn_col_g="255",
                    conn_col_b ="0",
                    done_col_r="255",
                    done_col_g="20",
                    done_col_b ="147",
                    upload_col_r="255",
                    upload_col_g="255",
                    upload_col_b ="0",
                    upload_dur ="4"
        )

    def get_template_vars(self):
        return dict(print_col_b=self._settings.get(["print_col_b"]))

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]
    def moteUSB(self):

        if moteType == 'USB':
            global mote
            mote = Mote()
            #for c in range(1,5):
                #mote.configure_channel(c, 16, False)

    def on_event(self,event,payload):
        global activeClient
        #self._logger.info("Mote Event handler:"+ str(event))
        if event == "Startup": # default 4 Blue flashes
            self.moteUSB()
            #mote = Mote() # uncomment for USB mote hub
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for t in range(4):
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, int(self._settings.get(["start_col_r"])),
                                                 int(self._settings.get(["start_col_g"])),
                                                 int(self._settings.get(["start_col_b"])))
                mote.show()
                time.sleep(1)
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, 0, 0, 0)
                        mote.show()
                time.sleep(1)

        if event == "Connected": # default Green
            if (self._settings.get(["lightOnConnect"]) and activeClient) or (not self._settings.get(["lightOnConnect"])):
                self.moteUSB()
                #mote = Mote() # uncomment for USB mote hub
                for c in range(1,5):
                    mote.configure_channel(c, 16, False)
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, int(self._settings.get(["conn_col_r"])),
                                                 int(self._settings.get(["conn_col_g"])),
                                                 int(self._settings.get(["conn_col_b"])))
                        mote.show()

        if event == "Disconnected": #  default Off
            self.moteUSB()
            #mote = Mote() # uncomment for USB mote hub
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, 0, 0, 0)
                    mote.show()

        if event == "Upload": # default yellow then back to green
            #mote = Mote() # uncomment for USB mote hub
            self.moteUSB()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, int(self._settings.get(["upload_col_r"])),
                                             int(self._settings.get(["upload_col_g"])),
                                             int(self._settings.get(["upload_col_b"])))
                    mote.show()
                    time.sleep(0.1)
            time.sleep(float(self._settings.get(["upload_dur"])))
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, 0,0,0)
                    mote.show()

        if event == "PrintStarted": # default white
            if (self._settings.get(["lightOnConnect"]) and activeClient) or (not self._settings.get(["lightOnConnect"])):
                #mote = Mote() # uncomment for USB mote hub
                self.moteUSB()
                for c in range(1,5):
                    mote.configure_channel(c, 16, False)
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, int(self._settings.get(["print_col_r"])),
                                                 int(self._settings.get(["print_col_g"])),
                                                 int(self._settings.get(["print_col_b"])))
                        mote.show()

        if event == "PrintFailed" or event == "Error": # default red
            if (self._settings.get(["lightOnConnect"]) and activeClient) or (not self._settings.get(["lightOnConnect"])):
                self.moteUSB()
                #mote = Mote() # uncomment for USB mote hub
                for c in range(1,5):
                    mote.configure_channel(c, 16, False)
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, int(self._settings.get(["error_col_r"])),
                                                 int(self._settings.get(["error_col_g"])),
                                                 int(self._settings.get(["error_col_b"])))
                        mote.show()

        if event == "PrintDone": # default pink
            if (self._settings.get(["lightOnConnect"]) and activeClient) or (not self._settings.get(["lightOnConnect"])):
                self.moteUSB()
                #mote = Mote() # uncomment for USB mote hub
                for c in range(1,5):
                    mote.configure_channel(c, 16, False)
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, int(self._settings.get(["done_col_r"])),
                                                 int(self._settings.get(["done_col_g"])),
                                                 int(self._settings.get(["done_col_b"])))
                        mote.show()

        if event == "ClientOpened": # default white
            activeClient = True

        if event == "ClientClosed": # default white
            activeClient = False

__plugin_name__ = "Mote Control"
__plugin_implementation__ = MoteControlPlugin()
