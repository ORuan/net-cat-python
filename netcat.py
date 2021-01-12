import sys, socket, getopt, subprocess, threading


#Define variables utils for us

listen = False
command = False
upload = False
execute = ''
target = ''
upload_destination = ''
port = 0


#Function responsible for inform about usage of command line and arguments
def usage():
    print('Ruan Pablo NetCat - python3')
    print(' ')
    pritn('Usage: netcat.py -t target_host -p port')
    pritn('-l --listen       - listen in [host]:[port] for incoming connections')
    pritn('-e --execute=file_to_run - execute for given file upon receiving a connection')
    print("-u --upload=destination - upon receiving connection upload a ¬ file and write to [destination]")
    print("-c --command - initialize a command shell")
    print("Examples: ")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
    print("echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135")                                                
    sys.exit(0)