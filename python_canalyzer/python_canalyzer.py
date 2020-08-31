import logging
from win32com.client import DispatchEx
import win32com
import time
import re
import sys

CANalyzer = None

class MeasEvents:

    def OnInit(self):
        global  CANalyzer
        CANalyzer.update_capl_funs()


class PythonCanalyzer(object):
    """

    """

    def __init__(self, canalyzer_config_path, capl_path=None, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self._capl_funcs = {}
        self._capl_path = capl_path
        self._CANalyzer = DispatchEx('CANalyzer.Application')
        self._CANalyzer.Open(canalyzer_config_path)
        if self._capl_path is not None:
            PythonCanalyzer._capl_names = self._get_capl_fun_names()
            self._CANalyzer.CAPL.Compile()
        global  CANalyzer
        CANalyzer = self
        self._event_handler = win32com.client.WithEvents(self._CANalyzer.Measurement, MeasEvents)
        self._CANalyzer.UI.Write.Output('measurement starting...')
        self._CANalyzer.Measurement.Start()
        while (not self._CANalyzer.Measurement.Running):
            time.sleep(1)
        self._CANalyzer.UI.Write.Output('measurement started...')
        self.logger.info("Canalyzer measurement started.")


    def close(self):
        self._CANalyzer.Quit()



    def _get_capl_fun_names(self):
        re_exp = "^(void|int|byte|word|dword|long|int64|qword)\s+([a-zA-Z0-9_]+)\s*\((void|int|byte|word|dword|long|int64|qword|float)\s*"
        names = []
        with open(self._capl_path) as capl:
            text = capl.read()
            res = re.findall(re_exp, text, re.M)
            names = [i[1] for i in res]
            self.logger.debug("CAPL functions:{0}".format(names))
        return names

    def get_capl_names(self):
        return self._capl_names

    def update_capl_funs(self):
        for name in PythonCanalyzer._capl_names:
            obj = self._CANalyzer.CAPL.GetFunction(name)
            self._capl_funcs[name] = obj

    def get_capl_func(self, name):
        if name in self._capl_funcs:
            return self._capl_funcs[name]
        else:
            return  None

    def get_can_bus_signal_value(self, ch, msg, signal):
        res = float(str(self._CANalyzer.Bus.GetSignal(ch, msg, signal)))
        return res

    
    def send_can_bus_signal_value(self, ch, msg, sig, value):
        """
        """
        ret_value = 0
        name = msg + "_" + sig 
        if name in self._capl_funcs:
            func = self._capl_funcs[name]
            if value:
                func.Call(value)
            else:
                func.Call()
            ret_value = 1
        else:
            ret_value = 0
            self.logger.error("{} CAPL function:{} not founded.".format(sys._getframe().f_code.co_name, name))
            raise NameError
        return ret_value
    
    def call_capl(self, name, value):
        ret_value = 0
        if name in self._capl_funcs:
            func = self._capl_funcs[name]
            if value:
                func.Call(value)
            else:
                func.Call()
            ret_value = 1
        else:
            ret_value = 0
            self.logger.error("{} CAPL function:{} not founded.".format(sys._getframe().f_code.co_name, name))
            raise NameError
        return ret_value

