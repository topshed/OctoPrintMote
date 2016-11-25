'''class motePrinterConnectPlugin(octoprint.plugin.EventHandlerPlugin):
    def on_event(self,event,payload):
        activePrinting = False
        self._logger.info("Mote Event handler:"+ str(event))
        if event == "Startup": # default 4 Blue flashes
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for t in range(4):
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, self._settings.get(["start_col_r"]),
                                                 self._settings.get(["start_col_g"]),
                                                 self._settings.get(["start_col_b"]))
                mote.show()
                time.sleep(1)
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, 0, 0, 0)
                mote.show()
                time.sleep(1)
        if event == "Connected": # default Green
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, self._settings.get(["conn_col_r"]),
                                             self._settings.get(["conn_col_g"]),
                                             self._settings.get(["conn_col_b"]))
                mote.show()
            mote.show()
        if event == "Disconnected": #  default Off
            activePrinting = False
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, 0, 0, 0)
            mote.show()
        if event == "Upload": # default yellow then back to green
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, self._settings.get(["upload_col_r"]),
                                             self._settings.get(["upload_col_g"]),
                                             self._settings.get(["upload_col_b"]))
            mote.show()
            time.sleep(self._settings.get(["upload_dur"]))
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, self._settings.get(["conn_col_r"]),
                                             self._settings.get(["conn_col_g"]),
                                             self._settings.get(["conn_col_b"]))
            mote.show()
        if event == "PrintStarted": # default white
            activePrinting = True
            if not self._settings.get(["lightOnConnect"]):
                mote = Mote()
                for c in range(1,5):
                    mote.configure_channel(c, 16, False)
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, self._settings.get(["print_col_r"]),
                                                 self._settings.get(["print_col_g"]),
                                                 self._settings.get(["print_col_b"]))
                mote.show()
        if event == "PrintFailed" or event == "Error": # default red
            activePrinting = False
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, self._settings.get(["error_col_r"]),
                                             self._settings.get(["error_col_g"]),
                                             self._settings.get(["error_col_b"]))
            mote.show()
        if event == "PrintDone": # default pink
            activePrinting = False
            mote = Mote()
            for c in range(1,5):
                mote.configure_channel(c, 16, False)
            for c in range(1,5):
                for pixel in range(16):
                    mote.set_pixel(c, pixel, self._settings.get(["done_col_r"]),
                                             self._settings.get(["done_col_g"]),
                                             self._settings.get(["done_col_b"]))
            mote.show()
        if event == "ClientOpened": # default white
            if self._settings.get(["lightOnConnect"]) and activePrinting:
                mote = Mote()
                for c in range(1,5):
                    mote.configure_channel(c, 16, False)
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, self._settings.get(["print_col_r"]),
                                                 self._settings.get(["print_col_g"]),
                                                 self._settings.get(["print_col_b"]))
                mote.show()
        if event == "ClientClosed": # default white
            if self._settings.get(["lightOnConnect"]) and activePrinting:
                mote = Mote()
                for c in range(1,5):
                    mote.configure_channel(c, 16, False)
                for c in range(1,5):
                    for pixel in range(16):
                        mote.set_pixel(c, pixel, 0, 0, 0)
                mote.show()
'''
