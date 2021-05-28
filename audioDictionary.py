import pyttsx3
from PyDictionary import PyDictionary


class Speaking:

	def speak(self, audio):

		
		engine = pyttsx3.init('sapi5')

		voices = engine.getProperty('voices')

		engine.setProperty('voice', voices[0].id)
		engine.say(audio)
		engine.runAndWait()


class Interacting:
	def Dictionary(self):
		speak = Speaking()
		dic = PyDictionary()
		speak.speak("Hi ther Which word do u want to find the meaning.")

		query = str(input())
		word = dic.meaning(query)
		print(len(word))

		for state in word:
			print(word[state])
			speak.speak("the meaning is" + str(word[state]) + "Thank you for using me! Have a graet day")


if __name__ == '__main__':
	Interacting()
	Interacting.Dictionary(self=None)
