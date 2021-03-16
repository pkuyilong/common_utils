PYTHON_INTERPRETER=/home/ssd1/zhaoguangwei/python_env/bin/python

function help(){
    echo "Usage:
        1. show -p {port}
            default path is current working directory

        2. show -p {port} -P {path/to/show/folder}"
}

function check_occupy(){
    port=$1
    occupy=$(netstat -ntul | grep ${port})
    if [[ -n "${occupy}" ]]
    then
        return 1
    fi
    return 0
}


while getopts "p:P:h" opt
do
    case $opt in
        h)
            help
            exit
            ;;
        p)
            port=${OPTARG}
            ;;
        P)
            path=${OPTARG}
            ;;
        P)
            path=${OPTARG}
            ;;
    esac
done
echo "port is ${port}"
echo "path is ${path}"


if [[ -n "${port}" ]]
then
    check_occupy ${port}
    if [[ $? -ne 0 ]]
    then
        echo "Port $port is Occupied!"
        exit
    fi
else
    while true
    do
        port=$((8000 + $RANDOM % 1000))
        check_occupy ${port}
        if [[ $? -eq 0 ]]
        then
            echo "Random port is $port"
            break
        else
            port=$((8000 + $RANDOM % 1000))
        fi
    done
fi

if [[ -z "${path}" ]]
then
    path=$(pwd)
else
    cd ${path}
    echo "Jump to $path"
fi

nohup ${PYTHON_INTERPRETER} -m ComplexHTTPServer ${port} 2>&1 & >/dev/null
if  [[ $? == 0 ]]
then
    echo "Start serving"
fi
