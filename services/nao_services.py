import argparse
from naoqi import ALProxy


def speak(text):
    tts = ALProxy("ALTextToSpeech", "192.168.137.202", 9559)
    tts.say(str(text))

def move_a_little(dist):
    tts = ALProxy("ALTextToSpeech", "192.168.137.202", 9559)
    motion = ALProxy("ALMotion", "192.168.137.202", 9559)
    tts.say("Moving 20 centimeters")
    motion.moveTo(dist, 0, 0)
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--text", type=str,
#                         help="Specify what you want the robot to speak")
    
#     args = parser.parse_args()
#     speak(args.text)