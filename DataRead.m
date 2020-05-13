format longG;

bag = rosbag('~/eece-5554/Lab2/lab2_ws/src/rtk_gps_pkg/bagfiles/Moving_Lot.bag')

rtk_fix = select(bag, 'Topic', 'rtk_fix');        
utm_fix = select(bag, 'Topic', 'utm_fix');
       
rtk_msgs = readMessages(rtk_fix);
utm_msgs = readMessages(utm_fix);
 
r = length(rtk_msgs);
m = length(utm_msgs);

i = 1;

for i = i:r
    
rtk_data(i,1) = rtk_msgs{i,1}.Latitude;
rtk_data(i,2) = rtk_msgs{i,1}.Longitude;
rtk_data(i,3) = rtk_msgs{i,1}.Altitude; 

utm_data(i,1) = utm_msgs{i,1}.Pose.Pose.Position.X;
utm_data(i,2) = utm_msgs{i,1}.Pose.Pose.Position.Y; 
utm_data(i,3) = utm_msgs{i,1}.Pose.Pose.Position.Z;
           
i = i + 1;

end

plot(utm_data(:,1)-utm_data(1,1),utm_data(:,2)-utm_data(1,2),'r*')
%axis([-.025 .025 -.025 .025]);
