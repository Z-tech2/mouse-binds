from multiprocessing import Process
from ctypes import windll

VK_XBUTTON2 = 0x06
VK_XBUTTON1 = 0x05

def get_key_state(v_key: int) -> bool:
    return bool(windll.user32.GetKeyState(v_key) & 0x80)


def one():
	while True:
	    if get_key_state(VK_XBUTTON2):
	        while get_key_state(VK_XBUTTON2):
	            # do stuff

def two():
	while True:
	    if get_key_state(VK_XBUTTON1):
	        while get_key_state(VK_XBUTTON1):
	            # do stuff

if __name__ == '__main__':
    Process(target=one).start()
    Process(target=two).start()
