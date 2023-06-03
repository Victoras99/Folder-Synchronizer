import os
import shutil
from datetime import datetime
import time
import argparse


def empty_replica_folder( replica_folder_path, log ):
    file_list = os.listdir( replica_folder_path )
    for file in file_list:
        p = os.path.join( replica_folder_path, file )
        if os.path.exists( p ):
            message = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            if os.path.isfile( p ):
                os.remove( p )
                message += f' - File { os.path.basename( p ) } removed from { p }\n'
            elif os.path.isdir( p ):
                shutil.rmtree( p )
                message += f' - Directory { os.path.basename( p ) } removed entirely from { p }\n'
            log.write( message )
            print( message )


def create_source_folder_copy( source_folder_path, replica_folder_path, log ):
    for file in os.listdir( source_folder_path ):
        p = os.path.join( source_folder_path, file )
        if os.path.exists( p ):
            message = datetime.now().strftime( '%d/%m/%Y %H:%M:%S' )
            rp = os.path.join( replica_folder_path, file )
            if os.path.isfile( p ):
                shutil.copyfile(p, rp)
                message += f' - { os.path.basename( p ) } file copied from {p} to {rp}.\n'
            elif os.path.isdir( p ):
                shutil.copytree( p, rp )
                message += f' - { os.path.basename( p ) } directory entirely copied from {p} to {rp}.\n'
            print( message )
            log.write(message)


def logfile_text( log ):
    log.write( datetime.now().strftime( '%d/%m/%Y %H:%M:%S' ) + f' - Log file created.\n' )


parser = argparse.ArgumentParser( description = 'Synchronizes two folders, source and replica' )

parser.add_argument('-sdp', '--sourceDirectoryPath', type=str, help='Enter source directory path')
parser.add_argument('-rdp', '--replicaDirectoryPath', metavar='replicaDirectoryPath', type=str, help='Enter replica directory path')
parser.add_argument('-si', '--syncInterval', metavar='syncInterval', type=float, help='Enter synchronization interval')
parser.add_argument('-lp', '--logFilePath', metavar='logFilePath', type=str, help='Enter log file path')

args = parser.parse_args()

sdp = args.sourceDirectoryPath
rdp = args.replicaDirectoryPath
si = args.syncInterval
lp = args.logFilePath


while True:
    with open(lp, 'a') as log:
        if os.path.getsize(lp) != 0:
            log.write(f'\n' * 2)
        print(f'\n')
        log.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S') + f' - SYNCHRONIZATION PROCESS STARTED...\n')
        print(datetime.now().strftime('%d/%m/%Y %H:%M:%S') + f' - SYNCHRONIZATION PROCESS STARTED...\n')
        empty_replica_folder(rdp, log)
        create_source_folder_copy(sdp, rdp, log)
        log.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S') + f' - SYNCHRONIZATION PROCESS FINISHED...\n')
        print(datetime.now().strftime('%d/%m/%Y %H:%M:%S') + f' - SYNCHRONIZATION PROCESS FINISHED...\n')
        time.sleep(si)





