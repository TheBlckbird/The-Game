local size = 10
local playerPosition = {x = 2, y = 2}

local function display()
    for y  = 1, size do
        for x = 1, size do
            if x == 1 or y == 1 or x == size or y == size  then
                io.write("#")
            elseif x == playerPosition.x and y == playerPosition.y then
                io.write("@")
            else
                io.write(" ")
            end

            io.write(" ")
        end

        print()
    end
end

local function do_action(action)
    local newPos = {x = playerPosition.x, y = playerPosition.y}
    
    if action == "w" then
        newPos.y = newPos.y - 1

    elseif action == "s" then
        newPos.y = newPos.y + 1

    elseif action == "a" then
        newPos.x = newPos.x - 1

    elseif action == "d" then
        newPos.x = newPos.x + 1

    elseif action == "q" then
        os.exit()
    end

    if newPos.x > 1 and newPos.x < size and newPos.y > 1 and newPos.y < size then
        playerPosition = newPos
    end
end

local function main_loop()
    while true do
        display()

        local input = io.read()
        do_action(input)
    end

end

main_loop()