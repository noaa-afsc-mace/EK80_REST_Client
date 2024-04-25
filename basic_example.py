"""


"""

from PyQt5 import QtCore
import ek80_rest_client


class basic_example(QtCore.QObject):

    stopClient = QtCore.pyqtSignal()
    stopApp = QtCore.pyqtSignal()

    def __init__(self, server_address, clean_server=False, parent=None):
        #  initialize the superclass
        super(basic_example, self).__init__(parent)

        #  connect the app stop signal to our stop method
        self.stopApp.connect(self.stop_app)

        #  store some important parameters
        self.client = ek80_rest_client.ek80_rest_client(server_address=server_address)
        self.client.subscriptionData.connect(self.subscriptionDataAvailable)
        self.client.cleanupComplete.connect(self.clientStopped)
        self.stopClient.connect(self.client.cleanup_client)

        #  check if we need to wipe all of the subscriptions (and endpoints)
        #  from the server. This is sometimes needed while developing client
        #  apps after they crash and leave their bits around on the server.
        if clean_server:
            self.client.cleanup_server()

        #  get this started...
        QtCore.QTimer.singleShot(0, self.startApp)


    def startApp(self):

        #  get the available channels
        self.channels = self.client.get_channels()
        print("Available Channels:")
        for chan in self.channels:
            print("    " + chan)

        #  query other various application states and display
        print("Operation Mode:", self.client.get_operation_mode())
        print("Operation State:", self.client.get_operational_state())
        print("Ping Interval:", self.client.get_ping_interval())
        print("Ping Mode:", self.client.get_ping_mode())
        print("Recording Settings:", self.client.get_recording_settings())
        print("Recording Depths")
        for chan in self.channels:
            print("    " + chan + ":", self.client.get_recording_range(chan))

        #  if there are any channels, subscribe to the first channel's bottom detection data
        if len(self.channels) > 0:
            print("Creating bottom depth subscription for channel " + self.channels[0])
            print("Bottom detection data will be displayed as it is received.")
            print("Press <ctrl>-C to exit")
            self.id = self.client.create_bottom_detection_subscription(self.channels[0])
        else:
            print('No channels found. Exiting...')
            QtCore.QCoreApplication.instance().quit()
            return


    def stop_app(self):

        print("Cleaning up the client...")
        self.stopClient.emit()


    @QtCore.pyqtSlot()
    def clientStopped(self):

        print("Client cleanup complete.")
        print("Application exiting...")
        QtCore.QCoreApplication.instance().quit()
        return


    @QtCore.pyqtSlot(object, str, dict)
    def subscriptionDataAvailable(self, clientObj, data_type, data):

        if data_type == 'bottom detection':
            #  print the results
            print(data)


    def external_stop(self):
        '''
        external_stop is called when one of the main thread exit handlers are called.
        It emits a stop signal that is then received by the QCoreApplication which then
        shuts everything down in the QCoreApplication thread.
        '''
        self.stopApp.emit()



def exit_handler(a,b=None):
    '''
    exit_handler is called when CTRL-c is pressed on Windows
    '''
    global ctrlc_pressed

    if not ctrlc_pressed:
        #  make sure we only act on the first ctrl-c press
        ctrlc_pressed = True
        print("CTRL-C detected. Shutting down...")
        console_app.external_stop()

    return True


def signal_handler(*args):
    '''
    signal_handler is called when ctrl-c is pressed when the python console
    has focus. On Linux this is also called when the terminal window is closed
    or when the Python process gets the SIGTERM signal.
    '''
    global ctrlc_pressed

    if not ctrlc_pressed:
        #  make sure we only act on the first ctrl-c press
        ctrlc_pressed = True
        print("CTRL-C or SIGTERM/SIGHUP detected. Shutting down...")
        console_app.external_stop()

    return True


if __name__ == '__main__':
    import sys
    import argparse

    #  by default we will not "clean" all of the subscriptions and endpoints
    #  from the server. Normally you wouldn't want or need to do this but during
    #  application development your application may crash and not clean up
    #  after itself. When this happens, you will not be able to
    clean_server = False

    #  create a state variable to track if the user typed ctrl-c to exit
    ctrlc_pressed = False

    #  Set up the handlers to trap ctrl-c
    if sys.platform == "win32":
        #  On Windows, we use win32api.SetConsoleCtrlHandler to catch ctrl-c
        import win32api
        win32api.SetConsoleCtrlHandler(exit_handler, True)
    else:
        #  On linux we can use signal to get not only ctrl-c, but
        #  termination and hangup signals also.
        import signal
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGHUP, signal_handler)

    #  parse the command line arguments
    parser = argparse.ArgumentParser(description='Example showing a simple usage of the ek80 REST client.')
    parser.add_argument("-s", "--server", help="Specify the EK80 server IP")
    parser.add_argument("-c", "--clean", help="Set to True to remove all server subscriptions before running.")
    args = parser.parse_args()
    if (args.server):
        server_address = str(args.server)
    if (args.clean):
        clean_server = True

    #  create an instance of QCoreApplication and and instance of the our example application
    app = QtCore.QCoreApplication(sys.argv)
    console_app = basic_example(server_address, clean_server=clean_server,
            parent=app)

    #  and start the event loop
    sys.exit(app.exec_())

