## Project Overview

In this project you will apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

Working in AWS
Using Jenkins or Circle CI to implement Continuous Integration and Continuous Deployment
Building pipelines
Working with Ansible and CloudFormation to deploy clusters
Building Kubernetes clusters
Building Docker containers in pipelines

### Project Tasks
In this project you will:
* Working in AWS
* Using Jenkins or Circle CI to implement Continuous Integration and Continuous Deployment
* Building pipelines
* Working with Ansible and CloudFormation to deploy clusters
* Building Kubernetes clusters
* Building Docker containers in pipelines

### Project Submission
For my submission:
- URLs including:
  1. Public Url to GitHub repository (not private) [URL01](https://github.com/trind2002/project5-capstone)
  1. URL hub.docker.com repository [URL02](https://hub.docker.com/repository/docker/trind7/udacity/general)
  1. Elastic Load Balancing (ELB)  [URL03]
- Your screenshots in JPG or PNG format, named using the screenshot number listed in the instructions. These screenshots should be included in your code repository in the root folder.
  1. Linting step both a failed. [SCREENSHOT01]
  1. Linting screenshot and a successful. [SCREENSHOT02]
  1. Take a screenshot of the Circle CI or Jenkins pipeline showing the deployment, and all stages passed successfully. [SCREENSHOT03]
  1. Take a screenshot of your AWS EC2 page showing the newly created. [SCREENSHOT04]
  1. Take a screenshot of the kubectl command output showing. [SCREENSHOT05]
  1. Take a screenshot showing that you can access the application after deployment. [SCREENSHOT06]

---
#### Circle CI
Add the following environment variables to your Circle CI project by navigating to your project
  - `AWS_ACCESS_KEY_ID`=(from IAM user with programmatic access)
  - `AWS_SECRET_ACCESS_KEY`= (from IAM user with programmatic access)
  - `AWS_DEFAULT_REGION`=(your default region in aws)
  - `AWS_SESSION_TOKEN`=(your aws session token)
  - `DOCKER_USER`=(your account hub.docker.com)
  - `DOCKER_PASS`=(your password hub.docker.com)
## Setup the Environment

1. Build AWS CloudFormation
```bash
cd build
./create.sh eksUdacityClusterStack eksctl-udacity-cluster.yml
```
2. kubectl command output:
[Link-Guide](https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html)
a. Create or update a kubeconfig file for your cluster. Replace region-code with the AWS Region that your cluster is in and replace my-cluster with the name of your cluster.
```bash
aws eks update-kubeconfig --region us-east-1 --name eksUdacityClusterStack
```
3. Test your configuration.
```bash
kubectl get svc
```



