# -*- coding: utf-8 -*-
"""
Lecture 3 Data Module - Wireless LAN, Frequency Bands & Android Intents
FNI-421 Mobile Computing - Dr. Soha Hussein (FCIS, Ain Shams University)
Strictly pure data: zero HTML markup.
"""

LECTURE_META = {
    "id": 3,
    "title": "Wireless LAN, Frequency Bands & Android Intents",
    "subtitle": "PAN/LAN/WAN/GAN taxonomy, IEEE 802.11 standards, 2.4 vs 5 GHz channels, and IPC via Intents",
    "icon": "📶",
    "color": "emerald",
}

summary_sections = [
    {
        "type": "definition",
        "heading": "Wireless Network Classification by Geographical Scale",
        "body": "Wireless networks are categorized into four geographical tiers based on coverage radius, transmission power, and propagation physics: (1) PAN (Personal Area Network): Coverage < 10 meters, designed for interconnecting personal gadgets around an individual (Bluetooth, Zigbee, NFC, UWB); (2) LAN (Local Area Network / WLAN): Coverage < 100-150 meters, providing high-bandwidth wireless access within buildings, homes, or university campuses (IEEE 802.11 Wi-Fi); (3) WAN (Wide Area Network / WWAN): Coverage across cities and regions up to 100 km, utilizing cellular telecommunications (3G, 4G LTE, 5G) or WiMAX (IEEE 802.16); (4) GAN (Global Area Network): Global planetary coverage utilizing Low Earth Orbit (LEO) and geostationary satellite constellations (Starlink, Iridium, GPS).",
    },
    {
        "type": "comparison",
        "heading": "IEEE 802.11 Wi-Fi Standards Evolution",
        "table": {
            "headers": ["Standard", "Release Year", "Frequency Band", "Max Raw Data Rate", "Modulation & Multiplexing", "Key Architectural Milestones"],
            "rows": [
                ["802.11b", "1999", "2.4 GHz", "11 Mbps", "DSSS (Direct Sequence Spread Spectrum) / CCK", "First widely adopted consumer Wi-Fi standard"],
                ["802.11a", "1999", "5.0 GHz", "54 Mbps", "OFDM (Orthogonal Frequency Division Multiplexing)", "Higher bandwidth, free from 2.4 GHz microwave clutter, shorter indoor range"],
                ["802.11g", "2003", "2.4 GHz", "54 Mbps", "OFDM & DSSS backward compatible", "Brought 54 Mbps speeds to the popular 2.4 GHz band"],
                ["802.11n (Wi-Fi 4)", "2009", "2.4 GHz & 5.0 GHz", "Up to 600 Mbps (4x4 MIMO)", "MIMO (Multiple Input Multiple Output), 40 MHz channels", "Introduced spatial multiplexing antennas and dual-band operation"],
                ["802.11ac (Wi-Fi 5)", "2013", "5.0 GHz", "Up to 6.93 Gbps (8x8 MIMO)", "256-QAM, 80/160 MHz channel bonding, MU-MIMO", "Downlink Multi-User MIMO; high-density enterprise throughput"],
                ["802.11ax (Wi-Fi 6)", "2019", "2.4, 5.0, & 6.0 GHz (6E)", "Up to 9.6 Gbps", "1024-QAM, OFDMA, Bi-directional MU-MIMO, TWT", "OFDMA resource units; designed for massive client density and IoT power saving"],
            ],
        },
    },
    {
        "type": "comparison",
        "heading": "2.4 GHz vs 5.0 GHz Frequency Bands Comparison",
        "table": {
            "headers": ["Metric", "2.4 GHz Wi-Fi Band", "5.0 GHz Wi-Fi Band"],
            "rows": [
                ["Wavelength (λ = c/f)", "≈ 12.5 cm (longer wavelength)", "≈ 6.0 cm (shorter wavelength)"],
                ["Indoor Propagation & Wall Penetration", "Superior penetration; bends around concrete edges and passes through drywall with lower absorption", "Inferior penetration; higher absorption by dense building materials (concrete, solid wood)"],
                ["Physical Reach / Coverage Range", "Extensive (up to 45-50 meters indoors)", "Limited (up to 15-20 meters indoors)"],
                ["Available Spectrum & Channels", "Only 3 non-overlapping 20 MHz channels (Channels 1, 6, and 11 in North America/ISM)", "At least 24 non-overlapping 20 MHz channels (UNII-1, UNII-2, UNII-3)"],
                ["Interference & Congestion", "Extremely congested (Bluetooth, microwave ovens, baby monitors, cordless phones share 2.4 GHz)", "Clean, low-interference spectrum with abundant channel bonding capacity"],
                ["Maximum Throughput", "Lower maximum data rates (limited channel bandwidth: 20/40 MHz)", "Much higher maximum data rates (channel bonding: 40, 80, and 160 MHz)"],
            ],
        },
    },
    {
        "type": "formula",
        "heading": "Wavelength, Frequency & Wave Amplitude Physics",
        "formula": "λ = c / f, where c = 3 × 10^8 m/s",
        "explanation": "For 2.4 GHz: λ = (3 × 10^8 m/s) / (2.4 × 10^9 Hz) = 0.125 m = 12.5 cm. For 5.0 GHz: λ = (3 × 10^8 m/s) / (5.0 × 10^9 Hz) = 0.06 m = 6.0 cm. Critical Rule: Wave AMPLITUDE determines the transmitted power and signal strength; amplitude is COMPLETELY INDEPENDENT of wave frequency! Two signals operating at 2.4 GHz and 5 GHz can transmit with the exact same power and amplitude.",
    },
    {
        "type": "definition",
        "heading": "Android Intents & Inter-Process Communication (IPC)",
        "body": "An Intent is an asynchronous messaging object used to request an action from another app component (Activities, Services, BroadcastReceivers). Intents are divided into two fundamental types: (1) Explicit Intents, which name the exact target component class (e.g., Intent(this, DetailActivity::class.java)) within the same application; and (2) Implicit Intents, which do not name a target class, but declare an abstract action (e.g., ACTION_VIEW, ACTION_SEND) and a data URI (e.g., tel:..., geo:..., content://...), allowing the Android OS to identify all registered apps on the device that can handle that request.",
    },
    {
        "type": "rule",
        "heading": "Implicit Intent Resolution & The 3 Non-Overlapping Channels Rule",
        "body": "Rule 1 (Implicit Intent Resolution): When an implicit intent is issued, Android matches the Intent's Action, Data URI (scheme, host, path, MIME type), and Category against the <intent-filter> tags registered in all installed apps' AndroidManifest.xml. If multiple matching apps exist, Android displays the App Chooser dialog. Rule 2 (2.4 GHz Wi-Fi Channels): In the 2.4 GHz ISM band, individual channels are spaced 5 MHz apart, but each standard 802.11 transmission requires a 20-22 MHz channel width. Consequently, only Channels 1, 6, and 11 do not overlap and can operate in the same physical space without co-channel interference.",
    },
    {
        "type": "code",
        "heading": "Kotlin Explicit vs Implicit Intent Launching",
        "lang": "kotlin",
        "code": """// 1. Explicit Intent: Launching an internal activity within the same application
val explicitIntent = Intent(this, DetailsActivity::class.java).apply {
    putExtra("ITEM_ID", 1042)
}
startActivity(explicitIntent)

// 2. Implicit Intent: Viewing a PDF file with user choice of app (Drive, Adobe, etc.)
val pdfUri: Uri = FileProvider.getUriForFile(context, "com.app.provider", pdfFile)
val implicitIntent = Intent(Intent.ACTION_VIEW).apply {
    setDataAndType(pdfUri, "application/pdf")
    addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
}
// Wrap in Chooser so the user can always pick their preferred reader
val chooser = Intent.createChooser(implicitIntent, "Open PDF with...")
startActivity(chooser)

// 3. Implicit Intent: Viewing a system Contact
val contactUri = ContentUris.withAppendedId(ContactsContract.Contacts.CONTENT_URI, contactId)
val viewContactIntent = Intent(Intent.ACTION_VIEW, contactUri)
startActivity(viewContactIntent)""",
        "explanation": "Explicit intents specify the exact destination class. Implicit intents use Action + URI + MIME type, delegating resolution to the OS so users can choose between multiple capable apps.",
    },
]

