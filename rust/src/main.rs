use text_io::read;

#[derive(Copy, Clone)]
struct Position {
    x: i32,
    y: i32,
}

fn display(size: i32, player_position: Position) -> String {
    let mut output: String = String::new();

    for y in 0..size {
        for x in 0..size {
            if x == 0 || y == 0 || x == size - 1 || y == size - 1 {
                output += "#";
            } else {
                if x == player_position.x && y == player_position.y {
                    output += "@";
                } else {
                    output += " ";
                }
            }
            output += " ";
        }
        output += "\n";
    }

    output
}

fn player_input(input: String, player_position: Position) -> Position {
    let mut new_position: Position = player_position;

    match input.as_str() {
        "w" => new_position.y -= 1,
        "s" => new_position.y += 1,
        "a" => new_position.x -= 1,
        "d" => new_position.x += 1,
        _ => println!("Invalid input"),
    }

    new_position
}

fn main() {
    let mut game_is_running: bool = true;
    let mut player_position: Position = Position { x: 1, y: 1 };

    while game_is_running {
        println!("{}", display(10, player_position));
        print!("Action (w, s, a, d, q): ");

        let input: String = read!();
        if input == "q" {
            game_is_running = false;
        } else {
            player_position = player_input(input, player_position);
        }
    }
}
