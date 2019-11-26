# PythonCanalyzer

A python implementation to control Vector Canalyzer via Win32Com interface.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Win32Com
```

### Installing


```
pip install pywin32
pip install pypiwin32
```


### This tool will open a CANalyzer configuration, and provide below functionlity:
1. Call CAPL functions;
2. Get CAN bus signal value;
3. Send CAN bus signal value(via CAPL functionlity)

### A demo:
```python
from python_canalyzer import PythonCanalyzer

canalyzer = PythonCanalyzer(r"E:\test\j1939.cfg", capl_path = r"E:\test\Config\Canalyzer\capl.can")
canalyzer.call_capl('CCVS1_RX_SA_232_EngShutdownOverrideSwitch', 3)
canalyzer.get_can_bus_signal_value(0, "DM01_T1", "DTC1")
canalyzer.send_can_bus_signal_value(0, "CCVS1_RX_SA_232", "EngShutdownOverrideSwitch",3)
```


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/sgnes/PythonCanalyzer/tags). 

## Authors

* **Guopeng SUN** - *Initial work* - [Guopeng SUN](https://github.com/sgnes)

See also the list of [contributors](https://github.com/sgnes/PythonCanalyzer/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
