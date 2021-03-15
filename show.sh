
PYTHON_INTERPRETER=/home/ssd1/zhaoguangwei/python_env/bin/python

help(){
    echo "Usage:
        show -p {port} -P {path/to/show/folder}"
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
    occupy=$(netstat -ntulp | grep ${port})
    if [[ -n "${occupy}" ]]
    then
        echo "Port $port is Occupied!"
        exit
    fi
else
    echo "Please set port"
    exit;
fi

if [[ -z "${path}" ]]
then
    path=$(pwd)
    cd ${path}
fi

nohup ${PYTHON_INTERPRETER} -m ComplexHTTPServer ${port} 2>&1 & >/dev/null
