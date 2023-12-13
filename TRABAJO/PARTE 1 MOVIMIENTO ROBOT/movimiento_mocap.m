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

%%
% robot frame, hide it
Br=robot.Parent();
Br.setVisible(0);

%%
% define a new rotated frame to be base frame
B0=RDK.AddFrame('B0 frame', Br);
Hr0=transl(150, 50, 300) * roty(pi / 2) * rotz(pi);%transl(0,0,222.5)*rotz(pi/2)*rotx(pi/2); 
B0.setPose(Hr0);
% from now on, all motions are taken with respect to B0
robot.setPoseFrame(B0);
%%
% Set the rest position joints
Jrest=[0, 0, 0, 0, 30, 0];%[0 -90 0 -90 0 0]';
robot.setJoints(Jrest);

% %% RobolinkItem/setPose()
% % This is the key method for setting the pose of a frame, robot target, ect
% % Requires a 4x4 homogeneos matrix as input
% 
% % Create a target defined by Cartesian pose in B0
% target = RDK.AddTarget('Target', B0);
% target.setAsCartesianTarget();
% 
% % define the pose (H transform)
% H_target=transl(550,0,-100)*rotz(pi/6)*rotx(pi/4);
% 
% % set the pose
% target.setPose(H_target);



%% SolveIK: for inverse kinematics
%para calcular todas las rotaciones conocido el punto objetivo

prog=RDK.AddProgram('My Prog');

% Create a joint target home
target = RDK.AddTarget('Home',B0,robot);
target.setAsJointTarget();
target.setJoints(Jrest);
% Add joint movement into the program
prog.MoveJ(target);

% define the pose (H transforms)
W=W1;
X=X2;
Y=Y2;
Z=Z2;
X1=X3;
Y1=Y3;
Z1=Z3;
q=quaternion(W,X,Y,Z);
longq=length(q);

%%

% Generate a sequence of targets and move along the targets (linear move)
angleY = 0;

for dy = 600:-100:100
    targetname = sprintf('Target TY=%i RY=%i', dy, angleY);
    target = RDK.AddTarget(targetname, B0, robot);
    % Move along Z direction of the reference frame
    pose = transl(0, dy, 0);
    % Keep the same orientation as home orientation
    
    pose = pose * roty(angleY * pi / 180);
    target.setPose(pose);
    %% 
    prog.MoveL(target);
    angleY = angleY + 20;
end





% for i=1:100:longq
%     targetname = sprintf('Target%i',i);
%     target = RDK.AddTarget(targetname, B0, robot);
%     ad=[zeros(4,3), [X1(i);Y1(i);Z1(i);0]];
%     qh=quat2tform(q(i))+ ad;
%     target.setPose(qh);
%     prog.MoveJ(target);
%     %prog.addMoveJ(qh);
% end
%%
%robot.Connect();
% Run the program we just created
prog.RunProgram();

% Wait for the movement to finish
while robot.Busy()
    pause(1);
    fprintf('Waiting for the robot to finish...\n');
end

% Run the program once again
fprintf('Running the program again...\n');
prog.RunProgram();