memory_aids = [
    {
        "title": "The 1-6-11 Rule for 2.4 GHz Wi-Fi",
        "content": "Channels 1, 6, and 11 are the ONLY non-overlapping 20 MHz channels in the 2.4 GHz band. Channels 2, 3, 4, and 5 interfere with both 1 and 6!",
    },
    {
        "title": "Wavelength vs Penetration Rule",
        "content": "Higher Frequency = Shorter Wavelength = Worse Wall Penetration.\n2.4 GHz (λ = 12.5 cm) penetrates walls and bends around obstacles.\n5.0 GHz (λ = 6.0 cm) offers higher bandwidth but is stopped easily by concrete walls.",
    },
    {
        "title": "Intent Golden Distinction",
        "content": "Explicit = Target known inside app (Class::class.java).\nImplicit = Target unknown or external (Action + Data URI + MIME type + createChooser).",
    },
    {
        "title": "Frequency vs Amplitude Independence",
        "content": "Frequency = Number of wave cycles per second (speed of oscillation).\nAmplitude = Height of wave peak (energy and transmitted power).\nFrequency does NOT determine amplitude!",
    },
]

mcqs = [
    {
        "id": "L3Q1",
        "q": "You want your app to open a PDF file located on the device. The file path is known, but you also want the user to have the choice of which app opens it (Adobe Reader, Google Drive, or other PDF viewers). Which approach is best?",
        "options": [
            "Create an explicit intent specifying the Adobe Reader package.",
            "Create an explicit intent for your app's internal PDF viewer.",
            "Use an implicit intent with ACTION_SEND and attach the PDF as an extra.",
            "Create an implicit intent with ACTION_VIEW and a file:// or content:// URI for the PDF.",
        ],
        "ans": 3,
        "explanation": "Official Course Quiz Question. Using an implicit intent with Intent.ACTION_VIEW and the MIME type 'application/pdf' allows the Android OS to display the system chooser containing all installed PDF viewer apps, allowing the user to select their preferred viewer.",
    },
    {
        "id": "L3Q2",
        "q": "Your app stores a contact ID that refers to a system contact. You want to show that contact's details in the system Contacts app. Which approach is correct?",
        "options": [
            "Create an explicit intent specifying the Contacts app's main activity.",
            "Create an implicit intent with ACTION_VIEW and a contact URI.",
            "Use an explicit intent targeting your app's ContactDetailsActivity.",
            "Send a broadcast intent with the contact URI.",
        ],
        "ans": 1,
        "explanation": "Official Course Quiz Question. System contacts are referenced by Content URIs (e.g., content://com.android.contacts/contacts/123). Launching an implicit intent with ACTION_VIEW and that URI instructs the Android OS to open the contact in the default contacts viewer.",
    },
    {
        "id": "L3Q3",
        "q": "Given the speed of light c = 3 × 10^8 m/s, what is the wavelength of a 2.4 GHz signal and a 5.0 GHz signal, and how is wave amplitude related to these frequencies?",
        "options": [
            "2.4 GHz has λ = 12.5 cm; 5 GHz has λ = 6 cm; amplitude is determined by frequency.",
            "2.4 GHz has λ = 12.5 cm; 5 GHz has λ = 6 cm; wave amplitude determines power and is completely independent of frequency.",
            "2.4 GHz has λ = 6 cm; 5 GHz has λ = 12.5 cm; amplitude decreases automatically as frequency increases.",
            "2.4 GHz has λ = 24 cm; 5 GHz has λ = 50 cm; amplitude is always equal to wavelength.",
        ],
        "ans": 1,
        "explanation": "Official Quiz & Midterm Physics Problem. λ = c/f. For 2.4 GHz, λ = (3×10^8) / (2.4×10^9) = 0.125 m = 12.5 cm. For 5.0 GHz, λ = (3×10^8) / (5×10^9) = 0.06 m = 6 cm. Amplitude represents the physical wave power/field strength and is independent of oscillation frequency.",
    },
    {
        "id": "L3Q4",
        "q": "In the 2.4 GHz Wi-Fi spectrum, which set of channels represents the standard non-overlapping 20 MHz channels commonly configured in multi-AP environments?",
        "options": [
            "Channels 1, 2, and 3",
            "Channels 1, 6, and 11",
            "Channels 2, 7, and 12",
            "Channels 1, 5, 9, and 13",
        ],
        "ans": 1,
        "explanation": "In 2.4 GHz Wi-Fi, each 20 MHz channel spans a 22 MHz spectral mask, while channel center frequencies are spaced only 5 MHz apart. Only Channels 1, 6, and 11 have at least 25 MHz separation between their center frequencies, preventing co-channel RF interference.",
    },
    {
        "id": "L3Q5",
        "q": "Which geographical wireless category covers a personal radius of less than 10 meters and includes technologies like Bluetooth, Zigbee, and NFC?",
        "options": [
            "WLAN (Wireless Local Area Network)",
            "WWAN (Wireless Wide Area Network)",
            "WPAN (Wireless Personal Area Network)",
            "WGAN (Wireless Global Area Network)",
        ],
        "ans": 2,
        "explanation": "WPAN (Wireless Personal Area Network) covers the immediate operational space around a person or device (typically up to 10 meters), focusing on low power, ad-hoc connectivity, and small data exchanges.",
    },
    {
        "id": "L3Q6",
        "q": "What happens when an app attempts to start an implicit intent for which NO installed application has a matching <intent-filter>?",
        "options": [
            "Android automatically downloads a compatible application from Google Play without asking.",
            "The method returns null silently and the app continues.",
            "An ActivityNotFoundException is thrown, causing the app to crash if unhandled.",
            "The Android OS reboots into safe mode.",
        ],
        "ans": 2,
        "explanation": "If startActivity() is called with an implicit intent that matches zero activities on the device, the Android OS throws an ActivityNotFoundException. Developers safeguard against this using intent.resolveActivity(packageManager) != null.",
    },
    {
        "id": "L3Q7",
        "q": "Which IEEE 802.11 standard introduced Multiple Input Multiple Output (MIMO) antenna technology and spatial multiplexing?",
        "options": [
            "802.11a",
            "802.11b",
            "802.11g",
            "802.11n (Wi-Fi 4)",
        ],
        "ans": 3,
        "explanation": "IEEE 802.11n (ratified in 2009) introduced MIMO (Multiple Input Multiple Output), allowing multiple transmitters and receivers to send independent data streams simultaneously over the same radio channel, boosting speeds up to 600 Mbps.",
    },
    {
        "id": "L3Q8",
        "q": "Why does a 2.4 GHz Wi-Fi signal penetrate solid obstacles (such as brick walls and doors) better than a 5 GHz Wi-Fi signal?",
        "options": [
            "2.4 GHz signals travel at a higher speed than 5 GHz signals.",
            "2.4 GHz has a longer wavelength (~12.5 cm vs 6 cm), which undergoes deeper spatial diffraction around edges and excites obstacle molecules less rapidly, resulting in lower absorption loss.",
            "5 GHz signals are converted into sound waves inside building materials.",
            "2.4 GHz routers are legally allowed to broadcast at ten times higher power.",
        ],
        "ans": 1,
        "explanation": "According to EM wave physics, longer wavelengths (lower frequencies) experience less atmospheric and obstacle attenuation and diffract more effectively around obstacles compared to shorter wavelengths, which are absorbed more rapidly as heat.",
    },
    {
        "id": "L3Q9",
        "q": "What is the primary role of an <intent-filter> tag inside an Android application's AndroidManifest.xml file?",
        "options": [
            "To filter out unwanted network spam and malware.",
            "To inform the Android OS of the specific types of implicit intents (actions, data types, and categories) that an Activity, Service, or Receiver can handle.",
            "To encrypt all database tables created by Room.",
            "To compress the APK by filtering unused drawables.",
        ],
        "ans": 1,
        "explanation": "An <intent-filter> is a declaration in the manifest specifying the capabilities of a component: which actions it can perform, which URI data schemes and MIME types it accepts, and which intent categories it belongs to.",
    },
    {
        "id": "L3Q10",
        "q": "What is the difference between Intent Extras and Intent Data URI?",
        "options": [
            "Extras can only store integers, while Data URIs store strings.",
            "Data URI specifies the resource identifier (URI) that the action operates upon, whereas Extras represent a key-value Bundle containing additional arbitrary data.",
            "Extras are public, while Data URIs are encrypted.",
            "Data URIs are only used in Explicit Intents, while Extras are used in Implicit Intents.",
        ],
        "ans": 1,
        "explanation": "The Data property (setData/getData) points to the target URI being manipulated (e.g., content://contacts/people/1), while Extras (putExtra/getExtras) are arbitrary key-value pairs packaged in a Bundle providing auxiliary parameters.",
    },
    {
        "id": "L3Q11",
        "q": "Why is the 5 GHz Wi-Fi band considered advantageous for high-throughput streaming despite having a shorter range than 2.4 GHz?",
        "options": [
            "Because 5 GHz can transmit through solid lead walls.",
            "Because 5 GHz offers significantly wider spectral bandwidth (up to 160 MHz bonded channels) and has 24+ non-overlapping channels with far less RF interference.",
            "Because 5 GHz signals do not require an access point or router.",
            "Because 5 GHz devices consume zero electrical power.",
        ],
        "ans": 1,
        "explanation": "5 GHz has a much larger spectrum allocation, allowing 24+ non-overlapping 20 MHz channels and multi-channel bonding (40, 80, 160 MHz). It is also free from common household interference like microwave ovens and Bluetooth.",
    },
    {
        "id": "L3Q12",
        "q": "Which IEEE 802.11 standard introduced Orthogonal Frequency Division Multiple Access (OFDMA), dividing channels into Resource Units (RUs) for high-density clients?",
        "options": [
            "802.11b",
            "802.11g",
            "802.11ac (Wi-Fi 5)",
            "802.11ax (Wi-Fi 6)",
        ],
        "ans": 3,
        "explanation": "Wi-Fi 6 (802.11ax) adopted OFDMA from cellular LTE/5G. OFDMA splits a Wi-Fi channel into sub-carriers grouped into Resource Units (RUs), enabling the AP to transmit to or receive from multiple clients simultaneously in a single transmission window.",
    },
    {
        "id": "L3Q13",
        "q": "When creating an implicit intent to share text or an image via social apps, which Intent Action is standard?",
        "options": [
            "Intent.ACTION_VIEW",
            "Intent.ACTION_EDIT",
            "Intent.ACTION_SEND",
            "Intent.ACTION_MAIN",
        ],
        "ans": 2,
        "explanation": "Intent.ACTION_SEND is the standard Android intent action used to share data (text, URLs, photos, documents) with another application selected by the user.",
    },
    {
        "id": "L3Q14",
        "q": "What is the function of Intent.createChooser(targetIntent, title)?",
        "options": [
            "It forces Android to display a selection dialog every time, preventing the user's previously selected 'Always' default from bypassing app choice.",
            "It compiles the app into a chooser library.",
            "It crashes the app if multiple apps can handle the intent.",
            "It filters out third-party applications from opening the intent.",
        ],
        "ans": 0,
        "explanation": "Intent.createChooser() wraps an intent so that the Android system always displays an activity picker dialog to the user, even if the user had previously selected a 'Always use this app' preference for that action.",
    },
    {
        "id": "L3Q15",
        "q": "In 802.11 Wi-Fi, what does DSSS stand for, and which standard popularized it?",
        "options": [
            "Dynamic Single Spectrum System, in 802.11ac",
            "Direct Sequence Spread Spectrum, popularized in 802.11b",
            "Digital Signal Synchronization Standard, in 802.11a",
            "Data Storage Switching System, in 802.11n",
        ],
        "ans": 1,
        "explanation": "DSSS (Direct Sequence Spread Spectrum) spreads the baseband data signal over a wider bandwidth using a chipping code (such as the 11-chip Barker sequence or CCK). It was the foundational modulation for IEEE 802.11b.",
    },
    {
        "id": "L3Q16",
        "q": "What is the category CATEGORY_DEFAULT in an intent filter?",
        "options": [
            "A category indicating the app has no security permissions.",
            "A category required in an <intent-filter> so that startActivity() can resolve and launch the activity with an implicit intent.",
            "A category that makes the activity the device home screen launcher.",
            "A deprecated tag that is ignored by modern Android versions.",
        ],
        "ans": 1,
        "explanation": "To receive implicit intents dispatched via startActivity(), an activity's <intent-filter> MUST include <category android:name='android.intent.category.DEFAULT'/>. If missing, startActivity() will not resolve to that activity.",
    },
    {
        "id": "L3Q17",
        "q": "Which network type connects inter-city enterprise sites across hundreds of kilometers using cellular 4G/5G or microwave towers?",
        "options": [
            "PAN",
            "LAN",
            "WAN",
            "BAN (Body Area Network)",
        ],
        "ans": 2,
        "explanation": "A Wide Area Network (WAN) spans broad geographical distances (cities, regions, or countries) using telecommunications circuits, leased lines, or cellular backhauls.",
    },
    {
        "id": "L3Q18",
        "q": "In Android, how do you safely pass a custom data object between Activities inside an Intent Extra?",
        "options": [
            "Convert the object to an integer and pass its memory address.",
            "Have the custom object implement Parcelable (or Serializable) and put it into the Intent via putExtra().",
            "Save the object as a global static variable in the Linux kernel.",
            "Pass the raw pointer through the HAL.",
        ],
        "ans": 1,
        "explanation": "In Android, IPC bundles require data to be serialized. Android provides the Parcelable interface (highly optimized for IPC memory layout in Android) or Java Serializable to package objects into Intent extras.",
    },
    {
        "id": "L3Q19",
        "q": "What happens if two adjacent Wi-Fi Access Points are configured on Channel 1 and Channel 3 in the 2.4 GHz band?",
        "options": [
            "Their data rates double due to cooperative MIMO.",
            "They cause destructive adjacent-channel interference because their 20 MHz spectra overlap, increasing packet collisions and retries.",
            "The router on Channel 3 shuts down automatically.",
            "They switch to Bluetooth mode automatically.",
        ],
        "ans": 1,
        "explanation": "Since Wi-Fi channels require 20-22 MHz bandwidth and are separated by only 5 MHz, Channel 1 (2412 MHz) and Channel 3 (2422 MHz) heavily overlap. Unlike co-channel devices that can coordinate CSMA/CA, adjacent-channel interference appears as raw RF noise, severely degrading throughput.",
    },
    {
        "id": "L3Q20",
        "q": "What does URI stand for in Android Intent handling, and what are its standard components?",
        "options": [
            "Universal Radio Interface: frequency and amplitude.",
            "Uniform Resource Identifier: scheme, authority/host, and path (e.g., content://media/external/images/4).",
            "User Runtime Instruction: compiler and dexer.",
            "Unified Routing Index: router MAC address and IP.",
        ],
        "ans": 1,
        "explanation": "A Uniform Resource Identifier (URI) uniquely identifies a resource on Android. It consists of a scheme (e.g., content, file, http, geo, tel), authority/host, and path, enabling Android to determine which ContentProvider or app handles it.",
    },
]

