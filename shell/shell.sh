i=1
while [[ $i == 1 ]]; do
echo -e "
\n
1.Currently logged users
2.Your shell directory 
3.Home directory
4.OS name & version
5.Current working directory
6.Number of users logged in
7.Show all available shells in your system
8.Hard disk information
9.CPU information
10.Memory information
11.File system information
12.Currently running process
13.Exit
"

read -p "Choose an option: " k

case $k in
	1)
		who
		;;
	2)
		which bash
		;;
	3)
		echo $HOME
		;;
	4)
		cat /etc/os-release
		;;
	5)
		pwd
		;;
	6)
		who | wc -l
		;;
	7)
		cat /etc/shells
		;;
	8)
		df -h
		;;
	9)
		cat /proc/cpuinfo
		;;
	10)
		free -h
		;;
	11)
		lsblk
		;;
	12)
		ps aux
		;;
	13)
		i=0
		echo "$(tput setaf 1)Script Ended..$(tput sgr0)"
		;;
	*)
		echo "$(tput setaf 1)Choose the correct option!!!....$(tput sgr0)"




	esac

done
