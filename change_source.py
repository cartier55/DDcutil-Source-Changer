import subprocess as sp 
import time

def get_source(passwd):
    sp.check_output(f"echo {passwd} | sudo -S ls", shell=True)
    source = sp.check_output(['sudo', 'ddcutil', 'getvcp', '0x60'], text=True)
    source = source.split()
    source = source[-2]
    return (source,passwd)

def change_source(tup):
    sp.check_output(['echo', tup[1], '|', 'sudo', '-S', 'ls'])
    if tup[0] == 'HDMI-1':
        change = sp.check_output(['sudo','ddcutil','setvcp', '0x60', '0x11'], text=True)
        if 'succeeded' in change:
            print('Jumping to HDMI-1.....')
    elif tup[0] == 'HDMI-2':
        change = sp.check_output(['sudo','ddcutil','setvcp', '0x60', '0x0f'], text=True)
        if 'succeeded' in change:
            print('Jumping to HDMI-2.....')
    return

def main():
    tup = get_source('omgawolf')
    change_source(tup)



if __name__ == "__main__":
    main()
