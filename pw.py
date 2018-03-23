#! python3
# pw.py - An insecure password locker program.
# pw.bat - saved in somewhere where defined in PATH user variable

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys,subprocess
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

if len(sys.argv) < 2:
    print('Usage: "pw <account>" - copy <account> password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name

if account in PASSWORDS:
    copy2clip(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)