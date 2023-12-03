%%
% Generate a Robolink object RDK. This object interface with RoboDK
RDK = Robolink;

% Get the library path
path=RDK.getParam('PATH_LIBRARY');

% Display a list of all items
RDK.ItemList();

%%
% Get some items in the station by their name. Each item is visible in the
% current project tree
robot = RDK.Item('UR3e');
fprintf('Robot selected:\t%s\n', robot.Name());
robot.setVisible(1);

%%
% robot frame, hide it
Br=robot.Parent();
Br.setVisible(0);

%%
% define a new rotated frame to be base frame
B0=RDK.AddFrame('B0 frame', Br);
Hr0= rotz(-pi/4)*rotx(pi);
B0.setPose(Hr0);
% from now on, all motions are taken with respect to B0
robot.setFrame(B0);

%%
%Set tool point to 200 m from robot frange in z (down) direction
H6p=transl(0,0,200);
robot.setHtool(H6p);

%%
% Set the rest position joints
Jrest=[135 -90 90 -90 -90 -90]';
robot.MoveJ(Jrest);

%% RobolinkItem/setPose()
% This is the key method for setting the pose of a frame, robot target, ect
% Requires a 4x4 homogeneos matrix as input

% Create a target defined by Cartesian pose in B0
target = RDK.AddTarget('Target', B0);
target.setAsCartesianTarget();

% define the pose (H transform)
H_target=transl(550,0,-100)*rotz(pi/6)*rotx(pi/4);

% set the pose
target.setPose(H_target);


%% SolveIK: for inverse kinematics

% define the pose (H transforms)
H_target=transl(550,0,-100)*rotz(pi/6)*rotx(pi/4);
% solve IK for nearest joints
IK_joints=robot.SolveIK(Hr0*H_target*inv(H6p));

robot.MoveJ(IK_joints)

%% SolveFK: for forward kinematics
robot.SolveFK([100 -90 125 90 -90 -45 -90])

%% SolveIK_All() computes the inverse kinematics for the specified robot and
% The function returns all available joint solutions as a 2D matrix
IK_joints=robot.SolveIK_All(Hr0*H_target*inv(H6p));
% There seems to be some problem. None of these brings the robot to the
% target

%% % Create a new program "prog"
prog = RDK.AddProgram('My Prog');
prog.addMoveJ(target); %prog.addMoveL(target); 
%prog.RunProgram()




