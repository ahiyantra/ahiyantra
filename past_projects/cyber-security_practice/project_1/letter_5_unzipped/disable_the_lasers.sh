echo -n "Enter a password to disable the Laser Beam"
echo
read -s first_password
pass=Passw0rd!
if [ $first_password == $pass ];
then
 echo "Disabling lasers!"
 echo "Kitten-topia is saved!"
 echo
 echo "      |\      _,,,---,,_"
 echo "ZZZzz /,\`.-'\`'    -.  ;-;;,_"
 echo "     |,4-  ) )-,_. ,\ (  \`'-'"
 echo "    '---''(_/--'  \`-'\_)  "
 echo
 echo
 echo "                        _ "
 echo "                       | \ "
 echo "                       | | "
 echo "                       | | "
 echo "  |\                   | | "
 echo " /, ~\                / / "
 echo "X     |-.....-------./ / "
 echo " ~-. ~  ~              | "
 echo "    \             /    | "
 echo "     \  /_     ___\   / "
 echo "     | /\ ~~~~~   \ | "
 echo "     | | \        || | "
 echo "     | |\ \       || ) "
 echo "    (_/ (_/      ((_/ "
else
 echo "WRONG PASSWORD"
fi

