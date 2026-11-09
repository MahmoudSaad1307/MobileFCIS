# -*- coding: utf-8 -*-
"""
Past Exams & Quizzes Data Module - FNI-421 Mobile Computing
Official Mid-Term Fall 2025 & Department Quizzes (Dr. Soha Hussein & Prof. Mohamed Hashim)
Strictly pure data: zero HTML markup.
"""

exam_mcqs = [
    {
        "id": "EQ1",
        "q": "When an Android app requests access to hardware (e.g., camera), which of the following best describes the path of execution?",
        "options": [
            "The app calls the HAL directly, bypassing system services for efficiency.",
            "The app uses framework APIs, which communicate with system services that interact with the HAL.",
            "The app uses native C/C++ libraries, which load the HAL module automatically.",
            "The app communicates with the kernel directly through system calls, without involving HAL.",
        ],
        "ans": 1,
        "explanation": "Official Midterm Fall 2025 (Question 1). The Android security model forbids direct app-to-driver or app-to-HAL interaction. The application calls Java API Framework methods (e.g. CameraManager), which make IPC/Binder calls to System Services. The system service checks permissions, interfaces with the C/C++ Hardware Abstraction Layer (HAL), and the HAL communicates with kernel drivers.",
        "concept": "Android Platform Stack & HAL",
        "lecture": 1,
    },
    {
        "id": "EQ2",
        "q": "Which Activity lifecycle method is called when the Activity becomes visible to the user?",
        "options": [
            "onCreate",
            "onStart",
            "onResume",
            "onPause",
        ],
        "ans": 1,
        "explanation": "Official Midterm Fall 2025 (Question 2). onStart() marks the boundary where the activity becomes visible to the user on screen. onResume() is called subsequently when the activity enters the foreground and gains interactive user focus.",
        "concept": "Activity Lifecycle",
        "lecture": 2,
    },
    {
        "id": "EQ3",
        "q": "When launching another activity (using: val intent = Intent(this, DetailsActivity::class.java); startActivity(intent);), which statement about the current activity is correct?",
        "options": [
            "onPause() always runs, but onStop() or onDestroy() may not run immediately.",
            "onDestroy() always runs because a new activity starts.",
            "onResume() runs before the new activity starts.",
            "The call is synchronous, so the new activity must finish first.",
        ],
        "ans": 0,
        "explanation": "Official Midterm Fall 2025 (Question 3). Android guarantees that the current activity's onPause() method completes before the incoming activity's onCreate()/onStart()/onResume() are executed. However, onStop() only runs if the current activity becomes completely invisible, and onDestroy() may not run until explicitly finished or reclaimed by the system.",
        "concept": "Activity Transitions",
        "lecture": 2,
    },
    {
        "id": "EQ4",
        "q": "What is the correct way to access the length of a nullable String variable in Kotlin?",
        "options": [
            "println(name.length)",
            "println(name?.length)",
            "println(name!!.length)",
            "println(length(name))",
        ],
        "ans": 1,
        "explanation": "Official Midterm Fall 2025 (Question 4). In Kotlin, accessing properties on a nullable type (String?) requires the safe-call operator (?.). println(name?.length) evaluates safely to null if name is null, avoiding NullPointerException.",
        "concept": "Kotlin Null Safety",
        "lecture": 4,
    },
    {
        "id": "EQ5",
        "q": "val name: String? = null\nval result = name?.let { it.uppercase() } ?: \"UNKNOWN\"\nprintln(result)\n\nWhat is the output?",
        "options": [
            "null",
            "UNKNOWN",
            "KOTLIN",
            "Throws a NullPointerException",
        ],
        "ans": 1,
        "explanation": "Official Midterm Fall 2025 (Question 5). Because name is null, the safe-call name?.let does not execute the lambda block and evaluates to null. The Elvis operator (?:) then provides the default right-hand fallback value, printing 'UNKNOWN'.",
        "concept": "Kotlin Operators & Idioms",
        "lecture": 4,
    },
    {
        "id": "EQ6",
        "q": "In Room, Order has a foreign key to User. If a User with related Order records is deleted without specifying onDelete, what happens?",
        "options": [
            "The deletion fails due to the foreign key constraint.",
            "The Order records are automatically deleted.",
            "The Order records remain but become orphaned.",
            "Room prompts the developer to choose a behavior at runtime.",
        ],
        "ans": 0,
        "explanation": "Official Midterm Fall 2025 (Question 6). In Room and SQLite, the default foreign key action is NO ACTION / RESTRICT. If child rows exist in the Order table referencing the User being deleted, the deletion operation is aborted and throws an SQLiteConstraintException.",
        "concept": "Room Persistence & Foreign Keys",
        "lecture": 4,
    },
    {
        "id": "EQ7",
        "q": "If class User has two fields, name and hobbies, then what is correct about the code below?\n\nval u1 = User(\"Sam\", mutableListOf(\"Chess\"))\nval u2 = u1.copy()\nu2.hobbies.add(\"Skiing\")",
        "options": [
            "u1.hobbies stays [\"Chess\"] (deep copy).",
            "u1.hobbies becomes [\"Chess\", \"Skiing\"] (shallow copy).",
            "u2 cannot add to hobbies since data classes are immutable.",
            "The code crashes due to a mutable list in a data class.",
        ],
        "ans": 1,
        "explanation": "Official Midterm Fall 2025 (Question 7). The auto-generated copy() method on Kotlin data classes performs a shallow copy. It copies the reference to the mutable list, not the list contents. Therefore, modifying u2.hobbies modifies the identical list instance referenced by u1.",
        "concept": "Kotlin Data Classes & Memory Models",
        "lecture": 4,
    },
    {
        "id": "EQ8",
        "q": "Which of the following is NOT true about Android Runtime (ART) and the Dalvik Executable (DEX) format?",
        "options": [
            "ART is capable of running multiple virtual machines on low-memory devices.",
            "DEX is a bytecode format specifically optimized for Android's memory constraints.",
            "Build tools such as d8 compile Java sources directly into DEX bytecode.",
            "DEX bytecode can only be executed on the Linux kernel without ART.",
        ],
        "ans": 3,
        "explanation": "Official Midterm Fall 2025 (Question 8). The Linux kernel has no native understanding of DEX bytecode. DEX bytecode can only be loaded and executed by the Android Runtime (ART) or legacy Dalvik VM.",
        "concept": "Android Runtime (ART) & DEX",
        "lecture": 1,
    },
    {
        "id": "EQ9",
        "q": "Which of the following best describes a compiler compared to an interpreter?",
        "options": [
            "Translates the entire program into machine code or intermediate bytecode before execution.",
            "Translates code line by line and executes each statement immediately.",
            "Directly executes high-level source code instructions without any translation phase.",
            "Translates code only when runtime errors or exceptions are detected.",
        ],
        "ans": 0,
        "explanation": "Official Department Quiz (Lec 1). A compiler translates the whole source code into binary machine code or target bytecode prior to execution, whereas an interpreter executes instructions line-by-line at runtime.",
        "concept": "Compilers & Virtual Machines",
        "lecture": 1,
    },
    {
        "id": "EQ10",
        "q": "Which Activity lifecycle method is called when another activity comes into the foreground?",
        "options": [
            "onCreate",
            "onStart",
            "onResume",
            "onPause",
        ],
        "ans": 3,
        "explanation": "Official Department Quiz (Lec 2). onPause() is immediately invoked when another activity moves into the foreground or a dialog takes user focus away from the active activity.",
        "concept": "Activity Lifecycle",
        "lecture": 2,
    },
    {
        "id": "EQ11",
        "q": "You are building an Activity that displays a live indicator of internet connectivity. You only want to receive connectivity change broadcasts while the user is actively viewing that screen. Once the Activity is no longer visible, it should stop listening. In which lifecycle methods should you register and unregister the BroadcastReceiver?",
        "options": [
            "Register in onCreate(), unregister in onDestroy()",
            "Register in onResume(), unregister in onPause()",
            "Register in onStart(), unregister in onStop()",
            "Register in a background thread and unregister when the app is closed",
        ],
        "ans": 2,
        "explanation": "Official Department Quiz (Lec 2). onStart() corresponds to the screen becoming visible, and onStop() corresponds to the screen becoming hidden. Registering in onStart() and unregistering in onStop() precisely matches the visible lifetime of the screen.",
        "concept": "BroadcastReceivers & Lifecycles",
        "lecture": 2,
    },
    {
        "id": "EQ12",
        "q": "You implement each screen of an app as a separate Fragment inside a single Activity, and never declare additional Activities in AndroidManifest.xml. Which of the following statements is TRUE?",
        "options": [
            "The app will crash at launch because all Fragments must be declared in AndroidManifest.xml.",
            "Each Fragment will have an independent lifecycle unrelated to the Activity hosting them.",
            "The Activity must still be declared in the manifest, but the Fragments do not need to be.",
            "Since you're using multiple Fragments, you no longer need an Activity at all.",
        ],
        "ans": 2,
        "explanation": "Official Department Quiz (Lec 2). Android requires all Activities to be registered in AndroidManifest.xml, but Fragments are dynamic sub-controllers managed inside an Activity's layout and require no manifest declarations.",
        "concept": "Fragments & Manifest Declarations",
        "lecture": 2,
    },
    {
        "id": "EQ13",
        "q": "You want your app to open a PDF file located on the device, allowing the user to select from their preferred PDF reader apps (Adobe Reader, Google Drive, etc.). Which approach is best?",
        "options": [
            "Create an explicit intent specifying the Adobe Reader package name.",
            "Create an explicit intent for your app's internal PDF viewer.",
            "Use an implicit intent with ACTION_SEND and attach the PDF as an extra.",
            "Create an implicit intent with ACTION_VIEW and a file:// or content:// URI for the PDF.",
        ],
        "ans": 3,
        "explanation": "Official Department Quiz (Lec 3). An implicit intent with Intent.ACTION_VIEW and the MIME type 'application/pdf' triggers the Android OS intent resolver, showing all installed apps capable of handling PDFs.",
        "concept": "Android Implicit Intents",
        "lecture": 3,
    },
    {
        "id": "EQ14",
        "q": "Which type of Bluetooth does a modern smart watch use when communicating with a smartphone?",
        "options": [
            "Bluetooth Classic only",
            "Bluetooth Low Energy (BLE) only",
            "Both Bluetooth Classic and Bluetooth Low Energy (BLE / Bluetooth Blue)",
            "None; smart watches use Infrared",
        ],
        "ans": 2,
        "explanation": "Official Department Quiz (Lec 4). Smartwatches use dual-mode Bluetooth: BLE for power-efficient background health sensor syncing and push notifications, and Bluetooth Classic for high-bandwidth audio streaming and phone calls.",
        "concept": "Bluetooth Classic vs BLE",
        "lecture": 4,
    },
    {
        "id": "EQ15",
        "q": "A mobile device moves from 2 meters away from a Wi-Fi router to 6 meters. Assuming ideal free-space propagation, how does the surface area of the expanding wave front change, and what happens to the power density received?",
        "options": [
            "Surface area increases by 3x; power density drops to 1/3 of its original value.",
            "Surface area increases by 6x; power density drops to 1/6 of its original value.",
            "Surface area increases by 9x; power density drops to 1/9 of its original value.",
            "Surface area increases by 12x; power density drops to 1/12 of its original value.",
        ],
        "ans": 2,
        "explanation": "Official Department Quiz (Lec 5). The surface area of a sphere is 4πd^2. Tripling the radius (from 2m to 6m, 3x) increases the surface area by 3^2 = 9x. Because the radiated power is distributed over 9 times the area, power density drops to 1/9.",
        "concept": "Power Density & Inverse-Square Law",
        "lecture": 5,
    },
    {
        "id": "EQ16",
        "q": "A smartphone receives a weaker 2.4 GHz signal after moving behind a structural concrete column. If the drop in RSSI is caused primarily by diffraction rather than absorption, what is physically happening to the wave's energy?",
        "options": [
            "The total electromagnetic energy of the wave remains unchanged, but energy is redistributed over a wider spatial angle behind the barrier.",
            "The electromagnetic wave energy is converted into heat at the sharp concrete edge.",
            "The frequency of the wave shifts to a lower value as it bends around the corner, reducing its power output.",
            "The wave reflects backward, destroying the energy through destructive interference.",
        ],
        "ans": 0,
        "explanation": "Official Department Quiz (Lec 5). In diffraction around an obstacle, no electromagnetic wave energy is absorbed or destroyed. Rather, the wavefront bends and disperses its energy across a wider spatial volume in the shadow region.",
        "concept": "Wave Diffraction Physics",
        "lecture": 5,
    },
]

