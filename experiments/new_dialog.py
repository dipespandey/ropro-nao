#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Using ALDialog Methods"""
from naoqi import ALProxy
import qi
import argparse
import sys
import paramiko

def main(session, topic_path, upload_dialog='n'):
    """
    This example uses ALDialog methods.
    It's a short dialog session with one topic.
    """
    # Getting the service ALDialog

    # upload the file to the robot using SSH (paramiko)
    # if upload_dialog in ['y', 'Y']:
    upload_file(topic_path)

    ALDialog = session.service("ALDialog")
    ALDialog.setLanguage("English")

    # Loading the topic given by the user (absolute path is required)
    topf_path = topic_path.decode('utf-8')
    topic_name = ALDialog.loadTopic(topf_path.encode('utf-8'))

    # Activating the loaded topic
    ALDialog.activateTopic(topic_name)

    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated
    ALDialog.subscribe('my_dialog_example')


    try:
        raw_input("\nSpeak to the robot using rules from the just loaded .top file. Press Enter when finished:")
    finally:
        # stopping the dialog engine
        ALDialog.unsubscribe('my_dialog_example')

        # Deactivating the topic
        ALDialog.deactivateTopic(topic_name)

        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload our topic and free the associated memory
        ALDialog.unloadTopic(topic_name)


def upload_file(source):
    username = 'nao'
    password='nao'
    host = '192.168.137.213'
    port=22
    file_name = source.split('/')[-1]
    destination = '/home/nao/.local/share/PackageManager/apps/{fn}'.format(fn=file_name)
    transport = paramiko.Transport((host,port))
    transport.connect(None,username,password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(source, destination)
    # Close
    print('done')
    if sftp: sftp.close()
    if transport: transport.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.137.213",
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")
    parser.add_argument("--topic-path", type=str, required=True,
                        help="absolute path of the dialog topic file (on the robot)")
    # parser.add_argument("-upload-dialog", type=str, default='n', required=True,
    #                     help="want to upload the topic file to the robot?")
    args, unknown = parser.parse_known_args()
    session = qi.Session()
    try:
        session.connect("tcp://{}:{}".format(args.ip, args.port))
    except RuntimeError:
        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.\n".format(args.ip, args.port))
        sys.exit(1)
    # options = parser.parse_args()
    # print(args.upload_dialog)
    postureProxy = ALProxy("ALRobotPosture", args.ip, 9559)
    if postureProxy.getPosture() != 'Stand':
        postureProxy.goToPosture("Stand", 1.0)
    main(session, args.topic_path)
