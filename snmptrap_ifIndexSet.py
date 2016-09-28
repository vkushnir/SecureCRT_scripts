# $language = "python"
# $interface = "1.0"

# Fix snmp mib interface index and find its value on CISCO devices

pmt = "#"

def waitEnd():
    crt.Screen.WaitForString("end", 5)
    crt.Screen.WaitForString(pmt, 5)

def ifSet(ifName):
    crt.Screen.Send("configure terminal\n")
    crt.Screen.Send("interface " + ifName + "\n")
    crt.Screen.Send("snmp ifindex persist\n")
    crt.Screen.Send("snmp trap link-status\n")
    crt.Screen.Send("end\n")
    waitEnd()

    crt.Screen.Send("\nshow snmp mib ifmib traps | i " + ifName + "\n")
    crt.Screen.Send("\nshow snmp mib ifmib ifindex " + ifName + "\n")
    crt.Screen.WaitForString(pmt, 5)

    crt.Screen.Send("write memory")
    return None

def ifClear(ifName):
    crt.Screen.Send("configure terminal\n")
    crt.Screen.Send("interface " + ifName + "\n")
    crt.Screen.Send("snmp ifindex clear\n")
    crt.Screen.Send("end\n")
    waitEnd()

    crt.Screen.Send("\nshow snmp mib ifmib traps | i " + ifName + "\n")
    crt.Screen.Send("\nshow snmp mib ifmib ifindex " + ifName + "\n")
    crt.Screen.WaitForString(pmt, 5)

    crt.Screen.Send("write memory")
    return None

def main():
    crt.Screen.Synchronous = True
	# Prompt for a interface name
	#
    ifdName = var = crt.Clipboard.Text

    ifName = crt.Dialog.Prompt("Enter inerface name like 'Fa0/1'", "ifName", ifdName)
    if ifName == "":
        return False

    # crt.Screen.Sendkeys("^U")
    crt.Screen.Send("\nend\n")
    waitEnd()

    crt.Screen.Clear()

    cmd = "show interfaces " + ifName + " description"
    crt.Screen.Send("\n\n\n\n\n\n\n\n" + cmd + "\n")
    crt.Screen.WaitForString(cmd, 5)
    crt.Screen.WaitForString(pmt, 5)

    mode = crt.Dialog.MessageBox("Setup or Clear interface " + ifName + " ifindex persist",
                          "SNMP IFINDEX", ICON_QUESTION | BUTTON_YESNOCANCEL | DEFBUTTON3)
    if mode == IDYES:
        ifSet(ifName)
    elif mode == IDNO:
        ifClear(ifName)
    else:
        return False

main()
