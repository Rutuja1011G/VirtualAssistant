import datetime
import speak
import webbrowser
import weather
import os
import pyjokes
import wikipedia





def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("my name is harry")  
      return "my name is harry"

    elif "hello" in data_btn  or "hiee" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey , How i can  help you !")  
        return "Hey , How i can  help you !" 
    

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days ") 
            return "I am doing great these days "   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure to stay with you")
           return "its my pleasure  to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning , i think you might need some help")
           return "Good morning , i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time)    

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok ")
            return "ok "  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 
    
    elif "good afternoon" in data_btn:
           speak.speak("Good afternoon , i think you might need some help")
           return "Good afternoon, i think you might need some help" 

    elif 'instagram' in data_btn or "open instagram" in  data_btn:
        url= 'https://instagram.com/'        
        webbrowser.get().open(url)
        speak.speak("instagram open") 
        return "instagram open"  

    elif 'open gmail' in data_btn or 'gmail'  in data_btn:
        url = 'https://mail.google.com/'
        webbrowser.get().open(url)
        speak.speak("gmail open")  
        return "gmail open" 

    elif "date" in data_btn:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak.speak(f"Today's date is {current_date}")
        return str(current_date)
    
    elif 'open Google Assistant' in data_btn:
        return "Google Assistant opened"


    elif 'tell me a joke' in data_btn:
        joke = pyjokes.get_joke()
        speak.speak(joke)


    elif 'open Facebook' in data_btn or 'Facebook' in data_btn:
        url = 'https://www.facebook.com/'
        webbrowser.get().open(url)
        speak.speak("Facebook opened")
        return "Facebook opened"
    
    
    elif 'open Amazon' in data_btn or 'Amazon' in data_btn:
        url = 'https://www.amazon.com/'
        webbrowser.get().open(url)
        speak.speak("Amazon opened")
        return "Amazon opened"
    
    elif 'open WhatsApp' in data_btn or 'WhatsApp' in data_btn:
        url = 'https://web.whatsapp.com/'
        webbrowser.get().open(url)
        speak.speak("WhatsApp opened")
        return "WhatsApp opened"
    
    elif 'open AI' in data_btn or 'AI' in data_btn:
         url='https://www.perplexity.ai/'
         webbrowser.ger().open(url)
         speak.speak("AI is ready for you")
         return "AI is ready for you"

    else :
        speak.speak( "i'm unable to understand!")
        return "i'm unable to understand!"       
