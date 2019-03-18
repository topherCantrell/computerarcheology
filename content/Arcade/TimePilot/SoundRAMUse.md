![Sound Board RAM](TimePilot.jpg)

# RAM Use

>>> memory

| | | |
| --- | --- | --- |
| 3000:300B | commandBuffer        | Buffer for incoming commands |
| 300C:300D | currentCaps          | Current cap-filter settings |
| 300F:3018 | musicDesc1           | |
| 3019:3022 | musicDesc2           | |
| 3023:302C | musicDesc3           | |
| 302D:3036 | musicDesc4           | |
| 3037:3040 | musicDesc5           | |
| 3041:3043 | ?command01?          | |
| 3044:3045 | ?command02?          | |
| 3047:3049 | ?command03?          | |
| 304A:304D | ?command04?          | |
| 304E:3050 | ?command05?          | |
| 3051:3054 | ?command06?          | |
| 3055:3058 | ?command07?          | |
| 3059:305C | ?command08?          | |
| 305D:3061 | ?command09?          | |
| 3062:3066 | ?command0A?          | |
| 3067:3068 | ?command0B?          | |
| 3069:306C | ?command0C?          | |
| 306D:306F | ?command0D?          | |
| 3070:3073 | ?command0E?          | |
| 3074:3075 | ?command0F?          | |
| 3076:3079 | ?command10?          | |
| 307A:307D | ?command11?          | |
| 307E:3082 | ?command12?          | |
| 3083:308A | ?command13?          | |
| 308B:3092 | ?command14?          | |
| 3093:3097 | ?command15?          | |
| 3098:3099 | ?command16?          | |
| 309A:309B | ?command17?          | |
| 309C:309E | ?command18?          | |
| 309F:30A2 | ?command19?          | |

SP set to 3400 at initialization

# Music Descriptors

Offset bytes in each descriptor:
* 00 - MSB of Delay and Note Number
* 01 - Running LSB Note delay (base delay)
* 02,03 - Music Pointer
* 04,05 - Note Table Base Pointer
* 06 Initial Amplitude
* 07 Running amplitude
* 08 LSB delay reload
* 09 Amplitude modification
