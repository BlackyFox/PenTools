# PenTools                 [![Build Status](https://travis-ci.org/BlackyFox/PenTools.svg?branch=master)](https://travis-ci.org/BlackyFox/PenTools)
Script getting and installing usefull tools for pentesting

## Usage
Right now, the script has only been tested on Kali.2016.2. Execution might not be as expected on other distributions.

To get the tools latests versions from their git (clone them into /opt):
```bash
python get_tools.py -g gitList.csv
```

To get them in a different path:
```bash
python get_tools.py -g gitList.csv -p PATH
```

To start the auto-config mode:
```bash
python get_tools.py -g gitList.csv -c
```
Note that the configuration must be written in the CSV file.

## Personalize
You can easily add or delete some tools just by modifying the CSV file.

When you are doing it, you must keep in mind the following rules:
* The order is the following: url, name, setup commands
* Always use double quotes `"` and not simple ones
* Always use a comma (`,`) to separate the objects
* If no configuration is requiered for installation, enter "NA" in the _setup_ column
* If different steps are required, use `&&`
* Note that every configuration are made inside the tool's directory

## Credits
This tool collects various tools during its process. Those ones are the following:
* [AD Control Path](https://github.com/ANSSI-FR/AD-control-paths)
* [Brutescrape](https://github.com/cheetz/brutescrape)
* [CMSmap](https://github.com/Dionach/CMSmap)
* [Discover](https://github.com/leebaird/discover)
* [Easy-P](https://github.com/cheetz/Easy-P)
* [EyeWitness](https://github.com/ChrisTruncer/EyeWitness)
* [gitrob](https://github.com/michenriksen/gitrob)
* [HTTPScreenshot](https://github.com/breenmachine/httpscreenshot)
* [icmpshock](https://github.com/cheetz/icmpshock)
* [libesedb](https://github.com/libyal/libesedb)
* [mimikatz](https://github.com/gentilkiwi/mimikatz)
* [net-creds](https://github.com/DanMcInerney/net-creds)
* [nishang](https://github.com/samratashok/nishang)
* [nishang (cheetz' fork)](https://github.com/cheetz/nishang)
* [PowerSploit](https://github.com/PowerShellMafia/PowerSploit)
* [PowerTools](https://github.com/PowerShellEmpire/PowerTools)
* [predasploit](https://github.com/MooseDojo/praedasploit)
* [rawr](https://bitbucket.org/al14s/rawr)
* [recon-ng](https://bitbucket.org/LaNMaSteR53/recon-ng)
* [reddit_xss](https://github.com/cheetz/reddit_xss)
* [Responder](https://github.com/SpiderLabs/Responder)
* [SecLists](https://github.com/danielmiessler/SecLists)
* [SET](https://github.com/trustedsec/social-engineer-toolkit)
* [sparta](https://github.com/SECFORCE/sparta)
* [spiderfoot](https://github.com/smicallef/spiderfoot)
* [sqlmap](https://github.com/sqlmapproject/sqlmap)
* [Veil](https://github.com/Veil-Framework/Veil)
* [wifiphisher](https://github.com/sophron/wifiphisher)
* [wifite](https://github.com/derv82/wifite)

## License

MIT License

Copyright (c) 2016 BlackyFox

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
