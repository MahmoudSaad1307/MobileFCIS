# -*- coding: utf-8 -*-
"""
Lecture 4 Data Module - Bluetooth, FHSS & Kotlin Room Database
FNI-421 Mobile Computing - Dr. Soha Hussein (FCIS, Ain Shams University)
Strictly pure data: zero HTML markup.
"""

LECTURE_META = {
    "id": 4,
    "title": "Bluetooth, FHSS & Kotlin Room Database",
    "subtitle": "Bluetooth Classic vs BLE, Piconets/Scatternets, Frequency Hopping Spread Spectrum, and Room persistence",
    "icon": "⚡",
    "color": "blue",
}

summary_sections = [
    {
        "type": "comparison",
        "heading": "Bluetooth Classic (BR/EDR) vs Bluetooth Low Energy (BLE)",
        "table": {
            "headers": ["Architectural Metric", "Bluetooth Classic (Basic Rate / EDR)", "Bluetooth Low Energy (BLE / Bluetooth Smart)"],
            "rows": [
                ["RF Channels & Spacing", "79 channels spaced 1 MHz apart (2402 - 2480 MHz)", "40 channels spaced 2 MHz apart (3 advertising, 37 data)"],
                ["Data Throughput", "1 Mbps (BR) to 2-3 Mbps (Enhanced Data Rate EDR)", "125 kbps (long-range coded), 1 Mbps, up to 2 Mbps"],
                ["Power Consumption", "High (designed for continuous active connections; 10-30 mA)", "Ultra-low (sleep-mode optimized, duty-cycled; < 10 mA peak, microamps standby)"],
                ["Connection Latency", "Slow connection setup (~100 ms)", "Extremely fast connection setup (< 6 ms)"],
                ["Primary Use Cases", "Continuous audio streaming (A2DP headsets, car audio), high-volume file transfers", "IoT sensors, heart rate monitors, beacons, smart watch fitness telemetry"],
                ["Dual-Mode Architecture", "Smart watches use BOTH: Classic for Bluetooth phone calls & music playback; BLE for continuous sensor telemetry & battery-saving notifications", "Standalone BLE used in coin-cell peripherals (e.g., smart tags, glucose monitors)"],
            ],
        },
    },
    {
        "type": "definition",
        "heading": "Bluetooth Network Topologies: Piconets & Scatternets",
        "body": "A Piconet is an ad-hoc star network formed by Bluetooth devices. Exactly one device acts as the Master, which defines the clock and the frequency-hopping channel sequence. A single Piconet can support at most 7 active Slaves simultaneously (identified by a 3-bit active member address 1-7). Up to 255 additional slave devices can remain synchronized in a low-power Parked state (Parked Member Address 8-bit). A Scatternet is formed when two or more Piconets overlap geographically; a device can participate in multiple piconets by time-multiplexing, serving as a Slave in one piconet and a Master or Slave in another piconet (a bridge node). A node can NEVER be master of two piconets simultaneously.",
    },
    {
        "type": "formula",
        "heading": "Frequency Hopping Spread Spectrum (FHSS) & Hopping Functions",
        "formula": "f(n) = (clock + g(n)) mod M, where M is the total number of RF channels",
        "explanation": "Bluetooth uses FHSS to prevent interference from Wi-Fi and microwave ovens in the 2.4 GHz band. The transmitter and receiver hop frequencies 1600 times per second (each slot is 625 microseconds). The hopping function takes the Master's free-running internal 28-bit clock and slave parameters, yielding a pseudo-random channel index. For M = 8 channels, the modulo operator ensures output channels stay bounded between 0 and 7. The spread of frequencies across the full range determines resilience against narrow-band jamming.",
    },
    {
        "type": "rule",
        "heading": "Adaptive FHSS (AFH) & The Determinism Axiom",
        "body": "Adaptive Frequency Hopping (AFH) monitors RF channel health and classifies channels into 'good' and 'bad' (interfered). When a hopping sequence lands on a bad channel, AFH remaps the hop to an alternate channel. Golden Exam Rule: The remapping algorithm MUST be completely DETERMINISTIC (e.g., f_remap = (ch + 1) mod 8). A random remapping strategy causes non-determinism, forcing Master and Slave out of lock-step unless complex synchronized seeds are transmitted. Determinism guarantees both ends independently calculate the exact same hopped frequency without wireless packet negotiation overhead.",
    },
    {
        "type": "steps",
        "heading": "Kotlin Room Persistence Architecture",
        "steps": [
            {
                "label": "1. @Entity",
                "text": "Annotates a Kotlin data class representing a SQLite database table. Specifies table name, primary keys (@PrimaryKey(autoGenerate = true)), column names (@ColumnInfo), and foreign key constraints (@ForeignKey).",
            },
            {
                "label": "2. @Dao (Data Access Object)",
                "text": "Interface or abstract class defining methods to query, insert, update, and delete database records. Room verifies all SQL statements inside @Query at compile-time, eliminating runtime SQL syntax errors.",
            },
            {
                "label": "3. @Database",
                "text": "Abstract class extending RoomDatabase. Serves as the main database access point. Lists all entity classes, declares schema version, and exposes abstract getter methods returning the DAO interfaces.",
            },
            {
                "label": "4. Singleton Instance",
                "text": "Room database instances are expensive to create. Must be held in a thread-safe Singleton using @Volatile and synchronized(this) double-checked locking.",
            },
        ],
    },
    {
        "type": "rule",
        "heading": "Room Foreign Key Default Constraints & Kotlin Shallow Copy Trap",
        "body": "Rule 1 (Room Foreign Keys): If an Entity (e.g., Order) has a @ForeignKey referencing another Entity (e.g., User), deleting a User record when associated Orders exist WITHOUT explicitly declaring onDelete behavior will FAIL with a SQLiteConstraintException. Room does NOT cascade-delete or orphan child records unless onDelete = ForeignKey.CASCADE or ForeignKey.SET_NULL is explicitly set. Rule 2 (Kotlin Shallow Copy): In Kotlin data classes, calling u1.copy() performs a SHALLOW copy: primitive values are copied by value, but object references (like mutable lists, maps, or nested objects) copy their memory reference. Mutating u2.hobbies.add('Skiing') mutates the same list referenced by u1.hobbies!",
    },
    {
        "type": "code",
        "heading": "Kotlin Room Implementation with Null-Safety & Singleton",
        "lang": "kotlin",
        "code": """// 1. Entities with Foreign Key
@Entity(tableName = "users")
data class User(
    @PrimaryKey(autoGenerate = true) val userId: Long = 0,
    val name: String,
    val email: String? // Nullable field
)

@Entity(
    tableName = "orders",
    foreignKeys = [ForeignKey(
        entity = User::class,
        parentColumns = ["userId"],
        childColumns = ["userOwnerId"],
        onDelete = ForeignKey.CASCADE // Without this, deleting User FAILS by default!
    )]
)
data class Order(
    @PrimaryKey(autoGenerate = true) val orderId: Long = 0,
    val userOwnerId: Long,
    val totalAmount: Double
)

// 2. Thread-Safe Room Singleton Database
@Database(entities = [User::class, Order::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao

    companion object {
        @Volatile // Guarantees atomic writes visible across all CPU threads
        private var INSTANCE: AppDatabase? = null

        fun getDatabase(context: Context): AppDatabase {
            return INSTANCE ?: synchronized(this) {
                val instance = Room.databaseBuilder(
                    context.applicationContext,
                    AppDatabase::class.java,
                    "app_database"
                ).build()
                INSTANCE = instance
                instance
            }
        }
    }
}""",
        "explanation": "Room provides an abstraction layer over SQLite. @Volatile guarantees that changes made by one thread to INSTANCE are immediately visible to all other threads, preventing duplicate database initialization.",
    },
]

