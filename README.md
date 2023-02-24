# iphone-system-logs
This simple python app connects to your iPhone's system logs and prints each log as it comes in. There are also instructions for additional software to install before running this app.

## Accessing iPhone logs in xCode
1. Connect your iPhone to your Mac via a wired connection.
2. In xCode, go to <b>Window > Devices</b> and select your connected device (under the <b>Devices</b> tab).
3. Click the <b>Open Console</b> button to view your device's logs.

## Installations For Python Script (MacOS ONLY)
1. Install <b>libimobiledevice</b> (globally) with brew: `brew install libimobiledevice`
2. Get your iPhone's device UDID. This can be accomplished in two ways:
  * Enter `idevice_id --list` and find your device's UDID
  * In xCode under <b>Window > Devices > `<your device>`</b> copy the device's <b>Identifier</b>.
3. Run the following command to view your iPhone's logs in the terminal: `idevicesyslog -u <device udid>`.
4. You should be all set up to run this app! Enjoy!

Sources:
 
[Access iPhone Logs in xCode](https://community.tealiumiq.com/t5/Tealium-for-iOS/How-do-I-access-the-iOS-device-logs/ta-p/16420#:~:text=Answer%201%20Install%20XCode%20on%20your%20computer.%202,on%20the%20device%20will%20be%20displayed%20here.%20)

[Instructions for Installing `libimobiledevice`](https://confusatory.org/post/127183189821/ios-debugging-device-console-without-wires)

[Additional Information on `libimobiledevice`](https://stackoverflow.com/questions/7277804/ios-iphone-ipad-ipodtouch-view-real-time-console-log-terminal)

** Next Step
  * Determine which logs specifically identify the start, close, and focus state of an app.
