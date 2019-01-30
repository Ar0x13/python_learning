#!/usr/bin/env python

import os
import sys 
import argparse
import tempfile

parser = argparse.ArgumentParser(description='Key-value storage')
parser.add_argument('-k','--key', help='Storage key', required=True)
parser.add_argument('-v','--val', help='Key value')
args = parser.parse_args()
print(args.key)
print(args.val)


def read_tmp_file():
    print("Current temp directory:", tempfile.gettempdir())
    try:
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    except:
        print("Cannot find tmp file or folder!")

def insert_data(key, value):
	data = {}
	data[key]=value
	with open(storage_path, 'w') as f:
		f.write(json.dumps(data)) 


def print_data(key, value=None):
	with open(storage_path, 'w') as f:
		print(f.read)



def main():
    print("Number of arguments: ", len(sys.argv))
    print("Argument List: ", str(sys.argv))
    read_tmp_file()
    # if len(sys.argv) == 3:
    #     print_data()
    if len(sys.argv) == 5:
    	insert_data()

    
if __name__ == '__main__':
    main()
