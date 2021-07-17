# -*- coding: utf-8 -*-

"""
ATB-AGAD-DIO Sample code
Copyright 2021 ADVALY SYSTEM Inc.

DI: /sys/devices/soc0/addon/DIx_INTF1/value
DO: /sys/devices/soc0/addon/DOx_INTF1/value

　起動時のSWの状態によってexportされるディレクトリが以下のように変化します。
  - SW1
    DI側 -> DI4、DI5
    DO側 -> DO0
  - SW2
    DI側 -> DI6、DI7
    DO側 -> DO1

  起動時に一度SW1、SW2の値を読んで処理を分岐しており、
  ランタイムでのSWの切り替えには対応しておりません。
"""
import sys
import re


def DI(num):
    """
    Read DI value

    Arguments:
        num   DI port number(0-7)

    Returns:
        int 0/1

    Exceptions:
        ValueError invalue port number
        IOError    failed to read a DI value
    """
    if num < 0 or num > 7:
        raise ValueError('Invalid DI port number')

    value = open('/sys/devices/soc0/addon/DI%d_INTF1/value' % num, 'r').readline()
    return int(value)


def DO(num, outval=None):
    """
    Write DO value.
    If no value is specified, returns current DO value

    Arguments:
        num   DO port number(0-1)
        value Output value

    Returns:
        int 0/1

    Exceptions:
        ValueError invalue port number
        IOError    failed to read a DI value
    """
    if num < 0 or num > 1:
        raise ValueError('Invalid DO port number')

    if outval == None:
        value = open('/sys/devices/soc0/addon/DO%d_INTF1/value' % num, 'r').readline()
    elif outval == 0 or outval == 1:
        open('/sys/devices/soc0/addon/DO%d_INTF1/value' % num, 'w').write(str(outval))
        value = outval
    else:
        raise ValueError('Invalid DO value')

    return int(value)


def main():
    # Parse command line arguments
    for arg in sys.argv[1:]:
        m = re.match('^[dD][oO]([01])=([01])$', arg)
        if m:
            # Set DO
            num = int(m.group(1))
            val = int(m.group(2))
            try:
                DO(num, val)
            except (ValueError, IOError):
                print('Set DO%d = (failed to write)' % num)
            else:
                print('Set DO%d = %d' % (num, val))

        else:
            # Error
            print('Invalid argment.')
            print('  ex. python %s' % sys.argv[0])
            print('      python %s DO[0|1]=[0|1]' % sys.argv[0])
            sys.exit(1)

    print('\n- List of current port status -')

    # Read DI
    for i in range(8):
        try:
            dival = DI(i)
        except (ValueError, IOError):
            print('DI%d = (failed to read)' % i)
        else:
            print('DI%d = %d' % (i, dival))

    # Read DO
    for i in range(2):
        try:
            doval = DO(i)
        except (ValueError, IOError):
            print('DO%d = (failed to read)' % i)
        else:
            print('DO%d = %d' % (i, doval))


if __name__ == '__main__':
    main()
