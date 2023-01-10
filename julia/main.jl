size = 10
playerPosition = [2,2]

function getDoorX()
    global size
    return floor(size / 2)
end

function newRoom(x,y)
    xPosition = getDoorX()
    return (x == xPosition && y == 0) || (x == xPosition && y == size - 1) && size > 5
end

function checkBorder(x,y)
    return (x == 0 || x == size - 1 || y == 0 || y == size - 1) && !newRoom(x,y)
end

function clear()
    if Sys.iswindows()
        run(`cls`)
    else
        run(`clear`)
    end
end

function display(size)
    outPutString = ""
    for y in 0:size - 1
        for x in 0:size - 1
            if x == playerPosition[1] && y == playerPosition[2]
                outPutString *= "@"
            elseif checkBorder(x, y)
                outPutString *= "#"
            else
                outPutString *= " "
            end
            outPutString *= " "
        end
        outPutString *= "\n"
    end
    print(outPutString)
end

function doAction(input)
    global playerPosition
    global size

    newPlayerPosition = copy(playerPosition)

    if input == "w"
        newPlayerPosition[2] -= 1

    elseif input == "s"
        newPlayerPosition[2] += 1

    elseif input == "a"
        newPlayerPosition[1] -= 1

    elseif input == "d"
        newPlayerPosition[1] += 1

    elseif input == "q"
        exit()
    end

    if newRoom(newPlayerPosition[1], newPlayerPosition[2])

        if newPlayerPosition[2] != 0
            size -= 1

            playerPosition = [getDoorX(), 0]
        else
            size += 1
            playerPosition = [getDoorX(), size - 1]
        end
    elseif !checkBorder(newPlayerPosition[1], newPlayerPosition[2])
        playerPosition = newPlayerPosition
    end
end

function main()
    while true
        clear()
        display(size)
        input = readline()
        doAction(input)
    end
end

main()