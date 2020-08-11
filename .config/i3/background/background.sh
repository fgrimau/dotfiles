notify-send Background-Manager "updating the background"
wget -q --spider http://google.com

if [ $? -eq 0 ]; then # The computer is connected to internet
    ID=$(( ( RANDOM % 1085 ) )) # Generate random number
    echo "Gathering image $ID"
    rm ~/.config/i3/background/1080 -f # Delete old image
    cd .config/i3/background
    wget https://picsum.photos/id/$ID/1920/1080 # Get new image
    if [[ $? -eq 0 ]];then
        echo "Got the image"
        AUTHOR=$(curl https://picsum.photos/id/$ID/info -s | jq -r '.author') # Get new image author

        # Print author's name on the image
        convert ~/.config/i3/background/1080  -font "/usr/share/fonts/TTF/DejaVuSans.ttf" -pointsize 14 -draw "gravity SouthEast \
            fill black  text 0,12 '$AUTHOR' \
            fill white  text 1,11 '$AUTHOR' " \
                ~/.config/i3/background/1080

        if grep -Fxq "$FILENAME" ~/.config/i3/background/favorites
        then
            echo "lol"
            # mark as favorite
        fi

        # Set image as background & remember ID
        feh --no-fehbg --bg-scale ~/.config/i3/background/1080
        echo $ID > ~/.config/i3/background/current_id
        notify-send Background-Manager "Done !"
    else
        echo "Failed to retreive image"
        notify-send Background-Manager "Failed to retreive image !" -u critical
    fi
else
    echo -1 > ~/.config/i3/background/current_id
    FILE=$(find ~/Pictures/Wallpapers/ -type f | shuf -n 1)
    feh --no-fehbg --bg-scale $FILE
fi
