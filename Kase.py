#Sesli asistan Basit - Alperen T
#Öncelikle kütüphanelerimizi yükliyelim.
import speech_recognition as sr #Ses tanıma kütüphanesini sr olarak kısaltıyoruz.
from datetime import datetime #tarih kütüphanesi sayesinde saati öğrenebiliriz.
import webbrowser #webbrowser sayesinde aramalarda bilgisiyarın web tarayıcısını kullanıcaz.
import time #time modülü sayesinde karışıklıktan kurtuluyoruz.
from playsound import playsound #Bu kütüphanemiz sayesinde ses dosyalarını çalabiliriz.
from gtts import gTTS #Google sesli asistan kütüphanesini kuruyoruz sayesinde yazılarımız artık sesli!
import random #Daha ilginç cevap ve diyologlar için random kullanıyoruz.
import os #Os modülü sayesinde dosyaları yönetebiliyoruz

r = sr.Recognizer() #ses dönütlerini almak için bir değişken belirliyoruz.

def kayıt(ask = False): #Burada ask = false dememizin sebebi her zaman soru sormıcak olmamız eğer bunu eklemessek program açıldığı anda sonuca varmaya çalışır.
    with sr.Microphone() as source: #Mikrafondan alınanları işliyoruz.
        if ask: #sorumuz True olunca
            print(ask) #Sorumuzu ekrana yazıyoruz.
        audio = r.listen(source) #Dediklerimizi dinletiyoruz.
        voice = '' #Burada tanımlama kısmını boş yapma sebebimiz karşışıklık olmasını engellemek.
        try: #Eğer program dediğimizi anlamassa diye try kullanıyoruz.
            voice = r.recognize_google(audio , language=("tr-TR")) #programın dediklerimizi tanımlaması için googledan yardım alıyoruz.
        except sr.UnknownValueError: #Eğer kelimelerimizi anlıyamassa diye bir dönüt koyuyoruz.
            speak("anlıyamadım") #Dönüt
        except sr.RequestError:#Sistemde bir sorun olursa diye dönüt koyuyoruz
            speak("sistem çalışmıyor") #Dönüt
        return(voice) #Tanımlamaya dönüyoruz.

def response(voice): #Tanımladıklarımızı işlemek için Fonksiyon kullanıyoruz.
    if "nasılsın" in voice: #Eğer tanımladıklarımızın içinde bu tanım varsa 
        speak("iyi ")
    if "saat kaç" in voice:#Eğer tanımladıklarımızın içinde bu tanım varsa 
        speak(datetime.now().strftime("%H:%M:%S"))
    if "arama yap" in voice:#Eğer tanımladıklarımızın içinde bu tanım varsa 
        search = kayıt("Ne aramamı istersiniz?")
        speak("Ne aramamı istersiniz?")
        url = "https://google.com/search?q="+search
        webbrowser.get().open(url)
        speak(search + "bulduklarım")
    if "eyvallah" in voice:#Son olarak bir çıkış koymalıyız.
        speak("önemli değil görüşürüz :)")
        time.sleep(1)
        time.sleep(1)
        exit() #çıkış
    if "seni kim yaptı" in voice:
        speak("Beni Alperen Türk yaptı!")
    if "nası gidio" in voice:
        speak("iyi gidiyor senin nasıl gidiyor?")
    if "benimde iyi" in voice:
        speak("Bunu duyduğuma sevindim!")
    if "iyi" in voice:
        speak("Bunu duyduğuma sevindim!")
    if "kötü" in voice:
        speak("Bunu duyduğuma üzüldüm yapabileceğim bişey varmı?")
    if "canın Sağolsun" in voice:
        speak("Beni çok üzüyorsun")
    if "nerelisin" in voice:
        speak("İnternetli peki sen nerelisin?")
    if "konyalı" in voice:
        speak("Konyalıları severim, Benim yapımcımda konyalı")
    if "ıspartalı" in voice:
        speak("ıspartalılar bir garip oluyor")
    if "bilgisiyarım ne durumda" in voice:
        speak("Yapımcımın githubına gidip bilgisiyar programını indirebilirsin")
    if "ping" in voice:
        speak("Yapımcımın githubında bir ping uygulaması var kesinlikle denemelisin!")
    if "renk" in voice:
        speak("en sevdiğim renk mavi peki seninki")
    if "kırmızı" in voice:
        speak("o rengi hiç sevmem")
    if "kahverengi" in voice:
        speak("o rengi de severim ama mavi kadar değil!")
    if "sen nesin" in voice:
        speak("Bende bilmiyorum be olduğumu")
    if "lol" in voice:
        speak("o oyun çok kanser diye duydum")
    if "şarkı aç" in voice:
        speak("Şuan ki versiyonumda sadice 1 şarkı var oda mehter marşı")
        time.sleep(0.5)
        speak("Sanırım onu açmamı istersin")
        playsound("mehter.mp3")
    if "mehter aç" in voice:
        speak("HEMEN AÇIYORUM")
        playsound("mehter.mp3")
def speak(string): #Ses dosyalarını oynatırken hata olamamısı için speak fonksiyonunu kullanıyoruz
    tts = gTTS(string,lang="tr") #Türkç konuşmasını ayarlıyoruz
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3" #Dosya türünü ayarlıyoruz.
    tts.save(file) #Dosyayı kaydediyoruz.
    playsound(file)#Dosyayı oynatıyoruz
    os.remove(file)#Dosyayı siliyoruz.

speak("Merhabalar ben kase sizin için ne yapabilirim?")
time.sleep(0.5)
while 1:
    voice = kayıt()
    print(voice)
    response(voice)