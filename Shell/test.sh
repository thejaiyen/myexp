#!sbash

echo  Check transit ...
tran=$(curl 45.114.175.112:8081/transit/transit.txt)

if [[ $(ip a |grep 10.69.1) ==  *$tran* ]]
then

echo Here in $tran ...

echo Download ip.txt ...
curl 45.114.175.112:8081/transit/ip.txt > ip.txt

echo Data ip.txt is ...
while read line;do echo $line;done < ip.txt

echo run script ...
#/bin/python3 wg_docker.py
echo ...Done...

else
echo Here is not $tran
fi