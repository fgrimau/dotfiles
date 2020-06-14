
if [[ "`cat ~/.config/i3/background/current_id`" != "-1" ]];then
    if grep -Fxq "`cat ~/.config/i3/background/current_id`" ~/.config/i3/background/favorites; then
        notify-send "Can't like image" "Image is already in favorites !" -u critical
    else
        echo `cat ~/.config/i3/background/current_id` >> ~/.config/i3/background/favorites && notify-send Sucess "Image marked as  favorite !" -a "Background Manager"
    fi
else
    notify-send "Can't like image" "Image is not from internet !" -u critical
fi
