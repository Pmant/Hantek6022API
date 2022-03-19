__version__ = '2.10.1'


from setuptools import setup
import os

setup(
    name='hantek6022api',
    author='Ho-Ro',
    author_email='horo@localhost',
    description='Python API and better FW for Hantek 6022 USB Oscilloscopes',
    long_description=
'''A Python API, tools for calibration, data capturing and visualisation
as well as an improved FW for Hantek 6022 USB Oscilloscopes''',
    platforms=['all'],
    version=__version__,
    license='GPLv2',
    url='https://github.com/Ho-Ro/Hantek6022API',
    packages=['PyHT6022', 'PyHT6022.Firmware'],
    package_data={'PyHT6022': [os.path.join('Firmware', 'DSO6022BE', 'dso6022be-firmware.hex'),
                               os.path.join('Firmware', 'DSO6022BL', 'dso6022bl-firmware.hex'),
                               os.path.join('Firmware', 'DSO6021', 'dso6021-firmware.hex'),
                               os.path.join('Firmware', 'DDS120', 'dds120-firmware.hex'),
                               os.path.join('Firmware', 'modded', 'mod_fw_01.ihex'),
                               os.path.join('Firmware', 'modded', 'mod_fw_iso.ihex'),
                               os.path.join('Firmware', 'stock', 'stock_fw.ihex'),]
    },
    include_package_data=True,
    install_requires=['libusb1']
)
