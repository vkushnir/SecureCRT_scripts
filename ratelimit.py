# $language = "python"
# $interface = "1.0"

"""
 This python module is used in SecureCRT
 for generate rate_limit values.

 Written by : Vladimir Kushnir
 Created date: 06.12.2016
 Last modified: 05.12.2016
"""
pmt = "#"

def main():
    crt.Screen.Synchronous = True
	# Prompt for a interface name
	#
    clip = var = crt.Clipboard.Text

    str_kbps = crt.Dialog.Prompt("Specify receive-side bandwidth in kilobits\n(to remove enter negate value)", "Bandwith", clip)
    try:
        kbps = int(str_kbps)
    except ValueError:
        return False

    if kbps < 0:
        strno = "no "
    else:
        strno = ""
    kbps = abs(kbps)

    # Calculate ratelimit values
    burst_time = 1.5
    bps = kbps * 1000
    burst_normal = int(round(bps / 8 * burst_time, 0))
    burst_max = 2 * burst_normal

    # Write ratelimit
    strb = strno + "bandwidth {0:d}\n"
    stri = strno + "rate-limit input {0:d} {1:d} {2:d} conform-action transmit exceed-action drop\n"
    stro = strno + "rate-limit output {0:d} {1:d} {2:d} conform-action transmit exceed-action drop\n"
    crt.Screen.Send(strb.format(kbps))
    crt.Screen.Send(stri.format(bps, burst_normal, burst_max))
    crt.Screen.Send(stro.format(bps, burst_normal, burst_max))

    crt.Screen.WaitForString(pmt, 5)

main()
