from midiutil import MIDIFile
from io import BytesIO
memFile = BytesIO()
address = input("Enter the address :")
address_letters = []
address_numbers = []

def splitString(str):
     
    alpha = ""
    num = ""
    for i in range(len(str)):
        if (str[i].isdigit() and str[i]!= '0'):
            num = num+ str[i]
        elif((str[i] >= 'A' and str[i] <= 'F') or
             (str[i] >= 'a' and str[i] <= 'f')):
            alpha += str[i]
    global address_letters
    address_letters = list(alpha)
    global address_numbers
    address_numbers = list(num)


splitString(address)
#print(address_numbers)
#print(address_letters)
address_duration = address_numbers[:len(address_letters)]
address_plugin = address_numbers[len(address_letters):]
print(address_duration)
print(address_plugin)
for i in range(len(address_letters)):
    if(address_letters[i] == 'a'):
        address_letters[i] = 57
    if(address_letters[i] == 'b'):
        address_letters[i] = 59
    if(address_letters[i] == 'c'):
        address_letters[i] = 60
    if(address_letters[i] == 'd'):
        address_letters[i] = 62
    if(address_letters[i] == 'e'):
        address_letters[i] = 64
    if(address_letters[i] == 'f'):
        address_letters[i] = 65
#print(address_letters)
#degrees  = [60, 62, 64, 65, 67, 69, 71, 72] # MIDI note number
track    = 0
channel  = 0
time     = 0   # In beats
tempo    = 60  # In BPM
volume   = 100 # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(track,time, tempo)
i = 0
for pitch in address_letters:
    duration = address_duration[i]
    #print(type(duration))
    #MyMIDI.addNote(track, channel, pitch, time, int(duration), volume)
    r = 1/int(duration)
    for j in range(int(duration)):
        MyMIDI.addNote(track, channel, pitch, time, int(duration), volume)
        time = time + r
    i+=1
    time = time + 0.4

#with open("track.mid", "wb") as output_file:
#    MyMIDI.writeFile(output_file)
MyMIDI.writeFile(memFile)
import pygame
import pygame.mixer
from time import sleep

pygame.init()
pygame.mixer.init()
memFile.seek(0)  # THIS IS CRITICAL, OTHERWISE YOU GET THAT ERROR!
pygame.mixer.music.load(memFile)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(0.00000005)
print ("Done!")