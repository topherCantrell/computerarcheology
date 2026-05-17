
def break_64(s):
    ret = []
    has_cr = False
    if s.endswith('[CR]'):
        s = s[:-4]
        has_cr = True
    while len(s) > 64:
        ret.append(s[:64])
        s = s[64:]
    if s:
        ret.append(s)
    if has_cr:
        ret[-1] += '[CR]'
    return ret

def fix_obj_ref(s):
    s = s.strip('"')
    if not s.startswith('#'):
        raise "STOP"
    return 'obj_'+s[1:]

with open("content/TRS80/Pyramid/Code.md", "r") as fi:    
    while True:
        line = fi.readline()
        if line.startswith("TODO_HERE:"):
            break
    while True:
        line = fi.readline()
        if line.startswith("4F44:"):
            break
        line = line.strip()
        if line.startswith('; "room_'):
            line = line[3:-5].strip() + ':'
            print(line)
            continue
        if line.startswith(';'):
            continue
        if not line:
            print()
            continue
        if ': 00' in line:
            print(line)
            continue

        if line[18] == '"':
            # initial verb matches
            line = line[:18] + line[19:]
            if line.endswith('" : ['):
                line = line[:-5]
            print(line)
            continue
        else:
            if line.endswith(',[') or line.endswith('],'):
                line = line[:-2]
            elif line.endswith(',') or line.endswith(']'):
                line = line[:-1]

            # No parameters
            if 'PrintInventory' in line:
                line = line.replace('"PrintInventory"', 'PrintInventory')                
            elif 'AssertPackIsEmptyExceptForEmerald' in line:
                line = line.replace('"AssertPackIsEmptyExceptForEmerald"', 'AssertPackIsEmptyExceptForEmerald')
            elif 'SaveGame' in line:
                line = line.replace('"SaveGame"', 'SaveGame')                
            elif 'LoadGame' in line:
                line = line.replace('"LoadGame"', 'LoadGame')                
            elif 'RandomizeDirections' in line:
                line = line.replace('"RandomizeDirections"', 'RandomizeDirections')                
            elif 'PrintScoreAndStop' in line:
                line = line.replace('"PrintScoreAndStop"', 'PrintScoreAndStop')                
            elif 'PrintScore' in line:
                line = line.replace('"PrintScore"', 'PrintScore')                
            elif 'PrintRoomDescription' in line:
                line = line.replace('"PrintRoomDescription"', 'PrintRoomDescription')                
            elif 'SubScriptAbortIfPass' in line:
                line = line.replace('"SubScriptAbortIfPass"', 'SubScriptAbortIfPass')            
            elif 'MoveToLastRoom' in line:
                line = line.replace('"MoveToLastRoom"', 'MoveToLastRoom')
            elif 'GetUserInputObject' in line:
                line = line.replace('"GetUserInputObject"', 'GetUserInputObject')
            elif 'DropUserInputObject' in line:
                line = line.replace('"DropUserInputObject"', 'DropUserInputObject')
            
            # One parameter
            elif 'AssertRandomIsGreaterThan' in line:
                line = line.replace('"AssertRandomIsGreaterThan"', 'AssertRandomIsGreaterThan')
                s = line.split(',')
                line = s[0] + '(' + s[1].strip('"')+')'
            elif 'MoveToRoom' in line:
                line = line.replace('"MoveToRoom"', 'MoveToRoom')
                s = line.split(',')
                line = s[0] + '(' + s[1].strip('"')+')'
            elif 'AssertObjectIsInPack' in line:
                line = line.replace('"AssertObjectIsInPack"', 'AssertObjectIsInPack')
                s = line.split(',')
                line = s[0] + '(' + fix_obj_ref(s[1])+')'                
            elif 'GetObjectFromRoom' in line:
                line = line.replace('"GetObjectFromRoom"', 'GetObjectFromRoom')
                s = line.split(',')
                line = s[0] + '(' + fix_obj_ref(s[1])+')'
            elif 'AssertObjectIsInCurrentRoom' in line:
                line = line.replace('"AssertObjectIsInCurrentRoom"', 'AssertObjectIsInCurrentRoom')
                s = line.split(',')
                line = s[0] + '(' + fix_obj_ref(s[1])+')'
            elif 'MoveObjectToCurrentRoom' in line:
                line = line.replace('"MoveObjectToCurrentRoom"', 'MoveObjectToCurrentRoom')
                s = line.split(',')
                line = s[0] + '(' + fix_obj_ref(s[1])+')'
            elif 'AssertObjectMatchesUserInput' in line:
                line = line.replace('"AssertObjectMatchesUserInput"', 'AssertObjectMatchesUserInput')
                s = line.split(',')
                line = s[0] + '(' + fix_obj_ref(s[1])+')'
            
            # Two parameters
            elif 'MoveObjectToRoom' in line:
                line = line.replace('"MoveObjectToRoom"', 'MoveObjectToRoom')
                line = line.replace('"','')                
                s = line.split(',')
                line = s[0] + '(' + fix_obj_ref(s[1]) + ', ' + s[2]+')'         
            elif 'MoveObjectIntoContainer' in line:
                line = line.replace('"MoveObjectIntoContainer"', 'MoveObjectIntoContainer')
                line = line.replace('"','')                
                s = line.split(',')
                line = s[0] + '(' + fix_obj_ref(s[1]) + ', ' + fix_obj_ref(s[2])+')'

            # Print message with long string
            elif 'PrintMessage' in line:
                i = line.find(',')
                msg = line[i+1:].strip('"')
                msg = break_64(msg)
                line = line[:i].replace('"PrintMessage"', 'PrintMessage')+'("'
                msg[-1] += '")'
                spaces = ';'+' ' * (len(line)-1)                
                line = line + msg[0]
                print(line)
                for m in msg[1:]:
                    print(spaces + m)
                # msg[-1] += '")'
                # for m in msg:
                #     print(">>>>>>>>",m)

            else:
                print(">>>UNKNOWN:", line)
                break
                
            # line = line.replace('"AssertObjectIsInPack"', 'AssertObjectIsInPack')
            # line = line.replace('"MoveObjectToRoom"', 'MoveObjectToRoom')
            # line = line.replace('"AssertObjectIsInPack"', 'AssertObjectIsInPack')
            # line = line.replace('"AssertObjectMatchesUserInput"', 'AssertObjectMatchesUserInput')
            # line = line.replace('"MoveObjectToCurrentRoom"', 'MoveObjectToCurrentRoom')
            # line = line.replace('"DropUserInputObject"', 'DropUserInputObject')
            # line = line.replace('"GetUserInputObject"', 'GetUserInputObject')
            # line = line.replace('"GetObjectFromRoom"', 'GetObjectFromRoom')


            if 'PrintMessage' not in line:
                print(line)
        
        


# with open("content/TRS80/Pyramid/new.md", "w") as fo:
            # if not line:
            #     break
            # line = line.strip()
            # if line.startswith("PS_00:"):
            #     line = line[:3] +f"{pc:02X}" + line[5:]
            #     pc += 1
            # fo.write(line + "\n")
#         pc = 0
#         for line in fi:
#             line = line.strip()
#             if line.startswith("PS_00:"):
#                 line = line[:3] +f"{pc:02X}" + line[5:]
#                 pc += 1
#                 print(line)
#             fo.write(line + "\n")

