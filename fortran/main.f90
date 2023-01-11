program main
    implicit none

    real :: display_var
    integer :: size
    integer :: player_x
    integer :: player_y
    character :: action

    size = 10
    player_x = 2
    player_y = 2

    ! while true
    do while (1 == 1)
        display_var = display()
        read *, action

        if ( action == "w" ) then
            if ( check_border(player_x, player_y - 1) == 0 ) then
                player_y = player_y - 1
            end if

        else if ( action == "s" ) then
            if ( check_border(player_x, player_y + 1) == 0 ) then
                player_y = player_y + 1
            end if

        else if ( action == "d" ) then
            if ( check_border(player_x + 1, player_y) == 0 ) then
                player_x = player_x + 1
            end if

        else if ( action == "a" ) then
            if ( check_border(player_x - 1, player_y) == 0 ) then
                player_x = player_x - 1
            end if

        else if ( action == "q" ) then
            exit
        end if

    end do

    contains

    integer function check_border(x, y) result(retval)
        integer, intent(in) :: x, y
        if ( x == 0 .or. y == 0 .or. x == size - 1 .or. y == size - 1 ) then
            retval = 1
        else
            retval = 0
        end if
        
    end function check_border

    integer function display()
        ! implicit none
        integer :: x
        integer :: y
        
        x = 0
        y = 0

        do y = 0, size - 1, +1
            do x = 0, size - 1, +1
                if ( x == player_x .and. y == player_y ) then
                    write(*,"(A)",advance="no") "@"
                else if ( check_border(x, y) == 1 ) then
                    write(*,"(A)",advance="no") "#"
                else
                    write(*,"(A)",advance="no") " "
                end if

                write(*,"(A)",advance="no") " "
            end do

            write (*,*) ""

        end do

        
    end function display

end program main