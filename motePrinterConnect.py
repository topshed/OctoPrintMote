# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from colorsys import hsv_to_rgb
from mote import Mote
import time

class motePrinterConnectPlugin(octoprint.plugin.EventHandlerPlugin):
    def on_event(self,event,payload):
        self._logger.info("Mote Event handler:"+ str(event))
        if event == "Startup": # 4 Blue flashes
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for t in range(4):
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, 0, 0, 255)
                mote.show()
                time.sleep(1)
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, 0, 0, 0)
                mote.show()
                time.sleep(1)
        if event == "Connected": #Green
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, 0, 255, 0)
                mote.show()
            mote.show()
        if event == "Disconnected": # Off
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, 0, 0, 0)
            mote.show()
        if event == "Upload": # Yellow then back to green
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, 255, 255, 0)
            mote.show()
            time.sleep(1)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, 0, 255, 0)
            mote.show()
        if event == "PrintStarted": # White
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, 255, 255, 255)
            mote.show()
        if event == "PrintFailed" or event == "Error": # Red
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, 255, 0, 0)
            mote.show()
        if event == "PrintDone": # Pink
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, 255, 20, 147)
            mote.show()


__plugin_name__ = "mote Event Handler"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Mote lighting for OctoPrint"
__plugin_implementation__ = motePrinterConnectPlugin()