exam_long = [
    {
        "id": "EL1",
        "type": "math",
        "title": "Bluetooth FHSS Frequency Hopping Function Analysis & Modulation",
        "marks": 5,
        "context": "You are part of a Bluetooth design team defining the frequency hopping sequence for Frequency Hopping Spread Spectrum (FHSS) across 8 available channels numbered 0 through 7 (M = 8), with master clock = 5. The message sequence to be transmitted across time slots n = 1 ... 10 is '0101010101'.",
        "parts": [
            {
                "label": "Part (a) — Calculate Hopping Sequence f1(n) = (clock + n^2) mod 8 and Amplitude Modulation Waveform [3 Marks]",
                "marks": 3,
                "steps": [
                    {
                        "label": "Step 1: Mathematical Calculation for Time Slots n = 1 to 10",
                        "formula": "f_1(n) = (5 + n^2) mod 8",
                        "result": "n=1: (5+1) mod 8 = 6\nn=2: (5+4) mod 8 = 9 mod 8 = 1\nn=3: (5+9) mod 8 = 14 mod 8 = 6\nn=4: (5+16) mod 8 = 21 mod 8 = 5\nn=5: (5+25) mod 8 = 30 mod 8 = 6\nn=6: (5+36) mod 8 = 41 mod 8 = 1\nn=7: (5+49) mod 8 = 54 mod 8 = 6\nn=8: (5+64) mod 8 = 69 mod 8 = 5\nn=9: (5+81) mod 8 = 86 mod 8 = 6\nn=10: (5+100) mod 8 = 105 mod 8 = 1",
                        "note": "Notice the repeating pattern of generated RF channels: [6, 1, 6, 5, 6, 1, 6, 5, 6, 1].",
                    },
                    {
                        "label": "Step 2: Amplitude Modulation Mapping of Transmitted Bits (0101010101)",
                        "formula": "Bit 1 = High Amplitude Carrier; Bit 0 = Low / Baseline Amplitude Carrier",
                        "result": "Slot 1 (Bit 0): Channel 6 with Low Amplitude\nSlot 2 (Bit 1): Channel 1 with High Amplitude\nSlot 3 (Bit 0): Channel 6 with Low Amplitude\nSlot 4 (Bit 1): Channel 5 with High Amplitude\nSlot 5 (Bit 0): Channel 6 with Low Amplitude\nSlot 6 (Bit 1): Channel 1 with High Amplitude\nSlot 7 (Bit 0): Channel 6 with Low Amplitude\nSlot 8 (Bit 1): Channel 5 with High Amplitude\nSlot 9 (Bit 0): Channel 6 with Low Amplitude\nSlot 10 (Bit 1): Channel 1 with High Amplitude",
                        "note": "Rubric: +1 point for accurate x/y axes (x = time slots 1..10, y = channels 0..7), +1 point for drawing AM with distinct amplitudes for 1-bits and 0-bits inside the hopping channels, +1 point for correct arithmetic computation of all 10 slots.",
                    },
                ],
                "answer": "The generated channel sequence is 6, 1, 6, 5, 6, 1, 6, 5, 6, 1. In Amplitude Modulation, bit '1' slots (slots 2, 4, 6, 8, 10) are drawn with full amplitude carrier oscillations, while bit '0' slots (slots 1, 3, 5, 7, 9) are drawn with reduced/low amplitude carrier oscillations on their respective channels.",
            },
            {
                "label": "Part (b) — Evaluation of Alternative Function f2(n) = (clock + 5n) mod 8 [2 Marks]",
                "marks": 2,
                "steps": [
                    {
                        "label": "Step 1: Compute Hopping Sequence for f2(n) with clock = 5",
                        "formula": "f_2(n) = (5 + 5n) mod 8",
                        "result": "n=1: (5 + 5) mod 8 = 10 mod 8 = 2\nn=2: (5 + 10) mod 8 = 15 mod 8 = 7\nn=3: (5 + 15) mod 8 = 20 mod 8 = 4\nn=4: (5 + 20) mod 8 = 25 mod 8 = 1\nn=5: (5 + 25) mod 8 = 30 mod 8 = 6\nn=6: (5 + 30) mod 8 = 35 mod 8 = 3\nn=7: (5 + 35) mod 8 = 40 mod 8 = 0\nn=8: (5 + 40) mod 8 = 45 mod 8 = 5\nn=9: (5 + 45) mod 8 = 50 mod 8 = 2\nn=10: (5 + 50) mod 8 = 55 mod 8 = 7",
                        "note": "Generated sequence: [2, 7, 4, 1, 6, 3, 0, 5, 2, 7].",
                    },
                    {
                        "label": "Step 2: Spread Analysis & Justification",
                        "formula": "Channel Diversity Ratio = Unique Channels Used / Total Channels",
                        "result": "f_1(n) uses ONLY 3 channels: {1, 5, 6}. Over 70% of slots cluster on Channel 6.\nf_2(n) visits ALL 8 channels: {0, 1, 2, 3, 4, 5, 6, 7} uniformly without clustering.",
                        "note": "Rubric: Full 2 points requires computing f2(n) outputs AND explicitly stating that f2 has superior frequency spread. Zero points if chosen without mathematical justification.",
                    },
                ],
                "answer": "f2(n) = (clock + 5n) mod 8 is significantly BETTER. As computed, f2(n) generates the sequence (2, 7, 4, 1, 6, 3, 0, 5, 2, 7), which evenly distributes transmissions across all 8 available channels. In contrast, f1(n) only touches 3 channels (1, 5, 6), heavily clustering on channel 6, which completely defeats the purpose of spread spectrum by creating high vulnerability to narrow-band interference.",
            },
        ],
    },
    {
        "id": "EL2",
        "type": "written",
        "title": "Adaptive FHSS Channel Remapping & The Determinism Axiom",
        "marks": 2,
        "context": "During a Bluetooth engineering team discussion on handling RF interference, two engineers debate over two Adaptive FHSS strategies: Strategy (A): If a bad channel occurs, use (ch + 1) mod 8. Strategy (B): If a bad channel occurs, pick a random good channel. Which strategy would you recommend, and why?",
        "parts": [
            {
                "label": "Engineering Recommendation & Determinism Proof [2 Marks]",
                "marks": 2,
                "steps": [
                    {
                        "label": "Criterion: Master-Slave Synchronicity",
                        "note": "In FHSS, the master and slave devices hop frequencies synchronously every 625 microseconds. They must both be tuned to the exact same RF carrier frequency simultaneously to communicate.",
                    },
                    {
                        "label": "Flaw of Strategy (B) (Random Hopping)",
                        "note": "A pseudo-random function without a synchronized runtime seed introduces non-determinism. The master and slave would select different replacement channels, resulting in immediate packet loss. Even if a synchronized seed is shared, distributing seeds adds latency and computational complexity.",
                    },
                    {
                        "label": "Advantage of Strategy (A) ((ch + 1) mod 8)",
                        "note": "Strategy (A) is completely deterministic. Since both the master and slave independently observe channel health and execute the same formula, both compute the exact same replacement channel without needing to transmit coordination packets over the air.",
                    },
                ],
                "answer": "I recommend Strategy (A): (ch + 1) mod 8. In frequency hopping spread spectrum, reproducibility and DETERMINISM are mandatory. Strategy (A) is a purely deterministic function, allowing both the master and the slave to independently calculate and switch to the exact same replacement channel in perfect synchrony. Strategy (B) introduces non-determinism; picking a random channel causes the master and slave to diverge onto different channels unless additional seed synchronization packets are exchanged, introducing dangerous wireless overhead and desynchronization.",
            },
        ],
    },
    {
        "id": "EL3",
        "type": "table",
        "title": "University Library Access System: NFC vs RFID Architectural Trade-off",
        "marks": 5,
        "context": "Your university wants to install a new access control system for the library. Requirements: (1) Students should be able to walk in quickly without forming queues; (2) The administration insists on keeping costs low; (3) Security is paramount (only enrolled students should be permitted entry). Evaluate NFC (smartphone tap / smart cards) vs RFID (long-range UHF reader scanning badges automatically), and defend the optimal engineering choice.",
        "parts": [
            {
                "label": "Architectural Trade-Off Analysis & Engineering Defense",
                "marks": 5,
                "steps": [
                    {
                        "label": "Comparison Metric Matrix",
                        "table": {
                            "headers": ["Architectural Metric", "NFC (13.56 MHz Near Field)", "Long-Range UHF RFID (860-960 MHz)"],
                            "rows": [
                                ["Operational Range", "Extremely short (< 10 cm, touch required)", "Long range (3 to 10 meters, walk-through)"],
                                ["Queuing & Throughput", "Requires intentional tap per student (~1-2 sec/person; potential bottleneck)", "Instantaneous walk-through scanning; zero queue formation"],
                                ["Credential Cost", "Zero extra cost if using students' own smartphones (Host Card Emulation); low card cost", "Very low passive tag badge cost ($0.10/badge), but requires physical badge issuance"],
                                ["Reader Infrastructure Cost", "Inexpensive NFC readers integrated into standard turnstiles", "Expensive high-power UHF portal reader antennas & gate portals"],
                                ["Security & Anti-Cloning", "High: Supports cryptographic challenge-response and biometric phone lock", "Low/Moderate: Basic EPC tags can be skimmed from distance or cloned without encryption"],
                                ["False Positive Triggering", "Zero: Intentional proximity required to trigger reader", "High: May accidentally read badges of students sitting near the entrance outside"],
                            ],
                        },
                        "note": "Official Course Quiz Rubric: There is no single dogmatic answer, but the student must systematically contrast cost, security, distance, and throughput trade-offs.",
                    },
                ],
                "answer": "Optimal Engineering Recommendation: NFC-based access using smartphone Host Card Emulation (HCE) with physical passive smart cards as backup. Defense: While UHF RFID provides superior walk-through speed with zero queuing, its broad read field creates severe security vulnerabilities: badges of students walking past outside the gate can trigger false door openings, and unencrypted UHF credentials are easily cloned with long-range sniffers. NFC guarantees intentional, authenticated user entry (<10 cm touch). By deploying multi-lane NFC turnstiles and leveraging students' existing smartphones via NFC HCE, the university achieves maximum cryptographic security while keeping badge distribution and hardware costs to a minimum.",
            },
        ],
    },
    {
        "id": "EL4",
        "type": "math",
        "title": "Wave Propagation Physics: 2.4 GHz vs 5.0 GHz Indoor Penetration Analysis",
        "marks": 4,
        "context": "Given the speed of light c = 3 × 10^8 m/s, mathematically determine why 2.4 GHz Wi-Fi provides superior indoor coverage and wall penetration compared to 5.0 GHz Wi-Fi, explaining both wavelength diffraction and molecular resonance effects.",
        "parts": [
            {
                "label": "Mathematical Derivation & Propagation Physics",
                "marks": 4,
                "steps": [
                    {
                        "label": "Step 1: Compute Wavelengths",
                        "formula": "λ = c / f",
                        "result": "λ_{2.4} = (3 × 10^8 m/s) / (2.4 × 10^9 s^-1) = 0.125 m = 12.5 cm\nλ_{5.0} = (3 × 10^8 m/s) / (5.0 × 10^9 s^-1) = 0.060 m = 6.0 cm",
                        "note": "2.4 GHz waves are more than twice as long as 5.0 GHz waves.",
                    },
                    {
                        "label": "Step 2: Knife-Edge Diffraction Analysis",
                        "formula": "Diffraction Angle & Penetration ∝ λ",
                        "result": "By the Huygens-Fresnel principle, electromagnetic waves diffract more effectively around obstacles whose physical dimensions are on the order of their wavelength. A 12.5 cm wave diffracts deeply into the shadow zone behind structural concrete columns, doorframes, and partitions, whereas a 6.0 cm wave behaves more like an optical beam, creating deep shadow zones.",
                        "note": "Total wave energy remains unchanged during diffraction, but is redistributed across a wider angle.",
                    },
                    {
                        "label": "Step 3: Molecular Absorption & Dielectric Loss",
                        "formula": "Attenuation Rate (dB/m) increases with frequency",
                        "result": "Higher frequency (5 GHz) oscillations excite the dipole moments of bound water molecules in drywall, brick, and human tissue at higher rates, converting wave energy into heat dissipation (thermal absorption loss).",
                        "note": "Free-space path loss (FSPL = (4πd/λ)^2) also increases quadratically with frequency.",
                    },
                ],
                "answer": "2.4 GHz achieves superior indoor coverage because its wavelength (12.5 cm) is more than double that of 5.0 GHz (6.0 cm). This longer wavelength enables deeper spatial diffraction around room corners and doorframes, while experiencing significantly lower molecular dielectric resonance absorption and lower free-space path loss when traversing walls.",
            },
        ],
    },
]

