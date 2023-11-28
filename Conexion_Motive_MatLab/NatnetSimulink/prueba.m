


function prueba(block)
% Level-2 MATLAB file S-Function for times two demo.

%   Copyright 1990-2009 The MathWorks, Inc.

  setup(block);
  %init natnet
  global natnetclient
  
%endfunction

function setup(block)
  
  %% Register number of input and output ports
  block.NumInputPorts  = 0;
  block.NumOutputPorts = 3;

  %% Setup functional port properties to dynamically
  %% inherited.
  block.SetPreCompOutPortInfoToDynamic;
  block.OutputPort(1).SamplingMode = 'Sample';
  block.OutputPort(2).SamplingMode = 'Sample';
  block.OutputPort(3).SamplingMode = 'Sample';
  
  %% Set block sample time to inherited
  block.SampleTimes = [0.1 0];
  
  %block.OutputPort(1).SamplingMode = 'Sample'; % Set the block simStateCompliance to default (i.e., same as a built-in block)
  block.SimStateCompliance = 'DefaultSimState';

  %% Run accelerator on TLC
  block.SetAccelRunOnTLC(true);
  
  %% Register methods
  block.RegBlockMethod('Outputs',                 @Output);  
  
%endfunction    original
  global natnetclient
  natnetclient = natnet;
  natnetclient.HostIP = '127.0.0.1';
  natnetclient.ClientIP = '127.0.0.1';
  natnetclient.ConnectionType = 'Multicast';
  natnetclient.connect;
  

  

function Output(block)
  global natnetclient
  data = natnetclient.getFrame; % method to get current frame
  if isempty(data.RigidBodies(1))
    block.OutputPort(1).Data = 0;
    block.OutputPort(2).Data = 0;
    block.OutputPort(3).Data = 0;
  else 
    %frame=data.Frame;
    %timestamp=data.Timestamp;
    %name=model.RigidBody( 1 ).Name;
	x=data.RigidBodies( 1 ).x * 1000;
	y=data.RigidBodies( 1 ).y * 1000;
    z=data.RigidBodies( 1 ).z * 1000;			
    block.OutputPort(1).Data = double(x);
    block.OutputPort(2).Data = double(y);
    block.OutputPort(3).Data = double(z);

    pause(1)
  end
  
  
%endfunction

