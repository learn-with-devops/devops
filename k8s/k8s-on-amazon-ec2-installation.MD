## Prerequisites:

      - You need to have created at least one AWS EC2 instance for acting as Master node and at least one AWS EC2 instance to act as a worker node.
      - In this tutorial, I have used Amazon Linux 2 AMI when I lunched EC2 instances, which is based on centos Linux. This AMI also has some pre-installed libraries that AWS does for you. However, you can use any centos-based system such as RHEL as well. In that case, most of the commands remain the same.
      - While launching AWS ec2 instances, make sure that you open all the ports in the related security groups.
      - Both the AWS EC2 instances need to be on the same VPC and preferably same availability zone.
      - Needless to say, you need to have putty/terminal to connect to your EC2 instances.

      Connect to both the ec2 instances using two putty terminals. Decide which EC2 instance would be the master/manager and which would be worker/slave. Henceforward we will call them master and worker nodes. There are a few commands that we need to run on the master as well as the worker node.

Hope you are ready with all that is written in the prerequisites.

## On both the master and worker nodes:

- Be a root user. Install Docker and start Docker service. Also, enable the docker service so that the docker service starts on system restarts.

        sudo su
        yum install docker -y 
        systemctl enable docker && systemctl start docker
        
- Create proper yum repo files so that we can use yum commands to install the components of Kubernetes.

        cat <<EOF > /etc/yum.repos.d/kubernetes.repo
        [kubernetes]

        name=Kubernetes

        baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64

        enabled=1

        gpgcheck=1

        repo_gpgcheck=0

        gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg

        exclude=kube*

        EOF
        
- sysctl command is used to modify kernel parameters at runtime. Kubernetes needs to have access to kernel’s IP6 table and so we need to do some more modifications. This includes disabling secure Linux.

        cat <<EOF >  /etc/sysctl.d/k8s.conf
        net.bridge.bridge-nf-call-ip6tables = 1
        net.bridge.bridge-nf-call-iptables = 1
        EOF

        sysctl --system
        setenforce 0
        
        
- Install kubelet, kubeadm and kubectl; start kubelet daemon

        yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
        systemctl enable kubelet && systemctl start kubelet
        
## Only on the Master Node:
        
        
        
