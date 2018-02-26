# $language = "python"
# $interface = "1.0"

# Add or remove VLAN form trunk interfaces


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


def modify_iface(name, vid, cmd):
    crt.Screen.Send("interface " + name + "\n")
    crt.Screen.Send("switchport trunk allowed vlan " + cmd + " " + str(vid) + "\n")
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
    value = crt.Dialog.Prompt("Enter VLAN number.", "VLAN", "1")
    if value == "":
        return False
    vlan_id = int(value)

    # Select operation
    btn_id = crt.Dialog.MessageBox(
        "Select YES to add or NO to remove VLAN ID:"+str(vlan_id)+" to interfaces:\n"+str(if_names)[1:-1],
        "Chose acton", BUTTON_YESNOCANCEL | ICON_QUESTION)
    if btn_id == IDYES:
        vlan_cmd = "add"
    elif btn_id == IDNO:
        vlan_cmd = "remove"
    else:
        return False

    # Do operation

    # crt.Screen.Sendkeys("^U")
    crt.Screen.Send("\nend\n")
    wait_end()

    crt.Screen.Clear()

    crt.Screen.Send("show vlan id " + str(vlan_id) + "\n")
    crt.Screen.WaitForString(pmt, 10)
    crt.Screen.Send("configure terminal\n")
    for if_name in if_names:
        modify_iface(if_name, vlan_id, vlan_cmd)
    crt.Screen.Send("\nend\n")
    wait_end()
    crt.Screen.Send("show vlan id " + str(vlan_id) + "\n")
    crt.Screen.WaitForString(pmt, 10)
    return


main()
