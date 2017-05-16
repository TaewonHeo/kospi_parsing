import win32service
import win32serviceutil
import win32event


class PySvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "PySvc"
    _svc_display_name_ = "Python Test Service"
    _svc_description_ = "This service writes stuff to a file"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        # create an event to listen for stop requests on
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)


    def SvcDoRun(self):
        import servicemanager
        import time
        f = open('./Adress.txt', 'w')

        f.write(time.time())


        # rc = None
        #
        # # if the stop event hasn't been fired keep looping
        # while rc != win32event.WAIT_OBJECT_0:
        #     f.write('TEST DATA\n')
        #     f.flush()
        #     # block for 5 seconds and listen for a stop event
        #     rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)
        #
        # f.write('SHUTTING DOWN\n')
        # f.close()

    def SvcStop(self):
        # tell the SCM we're shutting down
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PySvc)