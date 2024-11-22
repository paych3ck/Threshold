#!/bin/sh
sdk_version=$1
project_path=$2
google_drive_id=$3

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
    if gdown --id "${google_drive_id}" -O EverlastingSummer.zip; then 
        echo "Everlasting Summer downloaded successfully."
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
cp -r "${project_path}/." "EverlastingSummer/game"

echo "Linting project..."
"${sdk_path}/renpy.sh" "EverlastingSummer/game" lint
