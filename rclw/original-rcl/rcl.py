import sys
import math, time, random

ERROR = {
    "error": "Error",
    "nofilename": "No filename given",
    "filenotfound": "No file named ",

    "nocmdnamed": "No command named ",
    "notenoughargs": "Not enough args",
    "nowaypoint": "No waypoint named ",
    "notinteger": "Not an integer",
    "zerodivision": "Can't divide through zero",
    "unknownoperation": "Unknown operation"
}

def err(reason):
    print(ERROR["error"] + ": " + str(reason))
    quit()

try:
    filename = sys.argv[1]
except IndexError:
    err(ERROR["nofilename"])

try:
    file = open(filename, "r") #Datei öffnen und lesen
    code = file.read()
    file.close()
except FileNotFoundError:
    err(ERROR["filenotfound"] + filename)

code = code.split("\n") #Code in Array umwandeln

try:
    while True:
        code.remove("") #Alle leeren Zeilen entfernen
except ValueError:
    pass

waypoints = {}
for w in range(0,len(code)):
    l = code[w].split()
    if l[0] == "at":
        waypoints[l[1]] = w

variables = {"%OPEN": "{{", "%CLOSE": "}}"}
running = True
cursor = 0
lastpos = 0
try:
    while running:
        if cursor >= len(code): #Beenden, wenn Cursor größer ist als Länge des Codes (das Ende erreicht hat)
            break
        line = code[cursor]
        try:
            while True:
                line = line.replace(line[line.find("{{"):line.find("}}")+2], variables[line[line.find("{{")+2:line.find("}}")]]) #Komplizierter Befehl, ersetzt Variablennamen zu deren Werten
        except:
            pass
        line = line.split(" ")
        cmd = line[0]
        try:
            args = line[1:]
        except:
            args = []
        
        if cmd.startswith("//"): #Kommentare auslassen
            pass
        
        ##### STEURERUNGS- UND WICHTIGE BEFEHLE #####
        
        elif (cmd == "quit") or (cmd == "exit"):
            running = False
        
        elif cmd == "py":
            exec(" ".join(args))
        
        elif cmd == "if":
            condition = False
            try:
                if (args[1] == "==") or (args[1] == "eq"):
                    if args[0] == args[2]:
                        condition = True
                elif (args[1] == "!=") or (args[1] == "noteq"):
                    if args[0] != args[2]:
                        condition = True
                else:
                    err(ERROR["unknownoperation"])
                
                if condition:
                    if args[3] == "t":
                        if args[4] in waypoints:
                            lastpos = cursor
                            cursor = waypoints[args[4]]
                            continue
                        else:
                            err(ERROR["nowaypoint"] + args[4])
                    
                    elif args[3] == "r":
                        cursor = lastpos + 1
                        continue
                    
                    elif args[3] == "c":
                        try:
                            cursor = int(args[4])
                            continue
                        except ValueError:
                            err(ERROR["notinteger"])
                
            except IndexError:
                err(ERROR["notenoughargs"])
        
        elif cmd == "at":
            pass
        
        elif cmd == "to":
            if args[0] in waypoints:
                lastpos = cursor
                cursor = waypoints[args[0]]
                continue
            else:
                err(ERROR["nowaypoint"] + args[0])
        
        elif cmd == "ret":
            cursor = lastpos + 1
            continue
        
        elif cmd == "cursor":
            try:
                cursor = int(args[0])
                continue
            except ValueError:
                err(ERROR["notinteger"])
        
        ##### VARIABLENBEFEHLE #####
        
        elif cmd == "set":
            try:
                variables[args[0]] = " ".join(args[1:])
            except IndexError:
                err(ERROR["notenoughargs"])
        
        elif cmd == "input":
            try:
                variables[args[0]] = input()
            except IndexError:
                err(ERROR["notenoughargs"])
        
        elif cmd == "rand":
            try:
                random1 = int(args[1])
            except IndexError:
                err(ERROR["notenoughargs"])
            
            try:
                random2 = int(args[2])
                twonums = True
            except IndexError:
                twonums = False
            
            if twonums:
                randomnum = random.randint(random1,random2)
            else:
                randomnum = random.randint(0,random1)
            
            variables[args[0]] = str(randomnum)
        
        elif cmd == "math":
            try:
                args[2] = int(args[2])
            except IndexError:
                err(ERROR["notenoughargs"])
            
            try:
                args[3] = int(args[3])
                twonums = True
            except IndexError:
                twonums = False
            
            if args[1] == "add":
                mresult = int(args[2] + args[3])
            elif args[1] == "sub":
                mresult = int(args[2] - args[3])
            elif args[1] == "mul":
                mresult = int(args[2] * args[3])
            elif args[1] == "div":
                try:
                    mresult = int(args[2] / args[3])
                except ZeroDivisionError:
                    err(ERROR["zerodivision"])
            
            elif args[1] == "mod":
                mresult = int(args[2] % args[3])
            
            elif args[1] == "pow":
                if twonums:
                    mresult = int(math.pow(args[2], args[3]))
                else:
                    mresult = int(math.pow(args[2]))
            
            elif args[1] == "sqrt":
                mresult = int(math.sqrt(args[2]))
            
            else:
                err(ERROR["unknownoperation"])
            
            variables[args[0]] = str(mresult)
		
        ##### OTHER COMMANDS #####
        
        elif cmd == "wait":
            try:
                time.sleep(float(args[0]))
            except IndexError:
                err(ERROR["notenoughargs"])
        
        elif cmd == "out":
            print(" ".join(args))
        
        ##########################
        
        else:
            err(ERROR["nocmdnamed"] + cmd)
        
        vkeys = list(variables.keys())
        for v in range(0,len(vkeys)):
            variables[vkeys[v]] = str(variables[vkeys[v]])
        
        cursor += 1
except Exception as e:
    err(str(type(e)) + ": " + str(e))
