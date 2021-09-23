#!/bin/sh

## Check .env file
if [ ! -f .env ]; then
    printf "\r\n%sFile '.env' does not exist.%s\r\n\r\n" \
    "$(tput setaf 1)" "$(tput sgr 0)"
    exit
else
    ## Get COMPOSE_PROJECT_NAME variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep COMPOSE_PROJECT_NAME= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        COMPOSE_PROJECT_NAME=$(cat < .env | grep COMPOSE_PROJECT_NAME= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'COMPOSE_PROJECT_NAME' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit
    fi
fi

## Get docker container names
containerNames=$(docker ps --format "{{.Names}}" | grep "${COMPOSE_PROJECT_NAME}" | sort)

## Show menu function
show_menu(){
  echo "Which container do you want to enter (write a number)?"
  i=1
  validOptions=""
  containerNamesArray=""
  for name in $containerNames; do
      echo "$i) $name"
      if [ "$validOptions" = "" ]; then
        validOptions="${i}"
        containerNamesArray="${i}:${name}"
      else
        validOptions="${validOptions}|${i}"
        containerNamesArray="${containerNamesArray},${i}:${name}"
      fi
      i=$((i+1))
  done
  read -r option
}

## Select container by number
echo
show_menu
while true; do
  eval "
      case \"$option\" in
        $validOptions)
          break
        ;;
        *)
          show_menu
        ;;
      esac
  "
done

## Convert the selected number to the container name
selectedContainer=$(echo "$containerNamesArray" | cut -d"${option}" -f2 | cut -d":" -f2 | cut -d"," -f1)

echo
echo "$selectedContainer"

## Execute an interactive shell in the selected container
docker exec -it "$selectedContainer" sh





## Execute an interactive shell in the PHP container
#docker exec -it ${COMPOSE_PROJECT_NAME}_php sh





#show_menu(){
#    normal=`echo "\033[m"`
#    menu=`echo "\033[36m"` #Blue
#    number=`echo "\033[33m"` #yellow
#    bgred=`echo "\033[41m"`
#    fgred=`echo "\033[31m"`
#    printf "\n${menu}*********************************************${normal}\n"
#    printf "${menu}**${number} 1)${menu} Mount dropbox ${normal}\n"
#    printf "${menu}**${number} 2)${menu} Mount USB 500 Gig Drive ${normal}\n"
#    printf "${menu}**${number} 3)${menu} Restart Apache ${normal}\n"
#    printf "${menu}**${number} 4)${menu} ssh Frost TomCat Server ${normal}\n"
#    printf "${menu}**${number} 5)${menu} Some other commands${normal}\n"
#    printf "${menu}*********************************************${normal}\n"
#    printf "Please enter a menu option and enter or ${fgred}x to exit. ${normal}"
#    read opt
#}
#
#option_picked(){
#    msgcolor=`echo "\033[01;31m"` # bold red
#    normal=`echo "\033[00;00m"` # normal white
#    message=${@:-"${normal}Error: No message passed"}
#    printf "${msgcolor}${message}${normal}\n"
#}
#
#clear
#show_menu
#while [ $opt != '' ]
#    do
#    if [ $opt = '' ]; then
#      exit;
#    else
#      case $opt in
#        1) clear;
#            option_picked "Option 1 Picked";
#            printf "sudo mount /dev/sdh1 /mnt/DropBox/; #The 3 terabyte";
#            show_menu;
#        ;;
#        2) clear;
#            option_picked "Option 2 Picked";
#            printf "sudo mount /dev/sdi1 /mnt/usbDrive; #The 500 gig drive";
#            show_menu;
#        ;;
#        3) clear;
#            option_picked "Option 3 Picked";
#            printf "sudo service apache2 restart";
#            show_menu;
#        ;;
#        4) clear;
#            option_picked "Option 4 Picked";
#            printf "ssh lmesser@ -p 2010";
#            show_menu;
#        ;;
#        x)exit;
#        ;;
#        \n)exit;
#        ;;
#        *)clear;
#            option_picked "Pick an option from the menu";
#            show_menu;
#        ;;
#      esac
#    fi
#done
