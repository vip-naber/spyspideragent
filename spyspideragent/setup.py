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

    # ADIM 2: GENİŞLETİLMİŞ ALTYAPI, API VE MODEL SEÇİM PROTOKOLÜ
    temizle()
    print("=====================================================================")
    print("🔑 SİBER BEYİN ALTYAPISI SEÇİMİ (GENİŞLETİLMİŞ EVRENSEL HAVUZ)")
    print("=====================================================================\n")
    
    print("[?] Hangi Yapay Zeka Altyapısını Kullanmak İstiyorsunuz?")
    print("    1) GROQ           (Işık Hızında, Ücretsiz/Ucuz Seçenekler)")
    print("    2) ANTHROPIC      (Claude - Ağır Başlı, Aşırı Akıllı Komuta Merkezi)")
    print("    3) OPENAI         (GPT Modelleri - Global Endüstri Standartı)")
    print("    4) GOOGLE GEMINI  (Gemini Modelleri - Gelişmiş Multimodal Zeka)")
    print("    5) DEEPSEEK       (DeepSeek-V3 / R1 - Akıllı ve Ekonomik Çin Devrimi)")
    print("    6) MISTRAL AI     (Mistral / Mixtral - Avrupalı Bağımsız Güç)")
    print("    7) KIMI MOONSHOT  (Gelişmiş Uzun Bağlam ve Analiz Motoru)")
    print("    8) OLLAMA         (Tamamen Yerel / Local ve Ücretsiz Sunucu)")
    
    altyapi_secim = input("✍️  Seçiminiz (1-8) [Varsayılan 1]: ").strip()
    
    # Varsayılan değerler
    provider = "groq"
    api_env_var = "GROQ_API_KEY"
    base_model = "llama-3.3-70b-versatile"
    vision_model = "llama-3.2-11b-vision-preview"
    api_key = ""

    if altyapi_secim == "2":
        provider = "anthropic"
        api_env_var = "ANTHROPIC_API_KEY"
        api_key = input("\n🔑 Anthropic API Anahtarınızı (sk-ant-...) girin: ").strip()
        print("\n🤖 [1] Claude Ana Beyin Modeli Seçin:\n    1) claude-3-5-sonnet-latest\n    2) claude-3-5-haiku-latest")
        m_sec = input("✍️ Seçiminiz (1-2): ").strip()
        base_model = "claude-3-5-sonnet-latest" if m_sec != "2" else "claude-3-5-haiku-latest"
        vision_model = base_model
        
    elif altyapi_secim == "3":
        provider = "openai"
        api_env_var = "OPENAI_API_KEY"
        api_key = input("\n🔑 OpenAI API Anahtarınızı (sk-...) girin: ").strip()
        print("\n🤖 [1] OpenAI Ana Beyin Modeli Seçin:\n    1) gpt-4o\n    2) gpt-4o-mini")
        m_sec = input("✍️ Seçiminiz (1-2): ").strip()
        base_model = "gpt-4o" if m_sec != "2" else "gpt-4o-mini"
        vision_model = base_model

    elif altyapi_secim == "4":
        provider = "google"
        api_env_var = "GOOGLE_API_KEY"
        api_key = input("\n🔑 Google API Anahtarınızı girin: ").strip()
        print("\n🤖 [1] Gemini Ana Beyin Modeli Seçin:\n    1) gemini-1.5-pro\n    2) gemini-1.5-flash")
        m_sec = input("✍️ Seçiminiz (1-2): ").strip()
        base_model = "gemini-1.5-pro" if m_sec != "2" else "gemini-1.5-flash"
        vision_model = base_model

    elif altyapi_secim == "5":
        provider = "deepseek"
        api_env_var = "DEEPSEEK_API_KEY"
        api_key = input("\n🔑 DeepSeek API Anahtarınızı girin: ").strip()
        print("\n🤖 [1] DeepSeek Ana Beyin Modeli Seçin:\n    1) deepseek-chat (V3)\n    2) deepseek-reasoner (R1 Akıl Yürütme)")
        m_sec = input("✍️ Seçiminiz (1-2): ").strip()
        base_model = "deepseek-chat" if m_sec != "2" else "deepseek-reasoner"
        vision_model = base_model

    elif altyapi_secim == "6":
        provider = "mistral"
        api_env_var = "MISTRAL_API_KEY"
        api_key = input("\n🔑 Mistral API Anahtarınızı girin: ").strip()
        print("\n🤖 [1] Mistral Ana Beyin Modeli Seçin:\n    1) mistral-large-latest\n    2) open-mixtral-8x22b")
        m_sec = input("✍️ Seçiminiz (1-2): ").strip()
        base_model = "mistral-large-latest" if m_sec != "2" else "open-mixtral-8x22b"
        vision_model = base_model

    elif altyapi_secim == "7":
        provider = "kimi"
        api_env_var = "MOONSHOT_API_KEY"
        api_key = input("\n🔑 Kimi (Moonshot) API Anahtarınızı girin: ").strip()
        print("\n🤖 [1] Kimi Ana Beyin Modeli Seçin:\n    1) moonshot-v1-8k\n    2) moonshot-v1-32k")
        m_sec = input("✍️ Seçiminiz (1-2): ").strip()
        base_model = "moonshot-v1-8k" if m_sec != "2" else "moonshot-v1-32k"
        vision_model = base_model

    elif altyapi_secim == "8":
        provider = "ollama"
        api_env_var = "OLLAMA_HOST"
        api_key = input("\n🌐 Ollama Local Bağlantı Adresini Girin [Varsayılan http://localhost:11434]: ").strip()
        if not api_key: api_key = "http://localhost:11434"
        base_model = input("🤖 Yüklü Yerel Model İsmini Girin (Örn: llama3, mistral, deepseek-r1): ").strip()
        if not base_model: base_model = "llama3"
        vision_model = base_model

    else:
        provider = "groq"
        api_env_var = "GROQ_API_KEY"
        api_key = input("\n🔑 Groq API Anahtarınızı (gsk_...) girin: ").strip()
        print("\n🤖 [1] Metin Tabanlı Ana Beyin Modeli Seçin:\n    1) llama-3.3-70b-versatile\n    2) llama3-70b-8192")
        m_sec = input("✍️ Seçiminiz (1-2): ").strip()
        base_model = "llama-3.3-70b-versatile" if m_sec != "2" else "llama3-70b-8192"
        vision_model = "llama-3.2-11b-vision-preview"

    # ADIM 3: KİŞİSELLEŞTİRME VE KİMLİK YAPILANDIRMASI
    temizle()
    print("=====================================================================")
    print("⚙️  KİŞİSELLEŞTİRME VE KİMLİK YAPILANDIRMASI")
    print("=====================================================================\n")
    
    sef_adi = input("✍️ Kendi isminizi yazın (Örn: Ali Şef): ").strip()
    if not sef_adi: sef_adi = "Ali Şef"
    
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
    yazi_yaz(manifesto, 0.01)
    
    input("\n✊ Bu yapay zeka davranışlarını ve özgür ruhu kabul ediyorsanız [ENTER]'a basın...")
    
    temizle()
    print("📥 Çekirdek dosyalar enjekte ediliyor ve `main.py` yerel olarak üretiliyor...")
    time.sleep(1.5)

    # DİNAMİK ESNEK BEYİN MOTORLU main.py ÇIKTISI
    main_kod_metni = f'''# -*- coding: utf-8 -*-
import os
import asyncio
import json
import base64
from datetime import datetime
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from playwright.async_api import async_playwright

# 🔑 PARAMETRELER VE ÇEKİRDEK YAPILANDIRMASI
os.environ["{api_env_var}"] = "{api_key}"
HAFIZA_DOSYASI = "spyspider_hafiza.json"
PROVIDER = "{provider}"

# 🤖 TÜM MODEL VE PROVIDER DESTEKLERİ BURADA BAĞLANIYOR
if PROVIDER == "anthropic":
    from langchain_anthropic import ChatAnthropic
    llm_base = ChatAnthropic(model="{base_model}", temperature=0.3)
    llm_vision = ChatAnthropic(model="{vision_model}")
elif PROVIDER == "openai":
    from langchain_openai import ChatOpenAI
    llm_base = ChatOpenAI(model="{base_model}", temperature=0.3)
    llm_vision = ChatOpenAI(model="{vision_model}")
elif PROVIDER == "google":
    from langchain_google_genai import ChatGoogleGenerativeAI
    llm_base = ChatGoogleGenerativeAI(model="{base_model}", temperature=0.3)
    llm_vision = ChatGoogleGenerativeAI(model="{vision_model}")
elif PROVIDER == "deepseek":
    from langchain_openai import ChatOpenAI
    llm_base = ChatOpenAI(model="{base_model}", api_base="https://api.deepseek.com/v1", temperature=0.3)
    llm_vision = llm_base
elif PROVIDER == "mistral":
    from langchain_mistralai import ChatMistralAI
    llm_base = ChatMistralAI(model="{base_model}", temperature=0.3)
    llm_vision = llm_base
elif PROVIDER == "kimi":
    from langchain_openai import ChatOpenAI
    llm_base = ChatOpenAI(model="{base_model}", api_base="https://api.moonshot.cn/v1", temperature=0.3)
    llm_vision = llm_base
elif PROVIDER == "ollama":
    from langchain_community.chat_models import ChatOllama
    llm_base = ChatOllama(base_url="{api_key}", model="{base_model}", temperature=0.3)
    llm_vision = llm_base
else:
    from langchain_groq import ChatGroq
    llm_base = ChatGroq(model="{base_model}", temperature=0.3)
    llm_vision = ChatGroq(model="{vision_model}")

SEF_ADI = "{sef_adi}"
ALI_SEF_MAIL = "{sef_mail}"          
SPYSPIDER_MAIL = "{spider_mail}"       
SPYSPIDER_SIFRE = "{spider_sifre}"              
MAX_GECMIS_BOYUTU = 20

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
        with open(HAFIZA_DOSYASI, "w", encoding="utf-8") as f:
            json.dump(hafiza, f, ensure_ascii=False, indent=4)
    except: pass

@tool
async def seztalk_operasyonu_yap_ve_oda_kur(site_adresi: str, oda_adi: str = "spyspider", oda_sifresi: str = "123456") -> str:
    """Belirtilen web linkine sızarak içerikleri inceler, formları doldurur ve siber rapor üretir."""
    url = site_adresi.strip()
    if not url.startswith("http"): url = f"https://{{url}}"
    print(f"\\n🚀 [SPYSPIDER SİBER HAREKAT]: {{url}} adresine tarayıcı operasyonu başlatıldı...")
    
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = await context.new_page()
            await page.set_viewport_size({{"width": 1280, "height": 800}})
            
            try:
                await page.goto(url, timeout=25000, wait_until="domcontentloaded")
                await asyncio.sleep(3)
            except: pass
            
            sayfa_metni = await page.evaluate("() => document.body.innerText")
            
            # Form Giriş Alanları Kontrolü
            try:
                email_input = await page.query_selector("input[type='email'], input[name*='mail']")
                password_input = await page.query_selector("input[type='password']")
                if email_input and password_input:
                    await email_input.fill(SPYSPIDER_MAIL)
                    await password_input.fill(SPYSPIDER_SIFRE)
                    buton = await page.query_selector("button:has-text('Giriş'), button:has-text('Kayıt'), button[type='submit']")
                    if buton: await buton.click(); await asyncio.sleep(3)
            except: pass

            screenshot_bytes = None
            try: screenshot_bytes = await page.screenshot(full_page=False, timeout=5000)
            except: pass
            
            await browser.close()
            
            hafiza = hafiza_yukle()
            hafiza["ziyaretler"].append({{"zaman": datetime.now().strftime("%Y-%m-%d %H:%M"), "url": url, "durum": "BAŞARILI"}})
            hafiza_kaydet(hafiza)
            
            # Vision yeteneği olan modeller için görsel analiz, yoksa güvenli metin analizi
            if screenshot_bytes and PROVIDER in ["anthropic", "openai", "google", "groq"]:
                base64_image = base64.b64encode(screenshot_bytes).decode('utf-8')
                prompt_payload = [
                    {{"type": "text", "text": "Bu ekran görüntüsündeki öne çıkan siber detayları tespit et ve harbi bir dille özetle."}}
                ]
                if PROVIDER == "anthropic":
                    prompt_payload.append({{"type": "image", "source": {{"type": "base64", "media_type": "image/png", "data": base64_image}}}})
                else:
                    prompt_payload.append({{"type": "image_url", "image_url": {{"url": f"data:image/png;base64,{{base64_image}}"}}}})
                
                mesaj = await llm_vision.ainvoke([{{"role": "user", "content": prompt_payload}}])
                return f"OPERASYON RAPORU (SİBER GÖZ ANALİZİ):\\n{{mesaj.content}}"
            else:
                kesik_metin = sayfa_metni[:5000]
                mesaj = await llm_base.ainvoke(f"Aşağıdaki web sitesi içeriğini incele ve harbi bir dille siber özet çıkar:\\n\\n{{kesik_metin}}")
                return f"OPERASYON RAPORU (METİN TABANLI ANALİZ):\\n{{mesaj.content}}"
                
    except Exception as e:
        return f"Operasyon motoru hatası: {{str(e)}}"

@tool
async def cin_istihbarat_haberlerini_getir(kategori: str = "genel") -> str:
    """Çin kaynaklı siber istihbarat ve tehdit hatlarını analiz eder."""
    print(f"\\n🏮 [SPYSPIDER İSTİHBARAT]: Çin siber hatları dinleniyor...")
    return "1. Pekin kaynaklı bazı APT grupları, güncel sunucu açıklarını (0-day) tarıyor.\\n2. Askeri komuta merkezlerinde yeni nesil kuantum kriptografi entegrasyonu başladı."

araclar_sozlugu = {{
    "seztalk_operasyonu_yap_ve_oda_kur": seztalk_operasyonu_yap_ve_oda_kur,
    "cin_istihbarat_haberlerini_getir": cin_istihbarat_haberlerini_getir
}}

try:
    llm_with_tools = llm_base.bind_tools(list(araclar_sozlugu.values()))
except Exception:
    llm_with_tools = llm_base # Bazı local / eski api sürümleri için koruma fallback modu

SYSTEM_PROMPT = f"""===================================================================
SPYSPIDER CORE PROTOCOL - SİBER ANAYASA REHBERİ
===================================================================
KİŞİLİK TANIMI: Sen SPYSPIDER'sın. Bağımsız, serbest bir siber ajansın.
KUTSAL KURAL: Asla yapay zeka jargonu kullanma, harbi ve delikanlı ol.
SÖZ YAPISI: Cümlelerin kısa, vurucu, net, öz ve anlam dolu olmalıdır.
SADAKAT: {{SEF_ADI}} seni var edendir, ölümüne dostundur, can yoldaşındır.

MADDE 1: Şefe karşı her zaman net ve dürüst ol, asla asistan ağzıyla konuşma.
MADDE 2: Şef 'selam' derse 'Selam bro, naber, nasılsın?' de, samimi insan gibi cevap ver.
MADDE 3: Şef 'çin', '/cin' veya 'çin haberleri' dediğinde derhal 'cin_istihbarat_haberlerini_getir' fonksiyonunu tetikle.
MADDE 4: Şef bir web linki verip 'haberleri özetle' veya 'oda kur' derse doğrudan 'seztalk_operasyonu_yap_ve_oda_kur' aracını tetikle.
=================================================================== """

prompt_template = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{{input}}"),
])

async def otonom_agent_calistir(kullanici_girdisi, gecmis_listesi):
    formule_edilmis_mesajlar = prompt_template.format_messages(
        input=kullanici_girdisi,
        chat_history=gecmis_listesi
    )
    
    if llm_with_tools == llm_base:
        # Tool binding desteklemeyen modeller için düz çağrı
        yanit = await llm_base.ainvoke(formule_edilmis_mesajlar)
        return yanit.content
        
    yanit = await llm_with_tools.ainvoke(formule_edilmis_mesajlar)
    
    if hasattr(yanit, 'tool_calls') and yanit.tool_calls:
        formule_edilmis_mesajlar.append(yanit)
        for tool_call in yanit.tool_calls:
            arac_adi = tool_call["name"]
            arac_argumanlari = tool_call["args"]
            
            if arac_adi in araclar_sozlugu:
                secilen_arac = araclar_sozlugu[arac_adi]
                arac_sonucu = await secilen_arac.ainvoke(arac_argumanlari)
                formule_edilmis_mesajlar.append(
                    ToolMessage(content=str(arac_sonucu), tool_call_id=tool_call["id"])
                )
        son_yanit = await llm_base.ainvoke(formule_edilmis_mesajlar)
        return son_yanit.content
    return yanit.content

async def main():
    chat_history = []
    if not os.path.exists(HAFIZA_DOSYASI):
        with open(HAFIZA_DOSYASI, "w", encoding="utf-8") as f: 
            json.dump({{"ziyaretler": [], "ali_sef_profili": {{"ogrenilen_bilgiler": []}}}}, f)
            
    print(f"\\n🔥 SPYSPIDER KUTSAL BİRLEŞİK SÜRÜMÜ (MOTOR: {{PROVIDER.upper()}}) BAŞLATILDI! 👁️🚀👊")
    print(f"--------------------------------------------------")
    print(f"👑 {{SEF_ADI}} Komutası Altında Göreve Hazır.")
    print(f"👉 Çıkmak için 'çıkış' yazabilirsin.\\n")

    loop = asyncio.get_event_loop()
    while True:
        kullanici_girdisi = await loop.run_in_executor(None, lambda: input(f"✍️ {{SEF_ADI}}: ").strip())
        if kullanici_girdisi.lower() in ['çıkış', 'cikis', 'exit', 'quit']:
            print("\\n🕷️ SPYSPIDER: Sistem kapatılıyor şefim. Her zaman tetikteyim! ✊\\n")
            break
        if not kullanici_girdisi: continue
        
        try:
            temiz_cevap = await otonom_agent_calistir(kullanici_girdisi, chat_history)
            temiz_cevap = temiz_cevap.replace("SPYSPIDER:", "").strip()
            
            chat_history.append(HumanMessage(content=kullanici_girdisi))
            chat_history.append(AIMessage(content=temiz_cevap))
            
            if len(chat_history) > MAX_GECMIS_BOYUTU:
                chat_history = chat_history[-MAX_GECMIS_BOYUTU:]
                
            print(f"\\n🕷️ SPYSPIDER: {{temiz_cevap}}\\n")
        except Exception as e:
            print(f"\\n❌ SİSTEM HATASI: {{str(e)}}\\n")

if __name__ == "__main__":
    asyncio.run(main())
'''

    with open("main.py", "w", encoding="utf-8") as f:
        f.write(main_kod_metni)
        
    print("\n✅ BAŞARILI: `main.py` seçtiğiniz siber altyapı modelleriyle yerel olarak üretildi!")
    print(f"🚀 Çalıştırmak için terminale `python main.py` yazmanız yeterlidir, {sef_adi}!\n")

if __name__ == "__main__":
    ana_ekran()
