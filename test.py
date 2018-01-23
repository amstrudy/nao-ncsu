from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "192.168.2.3", 9559)
tts.say("Hello, World!")
