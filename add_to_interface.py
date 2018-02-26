# $language = "python"
# $interface = "1.0"

# Add command to interfaces


pmt = "#"


def init(obj):
    global crt
    crt = obj
    return


def wait_end():
    crt.Screen.WaitForString("end", 5)
    crt.Screen.WaitForString(pmt, 5)


def wait_exit():
    crt.Screen.WaitForString("exit", 5)
    crt.Screen.WaitForString(pmt, 5)


def modify_iface(name, cmd):
    crt.Screen.Send("interface " + name + "\n")
    crt.Screen.Send(cmd + "\n")
    crt.Screen.Send("exit\n")
    wait_exit()


def main():
    crt.Screen.Synchronous = True
    # Get interfaces list
    if_def_names = crt.Clipboard.Text
    value = crt.Dialog.Prompt("Enter inerfaces names like 'Fa0/1', separated by commas.",
                              "Interfaces list", if_def_names)
    if value == "":
        return False
    if_names = value.encode('ascii', 'ignore').split(",")

    # Get VLAN number
    if_cmd = crt.Dialog.Prompt("Enter command to add.", "Command", "")
    if if_cmd == "":
        return False

    # Do operation

    # crt.Screen.Sendkeys("^U")
    crt.Screen.Send("\nend\n")
    wait_end()

    crt.Screen.Clear()

    crt.Screen.Send("configure terminal\n")
    for if_name in if_names:
        modify_iface(if_name, if_cmd)
    crt.Screen.Send("\nend\n")
    wait_end()
    return


main()