memory_aids = [
    {
        "title": "Piconet 7-Active Limit",
        "content": "A Piconet has 1 Master and at most 7 ACTIVE Slaves (3-bit address). Additional 255 devices can wait in PARKED mode (8-bit address).",
    },
    {
        "title": "FHSS Hopping Speed & Determinism Rule",
        "content": "Bluetooth Classic hops 1600 times/sec (625 µs per slot).\nAFH remapping MUST BE DETERMINISTIC (e.g., (ch+1) mod 8) so master and slave calculate the same channel without communicating.",
    },
    {
        "title": "Kotlin Nullable Syntax Triad",
        "content": "val length = name?.length // Safe-call: returns Int? or null if name is null\nval len = name!!.length   // Non-null assertion: throws NullPointerException if null\nval out = name ?: 'DEFAULT' // Elvis operator: returns 'DEFAULT' if name is null",
    },
    {
        "title": "Data Class copy() Shallow Reference Trap",
        "content": "val u2 = u1.copy()\nIf u1 has a MutableList, u2 gets the SAME memory pointer. Adding to u2.hobbies alters u1.hobbies!",
    },
]

mcqs = [
    {
        "id": "L4Q1",
        "q": "What is the correct way to access the length of a nullable String variable in Kotlin?",
        "options": [
            "println(name.length)",
            "println(name?.length)",
            "println(name!!.length)",
            "println(length(name))",
        ],
        "ans": 1,
        "explanation": "Official Midterm Question 4. In Kotlin, accessing properties on a nullable reference (String?) requires the safe-call operator (name?.length). This returns the length as an Int? if name is non-null, or null safely without throwing an exception.",
    },
    {
        "id": "L4Q2",
        "q": "val name: String? = null\nval result = name?.let { it.uppercase() } ?: \"UNKNOWN\"\nprintln(result)\n\nWhat is the output?",
        "options": [
            "null",
            "UNKNOWN",
            "KOTLIN",
            "Throws a NullPointerException",
        ],
        "ans": 1,
        "explanation": "Official Midterm Question 5. Since name is null, the safe-call name?.let returns null without executing the let block. The Elvis operator (?:) detects the null on its left-hand side and evaluates the right-hand fallback expression: 'UNKNOWN'.",
    },
    {
        "id": "L4Q3",
        "q": "In Room, Order has a foreign key to User. If a User with related Order records is deleted without specifying onDelete, what happens?",
        "options": [
            "The deletion fails due to the foreign key constraint.",
            "The Order records are automatically deleted.",
            "The Order records remain but become orphaned.",
            "Room prompts the developer to choose a behavior at runtime.",
        ],
        "ans": 0,
        "explanation": "Official Midterm Question 6 & Course Quiz. By default, SQLite and Room enforce referential integrity using NO ACTION / RESTRICT. If child records exist referencing a parent key, deleting the parent record without explicit cascading rules (onDelete = CASCADE) throws a SQLiteConstraintException and fails.",
    },
    {
        "id": "L4Q4",
        "q": "If class User has two fields, name and hobbies, then what is correct about the code below?\n\nval u1 = User(\"Sam\", mutableListOf(\"Chess\"))\nval u2 = u1.copy()\nu2.hobbies.add(\"Skiing\")",
        "options": [
            "u1.hobbies stays [\"Chess\"] (deep copy).",
            "u1.hobbies becomes [\"Chess\", \"Skiing\"] (shallow copy).",
            "u2 cannot add to hobbies since data classes are immutable.",
            "The code crashes due to a mutable list in a data class.",
        ],
        "ans": 1,
        "explanation": "Official Midterm Question 7. Kotlin's auto-generated data class copy() function creates a shallow copy. Primitive properties are copied, but object references (such as mutableListOf) share the exact same memory reference. Mutating u2.hobbies modifies the identical list referenced by u1.",
    },
    {
        "id": "L4Q5",
        "q": "Which type of Bluetooth does a modern smart watch use when communicating with a smartphone?",
        "options": [
            "Bluetooth Classic only",
            "Bluetooth Low Energy (BLE) only",
            "Both Bluetooth Classic and Bluetooth Low Energy (BLE / Bluetooth Blue)",
            "None; smart watches use Infrared",
        ],
        "ans": 2,
        "explanation": "Official Course Quiz Question. Modern smartwatches implement dual-mode Bluetooth: BLE is used for continuous, power-efficient transmission of health metrics, sensor telemetry, and push notifications, while Bluetooth Classic is invoked for continuous high-throughput audio streaming and phone calls.",
    },
    {
        "id": "L4Q6",
        "q": "Given the frequency hopping function channel_n = (clock^2 * log(n^2)) % 7, how many distinct frequency channels are allowed to be used?",
        "options": [
            "6 channels",
            "7 channels (channels 0 through 6)",
            "8 channels",
            "14 channels",
        ],
        "ans": 1,
        "explanation": "Official Course Quiz Question. The modulo operator (% 7) constrains all calculated integer outputs to the discrete set {0, 1, 2, 3, 4, 5, 6}, which represents exactly 7 allowable frequency channels.",
    },
    {
        "id": "L4Q7",
        "q": "In a Bluetooth Piconet, what is the maximum number of ACTIVE slave devices that can communicate with the master at any given time?",
        "options": [
            "3",
            "7",
            "16",
            "255",
        ],
        "ans": 1,
        "explanation": "A Bluetooth piconet master addresses active slaves using a 3-bit Active Member Address (AM_ADDR), which allows at most 7 active slave devices simultaneously (addresses 1 through 7, as 0 is reserved for broadcast).",
    },
    {
        "id": "L4Q8",
        "q": "How many parked slave devices can maintain synchronization in a Bluetooth Piconet while in low-power standby?",
        "options": [
            "Up to 7",
            "Up to 14",
            "Up to 255",
            "Unlimited",
        ],
        "ans": 2,
        "explanation": "Devices in parked mode surrender their active member address and receive an 8-bit Parked Member Address (PM_ADDR), allowing up to 255 parked devices to stay synchronized to the master's clock.",
    },
    {
        "id": "L4Q9",
        "q": "What is the frequency hopping rate of standard Bluetooth Classic (BR/EDR) devices?",
        "options": [
            "100 hops per second",
            "800 hops per second",
            "1600 hops per second (one hop every 625 microseconds)",
            "3200 hops per second",
        ],
        "ans": 2,
        "explanation": "Standard Bluetooth Classic hops frequencies 1600 times per second across 79 channels. Each time slot has a duration of 1/1600 second = 625 microseconds.",
    },
    {
        "id": "L4Q10",
        "q": "What is a Bluetooth Scatternet?",
        "options": [
            "A network connecting Bluetooth devices directly to satellite orbits.",
            "An interconnected structure composed of two or more overlapping Piconets, bridged by one or more nodes participating as slaves or masters in different piconets.",
            "A network protocol that scatters packets across Wi-Fi routers.",
            "A security attack that disables Bluetooth hopping.",
        ],
        "ans": 1,
        "explanation": "A Scatternet is formed when multiple Piconets overlap. Bridge nodes share their time between piconets (e.g., slave in one piconet and master or slave in another) to route packets across piconet boundaries.",
    },
    {
        "id": "L4Q11",
        "q": "Why must Adaptive Frequency Hopping (AFH) remapping functions be deterministic rather than random?",
        "options": [
            "Because random numbers cannot be computed in Kotlin.",
            "Because both the Master and Slave must independently calculate and switch to the exact same replacement channel without needing to transmit coordination packets over the air.",
            "Because random hopping is banned by international telecommunication law.",
            "Because deterministic functions generate higher radio transmission power.",
        ],
        "ans": 1,
        "explanation": "Official Midterm Part B concept. If an AFH remapping function were random, the master and slave would hop to different channels unless they transmitted an extra seed/packet (which adds latency and can get lost). A deterministic function guarantees identical hopping synchronization at zero packet cost.",
    },
    {
        "id": "L4Q12",
        "q": "In Kotlin Room database architecture, what is the role of the @Dao annotation?",
        "options": [
            "It marks a class as a SQLite database table.",
            "It marks an interface containing CRUD query methods, allowing Room to generate type-safe SQLite database query implementations at compile time.",
            "It automatically displays database rows inside a RecyclerView.",
            "It binds the database directly to the Linux kernel driver.",
        ],
        "ans": 1,
        "explanation": "DAO stands for Data Access Object. Room requires an interface annotated with @Dao where developers declare query methods (@Insert, @Delete, @Query). Room generates the underlying SQLite implementation at compile time.",
    },
    {
        "id": "L4Q13",
        "q": "Why is the singleton database instance in Room declared with the @Volatile annotation?",
        "options": [
            "To prevent the database from being saved to internal device storage.",
            "To guarantee that value writes to the INSTANCE variable are instantly made visible to all other CPU threads, preventing double-checked locking race conditions.",
            "To automatically clear the database on app termination.",
            "To encrypt database tables with AES-256.",
        ],
        "ans": 1,
        "explanation": "In Java/Kotlin multi-threading, @Volatile ensures that writes to the reference variable are atomic and immediately visible across CPU caches of all threads, ensuring proper execution of the double-checked locking singleton pattern.",
    },
    {
        "id": "L4Q14",
        "q": "What happens if you execute a database query that requires a custom object type (e.g., java.util.Date) that Room does not know how to persist in SQLite?",
        "options": [
            "Room crashes at runtime when the first row is saved.",
            "Room fails the build at compile time unless a @TypeConverter method is provided to convert Date to a primitive type (like Long).",
            "SQLite automatically creates a new column data type called Date.",
            "The Date field is silently replaced with the number 0.",
        ],
        "ans": 1,
        "explanation": "Room provides compile-time verification: if an entity contains a non-primitive type that SQLite does not natively support (e.g., Date, List), compilation fails unless a @ProvidedTypeConverter or @TypeConverter is registered.",
    },
    {
        "id": "L4Q15",
        "q": "What is the difference between Bluetooth Classic's 79 channels and BLE's 40 channels?",
        "options": [
            "Bluetooth Classic channels are 1 MHz wide, while BLE channels are 2 MHz wide, with 3 dedicated advertising channels (37, 38, 39) placed between Wi-Fi channels to avoid interference.",
            "BLE channels only transmit voice, while Classic channels transmit text.",
            "Classic channels are spaced 5 MHz apart, while BLE is spaced 10 MHz apart.",
            "There is no difference; both use 79 channels.",
        ],
        "ans": 0,
        "explanation": "BLE divides the 2.4 GHz ISM band into 40 channels of 2 MHz width. Channels 37, 38, and 39 are dedicated advertising channels specifically situated in frequencies where Wi-Fi channels 1, 6, and 11 do not transmit peak energy.",
    },
    {
        "id": "L4Q16",
        "q": "How does a master device in a Bluetooth Piconet coordinate transmission times among slaves?",
        "options": [
            "Slaves transmit randomly using pure ALOHA protocol.",
            "The master uses Time Division Multiplexing (TDM) and alternating time slots: the master transmits in even slots (0, 2, 4...) and the addressed slave replies in the following odd slot (1, 3, 5...).",
            "All slaves transmit on the same frequency at the exact same instant.",
            "Slaves must dial a telephone operator to transmit.",
        ],
        "ans": 1,
        "explanation": "Bluetooth uses a Time-Division Duplex (TDD) scheme with 625 µs time slots. Master transmissions always start in even-numbered slots, and slave responses occur in odd-numbered slots, completely eliminating collisions.",
    },
    {
        "id": "L4Q17",
        "q": "In Kotlin, what does the non-null assertion operator (!!) do when applied to a nullable variable containing null?",
        "options": [
            "It safely returns a default empty string.",
            "It prints a warning in Logcat and sets the variable to 0.",
            "It immediately throws a NullPointerException (NPE) at runtime.",
            "It restarts the current Activity.",
        ],
        "ans": 2,
        "explanation": "The !! operator explicitly tells the compiler that the developer promises the variable is not null. If it actually evaluates to null at runtime, a NullPointerException is thrown immediately.",
    },
    {
        "id": "L4Q18",
        "q": "Which Room annotation allows a developer to perform asynchronous database queries that return continuous stream updates when underlying SQLite tables change?",
        "options": [
            "Returning Flow<List<T>> or LiveData<List<T>> from the @Dao query method.",
            "@AsyncEntity",
            "@ThreadLocked",
            "@ForegroundService",
        ],
        "ans": 0,
        "explanation": "Room has first-class integration with Kotlin Coroutines and Jetpack Architecture Components. Returning Flow<T> or LiveData<T> from a DAO method makes the query observable, automatically emitting new data whenever table rows are modified.",
    },
    {
        "id": "L4Q19",
        "q": "Can a Bluetooth device be the Master of two different Piconets simultaneously?",
        "options": [
            "Yes, a master can control up to 255 piconets at once.",
            "No, a device cannot be master of two piconets because a piconet's hopping sequence and clock are defined entirely by its master's internal clock.",
            "Yes, but only if BLE is disabled.",
            "Yes, if the device has two batteries.",
        ],
        "ans": 1,
        "explanation": "A device cannot be the master of two separate piconets simultaneously because each piconet's frequency hopping sequence and timing are derived directly from the master's free-running clock. However, a master in one piconet CAN be a slave in another.",
    },
    {
        "id": "L4Q20",
        "q": "What is the primary advantage of using Room over raw SQLiteOpenHelper in Android?",
        "options": [
            "Room eliminates the need for SQLite entirely by writing to text files.",
            "Room provides compile-time verification of raw SQL queries, eliminates boilerplate cursor mapping, and natively supports Coroutines and Flow.",
            "Room runs inside the Linux kernel directly for higher speed.",
            "Room does not require any database version migrations.",
        ],
        "ans": 1,
        "explanation": "While raw SQLiteOpenHelper checks queries only at runtime when executed, Room checks SQL syntax and table schema at compile-time, automatically generates Object-Relational Mapping (ORM) code, and eliminates cursor parsing boilerplate.",
    },
]

