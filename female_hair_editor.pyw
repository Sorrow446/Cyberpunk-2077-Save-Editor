import os
import sys

import PySimpleGUI as sg


sg.ChangeLookAndFeel('SystemDefaultForReal')

hairstyles = {
		'hairstyle_01': b'\x58\x3E\x5A\x10\xC1\x06\x93\x6D',
		'hairstyle_02': b'\x99\x7C\x69\x3E\x69\xAB\xAD\x1D',
		'hairstyle_03': b'\x3B\x29\xE5\x71\x96\x43\x99\x31',
		'hairstyle_04': b'\xBE\x6D\x3A\x2C\xDE\xE2\x46\x73',
		'hairstyle_05': b'\x67\xEA\x91\x93\xD2\x6F\xC6\x48',
		'hairstyle_06': b'\xD4\x38\x27\x5F\x5A\xA0\x61\xE6',
		'hairstyle_07': b'\x08\x9E\x7F\xAB\x5B\xD8\x59\x41',
		'hairstyle_08': b'\x28\x01\x92\x5B\xA5\x0E\x6E\xB8',
		'hairstyle_09': b'\xA0\xDB\x70\x21\x00\x67\x98\x12',
		'hairstyle_10': b'\x7F\xFD\x4F\xC9\xA9\x6B\x7D\x3F',
		'hairstyle_11': b'\x13\x31\x40\xFB\x20\x8C\x69\x78',
		'hairstyle_12': b'\xBB\xA2\xE9\x6E\x7C\x9B\x2F\x3A',
		'hairstyle_13': b'\x95\x77\x9C\xCB\xA2\xD1\x60\x7D',
		'hairstyle_14': b'\x55\xB9\xC1\x37\x5A\x6E\xD4\x63',
		'hairstyle_15': b'\x5D\x35\x28\x22\x0A\x67\xCE\x18',
		'hairstyle_16': b'\xF2\xFE\xED\x52\x0E\x3A\x09\xB6',
		'hairstyle_17': b'\x32\xFE\x6B\xD5\xCE\x46\xB9\xF8',
		'hairstyle_18': b'\x62\xCB\xC6\xE4\xE4\x80\xA5\x07',
		'hairstyle_19': b'\x7E\xF0\x66\xDD\x6E\x35\xFF\x00',
		'hairstyle_20': b'\xC8\x04\xF1\x98\xC8\x61\xBB\xE7',
		'hairstyle_21': b'\x3F\x28\x5C\x0B\xAF\x8A\xC1\x0B',
		'hairstyle_22': b'\xBF\x9F\x57\x77\x41\x86\xFD\x28',
		'hairstyle_23': b'\x20\x42\xD6\x1C\x06\xD6\xBB\x58',
		'hairstyle_24': b'\x6D\x26\x49\x31\x39\x6D\x5F\x38',
		'hairstyle_25': b'\xD6\xDE\x0B\xBC\x41\x43\x2F\x96',
		'hairstyle_26': b'\x4E\xBC\x5B\xAB\x53\x90\x82\x31',
		'hairstyle_27': b'\xE3\xBD\xE3\x53\xC5\xC0\xBF\x1D',
		'hairstyle_28': b'\x21\x86\x9C\x7C\x59\xBE\x44\x38',
		'hairstyle_29': b'\xD2\x6D\xE1\xF4\x1B\x80\x90\xDD',
		'hairstyle_30': b'\x71\xC6\x29\x6C\x50\x60\x8A\x2F',
		'hairstyle_31': b'\x29\x20\xBA\x77\x3D\xA5\xC5\x18',
		'hairstyle_32': b'\x4F\x9D\x1D\x9F\x6B\xF4\xAB\x7F',
		'hairstyle_33': b'\x63\xC1\x77\x94\x5E\x24\x1E\x1F',
		'hairstyle_34': b'\x0B\x32\x96\x79\x25\xA2\x95\xAF',
		'hairstyle_35': b'\x55\xB9\xC1\x37\x5A\x6E\xD4\x63',
		'hairstyle_36': b'\x19\x2C\x2C\xCB\xD5\x31\xFA\x05',
		'hairstyle_37': b'\xAA\x39\xBF\x64\x6C\xA2\x97\xDB',
		'hairstyle_38': b'\x85\x24\xF8\xA1\xBD\xC2\x71\x18'
}


def read_img(fname):
	with open(os.path.join('female_hair_editor_data', fname + ".png"), 'rb') as f:
		data = f.read()
	return data

	
def load_save(save_path):
	with open(save_path, 'rb') as f:
		data = f.read()
		start = data.find(b'\x83\x46\x50\x50') + 4
		for k, v in hairstyles.items():
			pos = data.find(v, start)
			if pos == -1:
				continue
			window.Element('hairstyle').Update(data=read_img(k))
			window.Element('hairstyle_drop').Update(k, values=([k for k in hairstyles.keys()]), disabled=False)
			return pos
		sg.Popup('Couldn\'t find bytes.')

def write_save(save_path, pos, data):
	with open(save_path, 'rb+') as f:
		f.seek(pos)
		f.write(data)

if __name__ == "__main__":
	try:
		if hasattr(sys, 'frozen'):
			os.chdir(os.path.dirname(sys.executable))
		else:
			os.chdir(os.path.dirname(__file__))
	except OSError:
		pass
	layout=[
		[sg.Frame(layout=[
			[sg.FileBrowse('Load save', key='browse', enable_events=True)], [sg.Button('Write save', key='write', enable_events=True, disabled=True)],
			[sg.Image(data=read_img('solid'), key='hairstyle')],
			[sg.T('Hairstyle:', font=('Helvetica', 10)), sg.Drop(values=(), size=(20,0), key='hairstyle_drop', disabled=True, enable_events=True)]], title=None)
	]]
	window = sg.Window('GUI', default_element_size=(40, 1)).Layout(layout).finalize()
	while True:
		event, values = window.Read(timeout=100)
		if event in (None, 'Exit'): 
			break
		if event == "browse" and values['browse']:
			pos = load_save(values['browse'])
			if pos:
				window.Element('write').Update(disabled=False)
		elif event == "hairstyle_drop":
			window.Element('hairstyle').Update(data=read_img(values['hairstyle_drop']))
		elif event == "write":
			write_save(values['browse'], pos, hairstyles[values['hairstyle_drop']])
	window.close()