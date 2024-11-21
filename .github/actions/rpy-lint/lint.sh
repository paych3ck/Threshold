#!/bin/sh
sdk_version=$1
project_path=$2
game_url=$3

sdk_name="renpy-${sdk_version}-sdk"

user_path=$(eval echo ~${USER})
sdk_path="${user_path}/${sdk_name}"

if [ ! -d "${sdk_path}" ]; then
    echo "Downloading RenPy SDK..."
    if wget -q "https://www.renpy.org/dl/${sdk_version}/${sdk_name}.tar.bz2"; then
        echo "SDK downloaded successfully."
    else
        echo "SDK download failed."
        exit 1
    fi

    echo "Unzipping SDK..."
    tar -xjf "./${sdk_name}.tar.bz2"
    mv "./${sdk_name}" "${user_path}"
    rm "./${sdk_name}.tar.bz2"
else
    echo "SDK already exists."
fi

if [ ! -d "game" ]; then
    echo "Downloading Everlasting Summer..."
    if gdown --id "1MM3B6VRDXJDwQphj_sWuG8AthqIu8s-y" -O EverlastingSummer.zip; then
        echo "Game downloaded successfully."
    else
        echo "Everlasting Summer download failed."
        exit 1
    fi

    echo "Unzipping Everlasting Summer..."
    unzip -q EverlastingSummer.zip
    if [ $? -ne 0 ]; then
        echo "Everlasting Summer unzip failed."
        exit 1
    fi

    rm EverlastingSummer.zip
else
    echo "Everlasting Summer already exists."
fi

echo "Copying mod files..."
cp -r "${project_path}/." "EverlastingSummer/game/mods/"

echo "Linting project..."
"${sdk_path}/renpy.sh" "game" lint
