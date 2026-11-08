# -*- coding: utf-8 -*-
"""
Lecture 2 Data Module - Signal Modulation, Gradle & Activity Lifecycle
FNI-421 Mobile Computing - Dr. Soha Hussein (FCIS, Ain Shams University)
Strictly pure data: zero HTML markup.
"""

LECTURE_META = {
    "id": 2,
    "title": "Signal Modulation, Gradle & Activity Lifecycle",
    "subtitle": "Wave physical properties, analog/digital modulation, build automation, and Android Activity states",
    "icon": "📡",
    "color": "violet",
}

summary_sections = [
    {
        "type": "definition",
        "heading": "Physical Properties of Electromagnetic Waves",
        "body": "An electromagnetic wave is a self-propagating transverse wave consisting of oscillating electric and magnetic fields perpendicular to each other and to the direction of propagation. A sinusoidal wave is mathematically expressed as s(t) = A · sin(2πft + φ), defined by four fundamental parameters: Amplitude (A, the peak strength or power of the wave), Frequency (f, number of cycles per second measured in Hertz, Hz), Wavelength (λ, physical distance between two consecutive peaks, where c = λ · f with c ≈ 3 × 10^8 m/s), and Phase (φ, the relative shift of the wave cycle at time t = 0).",
    },
    {
        "type": "comparison",
        "heading": "Analog Signals vs Digital Signals",
        "table": {
            "headers": ["Characteristic", "Analog Signals", "Digital Signals"],
            "rows": [
                ["Nature", "Continuous waveform varying smoothly over time", "Discrete values representing binary states (0s and 1s)"],
                ["Noise Sensitivity", "Highly susceptible; noise accumulates with amplification", "Highly immune; noise can be filtered using threshold detectors"],
                ["Signal Regeneration", "Amplifiers boost both the original signal and accumulated noise", "Repeaters reconstruct and clean the exact binary pulses"],
                ["Bandwidth Efficiency", "Less efficient for complex multiplexing", "Highly efficient; allows advanced compression and encryption"],
                ["Processing Hardware", "Analog filters, operational amplifiers, inductors", "Digital Signal Processors (DSPs), microprocessors, ASICs"],
            ],
        },
    },
    {
        "type": "comparison",
        "heading": "Analog Modulation Techniques (AM, FM, PM)",
        "table": {
            "headers": ["Modulation Type", "Modulated Parameter", "Equation / Principle", "Noise Immunity", "Bandwidth & Applications"],
            "rows": [
                ["Amplitude Modulation (AM)", "Carrier Amplitude", "s(t) = [A_c + m(t)] · cos(2πf_c t)", "Poor (atmospheric noise and interference distort amplitude directly)", "Narrow bandwidth (2 · B); AM broadcast radio (535-1605 kHz), aircraft radio"],
                ["Frequency Modulation (FM)", "Carrier Frequency", "s(t) = A_c · cos(2π[f_c + k_f · m(t)]t)", "High (noise affects amplitude, which FM receivers clip with limiters)", "Wider bandwidth (Carson's rule: 2(Δf + f_m)); FM radio (88-108 MHz), analog TV audio"],
                ["Phase Modulation (PM)", "Carrier Phase Angle", "s(t) = A_c · cos(2πf_c t + k_p · m(t))", "High (similar noise immunity to FM; closely related mathematically)", "Requires phase synchronization; used in telemetry, Wi-Fi, and digital foundations"],
            ],
        },
    },
    {
        "type": "comparison",
        "heading": "Digital Modulation Techniques (ASK, FSK, PSK, QAM)",
        "table": {
            "headers": ["Modulation Technique", "Parameter Varied", "Binary Representation", "Robustness & Characteristics"],
            "rows": [
                ["ASK (Amplitude Shift Keying)", "Carrier amplitude", "Bit 1: high amplitude carrier; Bit 0: zero or low amplitude", "Simple hardware; very susceptible to noise and fading; low power efficiency"],
                ["FSK (Frequency Shift Keying)", "Carrier frequency", "Bit 1: frequency f_1; Bit 0: frequency f_2", "Constant envelope; immune to amplitude noise; requires more bandwidth than ASK"],
                ["PSK (Phase Shift Keying)", "Carrier phase", "Bit 1: 0° phase shift; Bit 0: 180° phase shift (BPSK)", "Excellent noise immunity; constant envelope; standard in Wi-Fi and Bluetooth"],
                ["QAM (Quadrature AM)", "Both amplitude and phase", "Groups of bits (e.g., 16-QAM = 4 bits/symbol, 64-QAM = 6 bits)", "Extremely high spectral efficiency; requires high Signal-to-Noise Ratio (SNR)"],
            ],
        },
    },
    {
        "type": "definition",
        "heading": "Android Build Automation with Gradle",
        "body": "Gradle is an advanced, declarative build automation system used by Android Studio. The build system is organized into: (1) Gradle Wrapper (gradlew / gradlew.bat), ensuring all developers and CI pipelines build with the exact same verified Gradle runtime version without manual installation; (2) Project-level build.gradle, which defines repository endpoints (google(), mavenCentral()) and buildscript plugins common to all modules; (3) Module/App-level build.gradle, which specifies the compileSdk, targetSdk, minSdkVersion, dependencies (e.g., Room, Compose), and build types (debug, release). The AndroidManifest.xml declares app metadata, activities, permissions, and intent-filters, but Gradle controls compilation parameters, dependency resolution, and versioning.",
    },
    {
        "type": "steps",
        "heading": "Android Activity Lifecycle Callback Sequence",
        "steps": [
            {
                "label": "1. onCreate()",
                "text": "Called when the activity is first created. Perform one-time static setup: inflate layouts (setContentView), bind views, initialize ViewModels, and restore savedInstanceState bundles.",
            },
            {
                "label": "2. onStart()",
                "text": "Called when the activity becomes visible to the user. The activity enters the started state, but does not yet have user focus. Ideal for registering UI-related broadcast receivers or starting location updates.",
            },
            {
                "label": "3. onResume()",
                "text": "Called when the activity enters the foreground and gains interactive user focus. The app stays in this state until focus is taken away (e.g., by a phone call or starting another activity).",
            },
            {
                "label": "4. onPause()",
                "text": "Called when the activity loses focus and another activity enters the foreground (or a translucent dialog appears). Must execute very quickly; do NOT perform heavy database writes or network calls here.",
            },
            {
                "label": "5. onStop()",
                "text": "Called when the activity is no longer visible to the user (either covered completely by a new activity or sent to background). Release heavy resources and unregister broadcast receivers here.",
            },
            {
                "label": "6. onDestroy()",
                "text": "Called before the activity is destroyed (either finished by finish() or killed by the system for configuration changes like screen rotation). Final cleanup occurs here.",
            },
            {
                "label": "7. onRestart()",
                "text": "Called after onStop() when the activity is about to be displayed again. Followed immediately by onStart().",
            },
        ],
    },
    {
        "type": "rule",
        "heading": "Activity Lifecycle Visibility & Foreground Rules",
        "body": "Golden Rule 1: onStart() marks the boundary where an activity becomes VISIBLE. onResume() marks the boundary where it becomes INTERACTIVE (in the foreground). Golden Rule 2: When launching a new activity via startActivity(intent), onPause() ALWAYS executes synchronously on the current activity before the new activity can even be created or started. However, onStop() and onDestroy() may not execute immediately (or at all if killed by low memory). Golden Rule 3: All Activities must be declared in AndroidManifest.xml; Fragments are modular UI slices hosted inside an Activity and do NOT need to be declared in the manifest.",
    },
    {
        "type": "code",
        "heading": "Managing BroadcastReceivers with Lifecycle Awareness",
        "lang": "kotlin",
        "code": """class NetworkMonitorActivity : AppCompatActivity() {
    private val connectivityReceiver = object : BroadcastReceiver() {
        override fun onReceive(context: Context, intent: Intent) {
            updateNetworkIndicator()
        }
    }

    override fun onStart() {
        super.onStart()
        // Register receiver when screen becomes VISIBLE
        val filter = IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION)
        registerReceiver(connectivityReceiver, filter)
    }

    override fun onStop() {
        super.onStop()
        // Unregister when screen is NO LONGER VISIBLE to prevent memory leaks and battery drain
        unregisterReceiver(connectivityReceiver)
    }
}""",
        "explanation": "If a feature only needs to update the UI while the screen is visible to the user, the optimal pair of lifecycle callbacks is onStart() and onStop(). Registering in onResume() and unregistering in onPause() stops updates during multi-window or partial obscuring.",
    },
]

