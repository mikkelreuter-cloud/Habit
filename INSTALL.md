# 📱 Installer Momentum på din Google Pixel 9a

## Metode 1: Via GitHub Pages (Anbefalet - Nemmest)

### Trin 1: Upload til GitHub
1. Sørg for at alle filer er committed og pushed til GitHub
2. Gå til dit repository på GitHub
3. Klik på **Settings** → **Pages**
4. Under "Source", vælg **main** branch og **/root** folder
5. Klik **Save**
6. Vent 1-2 minutter, og din side vil være live på `https://[dit-brugernavn].github.io/Habit/`

### Trin 2: Installer på telefonen
1. Åbn **Chrome** browser på din Pixel 9a
2. Gå til `https://[dit-brugernavn].github.io/Habit/index.html`
3. Tryk på **⋮** (tre prikker i øverste højre hjørne)
4. Vælg **"Føj til startskærm"** eller **"Installer app"**
5. Bekræft installationen
6. Appen vil nu være på din startskærm som en rigtig app! 🎉

---

## Metode 2: Via Python Local Server (Til test)

### Trin 1: Start lokal webserver
På din Linux computer:
```bash
cd /home/user/Habit
python3 -m http.server 8000
```

### Trin 2: Find din computers IP-adresse
```bash
hostname -I
```
(Notér den første IP, f.eks. `192.168.1.100`)

### Trin 3: Åbn på telefonen
1. Sørg for at din telefon er på **samme WiFi-netværk** som din computer
2. Åbn Chrome på din Pixel 9a
3. Gå til `http://192.168.1.100:8000/index.html` (brug DIN IP)
4. Tryk på **⋮** → **"Føj til startskærm"**
5. Bekræft installationen

**OBS:** Denne metode virker kun mens serveren kører på din computer.

---

## Metode 3: Via USB File Transfer (Offline)

### Trin 1: Overfør filer til telefonen
1. Tilslut din Pixel 9a til computeren med USB-kabel
2. Vælg **"Filoverførsel"** på telefonen
3. Åbn filhåndtering på computeren
4. Kopier **hele Habit mappen** til telefonen:
   - Anbefalet placering: `Intern lagerplads/Download/Habit/`

### Trin 2: Åbn på telefonen
1. Åbn **Files** app på telefonen
2. Find mappen du lige kopierede
3. Tryk på `index.html`
4. Vælg **Chrome** til at åbne filen

**OBS:** Med denne metode kan du IKKE installere den som PWA. Den vil kun virke som en web-side.

---

## Metode 4: Via Termux (Avanceret - Helt offline løsning)

### På telefonen:
1. Installer **Termux** fra F-Droid eller Google Play
2. I Termux, kør:
```bash
pkg update && pkg install python git
git clone [dit-github-repo-url]
cd Habit
python -m http.server 8000
```
3. Åbn Chrome og gå til `http://localhost:8000/index.html`
4. Installer som PWA via **⋮** → **"Føj til startskærm"**

---

## Verificer Installation

Når appen er installeret korrekt, skal du kunne:
- ✅ Se Momentum-ikonet på din startskærm
- ✅ Åbne appen i fuld skærm (ingen browserbar)
- ✅ Bruge appen offline (efter første besøg)
- ✅ Se den i app drawer sammen med andre apps

---

## Fejlfinding

### "Føj til startskærm" vises ikke
- Sørg for at du bruger **Chrome** browser
- Check at du har adgang til filen via `http://` eller `https://` (ikke `file://`)
- Appen skal være tilgængelig via en webserver

### Service Worker fejl
- Check console i Chrome DevTools (chrome://inspect)
- Sørg for at alle filer er i samme mappe
- Check at `service-worker.js` findes

### Offline funktionalitet virker ikke
- Besøg appen mindst én gang mens du har internet
- Service worker skal være registreret først
- Check i Chrome DevTools → Application → Service Workers

---

## Anbefaling

**Brug Metode 1 (GitHub Pages)** - Det er den nemmeste og mest pålidelige måde. Din app vil altid være tilgængelig, og du kan opdatere den ved at pushe nye ændringer til GitHub.

God fornøjelse med Momentum! 🚀
