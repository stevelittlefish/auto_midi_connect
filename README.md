# auto_midi_connect
Automatically connect midi usb devices using ALSA (aconnect)

Simply run the script (with no arguments) and will automatically map every MIDI device onto every other MIDI device.

On my raspberry pi I set a udev rule (committed in this repository) to fire whenever any USB device is plugged in and run
the script.  I also had to set it to run once on startup so that devices that are already plugged in on boot will also be
routed properly.

If installing this on a raspberry pi you might want to make your filesystem readonly by following this tutoiral:
https://medium.com/@andreas.schallwig/how-to-make-your-raspberry-pi-file-system-read-only-raspbian-stretch-80c0f7be7353
as this will allow you to just unplug it to turn it off, instead of having to SSH onto the pi and shut it down properly!