memory_aids = [
    {
        "title": "Visibility vs Interaction Distinctions",
        "content": "onStart() = Screen is VISIBLE (drawn on display), but NOT interactive.\nonResume() = Screen is in FOREGROUND and INTERACTIVE (has user touch focus).\nonPause() = Screen lost focus (partially covered, dialog opened, or new activity launching).\nonStop() = Screen is COMPLETELY HIDDEN from view.",
    },
    {
        "title": "Activity Launch Order: Current vs New",
        "content": "When Activity A launches Activity B:\n1. A's onPause() runs FIRST.\n2. B's onCreate(), onStart(), and onResume() run.\n3. B is now visible and active.\n4. A's onStop() runs (only if B completely covers A).",
    },
    {
        "title": "Manifest Declaration Rule",
        "content": "Activities -> MUST be declared in AndroidManifest.xml (<activity android:name='...'>).\nFragments -> DO NOT belong in AndroidManifest.xml; they are dynamically or statically inflated inside an Activity layout.",
    },
    {
        "title": "Modulation Memory Triad",
        "content": "AM = Changes height of carrier wave (noisy).\nFM = Changes spacing/frequency of carrier wave (noise immune, wider bandwidth).\nPM = Changes starting angle/shift of carrier wave.",
    },
]

mcqs = [
    {
        "id": "L2Q1",
        "q": "Which Activity lifecycle method is called when the Activity becomes visible to the user?",
        "options": [
            "onCreate",
            "onStart",
            "onResume",
            "onPause",
        ],
        "ans": 1,
        "explanation": "Official Midterm Question 2 & Course Quiz. onStart() is called when the activity transitions from background to visible on the display. onResume() is called next, when the activity gains user touch focus and becomes interactive.",
    },
    {
        "id": "L2Q2",
        "q": "When launching another activity (using: val intent = Intent(this, DetailsActivity::class.java); startActivity(intent);), which statement about the current activity is correct?",
        "options": [
            "onPause() always runs, but onStop() or onDestroy() may not run immediately.",
            "onDestroy() always runs because a new activity starts.",
            "onResume() runs before the new activity starts.",
            "The call is synchronous, so the new activity must finish first.",
        ],
        "ans": 0,
        "explanation": "Official Midterm Question 3 & Course Quiz. When starting another activity, Android guarantees that the current activity's onPause() method completes before the new activity is created. onStop() executes only after the new activity is fully visible, and onDestroy() may not run until the back button is pressed or memory is reclaimed.",
    },
    {
        "id": "L2Q3",
        "q": "Which Activity lifecycle method is called when another activity comes into the foreground?",
        "options": [
            "onCreate",
            "onStart",
            "onResume",
            "onPause",
        ],
        "ans": 3,
        "explanation": "Official Course Quiz Question. When a new activity or dialog enters the foreground, the currently active activity immediately receives onPause().",
    },
    {
        "id": "L2Q4",
        "q": "You are building an Activity that displays a live indicator of internet connectivity. You only want to receive connectivity change broadcasts while the user is actively viewing that screen. Once the Activity is no longer visible, it should stop listening. In which lifecycle methods should you register and unregister the BroadcastReceiver?",
        "options": [
            "Register in onCreate(), unregister in onDestroy()",
            "Register in onResume(), unregister in onPause()",
            "Register in onStart(), unregister in onStop()",
            "Register in a background thread and unregister when the app is closed",
        ],
        "ans": 2,
        "explanation": "Official Course Quiz Question. onStart() is invoked when the activity becomes visible, and onStop() is invoked when the activity is no longer visible to the user. Registering in onStart() and unregistering in onStop() ensures updates occur precisely during the visible window.",
    },
    {
        "id": "L2Q5",
        "q": "You implement each screen of an app (login, dashboard, settings) as a separate Fragment inside a single Activity, and you never declare any additional Activities in AndroidManifest.xml. Which of the following statements is TRUE?",
        "options": [
            "The app will crash at launch because all Fragments must be declared in the AndroidManifest.xml file.",
            "Each Fragment will still have its own independent lifecycle, unrelated to the Activity that hosts them.",
            "The Activity must still be declared in the manifest, but the Fragments do not need to be.",
            "Since you're using multiple Fragments, you no longer need an Activity at all.",
        ],
        "ans": 2,
        "explanation": "Official Course Quiz Question. Fragments are lightweight UI controllers hosted within an Activity. Only Activities (and Services, BroadcastReceivers, ContentProviders) require registration in AndroidManifest.xml; Fragments are managed internally by the Activity's FragmentManager.",
    },
    {
        "id": "L2Q6",
        "q": "What is the primary purpose of the Gradle Wrapper (gradlew / gradlew.bat) included in an Android project repository?",
        "options": [
            "To wrap Java source files into C++ shared libraries.",
            "To allow anyone to build the project using a verified, declared Gradle version without having to manually install Gradle on their operating system.",
            "To compress PNG drawables into WebP format.",
            "To sign APKs with a production release keystore automatically.",
        ],
        "ans": 1,
        "explanation": "The Gradle Wrapper ensures reproducible builds across different development machines and CI/CD servers by automatically downloading and executing the exact Gradle runtime version configured in gradle-wrapper.properties.",
    },
    {
        "id": "L2Q7",
        "q": "What is the physical relationship between wave frequency (f), wavelength (λ), and the speed of light (c) in free space?",
        "options": [
            "c = λ · f",
            "f = c · λ",
            "λ = c · f^2",
            "c = f / λ",
        ],
        "ans": 0,
        "explanation": "The fundamental wave equation states that speed equals wavelength multiplied by frequency (c = λ · f). In a vacuum or air, c ≈ 3 × 10^8 m/s.",
    },
    {
        "id": "L2Q8",
        "q": "Why is Frequency Modulation (FM) significantly more resistant to natural noise and static interference than Amplitude Modulation (AM)?",
        "options": [
            "FM signals travel at twice the speed of light.",
            "Most electrical noise (lightning, sparks, ignition) manifests as amplitude variations, which FM receivers eliminate using amplitude limiters without altering the frequency-encoded message.",
            "FM waves have zero amplitude at all times.",
            "FM signals operate exclusively on infrared optical frequencies.",
        ],
        "ans": 1,
        "explanation": "Atmospheric and electrical interference primarily alters the amplitude of a propagating radio wave. Since an FM signal encodes the intelligence entirely in instantaneous frequency shifts, an FM receiver clips amplitude fluctuations with a limiter circuit without degrading the received message.",
    },
    {
        "id": "L2Q9",
        "q": "In digital modulation, what distinguishes Frequency Shift Keying (FSK) from Amplitude Shift Keying (ASK)?",
        "options": [
            "FSK varies the carrier frequency between two discrete values for bit 0 and bit 1, maintaining a constant amplitude envelope, whereas ASK modulates carrier amplitude.",
            "FSK changes the carrier phase by 180 degrees, while ASK changes frequency.",
            "FSK can only transmit analog audio, while ASK only transmits digital files.",
            "ASK requires two distinct carrier frequencies, while FSK uses only one.",
        ],
        "ans": 0,
        "explanation": "FSK alternates between two carrier frequencies ($f_1$ for '1', $f_0$ for '0') while maintaining constant amplitude envelope power. ASK represents '1' with high carrier amplitude and '0' with zero or reduced amplitude.",
    },
    {
        "id": "L2Q10",
        "q": "What happens when an Android device is rotated from portrait to landscape orientation if no special configuration handling is specified?",
        "options": [
            "The screen rotates smoothly without any lifecycle method callbacks.",
            "The current Activity is completely destroyed (onPause -> onStop -> onDestroy) and re-created (onCreate -> onStart -> onResume) to load alternative layout resources.",
            "The application terminates immediately with a runtime configuration crash.",
            "Only onResume() is called with the new orientation parameters.",
        ],
        "ans": 1,
        "explanation": "Screen rotation triggers a runtime configuration change. By default, Android restarts the current Activity by calling onPause(), onStop(), and onDestroy(), followed by onCreate(), onStart(), and onResume() so the app can inflate landscape-specific resources.",
    },
    {
        "id": "L2Q11",
        "q": "What is the difference between compileSdk and targetSdk in a module-level build.gradle file?",
        "options": [
            "compileSdk determines the visual theme, while targetSdk determines compiler speed.",
            "compileSdk specifies the Android API level against which the app is compiled at build time, while targetSdk indicates the API version against which the app has been tested for runtime behavioral changes.",
            "compileSdk is for Kotlin code, while targetSdk is for Java code.",
            "targetSdk must always be lower than minSdkVersion.",
        ],
        "ans": 1,
        "explanation": "compileSdk determines which platform APIs are available during compilation. targetSdk tells the Android OS runtime which platform behavior policies and security restrictions the app expects and has been verified to handle.",
    },
    {
        "id": "L2Q12",
        "q": "What is the primary role of Phase Shift Keying (PSK) in modern digital wireless standards such as Wi-Fi and Bluetooth?",
        "options": [
            "To increase transmission power exponentially.",
            "To encode digital bits by shifting the phase of the carrier sine wave at discrete symbol intervals, providing high noise resistance and constant envelope power.",
            "To eliminate the need for an antenna in the receiving radio.",
            "To convert digital pulses directly into acoustic sound waves.",
        ],
        "ans": 1,
        "explanation": "PSK (such as BPSK, QPSK, and 8-PSK) shifts the carrier wave phase by predefined angles (e.g., 0° and 180° for BPSK) to represent bits. It provides superior noise resilience compared to ASK and excellent spectral efficiency.",
    },
    {
        "id": "L2Q13",
        "q": "In which lifecycle state is an Activity considered 'partially obscured' (e.g., behind a permission prompt dialog or a semi-transparent theme)?",
        "options": [
            "Created",
            "Paused",
            "Stopped",
            "Destroyed",
        ],
        "ans": 1,
        "explanation": "When an Activity is still partially visible but does not hold user focus (such as when covered by a translucent activity or dialog), it remains in the Paused state (onPause() has run, but onStop() has not).",
    },
    {
        "id": "L2Q14",
        "q": "What is Quadrature Amplitude Modulation (QAM)?",
        "options": [
            "A modulation technique that varies both carrier amplitude and phase simultaneously, allowing multiple bits to be transmitted per symbol.",
            "A frequency modulation technique that uses four antennas simultaneously.",
            "A purely analog technique used exclusively in optical fiber lines.",
            "An audio compression algorithm used in MP3 encoders.",
        ],
        "ans": 0,
        "explanation": "QAM combines amplitude and phase modulation by mixing two carrier waves that are 90° out of phase (in-phase I and quadrature Q). This allows high-order constellations (e.g., 64-QAM, 256-QAM, 1024-QAM in Wi-Fi 6) carrying many bits per symbol.",
    },
    {
        "id": "L2Q15",
        "q": "Where should intensive one-time initialization, such as binding view hierarchies and setting up dependency injection, be performed in an Activity?",
        "options": [
            "In onResume()",
            "In onStart()",
            "In onCreate()",
            "In onPause()",
        ],
        "ans": 2,
        "explanation": "onCreate() is guaranteed to execute only once per Activity instantiation, making it the appropriate location for inflating layouts, initializing view bindings, and setting up persistent ViewModel references.",
    },
    {
        "id": "L2Q16",
        "q": "Which file in an Android project declares app permissions (e.g., CAMERA, ACCESS_FINE_LOCATION) and registered BroadcastReceivers?",
        "options": [
            "settings.gradle",
            "build.gradle (Module: app)",
            "AndroidManifest.xml",
            "proguard-rules.pro",
        ],
        "ans": 2,
        "explanation": "AndroidManifest.xml acts as the core contract between the application and the Android OS, declaring hardware requirements, permissions requested (<uses-permission>), and top-level app components.",
    },
    {
        "id": "L2Q17",
        "q": "What happens if an Activity in the Stopped state needs to be displayed to the user again?",
        "options": [
            "It calls onRestart() -> onStart() -> onResume().",
            "It calls onCreate() -> onResume() directly.",
            "It calls onPause() -> onResume().",
            "It cannot be displayed again and must be recreated from scratch.",
        ],
        "ans": 0,
        "explanation": "When an activity navigates back to the user from the Stopped state (without having been destroyed), the OS invokes onRestart(), followed by onStart() and onResume().",
    },
    {
        "id": "L2Q18",
        "q": "Why is it dangerous to perform long-running blocking operations (e.g., heavy disk I/O or network calls) inside onPause()?",
        "options": [
            "Because the phone's battery will immediately discharge.",
            "Because the transition to the next activity is blocked until onPause() finishes, causing perceptible UI lag and potentially triggering an Application Not Responding (ANR) error.",
            "Because onPause() runs in a separate process that has no file system access.",
            "Because Android automatically cancels network sockets when onPause() begins.",
        ],
        "ans": 1,
        "explanation": "Android will not start or resume the subsequent activity until the preceding activity's onPause() callback returns. Any lengthy operation in onPause() directly degrades screen transition performance and triggers ANR dialogs.",
    },
    {
        "id": "L2Q19",
        "q": "What is the Carson's Rule used for in telecommunication engineering?",
        "options": [
            "Calculating the battery life of an Android smartphone.",
            "Estimating the transmission bandwidth required for a frequency-modulated (FM) signal: B_T ≈ 2(Δf + f_m).",
            "Calculating the number of lines of code in a Gradle build file.",
            "Determining the exact number of pixels in a mobile screen.",
        ],
        "ans": 1,
        "explanation": "Carson's bandwidth rule gives an empirical approximation for the bandwidth required by an FM signal: B_T ≈ 2(Δf + f_m), where Δf is the peak frequency deviation and f_m is the highest modulating signal frequency.",
    },
    {
        "id": "L2Q20",
        "q": "If the Android system is critically low on RAM and an Activity in the onStop() state needs to be evicted, how does Android reclaim memory?",
        "options": [
            "It puts the activity in an infinite loop.",
            "It directly terminates the activity's hosting Linux process, bypassing onDestroy() if necessary.",
            "It writes the entire RAM contents to external flash memory.",
            "It forces the user to manually uninstall an application.",
        ],
        "ans": 1,
        "explanation": "Under extreme low-memory pressure, the Android Out-Of-Memory (OOM) killer kills background processes hosting stopped activities. In this scenario, onDestroy() is never executed, and state is preserved via onSaveInstanceState().",
    },
]
