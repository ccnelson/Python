
import win32com.client  # you need pywin32 installed

speaker = win32com.client.Dispatch("SAPI.SpVoice")

speaker.Speak("this is, text to speech")
