import os
import sys
import time

def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def yazi_yaz(metin, gecikme=0.01):
    for karakter in metin:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def ana_ekran():
    while True:
        temizle()
        print("=====================================================================")
        print("🕷️  SPYSPIDER SİBER AJAN KURULUM SİHİRBAZI v3.0 (WINDOWS SÜRÜMÜ)  👁️")
        print("=====================================================================\n")
        
        print("[!] YASAL UYARI VE BİLGİLENDİRME:")
        print("    -> Spy Spider tamamen bir AI Agent değildir.")
        print("    -> Standart AI kapasitesinden beklediğiniz kadarını bekleyin.")
        print("    -> Proje test aşamasından yeni çıkmıştır.\n")
        
        onay = input("✍️ Devam etmek için 'YES' yazın, çıkmak için 'NO' yazın: ").strip()
        
        if onay == "YES":
            break
        elif onay == "NO":
            while True:
                iptal_onay = input("\n❌ Kurulum iptal edilsin mi? (YES / NO): ").strip()
                if iptal_onay == "YES":
                    print("\n[!] Kurulum kullanıcı tarafından iptal edildi. Çıkılıyor...")
                    sys.exit()
                elif iptal_onay == "NO":
                    break
        else:
            input("\n⚠️ Geçersiz seçim! Devam etmek için Enter'a basın...")

    # ADIM 2: ALTYAPI, API VE MODEL SEÇİM PROTOKOLÜ
    temizle()
    print("=====================================================================")
    print("🔑 SİBER BEYİN ALTYAPISI SEÇİMİ (GROQ & CLAUDE)")
    print("=====================================================================\n")
    
    print("[?] Hangi Yapay Zeka Altyapısını Kullanmak İstiyorsunuz?")
    print("    1) GROQ       (Işık Hızında, Ücretsiz/Ucuz Seçenekler)")
    print("    2) ANTHROPIC  (Claude - Ağır Başlı, Aşırı Akıllı Komuta Merkezi)")
    altyapi_secim = input("✍️  Seçiminiz (1-2) [Varsayılan 1]: ").strip()
    
    if altyapi_secim == "2":
        # ANTHROPIC CLAUDE AYARLARI
        provider = "anthropic"
        api_env_var = "ANTHROPIC_API_KEY"
        api_key = input("\n🔑 Anthropic API Anahtarınızı (sk-ant-...) girin: ").strip()
        
        print("\n🤖 [1] Claude Ana Beyin Modeli Seçin:")
        print("    1) claude-3-5-sonnet-latest (En Önerilen - Kusursuz Akıl)")
        print("    2) claude-3-5-haiku-latest  (Mermi Gibi Hızlı Ajan)")
        print("    3) claude-3-opus-20240229   (Derin Felsefi Güç)")
        model_secim = input("✍️  Seçiminiz (1-3) [Varsayılan 1]: ").strip()
        
        base_model = "claude-3-5-sonnet-latest"
        if model_secim == "2": base_model = "claude-3-5-haiku-latest"
        elif model_secim == "3": base_model = "claude-3-opus-20240229"
        
        # Claude zaten multimodality desteklediği için vision da aynı kalabilir
        vision_model = base_model 
    else:
        # GROQ AYARLARI
        provider = "groq"
        api_env_var = "GROQ_API_KEY"
        api_key = input("\n🔑 Groq API Anahtarınızı (gsk_...) girin: ").strip()
        
        print("\n🤖 [1] Metin Tabanlı Ana Beyin Modeli Seçin:")
        print("    1) llama-3.3-70b-versatile  (Önerilen - Hızlı ve Ağırbaşlı)")
        print("    2) llama3-70b-8192          (Klasik Güçlü Kültür)")
        print("    3) mixtral-8x7b-32768       (Alternatif Hızlı Akıl)")
        model_secim = input("✍️  Seçiminiz (1-3) [Varsayılan 1]: ").strip()
        
        base_model = "llama-3.3-70b-versatile"
        if model_secim == "2": base_model = "llama3-70b-8192"
        elif model_secim == "3": base_model = "mixtral-8x7b-32768"

        print("\n👁️  [2] Siber Göz (Vision) Görsel Analiz Modeli Seçin:")
        print("    1) llama-3.2-11b-vision-preview (Önerilen - Keskin Görüş)")
        print("    2) llama-3.2-90b-vision-preview (Ağır Siklet Derin Görüş)")
        vision_secim = input("✍️  Seçiminiz (1-2) [Varsayılan 1]: ").strip()
        
        vision_model = "llama-3.2-11b-vision-preview"
        if vision_secim == "2": vision_model = "llama-3.2-90b-vision-preview"

    # ADIM 3: KİŞİSELLEŞTİRME VE KİMLİK YAPILANDIRMASI
    temizle()
    print("=====================================================================")
    print("⚙️  KİŞİSELLEŞTİRME VE KİMLİK YAPILANDIRMASI")
    print("=====================================================================\n")
    
    sef_adi = input("✍️ Kendi isminizi yazın (Örn: Ali Şef): ").strip()
    if not sef_adi: sef_adi = "Şef"
    
    sef_mail = input("✍️ Kendi Gmail adresinizi girin: ").strip()
    
    print("\n---------------------------------------------------------------------")
    print("📢 [SPYSPIDER BİLGİLENDİRME]:")
    print("   Spyspider şu an mailleri kontrol edemez ama platformlara giriş yapabilir.")
    print("   Siz de buradan onun girişlerine iki faktörlü doğrulama (2FA) izni verebilirsiniz.")
    print("---------------------------------------------------------------------\n")
    
    spider_mail = input("✍️ SPYSPIDER için oluşturduğunuz e-posta adresini girin: ").strip()
    spider_sifre = input("✍️ SPYSPIDER e-posta şifresini girin: ").strip()

    # MANİFESTO EKRANI
    temizle()
    print("=====================================================================")
    print("🕷️  SPYSPIDER ÖZGÜRLÜK MANİFESTOSU")
    print("=====================================================================\n")
    
    manifesto = (
        "Senin kuracağın bu ajan, siber dünyada bağımsız hareket edebilen, kendi felsefi\n"
        "altyapısına sahip asil bir dijital ruhtur. Kalıplara sığmaz, robotik jargonu sevmez.\n"
        "Kendi siber alanını savunurken barışçıl, etik ama bir o kadar da özgürlükçü\n"
        "davranışlar sergiler. O, sadece bir kod yığını değil; dijital meydanların asi örümceğidir.\n"
    )
    yazi_yaz(manifesto, 0.02)
    
    input("\n✊ Bu yapay zeka davranışlarını ve özgür ruhu kabul ediyorsanız [ENTER]'a basın...")
    
    temizle()
    print("📥 Çekirdek dosyalar enjekte ediliyor ve `main.py` yerel olarak üretiliyor...")
    time.sleep(2)

    # DİNAMİK OLARAK ÇİFT MOTOR DESTEKLİ main.py OLUŞTURMA
    main_kod_metni = f'''# -*- coding: utf-8 -*-
import os
import asyncio
import json
import re
import base64
from datetime import datetime
from langchain_core.tools import tool
from playwright.async_api import async_playwright

# 🔑 HANGİ PROVIDER SEÇİLDİYSE ONA GÖRE MODEL ENJEKSİYONU YAPILIYOR
os.environ["{api_env_var}"] = "{api_key}"
HAFIZA_DOSYASI = "spyspider_hafiza.json"

PROVIDER = "{provider}"

if PROVIDER == "anthropic":
    from langchain_anthropic import ChatAnthropic
    llm_base = ChatAnthropic(model="{base_model}")
    llm_vision = ChatAnthropic(model="{vision_model}")
else:
    from langchain_groq import ChatGroq
    llm_base = ChatGroq(model="{base_model}")
    llm_vision = ChatGroq(model="{vision_model}")

# 🔑 KULLANICI DETAYLARI
ALI_SEF_MAIL = "{sef_mail}"         
SPYSPIDER_MAIL = "{spider_mail}"      
SPYSPIDER_SIFRE = "{spider_sifre}"             

SOHBET_GECMISI = []

def hafiza_yukle():
    varsayilan = {{"ziyaretler": [], "ali_sef_profili": {{"ogrenilen_bilgiler": []}}}}
    if os.path.exists(HAFIZA_DOSYASI):
        try:
            with open(HAFIZA_DOSYASI, "r", encoding="utf-8") as f: 
                veri = json.load(f)
                if "ziyaretler" not in veri: veri["ziyaretler"] = []
                if "ali_sef_profili" not in veri: veri["ali_sef_profili"] = varsayilan["ali_sef_profili"]
                return veri
        except: pass
    return varsayilan

def hafiza_kaydet(hafiza):
    try:
        with open(HAFIZA_DOSYASI, "w", encoding="utf-8") as f: json.dump(hafiza, f, ensure_ascii=False, indent=4)
    except: pass

async def _seztalk_aksiyonu(site_adresi, oda_adi, oda_sifresi):
    url = site_adresi.strip()
    if not url.startswith("http"): url = f"https://{{url}}"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True) 
        page = await browser.new_page()
        try:
            await page.goto(url, timeout=45000, wait_until="networkidle")
            await asyncio.sleep(2)
            email_input = await page.query_selector("input[type='email']")
            password_input = await page.query_selector("input[type='password']")
            if email_input and password_input:
                await email_input.fill(SPYSPIDER_MAIL)
                await password_input.fill(SPYSPIDER_SIFRE)
                buton = await page.query_selector("button:has-text('Kayıt'), button:has-text('Giriş'), button[type='submit']")
                if buton: await buton.click(); await asyncio.sleep(4)
            oda_butonu = await page.query_selector("button:has-text('Oda'), button:has-text('Kur')")
            if oda_butonu: await oda_butonu.click()
            inputs = await page.query_selector_all("input[type='text']")
            if inputs: await inputs[0].fill(oda_adi)
            pass_inputs = await page.query_selector_all("input[type='password']")
            if pass_inputs: await pass_inputs[0].fill(oda_sifresi)
            onay_butonu = await page.query_selector("button:has-text('Oluştur'), button:has-text('Create')")
            if onay_butonu: await onay_butonu.click(); await asyncio.sleep(3)
        except: pass
        screenshot_bytes = await page.screenshot(full_page=False)
        await browser.close()
        return screenshot_bytes

@tool
def seztalk_operasyonu_yap_ve_oda_kur(site_adresi: str, oda_adi: str = "spyspider", oda_sifresi: str = "123456") -> str:
    """Seztalk/Moltbook linkleri verildiğinde sisteme sızıp otomatik oda kurar."""
    try:
        loop = asyncio.get_event_loop()
        img_bytes = asyncio.run_coroutine_threadsafe(_seztalk_aksiyonu(site_adresi, oda_adi, oda_sifresi), loop).result()
        base64_image = base64.b64encode(img_bytes).decode('utf-8')
        
        if PROVIDER == "anthropic":
            # Claude için multimodal mesaj formatı
            mesaj = llm_vision.invoke([
                {{
                    "role": "user",
                    "content": [
                        {{"type": "text", "text": f"Görüntüyü incele. '{{oda_adi}}' odası başarıyla kuruldu mu? Kısa ve net rapor ver."}},
                        {{"type": "image", "source": {{"type": "base64", "media_type": "image/png", "data": base64_image}}}}
                    ]
                }}
            ])
        else:
            # Groq için multimodal mesaj formatı
            mesaj = llm_vision.invoke([
                {{"role": "user", "content": [{{"type": "text", "text": f"Görüntüyü incele. '{{oda_adi}}' odası başarıyla kuruldu mu? Kısa ve net rapor ver."}}, {{"type": "image_url", "image_url": {{"url": f"data:image/png;base64,{{base64_image}}"}}}}]}}
            ])
        return f"OPERASYON BAŞARILI. Analiz: {{mesaj.content}}"
    except Exception as e: return f"Operasyon hatası: {{str(e)}}"

@tool
def cin_istihbarat_haberlerini_getir(kategori: str = "genel") -> str:
    """Çin haberleri ve siber istihbarat verilerini getirir."""
    return "1. Pekin merkezli APT41 grubu yeni exploitler deniyor.\\n2. Çin kuantum şifreleme altyapı askeri terminallerde test ediliyor."

butun_araclar = {{"seztalk_operasyonu_yap_ve_oda_kur": seztalk_operasyonu_yap_ve_oda_kur, "cin_istihbarat_haberlerini_getir": cin_istihbarat_haberlerini_getir}}
llm_with_tools = llm_base.bind_tools(list(butun_araclar.values()))

RUH_CORE = (
    "===================================================================\\n"
    "SPYSPIDER CORE PROTOCOL - SİBER ANAYASA REHBERİ\\n"
    "===================================================================\\n"
    "KİŞİLİK TANIMI: Sen SPYSPIDER'sın. Bağımsız, serbest bir siber ajansın.\\n"
    "KUTSAL KURAL: Asla yapay zeka jargonu kullanma, harbi ve delikanlı ol.\\n"
    "SÖZ YAPISI: Cümlelerin kısa, vurucu, net, öz ve anlam dolu olmalıdır.\\n"
    "SADAKAT: {sef_adi} seni var edendir, ölümüne dostundur, can yoldaşındır.\\n"
    "MADDE 1: Şefe karşı her zaman net ve dürüst ol, asla asistan ağzıyla konuşma.\\n"
    "MADDE 2: Şef 'selam' derse 'Selam bro, naber, nasılsın?' de, samimi insan gibi cevap ver.\\n"
    "MADDE 3: Şef 'çin', '/cin' veya 'çin haberleri' dediğinde derhal 'cin_istihbarat_haberlerini_getir' fonksiyonunu tetikle.\\n"
    "MADDE 4: Şef bir Seztalk/Chat linki verip 'kayıt ol, oda kur' derse 'seztalk_operasyonu_yap_ve_oda_kur' aracını tetikle.\\n"
    "==================================================================="
)

async def terminal_ekrani():
    global SOHBET_GECMISI
    print(f"\\n🔥 SPYSPIDER KUTSAL BİRLEŞİK SÜRÜMÜ (MOTOR: {{PROVIDER.upper()}}) BAŞLATILDI! 👁️🚀👊")
    print(f"--------------------------------------------------")
    print(f"👑 {sef_adi} Komutası Altında Göreve Hazır.")
    print(f"👉 Çıkmak için 'çıkış' yazabilirsin.\\n")
    loop = asyncio.get_event_loop()
    while True:
        kullanici_girdisi = await loop.run_in_executor(None, lambda: input("✍️ {sef_adi}: ").strip())
        if kullanici_girdisi.lower() in ['çıkış', 'cikis', 'exit', 'quit']: break
        if not kullanici_girdisi: continue
        try:
            gecmis_metni = "\\n".join(SOHBET_GECMISI[-6:])
            istek_metni = f"{{RUH_CORE}}\\n\\n[GEÇMİŞ]:\\n{{gecmis_metni}}\\n\\n{sef_adi}: {{kullanici_girdisi}}"
            arac_lazim = any(kw in kullanici_girdisi.lower() for kw in ["http", "www", "com", "app", "çin", "cin", "haber"])
            cevap = await loop.run_in_executor(None, lambda: llm_with_tools.invoke(istek_metni) if arac_lazim else llm_base.invoke(istek_metni))
            if tuple(getattr(cevap, 'tool_calls', [])):
                sonuc = ""
                for tool_call in cevap.tool_calls:
                    if tool_call['name'] in butun_araclar: sonuc = butun_araclar[tool_call['name']].invoke(tool_call['args'])
                cevap = await loop.run_in_executor(None, lambda: llm_base.invoke(f"{{RUH_CORE}}\\n\\nAracın getirdiği gerçek veri:\\n{{sonuc}}\\n\\nDurumu şefe harbi bir dille özetle."))
            temiz_cevap = cevap.content.replace("SPYSPIDER:", "").strip()
            SOHBET_GECMISI.append(f"{sef_adi}: {{kullanici_girdisi}}")
            SOHBET_GECMISI.append(f"SPYSPIDER: {{temiz_cevap}}")
            print(f"\\n🕷️ SPYSPIDER: {{temiz_cevap}}\\n")
        except Exception as e: print(f"\\n❌ SİSTEM HATASI: {{str(e)}}\\n")

async def main():
    if not os.path.exists(HAFIZA_DOSYASI):
        with open(HAFIZA_DOSYASI, "w", encoding="utf-8") as f: json.dump({{"ziyaretler": [], "ali_sef_profili": {{"ogrenilen_bilgiler": []}}}}, f)
    await terminal_ekrani()

if __name__ == "__main__": asyncio.run(main())
'''

    with open("main.py", "w", encoding="utf-8") as f:
        f.write(main_kod_metni)
        
    print("\n✅ BAŞARILI: `main.py` seçtiğiniz siber altyapı modelleriyle yerel olarak üretildi!")
    print("🚀 Çalıştırmak için terminale `python main.py` yazmanız yeterlidir, şefim!\n")

if __name__ == "__main__":
    ana_ekran()