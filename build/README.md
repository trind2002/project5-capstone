How to execute the Shell scripts?
./<file_name> argument_1 argument_2 argument_3

# Server
./create.sh eksUdacityClusterStack eksctl-udacity-cluster.yml
./delete.sh eksUdacityClusterStack

Troubleshoot: to grant the execute permission to the owner
chmod +x create.sh
chmod +x delete.sh