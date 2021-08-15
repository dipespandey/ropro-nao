#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Using ALDialog Methods"""

import qi
import argparse
import sys
import time

def main(session):
    """
    This example uses ALDialog methods.
    It's a short dialog session with two topics.
    """
    # Getting the service ALDialog
    ALDialog = session.service("ALDialog")
    ALDialog.setLanguage("English")

    # writing topics' qichat code as text strings (end-of-line characters are important!)
    topic_content_1 = ('topic: ~example_topic_content()\n'
                       'language: enu\n'
                       'concept:(food) [fruits chicken beef eggs]\n'
                       'u: (I [want "would like"] {some} _~food) Sure! You must really like $1 .\n'
                       'u: (how are you today) Hello human, I am fine thank you and you?\n'
                       'u: (Good morning Nao did you sleep well) No damn! You forgot to switch me off!\n'
                       'u: ([e:FrontTactilTouched e:MiddleTactilTouched e:RearTactilTouched]) You touched my head!\n')

    topic_content_2 = ('topic: ~dummy_topic()\n'
                       'language: enu\n'
                       'u:(test) [a b "c d" "e f g"]\n')

    topic_content_1 = ('topic: ~example_topic_content()\n'
                       'language: enu\n'
                       'concept:(food) [fruits chicken beef eggs]\n'
                       'u: (I [want "would like"] {some} _~food) Sure! You must really like $1 .\n'
                       'u: (how are you today) Hello human, I am fine thank you and you?\n'
                       'u: (Good morning Nao did you sleep well) No damn! You forgot to switch me off!\n'
                       'u: ([e:FrontTactilTouched e:MiddleTactilTouched e:RearTactilTouched]) You touched my head!\n')
    
    topic_content_3 = ('topic: ~maths_quiz()\n'
                       'language: enu\n'
                        'u:(Hi NAO) Hi little human. Would you like to play a maths quiz?\n'
                        'u1:(_[yes ok sure whynot]) Ok, I will ask you a few questions. You have 10 seconds to answer each of them. \
                                                    Let us go. What is three times fifty divided by ten? You have ten seconds to answer\n'
                            'u2:(*) The right answer is fifteen. Question two. what is two multiplied by sixteen divided by four?\n'
                                'u3:(*) The right answer is eight. Question three. what is one forth of sixteen?\n'
                                   'u4:(*) The right answer is four. Thank you for playing.\n'
                        'u1:(_[no notnow iwillpass]) Sorry, I will try to come up with something interesting for you next time\n')
                        
    # Loading the topics directly as text strings
    topic_name_1 = ALDialog.loadTopicContent(topic_content_1)
    topic_name_2 = ALDialog.loadTopicContent(topic_content_2)
    topic_name_3 = ALDialog.loadTopicContent(topic_content_3)

    # Activating the loaded topics
    ALDialog.activateTopic(topic_name_1)
    ALDialog.activateTopic(topic_name_2)
    ALDialog.activateTopic(topic_name_3)

    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated
    ALDialog.subscribe('my_dialog_example')

    try:
        raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:")
    finally:
        # stopping the dialog engine
        ALDialog.unsubscribe('my_dialog_example')

        # Deactivating all topics
        ALDialog.deactivateTopic(topic_name_1)
        ALDialog.deactivateTopic(topic_name_2)

        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload all topics and free the associated memory
        ALDialog.unloadTopic(topic_name_1)
        ALDialog.unloadTopic(topic_name_2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default='192.168.137.213',
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://{}:{}".format(args.ip, args.port))
    except RuntimeError:
        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.\n".format(args.ip, args.port))
        sys.exit(1)
    main(session)
