import os
import getpass

os.system("tput setaf 3")
print("\t\t\tMenu of ARTH Technologies")
os.system("tput setaf 7")
print("\t\t\t-------------------------")

passw= getpass.getpass("Enter your password:")

if passw!= "rootacc":
  print("Password Incorrect...!!!")
  exit()

while True:
  os.system("clear")
  os.system("tput setaf 3")
  print("\t\t\tMenu of ARTH Technologies")
  os.system("tput setaf 7")
  print("\t\t\t-------------------------")
  print("""
  \n
  1.LVM Management Menu.
  2.Docker Management Menu.
  3.HTTPD Server Management Menu.
  4.AWS CLI Menu.
  5.Hadoop Management Menu.
  6.Exit the menu.
  """)
  op = input("Enter your option: ")
  if op == '1':
   while True:
    os.system("clear")
    os.system("tput setaf 3")
    print("\t\t\tLogical Volume Management Menu")
    os.system("tput setaf 7")
    print("\t\t\t------------------------------")
    print("""
    \n
    Enter your choice:
    1.Show all the disks connected and more information about them.
    2.Display physical volume(s).
    3.Display logical volume(s).
    4.Display volume groups(s)
    5.Make physical volume.
    6.Make volume group.
    7.Make Partition(logical volume)
    8.Increase the size of logical volume.
    9.Decrease the size of logical volume.
    10.Increase the size of volume group.
    11.Mount the logical volume.
    12.Exit the menu.""") 

    ch = input("Enter your option: ")

    if ch == '1':
      os.system("fdisk -l")
      os.system("lsblk")
      
    elif ch == '2':
      a = input("Enter the name of the physical volume / want to view all the physical vol(all/name of physical vol: ")
      if a == 'all':
        os.system("pvdisplay")
      else:
        b = 'pvdisplay {}'.format(a)
        os.system(b)
    elif ch == '3':
      j = input("Enter the name of the logical volume / want to view all the logical vol(all/name of logical vol: ")
      if j == 'all':
       os.system("lvdisplay")
      else:
       k = input("Enter the name of the volume group of which the logical vol is a part and name of logical volume (eg. VG1/LV1) : ")
       i = 'lvdisplay {}'.format(k)
       os.system(i)
    elif ch == '4':
      r = input("Enter the name of the volume groups / want to see all the vol groups(all/name of a specific vol grp): ")
      if r == 'all' :
        os.system("vgdisplay")
      else:
        o = 'vgdisplay /dev/{}'.format(r)
        os.system(o)
    elif ch == '5':
      x = input("Enter the name of the hard-disk to be made physical volume: ")
      l = 'pvcreate {}'.format(x)
      os.system(l)
    elif ch == '6':
      p = input("Enter the name of the physical vol(s) to be made volume groups: ")
      z = input("Enter the name of the volume group you want to make: ")
      g = 'vgcreate {} {}'.format(z,p)
      os.system(g)
    elif ch == '7':
      r = input("Enter the size of the partition to be made: ")
      q = input("Enter the name of the partition(logical volume): ")
      s = input("Enter the name of the volume from which you want to create parttiton: ")
      y = 'lvcreate --size {} --name {} {}'.format(r,q,s)
      os.system(y)
      print("Formatting the partition created")
      y1 = 'mkfs.ext4 /dev/{}/{}'.format(s,q)
      os.system(y1)
      print("The logical volume has been formated and is ready to be mounted")
    elif ch == '8':
      n = input("Enter the size to be increased")
      k = input("Enter the name of the volume group of which the logical vol is a part and name of logical volume (eg. VG1/LV1) : ")    
      c = 'lvextend --size +{} /dev/{}'.format(n,k)
      os.system(c)
      print("Formatting the new partition")
      cc = 'resize2fs /dev/{}'.format(k)
      os.system(cc)

    elif ch == '9':

      qq= input("Need to unmount the partition before reducing the size,unmounted[y,n]:")
      if qq =='y':
       m = input("Enter the size to be decreased")
       k = input("Enter the name of the volume group of which the logical vol is a part and name of logical volume (eg. VG1/LV1) : ")
       c = 'lvreduce -L  -{} /dev/{}'.format(m,k)   
      else:
       ff = input("Enter the name of the folder mounted with the partition")
       um = 'umount {}'.format(ff)
       os.system(um)
       print("Unmounted {}".format(ff))
       m = input("Enter the size to be decreased")
       k = input("Enter the name of the volume group of which the logical vol is a part and name of logical volume (eg. VG1/LV1) : ")
       c = 'lvreduce -L  -{} /dev/{}'.format(m,k)
      print("Formatting the new reduced partition:")
      c = 'resize2fs /dev/{}'.format(k)
      print("Mounting back the folder")
      um = 'mount /dev/{} {}'.format(k,ff)

    elif ch == '10':
      em = input("Enter the name of the disk you further want to add the volume group: ")
      vv = input("Enter the name of the VG which you want to extend")
      em1 = 'vgextend {} {}'.format(vv,em)
      os.system(em1)


    elif ch == '11':
      m = input("Enter the name of the drive/partition/(vol group/log vol) to be mounted: ")
      fl = input("Enter the name of the folder to be mounted: ")
      mm = 'mount /dev/{} {}'.format(m,fl)
      os.system(mm)
      print("Successfully mounted {}".format(fl))

    elif ch == '12':
      break
    else:
      print("Invalid Input")
    input("Enter to continue...")
    
  elif op == '2':
   rl = input("Do you want to run docker remotely or locally [r/l]? : ")
   if rl =='r':
     ip = input("Enter the IP of the remote system: ")
   else:
     pass

   while True:
    os.system("clear")
    os.system("tput setaf 3")
    print("\t\t\t\tDocker Menu Management")
    os.system("tput setaf 7")
    print("\t\t\t\t----------------------")
    print("""\n
   1.Install Docker
   2.Start the docker services.
   3.Stop the docker services.
   4.Show the status of docker.
   5.Show all the docker images.
   6.Pull an image from docker hub.
   7.Show the active containers.
   8.Show all the containers stopped,active.
   9.Create a container.
   10.Start a stopped container.
   11.Stop a running container(s).
   12.Display log of a container.
   13.Remove/Delete a container(s).
   14.Remove/Delete a docker image.
   15.Exit the menu.
   """)
    ch = input("Enter your option: ")

    if ch == '1':
     if rl == 'r':
       os.system("ssh {} yum install docker-ce --nobest".format(ip))
     else:
       os.system("yum install docker-ce --nobest")

    elif ch == '2':
     if rl == 'r':
       os.system("ssh {} systemctl start docker".format(ip))
     else:
       os.system("systemctl start docker")

    elif ch == '3':
     if rl == 'r':
       os.system("ssh {} systemctl stop docker".format(ip))  
     else:
       os.system("systemctl stop docker")

    elif ch == '4':
     if rl == 'rl':
       os.system("ssh {} systemctl status docker".format(ip))
     else:
       os.system("systemctl status docker")

    elif ch == '5':
     if rl == 'r':
       os.system("ssh {} docker images".format(ip))
     else: 
       os.system("docker images")

    elif ch == '6':
     q = input("Enter the name of OS image you want to pull from the docker hub: ")
     if rl == 'r':
       q1 = 'ssh {} docker pull {}'.format(ip,q)
       os.system(q1)
     else:
       q1 = 'docker pull {}'.format(q)
       os.system(q1)

    elif ch == '7':
     if rl == 'r':
       os.system("docker ps")
     else:
       os.system("docker ps")

    elif ch == '8':
     if rl == 'r':
       os.system("docker ps -a")
     else:
       os.system("docker ps -a")

    elif ch == '9':
     o = input("Enter the name of the docker image of OS you want to launch: ")
     n = input("Enter the name of the container you want to give: ")
     if rl == 'r':
       on = 'ssh {} docker run -it -detach --name {} {}'.format(ip,n,o)
       os.system(on)
       at = input("Whether you want to attach the container to get the terminal of it [y/n]: ")
       if at == 'y':
         nm1 = 'ssh {} docker attach {}'.format(ip,n)
         os.system(nm1)
       else:
         pass

     else:
       on = 'docker run -it -detach --name {} {}'.format(n,o)
       os.system(on)
       at = input("Whether you want to attach the container to get the terminal of it [y/n]: ")
       if at == 'y':
         nm1 = 'docker attach {}'.format(n)
         os.system(nm1)
       else:
         pass

    elif ch == '10':
     nm = input("Enter the name of the container/ID: ")
     if rl == 'r':
       nm1 = 'ssh {} docker start {}'.format(ip,nm)
       os.system(nm1)
       at = input("Whether you want to attach the container to get the terminal of it [y/n]: ")
       if at == 'y':
         nm1 = 'ssh {} docker attach {}'.format(ip,nm)
         os.system(nm1)
       else:
         pass
     else:
       nm1 = 'docker start {}'.format(nm)
       os.system(nm1)
       at = input("Whether you want to attach the container to get the terminal of it [y/n]: ")
       if at == 'y':
         nm1 = 'docker attach {}'.format(nm)
         os.system(nm1)
       else:
         pass

    elif ch == '11':
     nm = input("Enter the name/ID of the OS  you want to stop or want to stop all the running OS[(name/ID of OS) / all]: ")
     if rl == 'r':
       if nm == 'all':
         os.system("ssh {} docker stop  `docker ps`".format(ip))
       else:
         l = 'ssh {} docker stop {}'.format(ip,nm)
         os.system(l)
     else:
       if nm == 'all':
         os.system("docker stop  `docker ps`")
       else:
         l = 'docker stop {}'.format(nm)
         os.system(l)

    elif ch == '12':
     d = input("Enter the name/ID of the OS whose Log you want to see: ")
     if rl == 'r':
       d1 = 'ssh {} docker log {}'.format(ip,d)
       os.system(d1)
     else:
       d1 = 'docker log {}'.format(d)
       os.system(d1)

    elif ch == '13':
     r = input("Enter the name of the OS or its container ID / Want to delete all the containers ? [(name/ID of OS) / all]: ")
     if rl == 'r':
       if r == 'all':
         os.system("docker rm `docker ps -a -q`")
       else:
         i = 'docker rm {}'.format(r)
         os.system(i)
     else:
       if r == 'all':
         os.system("docker rm `docker ps -a -q`")
       else:
         i = 'docker rm {}'.format(r)
         os.system(i)
    elif ch == '14':
     os.system("tput setaf 1")    
     print("WARNING : Make Sure no OS running is using the image(s) you want to remove")
     os.system("tput setaf 7")
     mk = input("Yes OS is running / None of the OS is running [y/n]: ")
     if rl == 'r':

       if mk == 'n':
         im = input("Enter the name of the image you want to delete or want to delete all the images [all/(name/ID of the OS)]: ")
         if im != 'all':
           im1 = 'docker rmi {}'.format(im)
           os.system(im1)
         else:
           os.system("docker rmi `docker images -q`")
       else:
         pass
     else:
       if mk == 'n':
         im = input("Enter the name of the image you want to delete or want to delete all the images [all/(name/ID of the OS)]: ")
         if im != 'all':
           im1 = 'docker rmi {}'.format(im)
           os.system(im1)
         else:
           os.system("docker rmi `docker images -q`")
       else:
         pass
     
    elif ch == '15':
     break
    
   
    else:
     print("Invalid Input..!!!")
    input("\n\nEnter to Continue")

  
  elif op == '3':
   io = input("You want to configure server remotely or locally [r/l] ?: ")
   if io == 'r':
     ip = input("Enter the IP of the remote system: ")
   else:
     io = 'l'
   while True:
    os.system("clear")
    os.system("tput setaf 3")
    print("\t\t\tHTTPD Server Management Menu")
    os.system("tput setaf 7")
    print("\t\t\t----------------------------")
    print("""
    \n
    0.Install HTTPD package.
    1.Start/Stop/View the HTTPS Service.
    2.Start/Stop/View Firewall service.
    3.Start/Stop/View SELinux service.
    4.Create a file of HTML.
    5.Exit the menu.  


   """)
    ch = input("Enter you choice: ")
    if ch == '0':
      if io == 'r':
        os.system("ssh {} yum install httpd".format(ip))
      else:
        os.system("yum install httpd")
    elif ch == '1':
      i = input("1.Start / 2.Stop / 3.View Status of HTTPD [1/2/3]: ")
      if io == 'r':
        if i == '1':
          os.system("ssh {} systemctl start httpd".format(ip))
        elif i == '2':
          os.system("ssh {} systemctl stop httpd".format(ip))
        elif i == '3':
          os.system("ssh {} systemctl status httpd".format(ip))
        else:
          print("Invalid Input...!!!")
      else:
        if i == '1':
          os.system("systemctl start httpd")
        elif i == '2':
          os.system("systemctl stop httpd")
        elif i == '3':
          os.system("systemctl status httpd")
        else:
          print("Invalid Input...!!!")

    elif ch == '2':
      f = input("1.Start / 2.Stop / 3.View Status of Firewall [1/2/3]: ")
      if io == 'r': 
        if f == '1':
          os.system("systemctl start firewalld")
        elif f == '2':
          os.system("systemctl stop firewalld")
        elif f == '3':
          os.system("systemctl status firewalld")
        else:
          print("Invalid Input...!!!")
      else:
        if f == '1':
          os.system("systemctl start firewalld")
        elif f == '2':
          os.system("systemctl stop firewalld")
        elif f == '3':
          os.system("systemctl status firewalld")
        else:
          print("Invalid Input...!!!")


    elif ch == '3':
      s = input("1.Start / 2.Stop / 3.View Status of SELinux [1/2/3]: ")
      if s == '1':
        os.system("setenforce 1")
      elif s == '2':
        os.system("setenforce 0")
      elif s == '3':
        os.system("getenforce")
      else:
        print("Invalid Input")
      os.system("tput setaf 3")
      print("NOTE : Enforcing implies SELinux is active.Permissive implies SELinux is inactive")
      os.system("tput setaf 7")

    elif ch == '4':
      n = input("Enter the name of the HTML file: ")
      print("After you complete the writing of the file press Enter then Ctrl + D")
      n1 = 'cat > {}'.format(n)
      os.system(n1)
      m = 'mv {} /var/www/html/'.format(n)
      os.system(m)
      os.system("tput setaf 10")
      print("The Webpage has been successfully created you can view the webpage")
      os.system("tput setaf 7")
    
    elif ch == '5':
      break

    else:
      print("Invalid Input...!!!")
    input("Enter to Continue...!!!")
 
  elif op == '4':
   while True:
    os.system("clear")
    os.system("tput setaf 3")
    print("\t\t\tAWS CLI Menu Management")
    os.system("tput setaf 7")
    print("\t\t\t-----------------------")
    print("""
    \n
   0.Install AWS CLI Version-2.
   1.Check AWS CLI version.
   2.Configure AWS.
   3.See running instances.
   4.See all the volumes created.
   5.Create instance.
   6.Create an EBS Volume and attaching.
   7.Attaching an already created Volume.
   8.Create Security group.
   9.Create Key Pair.
   10.Create a Bucket.
   11.Upload a file to the bucket.
   12.Create a Cloud Front Distribution.
   13.Exit the menu.

   """)
    ch = input("Enter your Choice: ")
    if ch == '0':
     os.system('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" ')
     os.system("unzip awscliv2.zip")
     os.system(" ./aws/install")
    elif ch == '1':
     os.system("aws --version")
    elif ch == '2':
     os.system("aws configure")
    elif ch == '3':
     os.system("aws ec2 describe-instances")
    elif ch == '4':
     os.system("aws ec2 describe-volumes")
    elif ch == '5':
     a = input("Enter the AMI-ID: ")
     b = input("Enter the number of instances you want to launch: ")
     c = input("Enter the type of instance you want to launch (eg: t2.micro): ")
     d = input("Enter the key name: ")
     e = input("Enter the security groups ID: ")
     f = input("Enter the subnet ID: ")
     aw = 'aws ec2 run-instances --image-id {} --count {} --instance-type {} --key-name {} --security-group-ids {} --subnet-id {}'.format(a,b,c,d,e,f)
     os.system(aw)
    elif ch == '6':
     g = input("Enter the type of volume you want to create (eg: gp2) :")
     h = input("Enter the size of volume you want to create : ")
     i = input("Enter the availability zone where you want to create the volume: ")
     aw1 = 'aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(g,h,i)
     os.system(aw1)
     os.system("tput setaf 9")
     o = input("EBS Volume successfully created...!!!\n\t\t Do you want to attach this volume to any instance ? [y/n]: ")
     os.system("tput setaf 7")
     if o == 'y':
       g1 = input("Enter the volume-id mentioned above :")
       g2 = input("Enter the instance-id of instance where you want to attach the volume :")
       g3 = input("Enter the name of the device as you want to name it (eg: /dev/sdf) : ")
       aw2='aws ec2 attach-volume --volume-id {} --instance-id {} --device {}'.format(g1,g2,g3)
       os.system(aw2)

    elif ch == '7':
     g1 = input("Enter the volume-id mentioned above :")
     g2 = input("Enter the instance-id of instance where you want to attach the volume :")
     g3 = input("Enter the name of the device as you want to name it (eg: /dev/sdf) : ")
     aw2='aws ec2 attach-volume --volume-id {} --instance-id {} --device {}'.format(g1,g2,g3)
     os.system(aw2)

    elif ch == '8':
     s1 = input("Enter the Security group name you want to give")
     s2 = input("Enter the description of the group")
     aw3='aws ec2 create-security-group --group-name {} --description {}'.format(s1,s2)
     os.system(aw3)
     
    elif ch == '9':
     k = input("Enter the name of the key you want to create: ")
     aw3= 'aws ec2 create-key-pair --key-name {}'.format(k)
     os.system(aw3)

    elif ch == '10':
     bn = input("Enter the name of the bucket: ")
     rn = input("Enter the name of the region where you want to create the bucket :")
     aw4 = 'aws s3api create-bucket --bucket {} --region {}'.format(bn,rn)
     os.system(aw4)
    elif ch == '11':
     f1 = input("Enter the path along with the name of file to be uploaded: ")
     f2 = input("Enter the name of the file: ")
     f3 = input("Enter the name of the bucket where it needs to be uploaded: ")
     aw5 = 'aws s3 cp "{}/{}" s3://{}/{}'.format(f1,f2,f3,f2)
     os.system(aw5)
    elif ch == '12':
     cf = input("Enter the object URL you want to set in the Cloud front distribution: ")   	
     aw6 = 'aws cloudfront create-distribution --origin-domain-name {}'.format(cf)
     os.system(aw6)

    elif ch == '13':
     break

    else:
     print("Invalid Input...!!!")
    input("Enter to continue...!!!")


  elif op == '5':
   while True:
    os.system("clear")
    os.system("tput setaf 3")
    print("\t\t\tHadoop Management Menu")
    os.system("tput setaf 7")
    print("\t\t\t----------------------")
    print("""
    1.Install JDK and Hadoop.
    2.Check JDK and Hadoop version.
    3.Configure Name Node.
    4.Configure Slave Node.
    5.Start/Stop Name-Node.
    6.Start/Stop Data-Node.
    7.Check the running service of Name-Node/Data-Node.
    8.Display Cluster Status.
    9.Upload a file to the cluster.
    10.Display the files on the cluster.
    11.Delete a file from the Cluster.
    12.Exit the Menu.

    """)
    ch = input("Enter your choice: ")
    if ch == '1':
      rl = input("You want to configure the Name-Node Locally or Remotely [l/r]: ")
      if rl == 'r':
        ip = input("Enter the IP of the remote system: ")
        os.system("ssh {} rpm -ivh jdk-8u171-linux-x64.rpm".format(ip))
        os.system("ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force".format(ip))

      else:  
        os.system("rpm -ivh jdk-8u171-linux-x64.rpm")
        os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force")

    elif ch == '2':
      print("JDK Version: ",end='')
      os.system("java -version")
      print("")
      print("Hadoop Version: ",end='')
      os.system("hadoop version")
      print("")

    elif ch == '3':
      rl = input("You want to configure the Name-Node Locally or Remotely [l/r]: ")
      if rl == 'r':
        ip = input("Enter the IP of the remote system: ")
      a = input("Enter the Name-Node IP: ")
      b = input("Enter the folder name of the name node: ")
      os.system("echo \<configuration\> >> core-site.xml")
      os.system("echo \<property\> >> core-site.xml")
      os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
      os.system("echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml".format(a))
      os.system("echo \<\/property\> >> core-site.xml")
      os.system("echo \<\/configuration\> >> core-site.xml")
      if rl == 'r':
        os.system("scp core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))
      else: 
        os.system("cp core-site.xml /etc/hadoop/core-site.xml")
      os.system("rm -rf core-site.xml")
      os.system("cp tempcore.xml core-site.xml")


      os.system("echo \<configuration\> >> hdfs-site.xml")
      os.system("echo \<property\> >> hdfs-site.xml")
      os.system("echo \<name\>dfs.name.dir\<\/name\> >> hdfs-site.xml")
      os.system("echo \<value\>{}\<\/value\> >> hdfs-site.xml".format(b))
      os.system("echo \<\/property\> >> hdfs-site.xml")
      os.system("echo \<\/configuration\> >> hdfs-site.xml")
      if rl == 'r':
        os.system("scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ip))
      else: 
        os.system("cp hdfs-site.xml /etc/hadoop/hdfs-site.xml")
      os.system("rm -rf hdfs-site.xml")
      os.system("cp tempcore.xml hdfs-site.xml")
    
      if rl == 'r':
        os.system("ssh {} mkdir {}".format(ip,b))
      else:
        os.system("mkdir {}".format(b))
      print("Formatting the Name-Node..!!")
      if rl == 'r':
        os.system("ssh {} hadoop namenode -format".format(ip))
      else:
        os.system("hadoop namenode -format")

    elif ch == '4':
      rl = input("You want to configure the Data-Node Locally or Remotely [l/r]: ")
      if rl == 'r':
        ip = input("Enter the IP of the remote system: ")
      a = input("Enter the Name-Node IP: ")
      b = input("Enter the folder name of the data node: ")
      os.system("echo \<configuration\> >> core-site.xml")
      os.system("echo \<property\> >> core-site.xml")
      os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
      os.system("echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml".format(a))
      os.system("echo \<\/property\> >> core-site.xml")
      os.system("echo \<\/configuration\> >> core-site.xml")
      if rl == 'r':
        os.system("scp core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))
      else: 
        os.system("cp core-site.xml /etc/hadoop/core-site.xml")
      os.system("rm -rf core-site.xml")
      os.system("cp tempcore.xml core-site.xml")


      os.system("echo \<configuration\> >> hdfs-site.xml")
      os.system("echo \<property\> >> hdfs-site.xml")
      os.system("echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml")
      os.system("echo \<value\>{}\<\/value\> >> hdfs-site.xml".format(b))
      os.system("echo \<\/property\> >> hdfs-site.xml")
      os.system("echo \<\/configuration\> >> hdfs-site.xml")
      if rl == 'r':
        os.system("scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ip))
      else: 
        os.system("cp hdfs-site.xml /etc/hadoop/hdfs-site.xml")
      os.system("rm -rf hdfs-site.xml")
      os.system("cp tempcore.xml hdfs-site.xml")
    
      if rl == 'r':
        os.system("ssh {} mkdir {}".format(ip,b))
      else:
        os.system("mkdir {}".format(b))

    elif ch == '5':
      rl = input("You configured the Name-Node Locally or Remotely [l/r]: ")
      if rl == 'r':
        ip = input("Enter the IP of the remote system: ")
      if rl == 'r':
        os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
      else:
        os.system("hadoop-daemon.sh start namenode")

    elif ch == '6':
      rl = input("You want configured the Data-Node Locally or Remotely [l/r]: ")
      if rl == 'r':
        ip = input("Enter the IP of the remote system: ")
      if rl == 'r':
        os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))
      else:
        os.system("hadoop-daemon.sh start datanode")


    elif ch == '7':
      nd = input("You want to check the running Name-Node/Slave-Node Service remotely or locally [r/l]: ")
      if rl == 'r':
        ip = input("Enter the IP of the remote system: ")
      if nd == 'r':
        os.system("ssh {} jps".format(ip))
      else:
        os.system("jps")

    elif ch == '8':
      os.system("hadoop dfsadmin -report")
 
    elif ch == '9':
      f = input("Enter the name of the file to be uploaded: ")
      os.system("hadoop fs -put {} /".format(f))
 
    elif ch == '10':
      os.system("hadoop fs -ls /")

    elif ch == '11':
      fn = input("Enter the name of the file to be deleted from the Cluster")
      os.system("hadoop fs -rm /{}".format(fn)) 
    elif ch == '12':
      break
    else:
      print("Invalid Input...!!!")
    input("Enter to Continue..!!")


  elif op == '6':
    exit()

  else:
    print("Invalid Input...!!!")
 
   

