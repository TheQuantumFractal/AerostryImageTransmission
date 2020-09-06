Setting up access point on Raspberry Pi:
$ sudo apt install hostapd
$ sudo systemctl unmask hostapd
$ sudo systemctl enable hostapd
$ sudo apt install dnsmasq
$ sudo printf "\ninterface wlan0\n    static ip\_address=192.168.4.1/24\n    nohook wpa\_supplicant" >> /etc/dhcpcd.conf
$ sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
$ sudo printf "interface=wlan0\ndhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h\ndomain=wlan\naddress=/gw.wlan/192.168.4.1"
$ sudo rfkill unblock wlan

$ sudo nano /etc/hostapd/hostapd.conf
WRITE:
country\_code=US
interface=wlan0
ssid=Aerostry
hw\_mode=g
channel=7
macaddr\_acl=0
auth\_algs=1
ignore\_broadcast\_ssid=0
wpa=2
wpa\_passphrase=GoCalBears
wpa\_key\_mgmt=WPA-PSK
wpa\_pairwise=TKIP
rsn\_pairwise=CCMP

$ sudo systemctl reboot

Refer to [this](https://www.raspberrypi.org/documentation/configuration/wireless/access-point-routed.md)
