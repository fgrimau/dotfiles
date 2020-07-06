for fullfile in /home/minigrim0/Downloads/*; do
    if [[ -f $fullfile ]]; then
        filename=$(basename -- "$fullfile")    
        extension="${filename##*.}"
        filename="${filename%.*}"
        if [[ ! -d $extension ]];then
            mkdir /home/minigrim0/Downloads/$extension
        fi
        mv $fullfile /home/minigrim0/Downloads/$extension/
    fi
done

